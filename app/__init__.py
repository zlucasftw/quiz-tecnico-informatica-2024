from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Define ORM do DB com método SQLAlchemy()
db = SQLAlchemy()

# Cria a função para montar a aplicação Flask e a RETORNA
def create_app():
    
    app = Flask(__name__, static_folder='/app/static')
    
    # Aplicando o CORS no app Flask para a API poder ser consumida por outra aplicação
    CORS(app)
    
    # app.config["SECRET_KEY"] = "key"
    
    # Configuração banco dados MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/quiz'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
    
    #Inicializa o metódo db para app
    db.init_app(app)
    
    # Importação dos Models
    from .models.quiz_model import Quiz #, Categorias
    from .models.categoria_model import Categoria
    from .models.contato_model import Contato
    from .models.login_model import Login
    
    # Início: Importamos e registramos o Blueprint para as rotas
    
    from .routes.routes import bp
    app.register_blueprint(bp)
    
    from .routes.quiz_routes import bp_quiz
    app.register_blueprint(bp_quiz)
    
    
    """ from .routes.login_routes import bp_login
    app.register_blueprint(bp_login) """
    
    # Fim: Importamos e registramos o Blueprint para as rotas    
    
    # Retorno da montagem do app
    return app    

    