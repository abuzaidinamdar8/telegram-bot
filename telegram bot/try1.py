from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7765642881:AAGnyNamwhVfLUgVFGkcM3UyIQSEuT7MpJo"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am Abuzaid Sir bot. Ask me anything.")

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
