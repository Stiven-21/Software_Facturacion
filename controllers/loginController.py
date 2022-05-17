from flask import flash,session
from models import getValidateLoginModel,getUserModel
def iniciarSesion(username,password):
    try:
        if username == '':
            flash('Usuario','malo')
        if password == '':
            flash('Contraseña','malo')
        else:
            result = getValidateLoginModel.validateLogin(username)
            if result[3] == password:
                user = getUserModel.getUser(result[0])
                session['token'] = result[0]
                session['user_id'] = result[1]
                session['username'] = result[2]
                session['user'] = user[2]+' '+user[3]
                session['rol'] = user[9]
                auth = True
            else:
                auth = False
        return auth
    except:
        flash("Usuario incorrecto","malo")
        print("Error occured in login Model")
    