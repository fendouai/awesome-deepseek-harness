# dsh-passwords

**Login gateway (password door) for the DeepSeek Harness web UI.**

[dsh-passwords](https://github.com/slywalker2006/dsh-passwords) turns DeepSeek Harness into a multi-tenant platform: anyone hitting the web UI must pass a login page first, and the owner manages accounts & per-subuser permissions from the dsh settings page.

## Features

- **First-run setup** — create the owner account on the first visit (single-time initialization, setup key guarded)
- **Multi-user accounts** — owner + subusers, managed from the dsh settings panel
- **Remote access** — safe to expose on a public server / cloud VM
- **Per-subuser permissions & quotas** — allowed workspaces/folders, hourly token cap, daily usage limit, upload / git-download switches, sandbox level
- **Security** — bcrypt password hashing, AES-256-GCM at-rest encryption, brute-force lockout with backoff, audit log, CSRF protection, TLS 1.2+ with 80→443 redirect and automatic Let's Encrypt certificates

## Install

```bash
# one-click (Debian/Ubuntu server)
curl -fsSL https://raw.githubusercontent.com/slywalker2006/dsh-passwords/main/install.sh | sudo bash

# or as a dsh plugin
npm i -g dsh-passwords
```

## Status

✅ active · BSD-3-Clause · TypeScript
