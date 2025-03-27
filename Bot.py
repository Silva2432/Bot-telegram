from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "SEU_TOKEN_AQUI"

# Comando /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Olá! Eu sou seu bot.")

# Responder a mensagens de texto
async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot está rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
