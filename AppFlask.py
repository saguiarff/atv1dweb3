from flask import Flask

app_Sofia = Flask (__name__)

@app_Sofia.route('/')
def raiz():
    return 'Olá!'

app_Sofia.run()