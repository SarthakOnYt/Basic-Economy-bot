
# Discord Economy Bot

A simple Discord bot that allows users to participate in a simulated economy by earning and managing virtual currency.

## Features

* Users can earn virtual currency through commands like `?work`.
* Users can view their current balance and the balance of others using the `?bal` command.
* Users can steal virtual currency from others (with limitations) using the `?rob` command.
* Users can receive a daily reward using the `?daily` command.
* Users can deposit and withdraw virtual currency from their bank using the `?dep` and `?wth` commands.

**Important Note:** This is a basic implementation and does not include features like item purchases or transactions between users.

## Installation

1. **Create a Discord Bot Application:**
   - Visit the Discord Developer Portal (https://discord.com/developers/applications) and create a new application.
   - Under the "Bot" section, create a bot user and obtain its token.

2. **Install Required Libraries:**
   ```bash
   pip install discord
