from pathlib import Path

# Conteúdo do README.md formatado em Markdown
readme_content = """
# 📢 FURIA CS:GO Fan Chat

![FURIA Logo](https://upload.wikimedia.org/wikipedia/pt/thumb/d/dc/FURIA_Esports_logo.png/200px-FURIA_Esports_logo.png)

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
