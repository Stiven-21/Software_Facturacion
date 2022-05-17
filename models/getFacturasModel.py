from config.database import db
cursor = db.cursor()
def getFacturas():
    try:
        cursor.execute("SELECT * FROM facturas")
        myresult = cursor.fetchall()
        return myresult
    except:
        print("Error en getUser")