from flask import flash,session
from models import getValidateLoginModel
def iniciarSesion(username,password):
    try:
        if username is '':
            flash('Usuario','malo')
        if password is '':
            flash('Contraseña','malo')
        else:
            result = getValidateLoginModel.validateLogin(username)
            if result[3] == password:
                session['token'] = result[0]
                session['user_id'] = result[1]
                session['username'] = result[2]
            else:
                flash("Usuario incorrecto","malo")
    except:
        print("Error occured in signinUser")
    