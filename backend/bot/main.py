from telegram.ext import Updater
from .commands import setup_handlers

TOKEN = "SEU_TOKEN_TELEGRAM"

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Configura os comandos
    setup_handlers(dp)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()