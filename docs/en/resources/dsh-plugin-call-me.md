---
title: "dsh-plugin-call-me"
description: "Your DeepSeek Harness agent rings your actual phone: it asks out loud, you answer out loud, and what you said steers the run."
keywords: "dsh-plugin-call-me, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plugin-call-me

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [radres](https://github.com/radres) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multi-agent |

## One-liner

> Your DeepSeek Harness agent rings your actual phone: it asks out loud, you answer out loud, and what you said steers the run.

## About

**Your DeepSeek Harness agent rings your actual phone.** It asks the question out loud, you answer out loud, and what you said goes straight back into the run. Every other reachability plugin sends you a notification. This one places a phone call. Your phone rings through CallKit like any other call, you pick it up, a voice reads the agent's question, you say "yes, ship it, but hold the migration", and the transcript of that sentence is what the agent reads next. No tab to come back to, no app to open, no keyboard. you walk away -> agent finishes -> your phone rings -> you answer out loud -> the run continues

## ✨ Key Features

- App Store: https://serdaroztetik.com/aiphone/go/dsh
- Privacy policy: https://serdaroztetik.com/aiphone/privacy
- Also available for Claude Code and as a remote MCP server: https://github.com/radres/call-me
- **iPhone only.** There is no Android app.
- **`approval.mode: answer` holds the desktop prompt while the phone rings.**
- **A voice answer is a transcript.** The approval path accepts only a clear yes
- There is no self-hosted deployment.

## 📦 Install

```bash
dsh plugin --profile web add github:radres/dsh-plugin-call-me
```

## 🚀 Quick Start

```bash
- insert:
    - id: call-me
      name: dsh-plugin-call-me
      config:
        number: '5551234567'
```

## 📚 Learn more

**Install**

dsh plugin --profile web add github:radres/dsh-plugin-call-me Plain JavaScript, no build step, so a git install needs no `allowBuilds` permission. Then pair a phone: 1. Get the **/call-me** app: https://serdaroztetik.com/aiphone/go/dsh (iPhone) 2. Open it. It shows a 10-digit number. 3. Tell the plugin about it, in the profile's `cordis.patch.yml`: - id: call-me name: dsh-plugin-call-me config: nu

**Prove the phone half in five seconds, before installing anyt**

curl -sS https://serdaroztetik.com/aiphone/ring \ -H 'content-type: application/json' \ -d '{"to":"<YOUR_10_DIGITS>","text":"Can you hear me?","from":"dsh"}' That is the same call the plugin makes. It blocks, rings your phone, and prints what you said back.

**Configuration**

Every field has a default that works. Add only what you want to change, and remember that a patch row replaces the whole `config` value, so restate the keys you need. Ring-the-phone-when-I-stop, and let me answer by voice: - id: call-me name: dsh-plugin-call-me config: number: '5551234567' turnEnd: mode: call graceSeconds: 60 approval: mode: answer

## 🔗 Links

- [GitHub Repository](https://github.com/radres/dsh-plugin-call-me)
- [Full README](https://github.com/radres/dsh-plugin-call-me#readme)
- [Back to the Plugins list](../plugins.md)
