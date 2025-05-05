from bot.database import db  # Reaproveita a conexão do Firebase

class TorcidaMessages:
    @staticmethod
    def save(usuario, mensagem):
        ref = db.reference('torcida')
        ref.push({"usuario": usuario, "mensagem": mensagem})