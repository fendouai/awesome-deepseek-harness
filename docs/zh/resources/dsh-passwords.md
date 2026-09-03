---
title: "dsh-passwords"
description: "dsh-passwords: DeepSeek Harness login gateway - first-run setup, at-rest encryption, brute-force lockout, audit log, HTTPS"
keywords: "dsh-passwords, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-passwords

> ⭐ **17** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 17 | 状态 | ✅ 活跃 |
| 作者 | [slywalker2006](https://github.com/slywalker2006) | 更新时间 | 2026-08-20 |

## 一句话介绍

> dsh-passwords: DeepSeek Harness login gateway - first-run setup, at-rest encryption, brute-force lockout, audit log, HTTPS

## 详细介绍

[English](README_en.md) | 简体中文                       给 DeepSeek Harness 加一层服务器级认证网关，使其成为可公网部署的多租户平台 登录认证 · 自动 HTTPS · 多租户权限 · 会话授权 · 审计加密 · 中英双语 [功能](#功能) · [快速开始](#快速开始) · [首次配置](#首次配置) · [卸载](#卸载) · [自动 HTTPS](#自动-https) · [部署拓扑](#部署拓扑) · [配置参考](#配置参考) · [常见问题](#常见问题) · [安全与隐私](#安全与隐私) · [参与贡献](#参与贡献) --- dsh 自带的网页界面没有登录与权限控制，公网部署后任何拿到地址的人都能直接使用。dsh-passwords 在 dsh 前面运行一个网关：未登录访问只见到登录页，登录后按账号执行权限与配额控制。项目收录于 [Awesome DeepSeek Harness](https://github.com/0xsline/awesome-deepseek-harness#security--governance)（Security & Governance）与 [Awesome DSH Plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin#security--permissions)（Security & Permissions）。

## ✨ 核心特性

- **登录认证**：首次配置创建主用户，之后所有访问先过登录页；会话 12 小时有效
- **自动 HTTPS**：向 Let's Encrypt 自动签发并续期证书，80 端口自动跳转 443，无需配置
- **多租户**：一个主用户加任意多个子用户，账号管理全部在 dsh 设置页完成
- **权限与配额**：工作区白名单、逐会话开关、每小时 token 上限、每日时长上限、沙盒三档、上传与下载开关、封禁
- **会话授权**：工作区权限不自动包含其中全部会话，主用户逐会话授予；归档状态在工作区列表与会话列表间保持一致
- **运维视图**：主用户可查看全部工作区与会话，下载非敏感普通文件
- **审计与安全**：登录限流与锁定、审计日志、SQLite 静态加密、登出即吊销会话
- **设置页卡片**：远程设置补丁重载、软件更新、账号与权限管理、站内留言，全部中英双语

## 📦 安装

```bash
# 1. Linux / macOS 一键安装
curl -fsSL https://raw.githubusercontent.com/slywalker2006/dsh-passwords/main/install.sh | bash

# 2. 先 clone 再安装
git clone https://github.com/slywalker2006/dsh-passwords && cd dsh-passwords
bash install.sh

# 3. npm 全局安装，适用于任意平台
npm install -g dsh-passwords
dsh-passwords install
```

## 🚀 快速开始

```bash
# 4. Docker
docker run -d \
  --name dsh-passwords \
  --restart unless-stopped \
  --env-file .env \
  -p 127.0.0.1:3088:3088 \
  -v dsh-home:/data/dsh \
  -v dsh-passwords-state:/data/dsh-passwords \
  skywalker237234/dsh-passwords
```

## 📚 更多信息

**安装**

五种安装方式，任选其一。宿主机安装会自动完成装依赖、编译、生成 SETUP_KEY、注册 dsh 插件、应用远程设置补丁；已有 `.env` 时不覆盖，重复运行安全。

**1. Linux / macOS 一键安装**

curl -fsSL https://raw.githubusercontent.com/slywalker2006/dsh-passwords/main/install.sh | bash

**2. 先 clone 再安装**

git clone https://github.com/slywalker2006/dsh-passwords && cd dsh-passwords bash install.sh

**3. npm 全局安装，适用于任意平台**

npm install -g dsh-passwords dsh-passwords install Windows 下载仓库里的 `install.bat` 双击运行。默认安装到 `%USERPROFILE%\dsh-passwords`。

## 🔗 链接

- [GitHub 仓库](https://github.com/slywalker2006/dsh-passwords)
- [完整 README](https://github.com/slywalker2006/dsh-passwords#readme)
- [返回dsh-passwords所在分类](../plugins.md)
