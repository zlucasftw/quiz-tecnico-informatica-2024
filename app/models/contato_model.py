from .. import db
from datetime import datetime

class Contato(db.Model):
    __tablename__ = 'contato'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    mensagem = db.Column(db.TEXT, nullable=False)
    telefone = db.Column(db.String(45), nullable=True)
    data_envio = db.Column(db.DateTime, default=datetime.now, nullable=False)
    data_atendimento = db.Column(db.DateTime, nullable=True)
    data_expiracao = db.Column(db.DateTime, nullable=True)
