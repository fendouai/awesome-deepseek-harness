---
title: "ego-browser"
description: "Bring the ego-lite agent browser (Chromium for AI agents) into DSH with 13 structured tools."
keywords: "ego-browser, browser, plugin, automation, deepseek harness, dsh"
---
# ego-browser

> ⭐ **29** · ✅ active · plugin · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Browser control |
| Stars | ⭐ 29 | Status | ✅ active |
| Author | [Fisfzy](https://github.com/Fisfzy) | Updated | 2026-08-21 |

## One-liner

> Bring the ego-lite agent browser (Chromium for AI agents) into DSH with 13 structured tools.

## About

**DSH 版本支持**：本版本针对 **DeepSeek Harness ≥ `0.1.2-alpha.1`** 适配（2026-08-28），`engines.dsh` 声明兼容地板为 `0.1.2-alpha.1`。适配点：client 运行时改名（`@deepseek-ai/dsh-client-store`）、client 模块注册 id 与装载行名按声明包名、`dsh.client.inject` 仅声明真实模块图行、`webServer` 以嵌套注入交付（可选服务），并同步侧边栏 Tab（dsh-better-sidebar）模式。较早的 0.1.0-rc.x / 0.1.1-rc.x 宿主请使用 v0.8.0 及更早版本。 **侧边栏支持（[dsh-better-sidebar](https://www.npmjs.com/package/dsh-better-sidebar)）**：当宿主安装了 `dsh-better-sidebar`（实测 0.17.x）时，实时观察窗注册为**侧边栏原生 Tab**——「Agent 浏览器」出现在侧边栏「+」菜单中，点击即打开并随侧边栏抽屉固定展示；agent 首次调用 `ego_*` 工具时会自动打开该 Tab。未安装 `dsh-better-sidebar` 时自动回退为右下角**浮动观察球**（`#dsh-ego-fab`）模式。两种形态共用同一套 SSE 实时推流 / 点击 / 输入 / 下载捕获能力。 把 [CitroLabs/ego-lite](https://github.com/CitroLabs/ego-lite)（给 AI Agent 用的 Chromium）接入 DeepSeek Harness：以 **32 个结构化 `ego_*` 工具**驱动浏览器，并配一套**实时观察前端口**——agen

## ✨ Key Features

- **v0.8.0**：**侧边栏 Tab 集成**——当 `dsh-better-sidebar` 可用时，实时查看窗注册为侧边栏原生 Tab（而非浮动浮窗），`ego_browser` 工具首次调用自动展开；内置 `EgoBrowserTab` React 组件 + `LivePreviewController` 实
- **v0.7.0**：观察窗状态灯**干活常绿、空闲呼吸**；`ego_script` 每次运行超时 `timeoutMs` 真正生效；前端 `frameCache`/`pageMeta` 按标签清理 + 上限兜底，杜绝长会话内存增长；状态路径家目录回退改 `os.homedir()` 跨平台化；新增 `.gitatt
- **v0.6.1**：卸载不再阻塞宿主退出（自愈链路稳定）；观察窗 worker **单实例守卫** + stale 状态清理；登录/人机验证引导条可关闭且互斥；**观察窗主动跟随 agent 正在操作的页面**（不再被后台重绘页抢占视图）。
- **v0.6.0**：工程收敛——`lib/` 定为唯一源，`build` 改语法校验，杜绝"一构建全回归"。（TS 重构后源码移至 `src/`，`lib/` 为构建产物，见「开发」一节。）
- **v0.5.0**：实时 SSE 推流 + 监控窗直接操作 agent 浏览器。
- **v0.4.0**：Windows 适配。
- 完整历史见 [CHANGELOG.md](CHANGELOG.md)。

## 🚀 Quick Start

```bash
dshx install ego-browser <ego-browser.tgz>                             # tarball 或 git URL 均可
dshx list                                                # 应显示：[on] ego-browser
```

## 📚 Learn more

**安装**

dshx install ego-browser <ego-browser.tgz> # tarball 或 git URL 均可 dshx list # 应显示：[on] ego-browser 观察窗设置中可选 `captureBackend=auto|cdp|ffmpeg`（默认 `auto`，当前解析为 CDP）、画质档位、CDP FPS/JPEG 质量/最大宽度，以及 FFmpeg FPS/最大宽度/码率/编码器/自定义路径。插件先检测自定义路径、系统 PATH 和托管缓存；检测到兼容 FFmpeg 前，设置页禁止选择 FFmpeg，并提供固定版本的一键下载。GitHub 下载可用 `githubMirror` 替换 `https://github.com`，例如 `https://gh-proxy.com/github.com`。FFmpeg 码率范围为 500-20000 k

## 🔗 Links

- [GitHub Repository](https://github.com/Fisfzy/ego-browser)
- [Full README](https://github.com/Fisfzy/ego-browser#readme)
- [Back to the Plugins list](../plugins.md)
