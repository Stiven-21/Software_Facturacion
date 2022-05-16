from config.database import db
cursor = db.cursor()
def validateLogin(username):
    try:
        cursor.execute("SELECT * FROM login WHERE user = '"+username+"'")
        myresult = cursor.fetchone()
        return myresult
    except:
        print("Error en validateLogin")