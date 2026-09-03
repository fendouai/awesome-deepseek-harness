---
title: "deepseek-harness-app (ipfred)"
description: "DeepSeek Harness 桌面应用。"
keywords: "deepseek-harness-app (ipfred), desktop, client, deepseek harness, dsh"
---
# deepseek-harness-app (ipfred)

> ⭐ **29** · ✅ 活跃 · 客户端 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 29 | 状态 | ✅ 活跃 |
| 作者 | [ipfred](https://github.com/ipfred) | 更新时间 | 2026-08-15 |

## 一句话介绍

> DeepSeek Harness 桌面应用。

## 详细介绍

把 DeepSeek Harness 网页端 `dsh web`，http://127.0.0.1:3080 用 [Pake](https://github.com/tw93/Pake)（Rust/Tauri）打包成 Windows / macOS / Linux 三平台桌面 App，并用 GitHub Actions 自动构建、发布到 GitHub Releases，方便任何人直接下载安装包。

## ✨ 核心特性

- 自己的电脑用：先 `dsh web`，再打开 App（对应下面的"本地打包"）。
- 分发给别人用：别人的电脑也要装 dsh 并启动它 —— 如果希望"装完即用"，见文末【进阶：把 dsh 服务打进安装包】。

## 📦 安装

```bash
# 方式一：不安装，直接跑（官方推荐；npx 会自动拉取最新版）
npx @deepseek-ai/dsh web

# 方式二：全局安装后运行（适合经常用）
npm install -g @deepseek-ai/dsh        # 或 pnpm add -g @deepseek-ai/dsh
dsh web

# 方式三：从源码跑
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness && pnpm install && pnpm run build
pnpm dsh web
```

## 🚀 快速开始

```bash
# 1. 安装 Pake（npm/pnpm 均可）
pnpm install -g pake-cli

# 2. 启动 dsh web
dsh web

# 3. 一键打包（内含启动检查，也可直接手动跑 pake 命令）
./scripts/build-locally.sh 0.1.0

# 4. 安装：产物在当前目录
#    macOS  双击 DeepSeekHarness_*.dmg
#    Windows 双击 DeepSeekHarness_x64.msi（AMD/Intel）或 DeepSeekHarness_arm64.msi（骁龙等 ARM）
#    Linux  sudo dpkg -i deepseek-harness_*.deb  或 运行 *.AppImage
```

## 📚 更多信息

**⚠️ 先理解原理（重要）**

这个 App 是"网页外壳"：它把 `http://127.0.0.1:3080` 这个地址包装成原生窗口。 dsh 的网页端不是静态网站（需要 dsh 服务注入启动数据），**所以运行时本机必须先启动 `dsh web`，再打开这个 App**。

**使用流程（给别人下载）**

1. 把这个目录推成一个 GitHub 仓库：`git init && git add . && git commit -m init && git push` 2. 打 tag 触发自动构建 + 发布： ```bash git tag v1.0.0 git push origin v1.0.0 ``` 3. 等约 10~25 分钟（首次编译较久，后续有缓存会快很多）。 构建完成自动出现在仓库 **Releases** 页面，三平台安装包直接可下载： - `DeepSeekHarness.dmg`（macOS，**universal 双架构**：Intel + Apple Silicon 一份通吃） - `DeepSeekHarness_x64.msi` / `DeepSeekHarness_arm64.msi`（Windows x64 与 ARM64 原生） - `deepseek-ha

**工作流设计要点**

一个平台失败不影响其他平台。 失败只会降级为默认值，不会让构建失败 —— CI 机器上 `127.0.0.1:3080` 不存在也没关系。 二次构建从 ~20 分钟降到 2~3 分钟。

**五、进阶：把 dsh 服务打进安装包（开箱即用）**

如果希望别人**装了就能用**（不用自己装 dsh/启动服务），需要把 dsh 命令行程序作为 Tauri **sidecar** 打进应用，App 启动时自动拉起服务、等端口就绪后加载页面： 1. 用 pake 生成后，在 `src-tauri/tauri.conf.json` 配置外部二进制： ```json "bundle": { "externalBin": ["binaries/dsh-server"] } ``` （构建时对应平台命名为 `dsh-server-<target-triple>`，随包分发 dsh 及其 web 资源。） 2. 在 `src-tauri/src/main.rs`（或 lib.rs）里启动 sidecar： ```rust let (mut rx, _child) = app.shell().sidecar("dsh-server")?.spawn(

## 🔗 链接

- [GitHub 仓库](https://github.com/ipfred/deepseek-harness-app)
- [完整 README](https://github.com/ipfred/deepseek-harness-app#readme)
- [返回deepseek-harness-app (ipfred)所在分类](../clients.md)
