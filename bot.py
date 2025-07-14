from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7683754796:AAFsefo83v8AKsnB9cu1_eB-HB7LLoe83gs"

# Asosiy menyu
def get_main_menu():
    return ReplyKeyboardMarkup(
        [
            ["✂️ Xizmatlar", "👤 Kabinet"],
            ["📅 Bandlovni bekor qilish", "🎁 Cashback"],
            ["📸 Instagram", "📲 Telegram"],
            ["📍 Lokatsiya", "ℹ️ Yordam"]
        ],
        resize_keyboard=True
    )

# Faqat menyu tugmasi bosilganda ishlaydi
async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Quyidagilardan birini tanlang:",
        reply_markup=get_main_menu()
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token("7683754796:AAFsefo83v8AKsnB9cu1_eB-HB7LLoe83gs").build()

    # Faqat "Menu" tugmasidan kelgan matnlar
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^Menu$"), show_menu))

    app.run_polling()
