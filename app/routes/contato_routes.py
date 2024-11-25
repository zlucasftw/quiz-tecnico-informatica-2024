from flask import Blueprint, jsonify, render_template, request, make_response, session, url_for, flash, redirect
# from sqlalchemy import Text
# from sqlalchemy.engine import Engine
from app.models.quiz_model import Quiz
from app.models.contato_model import Contato
from app.models.categoria_model import Categoria 
# from werkzeug.utils import secure_filename
from datetime import datetime
from app import db

bp = Blueprint("main", __name__, template_folder='../templates/main')

""" 

Serviço de tratamento para requisições no Endpoint de contato.

"""

@bp.route('/contato', methods=['GET'])
def listar_quiz_contato():
    
    contatos = Contato.query.all()
    
    lista_contatos = []
    
    for contato in contatos:
        contato = dict(contato)
        lista_contatos.append(contato)
    
    print(lista_contatos)
    
    if lista_contatos is not None:
        print(lista_contatos)
        return jsonify(lista_contatos)
    else:
        return make_response(404)
    

@bp.route('/contato', methods=['POST'])
def cadastrar_quiz_contato():

    if request.method == 'POST':
        contato = request.get_json()