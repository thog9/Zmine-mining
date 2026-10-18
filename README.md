# Zmine Bot Scripts 🚀

This collection of Python scripts automates mining, X (Twitter) social tasks, and quiz rewards on the **ZMINE** platform — a web mining ecosystem where users earn **Mh** by running 24h mining sessions, completing social tasks, and solving SI quizzes.

🔗 Register: [ZMINE](https://zmine.si/register?ref=ADNNMKJW)

---

## ✨ Features Overview

### General Features

- **Multi-Account Support**: Reads accounts from `accounts.json` (single source of truth) and processes them in parallel.
- **Colorful CLI**: Uses `colorama` for a boxed, color-coded menu with bilingual icons and 80-char borders.
- **Asynchronous Execution**: Built with `asyncio` + `Semaphore` for efficient concurrent processing (configurable thread count).
- **Error Handling**: Retry logic for API failures, with automatic re-login using `loginKey` when the session cookie expires.
- **Bilingual Support**: Supports both English and Vietnamese output.
- **Proxy Support**: Supports HTTP, HTTPS, SOCKS4 and SOCKS5 proxies via `proxies.txt`, plus a per-account pinned proxy.
- **Shared Account Store**: `accounts.txt` is a readable backup regenerated 100% from `accounts.json` on every save.
- **X (Twitter) Tokens**: `tokenX.txt` (`auth_token:ct0`) is used for linking accounts and running social tasks.
- **Credential Safety**: `LoginKey` is never printed on screen (it is still saved in `accounts.json` / `accounts.txt`).
- **Central Menu**: `main.py` runs every tool in its own event loop and returns to the menu when done.
- **No Prompts Needed**: Every tool reads its input files and runs; only `register.py` asks for the account count.

---

### Included Scripts

✨ **Central Menu** (`main.py`)

- ✅ Language selection (Tiếng Việt / English)
- ✅ Run any tool back-to-back without restarting the process
- ✅ Banner with website, Discord and Telegram channel

✨ **Register** (`scripts/register.py`)

- ✅ Bulk account registration with natural auto-generated display names
- ✅ Default referral code `ADNNMKJW` applied automatically
- ✅ Saves `loginKey` + recovery phrase into `accounts.json` / `accounts.txt`

✨ **Login / Import** (`scripts/login.py`)

- ✅ Imports existing accounts from `pvkey.txt` (one `loginKey` per line)
- ✅ Updates/refreshes cookies for accounts already in `accounts.json`
- ✅ Merges duplicates and rewrites `accounts.txt` from the JSON
- ✅ `loginKey|proxy` pins a dedicated proxy for that account

✨ **Mining** (`scripts/mining.py`)

- ✅ Activates the 24h mining session for every account
- ✅ Detects accounts already mining and skips them
- ✅ Displays hashpower / balance after activation

✨ **Connect X** (`scripts/connectX.py`)

- ✅ Full X (Twitter) OAuth linking flow for each account
- ✅ Matches `tokenX.txt` entries to accounts by `@username` or line order
- ✅ Detects accounts already linked on the server and skips them
- ✅ Auto-heals the local `xLinked` cache from the server state
- ✅ Debug output for HTTP status / redirect / state / code when a link fails

✨ **Social X Tasks** (`scripts/socialX.py`)

- ✅ Follow / like / repost / quote / reply tasks, verified via `POST /api/v1/social/verify`
- ✅ Repost / quote / reply over X internal GraphQL (X removed the old v1.1 endpoints)
- ✅ Re-checks unconfirmed tasks after a settle delay, so credited work is never reported as failed
- ✅ Delay between actions and bot-flag retry to stay under X's radar
- ✅ Reads the server state as authority for `xLinked`
- ✅ Built-in GraphQL query IDs, with an optional `x_graphql.json` override if X rotates them

✨ **SI Quiz** (`scripts/quiz.py`)

- ✅ 12 questions/day loop: `GET /si/tasks/next` → solve → `POST /si/tasks/answer`
- ✅ Rule engine (regex + math) covering the most common question forms
- ✅ AI fallback with provider chain via `ai.json`, plus `python scripts/quiz.py test-ai`

---

## 🛠️ Prerequisites

Before running the scripts, ensure you have the following installed:

- **Python 3.10+**
- **pip** (Python package manager)
- **Dependencies**: Install via `pip install -r requirements.txt`
- **pvkey.txt**: Add `loginKey` values (one per line) to import existing accounts
- **tokenX.txt**: Add X (Twitter) cookies (`auth_token:ct0`) to link accounts and run social tasks
- **proxies.txt** (optional): Add proxy addresses for network requests
- **ai.json** (optional): Add an AI key for the quiz fallback

---

## 📦 Installation

1. **Clone or download this repository:**
   ```sh
   git clone https://github.com/thog9/Zmine-mining.git
   cd Zmine-mining
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Prepare input files:**

   Copy the sample files and fill in your own data:
   ```sh
   cp pvkey.txt
   cp tokenX.txt
   cp proxies.txt
   cp ai.json
   ```

   `pvkey.txt` — one account per line (`loginKey`, optional pinned proxy):
   ```
   LOGINKEY_1
   LOGINKEY_2
   ```

   `tokenX.txt` — one X account per line (`auth_token:ct0`):
   ```
   AUTH_TOKEN_1:CT0_1 or AUTH_TOKEN_1|CT0_1
   AUTH_TOKEN_2:CT0_2 or AUTH_TOKEN_2|CT0_2
   ```

   `proxies.txt` (optional) — one proxy per line, 4 formats accepted:
   ```
   ip:port
   ip:port:user:pass
   socks5://user:pass@host:port
   http://user:pass@host:port
   ```

   `ai.json` (optional) — AI key for the quiz fallback:
   ```json
   { "groq": "GROQ_API_KEY" }
   ```
   Providers are tried in order: `groq` → `gemini` → `openrouter` → `ollama` (local). Without `ai.json`, only the rule engine runs.

4. **Run:**
   ```sh
   python main.py
   ```
   - Choose a language (Vietnamese / English).
   - Select the script you want to run.

**Language Selection:**
- Choose between Vietnamese (Tiếng Việt) and English.
- All scripts support bilingual output.

---

## 📁 Project Structure

```
Zmine-automation/
├── main.py                # Central menu system
├── pvkey.txt              # LoginKeys (input, optional)
├── tokenX.txt             # X (Twitter) tokens (input, optional)
├── proxies.txt            # Proxies (input, optional)
├── ai.json                # AI keys for quiz fallback (input, optional)
├── accounts.json          # Account store (auto-generated)
├── accounts.txt           # Readable backup (auto-generated from JSON)
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── scripts/               # Individual scripts
    ├── register.py        # Account registration bot
    ├── login.py           # Login / import bot
    ├── mining.py          # 24h mining activation bot
    ├── connectX.py        # X (Twitter) account linking bot
    ├── socialX.py         # X (Twitter) social task bot
    └── quiz.py            # SI quiz solver (rule engine + AI fallback)
```

---

## 📨 Contact

Connect with us for support or updates:

- **Telegram**: [thog099](https://t.me/thog099)
- **Channel**: [CHANNEL](https://t.me/thogairdrops)
- **Group**: [GROUP CHAT](https://t.me/thogchats)
- **Discord**: [DISCORD](https://discord.gg/MnmYBKfHQf)
- **X**: [Thog](https://x.com/thog099)

---

## ☕ Support Us

Love these scripts? Fuel our work with a coffee!

🔗 BUYMECAFE: [BUY ME CAFE](https://buymecafe.vercel.app/)

🔗 WEBSITE: [BUY SCRIPTS](https://thogtoolhub.com/)
