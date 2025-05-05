import firebase_admin
from firebase_admin import credentials, db

def init_firebase():
    cred = credentials.Certificate("path/to/firebase-key.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://seu-projeto.firebaseio.com"})

def get_next_match():
    ref = db.reference('proximos_jogos')
    return ref.get()