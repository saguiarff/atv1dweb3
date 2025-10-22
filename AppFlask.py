from flask import Flask, render_template

app_Sofia = Flask(__name__ , template_folder='templates')


@app_Sofia.route("/")  
def homepage():          
    return render_template ("homepage.html")

@app_Sofia.route("/contato")
def contato():
    return render_template("contato.html") 

if __name__ == "__main__": 
    app_Sofia.run(port = 8000)