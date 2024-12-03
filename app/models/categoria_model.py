""" 

Modelo de categoria que representa o objeto que irá ser mapeado
para um registro no banco de dados relacional

"""

from .. import db
from sqlalchemy.orm import relationship

class Categoria(db.Model):
    __tablename__= 'categoria'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    
    # categoria_quiz_fk = relationship("Quiz", back_populates="categoria_quiz_fk") 
