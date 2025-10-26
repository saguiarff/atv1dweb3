from flask import Flask, render_template
from flask import request   #para trabalhar com os métodos GET e POST
from flask import flash     #para msgs popup
from flask import redirect  #para redirecionar páginas

app_Sofia = Flask(__name__, template_folder='templates') 

app_Sofia.config['SECRET_KEY'] = "palavra-secreta-IFRO"

@app_Sofia.route("/")       
@app_Sofia.route("/index")  
def indice():
    return render_template ("index.html") 

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

@app_Sofia.route("/autenticar", methods=['GET','POST']) 
def autenticar():
    #método POST - pega nos fields (campos) do formulário
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    if verificar_login(usuario, senha):
        msg = "Login e senha corretos. Acesso permitido."
        return f"{msg} para {usuario} "
    else:
        #para não dar msg. na outra página, vamos manter na própria página com flash
        #adicionar import flash
        flash("Dados inválidos!")
        flash("Login ou senha incorretos. Acesso negado.")
        return redirect ('/login') #adicionar import redirect

# Base de dados de login e senha usando um dicionário com o par chave:valor -> usuario:senha
tabelaUsuarios = {
    "sofia": "SuperSenh@2000",
    "alunoIFRO": "SuperSenh@2000",
    "visitante": "SuperSenh@2000"
}

# Verificação de login e senha
def verificar_login(login, senha):
    if login in tabelaUsuarios and tabelaUsuarios[login] == senha:
        return True
    else:
        return False

@app_Sofia.route("/novocadastro/<nome_usuario>" , methods=['POST'])
@app_Sofia.route("/novocadastro/", defaults={"nome_usuario":""} , methods=['POST'])
def cadastroUsuario(nome_usuario):
    nome_usuario = request.form.get('nome_usuario')
    return render_template("cadastro.html", nome_login = nome_usuario ) 

if __name__ == "__main__": 
    app_Sofia.run(port = 8000) 