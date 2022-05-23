from config.database import db
cursor = db.cursor()
def getUser(id):
    try:
        id= str(id)
        cursor.execute("SELECT * FROM users,roles WHERE id_user = '"+id+"' AND users.id_rol=roles.id_rol")
        myresult = cursor.fetchone()
        return myresult
    except:
        print("Error en model getUser")
        
def getUserSearch(identificacion):
    try:
        identificacion = str(identificacion)
        cursor.execute("SELECT * FROM users, roles WHERE identificacion = '"+identificacion+"' AND users.id_rol = roles.id_rol ")
        usuario = cursor.fetchone()
        return usuario
    except:
        print("Error en model getUserSearch")