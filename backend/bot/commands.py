from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from .database import get_next_match, get_player_stats
from .utils import fetch_hltv_stats

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🔥 Bem-vindo ao FURIA Fan Chat! Use /proximojogo ou /placar.")

def proximo_jogo(update: Update, context: CallbackContext):
    match = get_next_match()  # Função que busca no banco de dados
    update.message.reply_text(f"🗓 Próximo jogo: {match['time']} vs {match['adversario']}")

def setup_handlers(dp):
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("proximojogo", proximo_jogo))