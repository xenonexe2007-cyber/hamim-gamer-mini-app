import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
WEBAPP_URL = os.getenv("WEBAPP_URL", "").strip()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not WEBAPP_URL.startswith("https://"):
        await update.effective_message.reply_text(
            "Mini App এখনো সেটআপ হয়নি। Admin-কে WEBAPP_URL (HTTPS) সেট করতে বলুন।"
        )
        return

    keyboard = [[
        InlineKeyboardButton(
            "🎮 OPEN HAMIM GAMER",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]
    await update.effective_message.reply_text(
        "⚡ HAMIM GAMER — NEON EDITION\n\n"
        "Welcome, Gamer!\n"
        "নিচের বাটনে চাপ দিয়ে Mini App খুলুন।",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is missing")
    if not WEBAPP_URL.startswith("https://"):
        raise RuntimeError("WEBAPP_URL must be a public HTTPS URL")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("HAMIM GAMER bot is starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
