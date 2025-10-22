from flask import Flask, render_template

app_Sofia = Flask(__name__ , template_folder='templates')

@app_Sofia.route("/")
def homepage():          
    return render_template ("homepage.html")

@app_Sofia.route("/contato")
def contato():
    return render_template("contato.html") 

@app_Sofia.route("/index")
def indice():
    return render_template ("index.html", nome = "Sofia") 

@app_Sofia.route("/usuario")
def dados_usuario():
    dados_usu = {"nome": "Sofia", "ocupacao": "Estudante", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html", dados = dados_usu)

if __name__ == "__main__": 
    app_Sofia.run(port = 8000) 
