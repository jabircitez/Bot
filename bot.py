from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7931349521:AAHIx9M8foNpfR8hgKNb0y3jRKezpud51RI"

async def start(update, context):
    await update.message.reply_text("ربات فعال است استاد JABIR OWNER ❤️🔥")

async def echo(update, context):
    await update.message.reply_text("ربات فعال است استاد JABIR OWNER ❤️🔥")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot is running on Render...")
    app.run_polling()

if __name__ == "__main__":
    main()
