from flask import Flask, render_template
from flask import request   #para trabalhar com os métodos GET e POST
from flask import jsonify   #para troca de dados em formato JSON

app_Sofia = Flask(__name__, template_folder='templates') 
# no caso de usar flash pede a configuração de uma chave secreta
app_Sofia.config['SECRET_KEY'] = "palavra-secreta-IFRO"

@app_Sofia.route("/")   
@app_Sofia.route("/index")  
def indice():
    return render_template ("index.html") 

@app_Sofia.route("/contato")
def contato():
    return render_template("contato.html") 


@app_Sofia.route("/usuario/<nome_usuario>;<nome_profissao>")


@app_Sofia.route("/usuario", defaults={"nome_usuario":"Sofia","nome_profissao":"Estudante"})  
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("usuario.html", nome=nome_usuario, dados = dados_usu)  


@app_Sofia.route("/login")
def login():
    return render_template("login.html") 

@app_Sofia.route('/teste', methods=['GET', 'POST'])
def test_route():
    if request.method == 'GET':
        return jsonify(message="Requisição GET recebida!"), 200
    elif request.method == 'POST':
        return jsonify(message="Requisição POST recebida!"), 200
    else:
        return jsonify(error="Método não permitido"), 405

"""
Para poder recuperar os argumentos passados nos parâmetros na URL precisa importar o pacote
from flask import request

Também precisa colocar que essa página aceita requisições de tipo GET ou POST
O GET é padrão, mas no caso do POST altere no html method="POST"

"""
@app_Sofia.route("/autenticar", methods=['GET','POST']) 
def autenticar_api():
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    if verificar_login(usuario, senha):
        return jsonify({"status": True, "mensagem": "Login bem-sucedido"})
    else:
        return jsonify({"status": False, 
                        "mensagem": "Login ou senha incorretos",
                        "user": usuario,
                        "pwd": senha }), 401
    
# Em caso de falha, código 401 (Unauthorized) para ajudar a interpretar a resposta corretamente.

"""  FUNÇÕES Auxiliares """
# Base de dados de login e senha usando um dicionário com o par chave:valor -> usuario:senha
tabelaUsuarios = {
    "sofia": "SuperSenh@2000",
    "alunoIFRO": "SuperSenh@2010",
    "visitante": "SuperSenh@2020"
}

# Verificação de login e senha
def verificar_login(login, senha):
    # procura pela chave no dicionário e pelo valor associado a chave, que é a senha
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