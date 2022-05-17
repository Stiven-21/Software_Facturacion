from flask import session
def autenticado():
    if 'username' in session:
        return True
    else:
        return False