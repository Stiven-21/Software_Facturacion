from config.database import db
cursor = db.cursor()

def CrearCliente(identificacion, nombre, apellido, ciudad, telefono, email, id_rol):
    try:
        cursor.execute("INSERT INTO users(identificacion, nombre, apellido, telefono, email, ciudad, id_rol) values(%s,%s,%s,%s,%s,%s,%s)", (
            identificacion, 
            nombre, 
            apellido,
            telefono, 
            email,
            ciudad,
            id_rol
        ))
        db.commit()
    except:
        print("Ha ocurrido un error en el model CrearCliente")