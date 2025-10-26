from flask import Flask, render_template

app_Sofia = Flask(__name__, template_folder='templates') 

@app_Sofia.route("/")       
@app_Sofia.route("/index")  
def indice():
    return render_template ("index.html", nome = "Sofia") 

@app_Sofia.route("/contato")
def contato():
    return render_template("contato.html") 

@app_Sofia.route("/login")
def login():
    return render_template("login.html") 

@app_Sofia.route("/usuario", defaults={"nome_usuario":"Sofia","nome_profissao":"Estudante"}) 
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("usuario.html", nome=nome_usuario, dados = dados_usu)  

if __name__ == "__main__": 
    app_Sofia.run(port = 8000) 