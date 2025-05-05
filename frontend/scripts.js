document.addEventListener("DOMContentLoaded", () => {
  // Conexão WebSocket - use seu IP real em produção
  const socket = io("http://localhost:5000", {
    reconnectionAttempts: 5,
    timeout: 10000,
  });

  // Debug de conexão
  socket.on("connect", () => {
    console.log("✅ Conectado ao servidor WebSocket");
  });

  socket.on("connect_error", (err) => {
    console.error("❌ Erro de conexão:", err.message);
  });

  // Envio de mensagens
  document.getElementById("send-message")?.addEventListener("click", () => {
    const messageInput = document.getElementById("message-input");
    if (messageInput && messageInput.value.trim()) {
      socket.emit("torcida_message", {
        user: "Usuário", // Substitua por nome real
        text: messageInput.value,
      });
      messageInput.value = ""; // Limpa o campo
    }
  });

  // Recebimento de mensagens
  socket.on("new_message", (data) => {
    const chat = document.getElementById("torcida-chat");
    if (chat) {
      const messageElement = document.createElement("div");
      messageElement.className = "message";
      messageElement.innerHTML = `<strong>${data.user}:</strong> ${data.text}`;
      chat.appendChild(messageElement);
      chat.scrollTop = chat.scrollHeight; // Auto-scroll
    }
  });
});
