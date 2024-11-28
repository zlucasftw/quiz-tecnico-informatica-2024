from .. import db

""" 

Modelo de categoria que representa o objeto que irá ser mapeado
para um registro no banco de dados relacional

"""

class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    url_imagem = db.Column(db.String(255), nullable=False)
    quantidade_perguntas = db.Column(db.Integer, nullable=False)
    # id_perguntas = db.Column(db.Integer, nullable=False)
    # perguntas= db.Column(db.String(255), nullable=False)
    categoria_id = db.Column(db.Integer, nullable=False)
    pergunta_id = db.Column(db.Integer, nullable=False)
    
    def quiz_todict(self):
        return {
            "titulo": self.titulo,
            "url_imagem": self.url_imagem,
            "quantidade_perguntas": self.quantidade_perguntas,
            "categoria_id": self.categoria_id,
            "pergunta_id": self.pergunta_id
        }
    
# class Categorias(db.Model):
#     __tablename__: 'categorias'
#     id = db.Column(db.Integer, primary_key=True)
#     titulo = db.Column(db.String(60), nullable=False)

# class Frutas(db.Model):
#     __tablename__ = 'frutas'
#     id = db.Column(db.Integer, primary_key=True)
#     nome_fruta = db.Column(db.String(100), nullable=False)
#     quantidade = db.Column(db.Integer, unique=True, nullable=False)
#     cor = db.Column(db.String(100), nullable=False)
#     data_aquisicao = db.Column(db.Date, nullable=True)
#     categoria_id = db.Column(db.Integer, nullable=True)
#     status = db.Column(db.Integer, nullable=True, default="1")
    
    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "nome_fruta": self.nome_fruta,
    #         "quantidade": self.quantidade,
    #         "cor": self.cor,
    #         "data_aquisicao": self.data_aquisicao,
    #         "categoria_id": self.categoria_id,
    #     }

# class Categorias(db.Model):
#     __tablename__ = 'categorias'
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(50), nullable=False)