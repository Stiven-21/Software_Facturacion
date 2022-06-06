from config.database import db
cursor = db.cursor()

def CrearLogin(id_cliente, usuario, password):
    try:
        cursor.execute("INSERT INTO login(id_user, user, password) values(%s,%s,%s)", (
            id_cliente,
            usuario,
            password
        ))
        db.commit()
    except:
        print("Ha ocurrido un error en el model CrearLogin")
    