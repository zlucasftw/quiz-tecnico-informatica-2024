""" 

Modelo de login que representa o objeto que irá ser mapeado
para um registro no banco de dados relacional

"""

from .. import db

class Login(db.Model):
    __tablename__ = 'login'
    id_admin = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
