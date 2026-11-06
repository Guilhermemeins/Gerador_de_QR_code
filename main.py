
from flask import Flask, render_template, request, send_from_directory
import qrcode
import io
import base64

# Criar aplicativo Flask
app = Flask(__name__, template_folder=".")

# Disponibilizar o JavaScript ao navegador
@app.route("/script.js")
def servir_javascript():
    return send_from_directory(".", "script.js")

# Criar rota da página inicial
@app.route("/", methods=["GET", "POST"])
def inicio():

    imagem = None

    # Verificar se o formulário foi enviado
    if request.method == "POST":

        # Receber o link do HTML
        link = request.form.get("link", "").strip()

        if link:
            # Gerar QR Code com Python
            qr = qrcode.make(link)

            # Guardar imagem na memória
            buffer = io.BytesIO()
            qr.save(buffer, format="PNG")

            # Converter imagem para base64
            imagem_base64 = base64.b64encode(
                buffer.getvalue()
            ).decode("utf-8")

            imagem = "data:image/png;base64," + imagem_base64

    # Enviar resultado para o HTML
    return render_template("index.html", imagem=imagem)

# Iniciar servidor local
if __name__ == "__main__":
    app.run(debug=True)
