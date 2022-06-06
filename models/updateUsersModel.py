from config.database import db
cursor = db.cursor()

def UpdateRol(id_cliente):
    try:
        cursor.execute("UPDATE users SET id_rol = 2 WHERE id_user = "+id_cliente+" ")
        db.commit()
    except:
        print("Ha ocurrido un error en el model UpdateRol")
        
def UpdateUser(id_usuario, identificacion, nombre, apellido, ciudad, telefono, email):
    try:
        cursor.execute("UPDATE users SET identificacion = %s, nombre = %s, apellido = %s, telefono = %s, email = %s, ciudad = %s WHERE id_user = %s ", (
            identificacion,
            nombre,
            apellido,
            telefono,
            email,
            ciudad,
            id_usuario
        ))
        db.commit()
    except:
        print("Ha ocurrido un error en el model UpdateUser")
    