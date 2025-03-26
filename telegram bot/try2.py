from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os

# ✅ Use absolute path for the image folder
IMAGE_FOLDER = r"C:\Users\ABUZAID\OneDrive\Desktop\TELEGRAM BOT"  
IMAGE_NAME = "img5.jpg"  # Ensure this matches the exact file name

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! Send 'image' to receive the specific image.")

async def send_image(update: Update, context: CallbackContext) -> None:
    image_path = os.path.join(IMAGE_FOLDER, IMAGE_NAME)
    print(f"Checking file path: {image_path}")  # Debugging output
    if os.path.exists(image_path):
        with open(image_path, "rb") as img:
            await update.message.reply_photo(photo=img)
    else:
        await update.message.reply_text(f"Image not found at {image_path}")

def main():
    TOKEN = "7765642881:AAGnyNamwhVfLUgVFGkcM3UyIQSEuT7MpJo" # Replace with your actual bot token
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("(?i)image"), send_image))
    
    app.run_polling()

if __name__ == "__main__":
    main()
