from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = "palavra-secreta-SOFIA"

usuario_logado = None

# Banco de dados simulado
USUARIOS = {
    "sofia@email.com": "Senh@1",
    "visitante@email.com": "Senh@2"
}

@app.route("/")
@app.route("/index")
def index():
    if not usuario_logado:
        flash("Faça login para acessar esta página!")
        return redirect('/login')
    return render_template("index.html", usuario=usuario_logado)

@app.route("/contato")
def contato():
    if not usuario_logado:
        flash("Faça login para acessar a página de contato!")
        return redirect('/login')
    return render_template("contato.html", usuario=usuario_logado)

@app.route("/login")
def login():
    if usuario_logado:
        flash("Você já está logado!")
        return redirect('/index')
    return render_template("login.html")

@app.route("/autenticar", methods=['POST'])
def autenticar():
    global usuario_logado
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    if usuario in USUARIOS and USUARIOS[usuario] == senha:
        usuario_logado = usuario
        flash(f"Bem-vindo(a), {usuario}!")
        return redirect('/index')
    flash("Login ou senha incorretos.")
    return redirect('/login')

@app.route("/logout")
def logout():
    global usuario_logado
    usuario_logado = None
    flash("Logout realizado com sucesso!")
    return redirect('/login')

@app.route("/novocadastro", methods=['POST'])
def cadastro():
    nome_usuario = request.form.get('nome_usuario', '')
    return render_template("cadastro.html", nome_login=nome_usuario)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
