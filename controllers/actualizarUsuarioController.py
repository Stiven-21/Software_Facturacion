from flask import flash, session
from controllers import validacionesController
from models import getclientesmodel, updateUsersModel

def ActualizarCliente(identificacion, nombre, apellido, ciudad, telefono, email, ValIdentificacion):
    try:
        if identificacion == '':
            flash('La identificacion no puede estar vacia','false')
            return False
        else:
            if len(str(identificacion)) < 8:
                flash('La identificacion no puede contener menos de 8 caracteres','false')
                return False
            else:
                if identificacion != ValIdentificacion:
                    if getclientesmodel.GetClientes(identificacion=identificacion):
                        flash('La identificacion ya se encuentra registrada','false')
                        return False
                if nombre == '':
                    flash('Debe ingresar un nombre de cliente','false')
                    return False
                elif apellido == '':
                    flash('Debe ingresar un apellido','false')
                    return False
                elif telefono == '':
                    flash('Debe ingresar un telefono','false')
                    return False
                elif ciudad == '':
                    flash('Debe ingresar un ciudad','false')
                    return False
                elif email == '':
                    flash('Debe ingresar un email','false')
                    return False
                elif not validacionesController.Email(email):
                    flash('El email no es valido','false')
                    return False
                else:
                    enviarclientedatabase(identificacion, nombre, apellido, ciudad, telefono, email)
                    flash('Cliente actualizado con exito!','true')
                    return True
    except:
        print("Ha ocurrido un error en el controlador de crear cliente")
        
def enviarclientedatabase(identificacion, nombre, apellido, ciudad, telefono, email):
    id_usuario = session.get('token')
    updateUsersModel.UpdateUser(id_usuario=id_usuario, identificacion=identificacion, nombre=nombre, apellido=apellido, ciudad=ciudad, telefono=telefono, email=email)