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
            
    except:
        print("Error occured in signinUser")
    