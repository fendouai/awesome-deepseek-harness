---
title: "dsh-better-browser"
description: "DSH 真实浏览器插件：通过 Kimi WebBridge 让 Agent 操作用户已登录的浏览器，并提供 13 个 webbridge_* 工具。 / Let DSH Agents use your signed-in browser through thirteen Kimi WebBridge tools."
keywords: "dsh-better-browser, browser, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-better-browser

> ⭐ **10** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Browser control |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [titanwings](https://github.com/titanwings) | Updated | — |

## One-liner

> DSH 真实浏览器插件：通过 Kimi WebBridge 让 Agent 操作用户已登录的浏览器，并提供 13 个 webbridge_* 工具。 / Let DSH Agents use your signed-in browser through thirteen Kimi WebBridge tools.

## About

🔐  需要 Agent 操作已经登录的网站，又不想复制 Cookie 或重新登录？ 🧭  需要导航、点击、填写、截图和网络检查组成一条完整工作流？ 🧠  希望浏览器状态留在本机，而不是不断塞进模型上下文？

## 📦 Install

```bash
dsh plugin --profile web add github:titanwings/dsh-better-browser#v0.3.6
```

## 🚀 Quick Start

```bash
navigate → snapshot → click/fill → snapshot → screenshot/network
```

## 📚 Learn more

***让 Agent 使用你已经登录的真实浏览器。***

<br> <table> <tr><td align="left"> 🔐 &nbsp;需要 Agent 操作已经登录的网站，又不想复制 Cookie 或重新登录？<br> 🧭 &nbsp;需要导航、点击、填写、截图和网络检查组成一条完整工作流？<br> 🧠 &nbsp;希望浏览器状态留在本机，而不是不断塞进模型上下文？ </td></tr> </table>

**1. 安装 Kimi WebBridge**

Kimi WebBridge 是月之暗面的独立产品，本仓库不包含它的守护进程或浏览器扩展。 请先参考 Kimi 官方[产品页](https://www.kimi.com/zh-hans/products/kimi-webbridge)与 [帮助中心](https://www.kimi.com/help/kimi-webbridge)： curl -fsSL https://cdn.kimi.com/webbridge/install.sh | bash kimi-webbridge status # 期望看到 "extension_connected": true 同时需要从官方商店安装 **Kimi WebBridge** 扩展： 安装并启用扩展后保持浏览器运行，再执行 `kimi-webbridge status`。只有 `"extension_connected": true` 才表

**2. 安装 DSH 插件**

dsh plugin --profile web add github:titanwings/dsh-better-browser#v0.3.6 重启 `dsh web` 并刷新页面。模型随后即可看到 `webbridge_*` 工具。守护进程未 运行时，工具会返回 `daemon_unreachable`，不会静默降级。 --- <a id="quick-start"></a>

## 🔗 Links

- [GitHub Repository](https://github.com/titanwings/dsh-better-browser)
- [Full README](https://github.com/titanwings/dsh-better-browser#readme)
- [Back to the MCP & Integrations list](../integrations.md)
