import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)


# =========================
# تنظیمات
# =========================

BOT_TOKEN = "8882897095:AAFu1y-HieT8uW_8WT1cdjajnKzkM4opqhA"

GAME_URL = os.getenv(
    "GAME_URL",
    "https://USERNAME.github.io/REPOSITORY/"
)


# =========================
# /start
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🎮 اجرای بازی",
                web_app=WebAppInfo(url=GAME_URL)
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "سلام 👋\n\n"
        "به بازی خوش اومدی!\n"
        "برای شروع روی دکمه زیر بزن 👇",
        reply_markup=reply_markup
    )


# =========================
# اجرای ربات
# =========================

def main():

    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN تنظیم نشده است."
        )

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    print("🤖 Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
