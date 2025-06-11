Podcast Alternative Titles Telegram Bot

This Telegram bot connects to the podcast backend API and generates alternative episode titles on user request.

Features
	•	Users send a command /alt <episode_id> <prompt>
	•	The bot sends the prompt to the backend API endpoint /episodes/{episode_id}/generate_alternative
	•	The bot replies with the AI-generated alternative title

Setup and Run
	1.	Clone this bot repository or create a folder inside your project for the bot code.
	2.	Create a .env file with these variables:

How to create a Telegram bot and get a token
	1.	Open Telegram and find the BotFather bot.
	2.	Use the command /newbot and follow instructions to create your bot.
	3.	Copy the bot token provided by BotFather.
	4.	Add this token to your .env file as TELEGRAM_TOKEN.

TELEGRAM_TOKEN=your_telegram_bot_token
BOT_API_URL=http://localhost:8000  # or your deployed API base URL
    

Install dependencies:
pip install python-telegram-bot requests python-dotenv


Run the bot:
python bot.py


How to Use

Send a message in Telegram to your bot like:

/alt 1 Rewrite the title for Gen Z

	•	1 is the episode ID
	•	The rest is the prompt for the alternative title generation

The bot will reply with alternative title suggestions.
