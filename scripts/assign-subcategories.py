#!/usr/bin/env python3
"""Assign `subcategory` values to registry entries so large categories can be
split into finer groups on the category pages.

Rules are keyword-based (name + description, EN + ZH) and stored back into
data/*.json so the grouping is stable and hand-editable.

Usage:
    python3 scripts/assign-subcategories.py [--dry-run]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
FILES = ["plugins.json", "skills.json", "workflows.json", "agents.json", "clients.json",
         "integrations.json", "examples.json", "tutorials.json", "awesome-lists.json", "related.json"]

RULES = {
    # category -> [(subcategory, [(pattern, kind)] )]  kind: "name" | "desc" | "both"
    "developer": [
        ("cost-billing", ["balance", "billing", "cost", "usage", "quota", "spend", "token",
                          "费用", "余额", "计费", "统计", "用量"]),
        ("security-ops", ["security", "audit", "password", "health", "check", "doctor",
                          "安全", "审计", "健康", "检查", "运维", "ops", "plugin-check", "restart"]),
        ("code-testing", ["test", "review", "diff", "lint", "git", "commit", "branch",
                          "测试", "审查", "评审", "diff"]),
        ("files-import", ["import", "export", "upload", "mount", "file", "pdf", "doc",
                          "导入", "导出", "上传", "文件", "挂载", "conversation"]),
        ("tools", ["tool", "toolkit", "regex", "json", "csv", "calculator", "encoding",
                   "工具", "工具包", "计算器", "正则"]),
    ],
    "ui": [
        ("generative-ui", ["generate", "canvas", "preview", "render", "visualiz", "genui",
                           "interactive", "artifact", "生成", "画布", "预览", "渲染", "可视化"]),
        ("skins-themes", ["skin", "theme", "skin", "皮肤", "主题", "换肤", "wallpaper", "背景"]),
        ("desktop-pets", ["pet", "whale", "companion", "宠物", "鲸鱼", "桌宠", "q宠"]),
        ("sidebar-panels", ["sidebar", "panel", "workbench", "dock", "side panel", "tabs",
                            "侧边栏", "面板", "工作台", "dock"]),
        ("status-stats", ["status", "stats", "stat", "token", "cost", "balance", "tps",
                          "状态", "统计", "token", "费用", "余额", "进度", "label"]),
        ("input-enhancement", ["input", "composer", "paste", "drag", "history", "wordbox",
                               "输入", "粘贴", "拖拽", "历史", "词箱"]),
        ("navigation", ["nav", "index", "milestone", "timeline", "turn", "jump",
                        "导航", "索引", "跳转", "时间线"]),
    ],
    "memory": [
        ("memory-systems", ["memory", "memor", "remember", "recall", "mneme", "mnemon",
                            "memento", "memoria", "vault", "记忆", "回忆", "召回"]),
        ("context-management", ["context", "compress", "prun", "compact", "token",
                                "上下文", "压缩", "剪枝", "精简"]),
        ("context-audit", ["audit", "inspect", "payload", "diagnos", "审计", "检查", "诊断", "会话"]),
    ],
    "search": [
        ("web-search", ["search", "web", "exa", "duckduckgo", "bing", "jina", "搜索", "检索"]),
        ("news-rss", ["news", "rss", "brief", "feed", "新闻", "资讯", "简报"]),
        ("url-collection", ["url", "bookmark", "collect", "收藏", "链接管理", "knowledge"]),
    ],
    "vision": [
        ("vision-tools", ["vision", "image", "ocr", "see", "visual", "视觉", "图片", "看图", "ocr"]),
        ("vision-bridges", ["bridge", "proxy", "vlm", "multimodal", "桥接", "代理"]),
    ],
}


def matches(e, patterns):
    hay = (e["name"] + " " + e["description"] + " " + e["description_zh"]).lower()
    return any(p.lower() in hay for p in patterns)


def main():
    dry = "--dry-run" in sys.argv
    changed = 0
    for fname in FILES:
        path = DATA_DIR / fname
        data = json.loads(path.read_text())
        dirty = False
        for e in data:
            cat = e.get("category")
            rules = RULES.get(cat)
            if not rules:
                continue
            sub = None
            for sub_name, patterns in rules:
                if matches(e, patterns):
                    sub = sub_name
                    break
            if sub and e.get("subcategory") != sub:
                e["subcategory"] = sub
                dirty = True
                changed += 1
            elif not sub and e.get("subcategory"):
                del e["subcategory"]
                dirty = True
        if dirty and not dry:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"{'would assign' if dry else 'assigned'} subcategories to {changed} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
