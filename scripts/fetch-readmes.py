#!/usr/bin/env python3
"""Fetch every registry entry's README and extract a unified structured summary.

Writes data/readmes.json: { id: { intro, features[], install, usage, license } }

Usage:
    python3 scripts/fetch-readmes.py [--token gho_xxx]
"""
import argparse
import json
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
OUT = DATA_DIR / "readmes.json"

BLOCK = re.compile(r"```(\w*)\n(.*?)```", re.S)
HEADING = re.compile(r"^#{1,4}\s+(.*)$")
BULLET = re.compile(r"^[-*]\s+(.*)$")
BADGE = re.compile(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)|!\[[^\]]*\]\([^)]*\)|<img[^>]*>|https?://[^\s)]+\.(png|jpg|gif|svg|webp)")
TOC_HEAD = re.compile(r"^(##+\s*)?(目录|contents|table of contents|导航)$", re.I)
FEATURE_HEAD = re.compile(r"(feature|特性|功能|亮点|what.{0,15}(do|is)|capabilit|key points|核心|特点|特色)", re.I)
INSTALL_RE = re.compile(r"(npm (i|install)|pnpm (add|i|install)|yarn add|dsh plugin|git clone|brew install|pip install|uv add|npx @deepseek-ai)", re.I)


def api_readme(repo, token):
    headers = {"Accept": "application/vnd.github.raw",
               "User-Agent": "awesome-dsh-readmes"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    url = f"https://api.github.com/repos/{repo}/readme"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=25) as resp:
                return resp.read().decode("utf-8", errors="ignore")
        except urllib.error.HTTPError as e:
            if e.code in (404, 403):
                return ""
            time.sleep(3 * (attempt + 1))
        except Exception:  # noqa: BLE001
            time.sleep(2)
    return ""


def clean_line(line):
    line = BADGE.sub("", line).strip()
    return re.sub(r"\s+", " ", line).strip()


def sections(text):
    """Split markdown into (heading, body-lines) sections."""
    out, cur_head, cur = [], "", []
    for line in text.splitlines():
        m = HEADING.match(line)
        if m:
            out.append((cur_head, cur))
            cur_head, cur = m.group(1).strip(), []
        else:
            cur.append(line)
    out.append((cur_head, cur))
    return out


def parse(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    result = {"intro": "", "features": [], "install": "", "usage": "", "license": ""}

    secs = sections(text)

    # --- intro: first meaningful paragraphs (skip title, toc, badges) ---
    para, seen_title = [], False
    for head, body in secs:
        if not head:
            continue
        if TOC_HEAD.match(head):
            continue
        seen_title = True
        joined = [clean_line(l) for l in body]
        joined = [l for l in joined if l and not l.startswith(("|", ">", "```"))
                  and not re.match(r"^[^|]{0,15}\|\s*\[?(English|中文|简体)", l)]
        text_block = " ".join(joined)
        if len(text_block) > 60:
            para.append(text_block)
        if len(para) >= 1:
            break
    if para:
        result["intro"] = para[0][:500]

    # --- features: bullets under feature-ish headings (or any section's bullets) ---
    for head, body in secs:
        if not FEATURE_HEAD.search(head or ""):
            continue
        bullets = [clean_line(BULLET.match(l).group(1)) for l in body if BULLET.match(l)]
        result["features"] = [b[:140] for b in bullets if b][:6]
        if result["features"]:
            break
    if not result["features"]:
        for head, body in secs[:4]:
            bullets = [clean_line(BULLET.match(l).group(1)) for l in body if BULLET.match(l)]
            result["features"] = [b[:140] for b in bullets if b][:4]
            if result["features"]:
                break

    # --- install: first short code block containing an install command ---
    blocks = BLOCK.findall(text)
    for lang, code in blocks:
        code = code.strip()
        if INSTALL_RE.search(code) and len(code) < 400:
            result["install"] = code[:400]
            break

    # --- usage: first code block after install position, or usage section ---
    if result["install"]:
        pos = text.find(result["install"])
        for lang, code in blocks:
            idx = text.find(code)
            if idx > pos and code.strip() != result["install"] and len(code.strip()) < 400:
                result["usage"] = code.strip()[:400]
                break
    if not result["usage"]:
        for lang, code in blocks:
            if len(code.strip()) < 400 and code.strip() != result["install"]:
                result["usage"] = code.strip()[:400]
                break

    # --- license ---
    m = re.search(r"^#+\s*license\s*:?\s*(.*)$", text, re.I | re.M)
    if m:
        result["license"] = m.group(1).strip()[:60]

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=None)
    parser.add_argument("--jobs", type=int, default=10)
    args = parser.parse_args()

    entries = []
    for f in sorted(DATA_DIR.glob("*.json")):
        if f.name in ("candidates.json", "readmes.json", "official-guides.json"):
            continue
        for e in json.loads(f.read_text()):
            if isinstance(e, dict) and "repository" in e:
                entries.append(e)

    cache = {}
    if OUT.exists():
        cache = json.loads(OUT.read_text())

    def work(e):
        repo = e["repository"].replace("https://github.com/", "").rstrip("/")
        if e["id"] in cache and cache[e["id"]].get("_done"):
            return e["id"], None
        md = api_readme(repo, args.token)
        if not md:
            return e["id"], {"_done": False, "intro": "", "features": [], "install": "", "usage": "", "license": ""}
        parsed = parse(md)
        parsed["_done"] = True
        return e["id"], parsed

    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(work, e): e for e in entries}
        ok = 0
        for fut in as_completed(futs):
            eid, parsed = fut.result()
            if parsed is not None:
                cache[eid] = parsed
                if parsed.get("_done"):
                    ok += 1

    OUT.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
    with_features = sum(1 for v in cache.values() if v.get("features") or v.get("intro"))
    print(f"readmes cached: {len(cache)} ({ok} fetched fresh), with content: {with_features}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
