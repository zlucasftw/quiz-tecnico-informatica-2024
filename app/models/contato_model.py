from .. import db

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    mensagem = db.Column(db.TEXT, nullable=False)
    telefone = db.Column(db.String(45), nullable=True)
    data_envio = db.Column(db.DateTime, nullable=False)
