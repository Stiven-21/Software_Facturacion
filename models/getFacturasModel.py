from config.database import db
cursor = db.cursor()
def getFacturas():
    try:
        cursor.execute("SELECT * FROM facturas,estado,users,roles WHERE facturas.id_user = users.id_user AND facturas.id_estado = estado.id_estado AND users.id_rol = roles.id_rol")
        myresult = cursor.fetchall()
        return myresult
    except:
        print("Error en getFacturas model")