async function sendQuery() {
    const input = document.getElementById("queryInput");
    const message = input.value.trim();
    if (message === "") return;

    appendMessage("user", message);

    const response = await fetch('/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: message })
    });

    const data = await response.json();
    appendMessage("agent", data.response);

    input.value = "";
}

function appendMessage(type, text) {
    const messagesDiv = document.getElementById("messages");
    const messageEl = document.createElement("div");
    messageEl.className = type;
    messageEl.innerText = text;
    messagesDiv.appendChild(messageEl);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
