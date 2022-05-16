from config.database import db
cursor = db.cursor()
def validateLogin(username):
    try:
        print(username)
        cursor.execute("SELECT * FROM login WHERE user = '"+username+"'")
        myresult = cursor.fetchone()
        print(myresult)
        return myresult
    except:
        print("Error en validateLogin")