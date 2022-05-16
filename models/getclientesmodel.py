from config.database import db
cursor = db.cursor()

def GetClientes(identificacion):
    try:
        cursor.execute('SELECT * FROM users WHERE identificacion = %s ',(identificacion,))
        cliente = cursor.fetchone()
        return cliente
    except:
        print("Ha ocurrido un error en el model GetClientes")
