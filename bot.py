from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def get_main_menu():
    return ReplyKeyboardMarkup(
        [
            ["👤 Shaxsiy kabinet", "✂️ Xizmatlar"],
            ["📅 Bandlovni bekor qilish", "🎁 Cashback"]
        ],
        resize_keyboard=True
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! 'Barber Shaxzod' botiga xush kelibsiz.\nBuyruqlardan birini tanlang 👇",
        reply_markup=get_main_menu()
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token("7683754796:AAFsefo83v8AKsnB9cu1_eB-HB7LLoe83gs").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
