from flask import Flask, redirect,render_template,url_for,request,session
from controllers.autenticacionController import autenticado
from controllers import loginController

app = Flask(__name__)
app.secret_key = 'asdkfaysdf28372@'

@app.route("/", methods=["GET", "POST"])
def index():
    if autenticado():
        return render_template("index.html")
    else:
        return render_template("views/login/login.html")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if autenticado():
        return render_template("index.html")
    else:
        if request.method=='POST':
            usuario=request.form['username']
            password=request.form['password']
            if loginController.iniciarSesion(usuario,password):
                return redirect("/")
            else:
                return render_template("views/login/login.html")
        return render_template("views/login/login.html")
    
@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

app.run(debug=True)
