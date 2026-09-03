---
title: "dsh-github-login"
description: "DeepSeek Harness 生态的 GitHub 可视化登录工具（零终端）：设备码流程，令牌同步 gh CLI | Visual GitHub login for the DSH ecosystem - no terminal needed"
keywords: "dsh-github-login, vision, plugin, coding, git, terminal, deepseek harness, dsh"
---
# dsh-github-login

> ⭐ **5** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [Noob-stupid](https://github.com/Noob-stupid) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, git, terminal |

## 一句话介绍

> DeepSeek Harness 生态的 GitHub 可视化登录工具（零终端）：设备码流程，令牌同步 gh CLI | Visual GitHub login for the DSH ecosystem - no terminal needed

## 详细介绍

一个零终端的 GitHub 登录小工具：打开窗口 → 生成设备码 → 授权 → 完成。 **设备码流程在窗口内（Chromium 网络栈）执行**，与你的浏览器共用同一网络通道—— 浏览器能打开 GitHub，这里就能完成登录，不受终端/代理配置差异影响。

## ✨ 核心特性

- **窗口内授权**：授权页直接内嵌在窗口里（`<webview>`），带 **前进 / 后退 / 刷新** 按钮，
- 登录成功后令牌保存在 `~/.dsh/github-auth.json`；
- 同时同步进 gh CLI 的 `~/.config/gh/hosts.yml`，**gh 命令行立即可用**（keyring 存在时 gh 以 keyring 优先）；
- 托盘常驻：随时查看账号状态 / 一键退出登录；
- 复用 GitHub CLI 的公开 OAuth client_id（`178c6fc778ccc68e1d6a`），权限范围

## 📦 安装

```bash
dsh plugin --profile web add github:Noob-stupid/dsh-github-login
```

## 🚀 快速开始

```bash
npm install        # 安装 electron（已配置国内镜像）
npm start          # 直接运行
npm run dist       # 打包为便携版单文件 exe（dist/DSH-GitHub-Login.exe）
```

## 📚 更多信息

**安装（DSH 插件模式）**

一条命令装进 DSH，并自动启用宿主端插件（提供登录状态接口 + 一键唤起登录窗口）： dsh plugin --profile web add github:Noob-stupid/dsh-github-login 宿主端环回接口： 独立工具用法（不带 DSH 也行）：

**原理**

GitHub Device Flow： 1. `POST https://github.com/login/device/code` → `user_code` + `device_code` 2. 在窗口内嵌浏览器（或外部浏览器）打开 `https://github.com/login/device`，输入 `user_code` 授权 3. 按 GitHub 给出的 `interval` 轮询 `POST https://github.com/login/oauth/access_token` 4. 拿到 `access_token` → 主进程落盘 + 写入 gh 配置 轮询严格遵循服务器间隔；网络抖动不中断（验证码 15 分钟有效期）；授权成功 即完成，用户名查询是尽力而为的补充。

## 🔗 链接

- [GitHub 仓库](https://github.com/Noob-stupid/dsh-github-login)
- [完整 README](https://github.com/Noob-stupid/dsh-github-login#readme)
- [返回dsh-github-login所在分类](../plugins.md)
