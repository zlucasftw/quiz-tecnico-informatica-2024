from .. import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship 
from typing import ClassVar

""" 

Modelo de categoria que representa o objeto que irá ser mapeado
para um registro no banco de dados relacional

"""

class Quiz(db.Model):
    
    __tablename__ = 'quiz'
    id:ClassVar[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    url_imagem = db.Column(db.String(255), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(ForeignKey("categoria.id"))
    pergunta_id = db.Column(ForeignKey("pergunta.id"))
    
    categoria_id_fk = relationship("Categoria", back_populates="categoria_quiz_fk")
    pergunta_id_fk = relationship("Perguntas", back_populates="perguntas_quiz_fk")
    
    def quiz_todict(self):
        return {
            "titulo": self.titulo,
            "url_imagem": self.url_imagem,
            "quantidade_perguntas": self.quantidade_perguntas,
            "categoria_id": self.categoria_id,
            "pergunta_id": self.pergunta_id
        }
    
