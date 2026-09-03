---
title: "dsh-update-checker"
description: "DeepSeek Harness 主程序与插件更新管理：npm/GitHub 双源 semver 比对、多语言横幅、一键更新（主程序自动备份/校验/回滚，插件临时目录安装）、更新后看门狗重启。Update management for DeepSeek Harness and its plugins: dual-source semver checks, locale banner, one-click updates with backup/rollback, watchdog restart."
keywords: "dsh-update-checker, vision, plugin, coding, git, deepseek harness, dsh"
---
# dsh-update-checker

> ⭐ **13** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 13 | Status | ✅ active |
| Author | [Airmetro](https://github.com/Airmetro) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, git |

## One-liner

> DeepSeek Harness 主程序与插件更新管理：npm/GitHub 双源 semver 比对、多语言横幅、一键更新（主程序自动备份/校验/回滚，插件临时目录安装）、更新后看门狗重启。Update management for DeepSeek Harness and its plugins: dual-source semver checks, locale banner, one-click updates with backup/rollback, watchdog restart.

## About

A permanent Cordis plugin for the [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) Web GUI that **auto-checks for new DeepSeek Harness releases and installed third-party plugin updates** (the former standalone `dsh-plugin-checker` was merged in v1.1.0), asks the user, and one-click updates with success/failure feedback.

## ✨ Key Features

- **Full update lifecycle** — check, backup, update, **rollback**, and restart, all in one plugin.
- **Main program check** — compares the installed `@deepseek-ai/dsh` against the npm latest (full packument, **stable-first**, semver-aware — pre-release builds l
- **Third-party plugin check** — scans installed non-official plugins (layout-agnostic, incl. pnpm-hoisted `node_modules`), cross-compares each against **npm + Gi
- **Working GitHub channel** — dedicated HTTPS client for GitHub domains (tolerates self-signed local proxies; the npm registry still uses strict TLS), with redir
- **In-GUI banner** — locale-aware (zh/en follows the DSH UI language), states update / up-to-date / failure, with a suppression flag and a **change brief** (vX→v
- **One-click update with safety** — main program: dry-run guard (abort if the plan contains `remove`) → snapshot backup (version manifests + a `main-snapshot` co
- **Real rollback** — main program via `POST /rollback`, plugins via `POST /plugin-rollback`; `GET /backups.json` lists both.
- **Restart with watchdog** — launcher derived from the current process argv, kill by PID + port, recovery confirmed by port listening + an HTTP 200 probe (`GET /

## 🚀 Quick Start

```bash
# $DSH_HOME/profiles/web/cordis.patch.yml
- insert:
    - id: dsh-update-checker
      name: 'dsh-update-checker'
```

## 📚 Learn more

**Install & mount**

The package is a [profile bundle](https://github.com/deepseek-ai/deepseek-harness) (its manifest declares `dsh.bundle.patch`).

**Safe option A — install in a temp dir, then copy only this p**

npm i dsh-update-checker --prefix <temp-dir> --no-save cp -r <temp-dir>/node_modules/dsh-update-checker $DSH_HOME/profiles/node_modules/

**Configuration & portability**

All paths are **auto-detected at runtime — nothing is hardcoded**: - systemd / `npm -g` escape hatch: if auto-detection ever misses your setup, set `DSH_DEPLOY_ROOT` to the directory that contains `node_modules/@deepseek-ai/dsh` (e.g. `<npm prefix>/lib` on Linux).

**Platform & install-layout support**

- **Windows only** — the restart flow spawns PowerShell. - Main-program update adapts: in-place `npm install` when the deploy root has a `package.json`, `npm install -g` otherwise; both run the dry-run guard and re-read the installed version afterwards. - Plugin updates — temp-dir install + copy, npm 11/12+ compatible.

## 🔗 Links

- [GitHub Repository](https://github.com/Airmetro/dsh-update-checker)
- [Full README](https://github.com/Airmetro/dsh-update-checker#readme)
- [Back to the Plugins list](../plugins.md)
