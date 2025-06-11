import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
BOT_API_URL = os.getenv('BOT_API_URL')


async def alt_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        episode_id = int(context.args[0])
        prompt = ' '.join(context.args[1:])

        payload = {
            'target': 'title',
            'prompt': prompt
            }
        url = f"{BOT_API_URL}/episodes/{episode_id}/generate_alternative"

        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()

        result = data['generated_alternative']
        await update.message.reply_text(result)

    except (IndexError, ValueError):
        await update.message.reply_text('Usage: /alt <episode_id> <prompt>')
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler('alt', alt_command))
    app.run_polling()
