from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum!\nXush kelibsiz! 👋\nBu test bosqichidagi bot."
    )

# Botni ishga tushirish
if __name__ == "__main__":
    app = ApplicationBuilder().token("7683754796:AAFsefo83v8AKsnB9cu1_eB-HB7LLoe83gs").build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()
