---
title: "xgone/dsh-remote"
description: "让 DeepSeek Harness 可以被安全地远程访问：账号密码认证 + MFA（TOTP）登录门禁、签名会话 Cookie、角色权限、浏览器内目录选择器、账号管理设置页。"
keywords: "xgone/dsh-remote, security, plugin, ui, deepseek harness, dsh"
---
# xgone/dsh-remote

> ⭐ **41** · 🧪 实验性 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 安全 |
| 星数 | ⭐ 41 | 状态 | 🧪 实验性 |
| 作者 | [xgone](https://github.com/xgone) | 更新时间 | 2026-08-20 |

## 一句话介绍

> 让 DeepSeek Harness 可以被安全地远程访问：账号密码认证 + MFA（TOTP）登录门禁、签名会话 Cookie、角色权限、浏览器内目录选择器、账号管理设置页。

## 详细介绍

[English](README.en.md) | **中文** **让 DeepSeek Harness 可以被安全地远程访问**：在 `dsh web` 前增加账号密码 + MFA（两步验证） 门禁，外网浏览器登录后即可使用完整功能——全程不在宿主机上弹出任何原生窗口。

## ✨ 核心特性

- **远程访问**：经反向代理（nginx / ssh 隧道 / Tailscale / Frp 等）暴露后，外部浏览器登录即用
- **登录门禁**：未登录访问任何路径都是登录页，`/api` 与 WebSocket 全部要求有效会话；密码
- **MFA 两步验证（TOTP）**：兼容 Google Authenticator / 1Password / Authy 等标准认证器，扫码
- **远程文件面板**：点击文件路径不再在宿主机桌面打开，而是按类型在右侧边栏预览——代码带语法
- **多账号（可选）**：默认仅管理员；关闭 `adminOnly` 后支持 admin / user / guest 三级权限。
- **界面跟随 DSH**：浅色 / 深色主题自动跟随，中英双语跟随 DSH 应用语言。
- **远程访问更快**：响应自动 gzip 压缩（默认仅远程），静态资源配合边缘缓存。

## 📦 安装

```bash
dsh plugin --profile web add @xgone/dsh-remote
```

## 🚀 快速开始

```bash
dsh web
```

## 📚 更多信息

**功能特性**

全部功能；选择 / 新建工作区是浏览器内的目录对话框，不会在宿主机弹窗；WebSocket 事件流全通。 scrypt 加密存储、登录失败限速、首个管理员仅限本机创建。 绑定 + 10 个一次性备用码；忘记动态码时管理员可代为关闭。 高亮与复制、Markdown 渲染排版、图片 / PDF / 视频 / 音频内联、文本与目录浏览、Word（.docx） 提取纯文本；不支持预览的文件点击直接下载。默认仅允许 DSH 主目录与工作目录，可在设置页添加 允许的目录。

**配置**

编辑 `~/.dsh/profiles/web/cordis.patch.yml` 中 `remote` 行的 config。常用项： config: enabled: true # false = 关闭门禁（被锁在门外时的逃生通道） session: secure: false # HTTPS 部署改为 true adminOnly: true # false = 启用多角色（admin/user/guest）与账号管理 bootstrap: # 可选：预置首个管理员（仅账号库为空时生效） username: admin password: '换成一个强密码' 默认值即开箱可用；完整配置项（会话、MFA、限速、gzip、文件面板等）见 [docs/REFERENCE.md](docs/REFERENCE.md#13-完整配置参考cordispatchyml)。

## 🔗 链接

- [GitHub 仓库](https://github.com/xgone/dsh-remote)
- [完整 README](https://github.com/xgone/dsh-remote#readme)
- [返回xgone/dsh-remote所在分类](../plugins.md)
