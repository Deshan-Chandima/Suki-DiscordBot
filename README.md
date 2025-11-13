# 🎮 Discord Bot — Role Manager & Moderation Bot

A fully functional **Discord bot** built with `discord.py`, designed to manage roles, send automated messages, moderate chat content, and make your server more interactive with polls and custom commands.

---

## 🚀 Features

✅ **Welcome Message** — Automatically greets new members in DMs.  
✅ **Profanity Filter** — Deletes messages containing banned words and warns users.  
✅ **Role Management** — Assign or remove specific roles using simple commands.  
✅ **Poll System** — Create quick thumbs-up/thumbs-down polls with one command.  
✅ **Private Messaging** — Send yourself a private message via command.  
✅ **Command Replies** — The bot can reply directly to your messages.  
✅ **Role-based Access** — Restrict secret commands to users with specific roles.  
✅ **Logging Enabled** — Activity is logged to `discord.log` for debugging and monitoring.

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites
Make sure you have:
- Python 3.8 or newer  
- A Discord account and a bot token (from the [Discord Developer Portal](https://discord.com/developers/applications))  
- `pip` installed  

---

### 2️⃣ Installation

Clone this repository:

```bash
git clone https://github.com/Deshan-Chandima/discord-role-bot.git
cd discord-role-bot
```

Install dependencies:

```bash
pip install discord.py python-dotenv
```

---

### 3️⃣ Configuration

Create a `.env` file in the root directory:

```bash
DISCORD_TOKEN=your_discord_bot_token_here
```

---

### 4️⃣ Run the Bot

Start the bot with:

```bash
python bot.py
```

You should see:

```
We are Ready to go in, Suki
```

---

## 💬 Commands

| Command | Description | Example |
|----------|--------------|----------|
| `!hello` | Greets the user | `!hello` |
| `!assign` | Assigns a predefined role | `!assign` |
| `!remove` | Removes a predefined role | `!remove` |
| `!dm <message>` | Sends a DM to yourself | `!dm Hello bot!` |
| `!reply` | Replies to your message | `!reply` |
| `!poll <question>` | Creates a yes/no poll | `!poll Should we add a new channel?` |
| `!secret` | Secret command (requires special role) | `!secret` |

---




## 🧠 Logging

All logs are written to:
```
discord.log
```
This helps you monitor activity, errors, and debugging information.

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Library:** discord.py  
- **Environment Handling:** python-dotenv  
- **Logging:** Python logging module  

---

## 👨‍💻 Author

**Deshan Chandima**  


---

## ⭐ Contribute

If you’d like to contribute:
1. Fork this repo  
2. Create a new branch (`feature/my-feature`)  
3. Commit your changes  
4. Push to your branch  
5. Create a Pull Request  


