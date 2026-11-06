from flask import Flask, render_template,request
import qrcode
import io
import base64

#criar aplicativo flask 
app = Flask(__name__, template_folder=".")

#criar rota da página inicial 
@app.route("/", methods=["GET", "POST"])
def inicio():
    
    imagem= None
    
    #Verificar se o formulário foi enviado 
    if request.method ==  "POST":
        
      #receber o link html
       link = request.form.get("link", "").strip()
       
       if link: 
           #gerador QRCode
           qr = qrcode.make(link)
           
           #Guardar imagem na memória
           buffer = io.BytesIO()
           qr.save(buffer,format="PNG") 
           
           #Converte imagem para base64
           imagem_base64 =base64.b64encode(
               buffer.getvalue()
               
           ).decode ("utf-8")
           imagem = "data:image/png;base64,"+ imagem_base64
           
    #Enviar resultado para o HTML
    return render_template ("index.html", imagem=imagem) 

#iniciar servidor 
if __name__ == "__main__":
    app.run(debug=True)
           
        
    