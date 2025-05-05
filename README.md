# 📢 FURIA CS:GO Fan Chat

![FURIA Logo]([https://upload.wikimedia.org/wikipedia/pt/thumb/d/dc/FURIA_Esports_logo.png/200px-FURIA_Esports_logo.png](https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png))

## 🚀 Visão Geral

O **FURIA CS:GO Fan Chat** é uma plataforma completa para torcedores acompanharem o time de CS:GO da FURIA, com:

- 💬 Chat em tempo real entre fãs  
- 📊 Estatísticas atualizadas dos jogadores  
- 🔔 Notificações de jogos ao vivo  
- 🤖 Integração com Telegram  

---

## 💻 Tecnologias Utilizadas

| Componente     | Tecnologias |
|----------------|-------------|
| **Frontend**   | HTML5, CSS3, JavaScript, Socket.IO Client |
| **Backend**    | Python (Flask), Flask-SocketIO, python-telegram-bot |
| **Banco de Dados** | Firebase Realtime Database |
| **Infraestrutura** | Docker, Nginx (para produção) |

---

## ⚙️ Instalação Local

### ✅ Pré-requisitos

- Python 3.9+
- Node.js (para builds opcionais)
- Conta no Firebase

### 🔧 Passo a Passo

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/furia-fan-chat.git
cd furia-fan-chat
Configure o ambiente:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
Configure as variáveis de ambiente:

bash
Copiar
Editar
cp .env.example .env
Edite o .env com suas credenciais.

Inicie os serviços:

bash
Copiar
Editar
# Terminal 1 - Backend
python backend/app.py

# Terminal 2 - Frontend (opcional se usar Flask para servir)
cd frontend
python -m http.server 8000
🌐 Acessando a Aplicação
Modo desenvolvimento: http://localhost:8000

API/WebSocket: ws://localhost:5000

📱 Integração com Telegram
Crie um bot com @BotFather

Configure o token no .env

O bot estará disponível em: https://t.me/seu_bot

🐳 Docker (Para Produção)
bash
Copiar
Editar
docker build -t furia-chat .
docker run -p 5000:5000 -p 8000:8000 furia-chat
🛠 Estrutura de Arquivos
bash
Copiar
Editar
furia-fan-chat/
├── backend/
│   ├── app.py              # Servidor principal
│   ├── bot/                # Lógica do bot Telegram
│   └── websocket/          # Handlers WebSocket
├── frontend/
│   ├── index.html          # Landing page
│   ├── css/                # Estilos
│   └── js/                 # Scripts
├── .env.example            # Modelo de configuração
└── requirements.txt        # Dependências Python
🤝 Como Contribuir
Faça um fork do projeto

Crie uma branch:

bash
Copiar
Editar
git checkout -b feature/incrivel
Commit suas mudanças:

bash
Copiar
Editar
git commit -m 'Add incrível feature'
Push para a branch:

bash
Copiar
Editar
git push origin feature/incrivel
Abra um Pull Request ✨

📄 Licença
Distribuído sob licença MIT. Veja o arquivo LICENSE para mais informações.

✉️ Contato
Equipe de Desenvolvimento - dev@furiafanchat.com

Twitter: @FuriaFanChat

⚡ VAMO FURIA!
🚀 Desenvolvido com 💛🖤 pela comunidade fURIA

