// static/script.js

// Novo: Função para abrir e fechar o chat
function toggleChat() {
    const chatBox = document.querySelector('.chat-box');
    const openBtn = document.getElementById('open-chat-btn');
    
    // Alterna a classe 'open'
    chatBox.classList.toggle('open');

    // Opcional: Altera o ícone do botão quando aberto/fechado
    if (chatBox.classList.contains('open')) {
        openBtn.textContent = '–'; // Altera para um traço (ou ícone de fechar)
    } else {
        openBtn.textContent = '💬'; // Volta para o ícone de mensagem
    }
    
    // Se estiver abrindo, garante que o chat esteja no final
    if (chatBox.classList.contains('open')) {
        const chatWindow = document.getElementById('chat-window');
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
}

async function sendMessage() {
    const inputElement = document.getElementById('user-input');
    const message = inputElement.value.trim();

    if (!message) return; // Don't send empty messages

    const chatWindow = document.getElementById('chat-window');

    // 1. Display the user's message
    appendMessage(message, 'user-message');
    inputElement.value = ''; // Clear the input field

    // 2. Display a "loading" message while waiting for the bot
    const loadingMessageElement = appendMessage('...', 'bot-message-loading');

    // 5. Scroll to the bottom of the chat window before request
    chatWindow.scrollTop = chatWindow.scrollHeight;

    try {
        // 3. Send the message to the FastAPI backend
        // NOTE: Uses relative path /get_response
        const response = await fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        const botReply = data.message;

        // 4. Replace the loading message with the actual bot reply
        loadingMessageElement.textContent = botReply;
        // Ensure the base class is always present for correct styling
        loadingMessageElement.classList.remove('bot-message-loading');
        loadingMessageElement.classList.add('bot-message');

    } catch (error) {
        console.error('Error sending message:', error);
        loadingMessageElement.textContent = 'Erro de conexão ou do servidor. Tente novamente.';
        loadingMessageElement.classList.remove('bot-message-loading');
    }

    // 5. Scroll to the bottom of the chat window after response
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function appendMessage(message, className) {
    const chatWindow = document.getElementById('chat-window');
    const messageElement = document.createElement('div');
    messageElement.classList.add('bot-message'); 
    messageElement.classList.add(className);
    messageElement.textContent = message;
    chatWindow.appendChild(messageElement);
    return messageElement;
}
// Optional: Allow sending message by pressing Enter key
document.addEventListener('DOMContentLoaded', () => {
    const inputElement = document.getElementById('user-input');
    if (inputElement) { // Garante que o input existe
        inputElement.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
});