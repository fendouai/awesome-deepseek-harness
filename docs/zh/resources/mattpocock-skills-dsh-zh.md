---
title: "mattpocock-skills-dsh-zh"
description: "Matt Pocock 25 个技能正文全译中文（技术术语保留英文并附注释）。"
keywords: "mattpocock-skills-dsh-zh, coding, skill, deepseek harness, dsh"
---
# mattpocock-skills-dsh-zh

> ⭐ **1** · ✅ 活跃 · 技能 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 编码 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [gongyijie85](https://github.com/gongyijie85) | 更新时间 | 2026-08-16 |

## 一句话介绍

> Matt Pocock 25 个技能正文全译中文（技术术语保留英文并附注释）。

## 详细介绍

[mattpocock-skills-dsh](https://github.com/gongyijie85/mattpocock-skills-dsh) 的 **中文技能版**:Matt Pocock 完整发布技能集(25 个 SKILL.md)的正文全部译为中文, 适配 **DeepSeek Harness (DSH)** 的 Cordis 插件架构。

## 📦 安装

```bash
dsh plugin --profile web add mattpocock-skills-dsh-zh
# 或 GitHub
dsh plugin --profile web add github:gongyijie85/mattpocock-skills-dsh-zh
```

## 📚 更多信息

**移植与翻译说明**

wait-what 的 `CONTEXT-MAP.md` 指引(to-tickets 的 wide-refactor 内容初版已含)。 保持原样,`description` 译为中文(便于中文触发)。 损伤模型对概念的调用。 去除;`/clear`、`/compact` 保留。 文件名不变(由 `resourceBase` 解析),未纳入本次翻译范围。

**工作原理 / 添加技能 / 许可证**

同 [mattpocock-skills-dsh](https://github.com/gongyijie85/mattpocock-skills-dsh) (host 层 `ctx.skills.registerProvider`,`lib/index.js` 零运行时依赖,原生解析 折叠 YAML frontmatter)。MIT;技能内容 © Matt Pocock,中文翻译与 DSH 移植 © mattpocock-skills-dsh-zh contributors。见 [LICENSE](LICENSE)。

## 🔗 链接

- [GitHub 仓库](https://github.com/gongyijie85/mattpocock-skills-dsh-zh)
- [完整 README](https://github.com/gongyijie85/mattpocock-skills-dsh-zh#readme)
- [返回mattpocock-skills-dsh-zh所在分类](../skills.md)
