from flask import Flask

app_Sofia = Flask (__name__)


@app_Sofia.route('/')
@app_Sofia.route('/ola')
def raiz():
    return 'Olá!'


def saudacoes(nome):
    return f'Olá, {nome}!'


if __name__ == "__main__" :
    app_Sofia.run(port = 8000)