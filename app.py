from flask import Flask, redirect,render_template,url_for,request,session, jsonify
from controllers.autenticacionController import autenticado
from controllers.validacionesController import numero
from controllers import CrearClienteController, actualizarUsuarioController
from models import getUserModel, getRolesModel, getLoginModel, insertLoginModel, updateUsersModel
from controllers import CrearClienteController,loginController,facturasController

app = Flask(__name__)
app.secret_key = 'asdkfaysdf28372@'

@app.route("/", methods=["GET", "POST"])
def index():
    if autenticado():
        if request.method == 'GET':
            facturas = facturasController.facturasController()
            print(facturas)
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
            return redirect(url_for('CrearUsuario'))
        return render_template("views/users/crear_cliente.html")
    else:
        return render_template("views/login/login.html")
    
@app.route("/mi-perfil", methods=['GET', 'POST'])
def miPerfil():
    if autenticado():
        usuario = getUserModel.getUser(session.get('token'))
        if request.method=='POST':
            identificacion = numero(request.form['identificacion'])
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            telefono = request.form['telefono']
            ciudad = request.form['ciudad']
            email = request.form['email']
            if not actualizarUsuarioController.ActualizarCliente(identificacion, nombre, apellido, ciudad, telefono, email, usuario[1]):
                return render_template('views/profile/mi_perfil.html', usuario=usuario, identificacion=identificacion, nombre=nombre, apellido=apellido, email=email, telefono=telefono, ciudad=ciudad)
            return redirect(url_for('miPerfil'))
        identificacion = usuario[1]
        nombre = usuario[2]
        apellido = usuario[3]
        email = usuario[5]
        telefono = usuario[4]
        ciudad = usuario[6]
        return render_template('views/profile/mi_perfil.html', usuario=usuario, identificacion=identificacion, nombre=nombre, apellido=apellido, email=email, telefono=telefono, ciudad=ciudad)
    else:
        return render_template("views/login/login.html")
    
@app.route('/buscar-usuario', methods=['POST'])
def buscarUsuario():
    if autenticado():
        identificacion = numero(request.form['identificacion_search'])
        usuario = getUserModel.getUserSearch(identificacion=identificacion)
        return jsonify(usuario)
    else:
        return render_template("views/login/login.html")
    
@app.route('/roles', methods=['GET'])
def trearRoles():
    if autenticado():
        roles = getRolesModel.getRoles()
        return jsonify(roles)
    else:
        return render_template("views/login/login.html")
    
@app.route('/cliente-usuario', methods=['POST'])
def traerClienteUsuario():
    if autenticado():
        usuario = request.form['usuario']
        login = getLoginModel.GetLoginUser(usuario=usuario)
        return jsonify(login)
    else:
        return render_template("views/login/login.html")
    
@app.route('/guardar-login', methods=['POST'])
def crearLogin():
    if autenticado():
        id_cliente = request.form['id_cliente']
        usuario = request.form['usuario']
        password = request.form['password']
        insertLoginModel.CrearLogin(id_cliente=id_cliente, usuario=usuario, password=password)
        updateUsersModel.UpdateRol(id_cliente=id_cliente)
        return "Login registrado correctamente correctamente"
    else:
        return render_template("views/login/login.html")
    
@app.route('/crear-factura', methods=['GET','POST'])
def crearFactura():
    if autenticado():
        return render_template("views/facturas/crear.html")
    else:
        return render_template("views/facturas/crear.html")
    
@app.route("/cliente", methods=['POST'])
def Cliente():
    if autenticado():
        return render_template("views/facturas/crear.html")
    else:
        return render_template("views/facturas/crear.html")
    
    
app.run(debug=True)
