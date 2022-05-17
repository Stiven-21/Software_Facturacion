from flask import Flask, redirect,render_template,url_for,request,session
from controllers.autenticacionController import autenticado
from controllers.validacionesController import numero
from controllers import CrearClienteController,loginController,facturasController

app = Flask(__name__)
app.secret_key = 'asdkfaysdf28372@'

@app.route("/", methods=["GET", "POST"])
def index():
    if autenticado():
        if request.method == 'GET':
            facturas = facturasController.facturasController()
            #print(facturas)
            return render_template("index.html",facturas = facturas)
        if request.method == 'POST':
            return render_template("index.html")
    else:
        return render_template("views/login/login.html")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if autenticado():
        return render_template("index.html")
    else:
        if request.method=='POST':
            username=request.form['username']
            password=request.form['password']
            if loginController.iniciarSesion(username,password):
                return redirect("/")
            else:
                return render_template("views/login/login.html",username=username)
        return render_template("views/login/login.html")
@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/crear-cliente", methods=["GET", "POST"])
def CrearUsuario():
    if autenticado():
        if request.method=='POST':
            identificacion = numero(request.form['identificacion'])
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            telefono = request.form['telefono']
            ciudad = request.form['ciudad']
            email = request.form['email']
            if not CrearClienteController.CrearCliente(identificacion, nombre, apellido, ciudad, telefono, email):
                return render_template("views/users/crear_cliente.html", identificacion=identificacion, nombre=nombre, apellido=apellido, telefono=telefono, ciudad=ciudad, email=email )
            return redirect('/crear-usuario')
        return render_template("views/users/crear_cliente.html")
    else:
        return render_template("views/login/login.html")
    
app.run(debug=True)
