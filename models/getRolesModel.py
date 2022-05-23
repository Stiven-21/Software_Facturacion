from config.database import db
cursor = db.cursor()
def getRoles():
    try:
        cursor.execute("SELECT * FROM roles ")
        roles = cursor.fetchone()
        return roles
    except:
        print("Error en model getRoles")