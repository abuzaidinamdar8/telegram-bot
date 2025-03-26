from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler(timezone=pytz.timezone("UTC"))  # Explicit UTC timezone
scheduler.start()


BOT_TOKEN = "7765642881:AAGnyNamwhVfLUgVFGkcM3UyIQSEuT7MpJo"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I'm your abuzaid")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
