from flask import Flask  

app_Sofia = Flask (__name__) 

@app_Sofia.route('/')   
@app_Sofia.route('/rota1') 
def rota1(): 
    return 'Olá!'

@app_Sofia.route('/rota2')
def rota2():
    resposta = "<H3> Essa é outra página da rota 2 <H3>"
    return resposta

def saudacoes (nome): 
    return f'Olá, {nome}'

if __name__ == "__main__" :
    app_Sofia.run(port = 8000) 
                                                            