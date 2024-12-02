
from .. import db

from sqlalchemy.orm import relationship

class Perguntas(db.Model):
    __tablename__ = 'perguntas'
    alternativas = db.Column(db.TEXT, nullable=False)
    resposta_correta = db.Column(db.Boolean, nullable=False)

    perguntas_quiz_fk = relationship("Quiz", back_populates="pergunta_id_fk")
