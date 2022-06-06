from config.database import db
cursor = db.cursor()

def GetLoginUser(usuario):
    try:
        cursor.execute('SELECT * FROM login WHERE login.user = %s ',(usuario,))
        login = cursor.fetchone()
        return login
    except:
        print("Ha ocurrido un error en el model GetLoginUser")