
from .. import db

from sqlalchemy.orm import relationship

class Perguntas(db.Model):
    __tablename__ = 'perguntas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alternativas = db.Column(db.TEXT, nullable=False)
    resposta_correta = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            "alternativas": self.alternativas,
            "resposta_correta": self.resposta_correta
        }
    # perguntas_quiz_fk = relationship("Quiz", back_populates="pergunta_id_fk")
