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

# @bp.route('/categorias', methods=['GET'])
# def quiz_categorias():
#     categorias = Categorias.query.all()
#     categorias_quiz = []
#     for categoria in categorias:
#         categorias.append(Categorias(fruta))
#     print(frutasQuitanda)
#     return jsonify(frutasQuitanda)

@bp.route('/quiz', methods=['GET'])
def listar_quiz():
    
    quiz = Quiz.query.all()
    
    info_quiz = []
    
    for info in quiz:
        info = dict(info)
        info_quiz.append(info)
        
    print(info_quiz)
    
    if info_quiz is not None:
        print(info_quiz)
        return jsonify(info_quiz)
    else:
        return make_response(404)
    
    # print(info_quiz)
    # return jsonify(info_quiz)

@bp.route('/quiz', methods=['POST'])
def cadastrar_quiz():
    
    if request.method == 'POST':
        # quiz = {}        
        # quiz['quantidade'] = request.form('quantidade')
        # quiz['titulo'] = request.form('titulo')
        # quiz['perguntas'] = request.form('perguntas')
        # quiz['id_categoria'] = request.form('id_categoria')
        quiz = request.get_json()
        quiz_titulo = quiz['titulo']
        quiz_quantidade_perguntas = quiz['quantidade_perguntas']
        quiz_categoria_id = quiz['categoria_id']
        quiz_pergunta_id = quiz['pergunta_id']
        
        novo_quiz = Quiz(titulo=quiz_titulo, quantidade_perguntas=quiz_quantidade_perguntas, categoria_id=quiz_categoria_id, pergunta_id=quiz_pergunta_id)
        novo_quiz_dict = {}
        
        try:
            db.session.add(novo_quiz)
            db.session.commit()
            
            novo_quiz_dict['id'] = novo_quiz.id
            novo_quiz_dict['titulo'] = novo_quiz.titulo
            novo_quiz_dict['quantidade_perguntas'] = novo_quiz.quantidade_perguntas
            novo_quiz_dict['categoria_id'] = novo_quiz.categoria_id
            novo_quiz_dict['pergunta_id'] = novo_quiz.pergunta_id
            # novo_quiz_dict['']
            print(jsonify(novo_quiz_dict))
            return jsonify(novo_quiz_dict), 201
        except Exception as erro:
            db.session.rollback()
            return make_response(504)
            
        
        # quiz = jsonify(perguntas)
        # if quiz is not None:
        #     return quiz
        # else:
        #     make_response(404)
        
    else:
        make_response(404)
    

        
    


""" 

Serviço de tratamento para requisições no Endpoint de categoria.

"""

# @bp.route('/categoria/<nome_categoria>', methods=['POST'])
# def listar_quiz_categorias(nome_categoria : str):
#     query = text("SELECT IF EXISTS nome FROM categoria WHERE nome = :n_c")
#     categoria_bd = db.engine.execute(query, n_c=nome_categoria)
    
#     return []