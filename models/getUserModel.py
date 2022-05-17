
from config.database import db
cursor = db.cursor()
def getUser(id):
    try:
        id= str(id)
        cursor.execute("SELECT * FROM users,roles WHERE id_user = '"+id+"' and roles.id_rol = users.id_rol")
        myresult = cursor.fetchone()
        return myresult
    except:
        print("Error en getUser")