const ws = new WebSocket("ws://172.16.0.197/ws");

ws.onmessage = (event) => {
  // Se obtienen los datos
  const data = JSON.parse(event.data);
  const autor = data["autor"];
  const contenido = data["contenido"];

  // Se crea los elementos correspondientes
  const messages = document.getElementById("messages");
  const message = document.createElement("li");

  const userElement = document.createElement("spam");
  userElement.classList.add("user");
  userElement.innerText = autor;
  message.appendChild(userElement);

  const messageElement = document.createElement("spam");
  userElement.classList.add("message-content");
  messageElement.innerText = contenido;
  message.appendChild(messageElement);

  messages.appendChild(message);
};

function sendMessage(event) {
  event.preventDefault();
  try {
    var inputUsuario = document.getElementById("usuario");
    var inputContenido = document.getElementById("contenido");
    ws.send(
      JSON.stringify({
        autor: inputUsuario.value,
        contenido: inputContenido.value,
      })
    );
    inputContenido.value = "";
  } finally {
    return false;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("send").onclick = sendMessage;
});
