
const formulario = document.getElementById("formulario");
const campo = document.getElementById("link");
const resultado = document.getElementById("resultado");
const qrcode = document.getElementById("qrcode");
const baixar = document.getElementById("baixar");

formulario.addEventListener("submit", function(evento) {
    evento.preventDefault();

    const texto = campo.value.trim();

    if (texto === "") {
        alert("Digite um link ou texto!");
        return;
    }

    qrcode.innerHTML = "";

    new QRCode(qrcode, {
        text: texto,
        width: 220,
        height: 220
    });

    resultado.hidden = false;
});

baixar.addEventListener("click", function() {
    const canvas = qrcode.querySelector("canvas");
    const imagem = qrcode.querySelector("img");

    const endereco = canvas
        ? canvas.toDataURL("image/png")
        : imagem.src;

    const link = document.createElement("a");
    link.href = endereco;
    link.download = "qrcode.png";
    link.click();
});
