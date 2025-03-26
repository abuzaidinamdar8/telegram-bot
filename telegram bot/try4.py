from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os

# ✅ Use absolute path for the media folder
MEDIA_FOLDER = r"C:\Users\ABUZAID\OneDrive\Desktop\TELEGRAM BOT"  
FIRST_IMAGE = "fam.jpeg"  # First image sent after start
PUNE_TRIP_MEDIA = [   "fam1.jpeg", "fam2.jpeg", "fam3.jpeg", "fam 4.jpeg", "fam 5.jpeg", "fam 6.jpeg", "fam 7.jpeg", "fam 8.jpeg",]  # Add all images/videos for Pune Trip

async def start(update: Update, context: CallbackContext) -> None:
    messages = [
        "HELLO I AM Abuzaid'S Sir Bot!",
        "I am a bot that will provide images  of the family trip...",
        "Hello! type 'image' to receive the image."
    ]
    for msg in messages:
        await update.message.reply_text(msg)

async def send_image(update: Update, context: CallbackContext) -> None:
    image_path = os.path.join(MEDIA_FOLDER, FIRST_IMAGE)
    if os.path.exists(image_path):
        with open(image_path, "rb") as img:
            await update.message.reply_photo(photo=img)
        await update.message.reply_text("Want to relive past trips? Type the 'Pune Trip' name to see all images!")
    else:
        await update.message.reply_text(f"Image not found at {image_path}")

async def send_pune_trip_media(update: Update, context: CallbackContext) -> None:
    for media_file in PUNE_TRIP_MEDIA:
        media_path = os.path.join(MEDIA_FOLDER, media_file)
        if os.path.exists(media_path):
            with open(media_path, "rb") as media:
                if media_file.endswith(".mp4"):
                    await update.message.reply_video(video=media)
                else:
                    await update.message.reply_photo(photo=media)
        else:
            await update.message.reply_text(f"File not found: {media_file}")


def main():
    TOKEN = "7765642881:AAGnyNamwhVfLUgVFGkcM3UyIQSEuT7MpJo"   # Replace with your actual bot token
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("(?i)^image$"), send_image))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("(?i)^Pune Trip$"), send_pune_trip_media))
    
    app.run_polling()

if __name__ == "__main__":
    main()
