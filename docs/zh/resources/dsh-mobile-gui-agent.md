---
title: "dsh-mobile-gui-agent"
description: "Android Mobile GUI Agent plugin for DeepSeek Harness with ADB control, iterative verification, approvals, and a Web mobile view"
keywords: "dsh-mobile-gui-agent, mobile, client, coding, multi-agent, ui, deepseek harness, dsh"
---
# dsh-mobile-gui-agent

> ⭐ **9** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 移动端 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [kunjinkao-os](https://github.com/kunjinkao-os) | 更新时间 | — |

## 一句话介绍

> Android Mobile GUI Agent plugin for DeepSeek Harness with ADB control, iterative verification, approvals, and a Web mobile view

## 详细介绍

`dsh-mobile-gui-agent` is an installable DeepSeek Harness plugin for controlling Android devices through ADB. It adds a **mobile_gui_agent** entry to the Harness Web UI and drives every task through an observe → decide → act → verify loop. The repository is a single publishable npm package. The bundle patch inserts one Cordis plugin row; that plugin composes the ADB Provider, the Phone Agent Consumer, the Phone tools, the Typert Remote adapter, and the browser client under one lifecycle.

## 📦 安装

```bash
adb devices -l
dsh plugin --profile web add github:kunjinkao-os/dsh-mobile-gui-agent#v0.2.1
dsh --profile web --dump-config
dsh --profile web
```

## 🚀 快速开始

```bash
adb devices -l
```

## 📚 更多信息

**Quick start**

Connect and authorize an Android device, then install the pinned release into the Harness Web profile: adb devices -l dsh plugin --profile web add github:kunjinkao-os/dsh-mobile-gui-agent#v0.2.1 dsh --profile web --dump-config dsh --profile web The device row must report `device`. The configuration dump must contain a `# == dsh-mobile-gui-agent` layer and one `dsh-mobile-gui-agent` row. For the cl

**Demos**

Opening Android Settings and navigating to the Wi-Fi page: Opening Taobao with `deepseek_mobile`:

**Installation options**

To install a local checkout into the standard Web profile: dsh plugin --profile web add ./dsh-mobile-gui-agent dsh --profile web --dump-config dsh --profile web When running Harness from its source checkout, use `pnpm dsh` in place of `dsh`: pnpm dsh plugin --profile web add ../dsh-mobile-gui-agent pnpm dsh --profile web --dump-config pnpm dsh --profile web The dump must contain a `# == dsh-mobile

**Configuration**

The bundle supplies safe defaults in [`cordis.patch.yml`](cordis.patch.yml). Override the complete plugin row in the profile's `cordis.patch.yml` because Harness patch rows replace, rather than deep-merge, their `config` value. name: dsh-mobile-gui-agent config: adb: adbPath: adb # unicodeImeApkPath: /absolute/path/to/reviewed/ADBKeyboard.apk commandTimeoutMs: 10000 processGraceMs: 1000 screenshot

## 🔗 链接

- [GitHub 仓库](https://github.com/kunjinkao-os/dsh-mobile-gui-agent)
- [完整 README](https://github.com/kunjinkao-os/dsh-mobile-gui-agent#readme)
- [返回dsh-mobile-gui-agent所在分类](../clients.md)
