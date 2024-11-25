from flask import Blueprint, jsonify, render_template, request, make_response, session, url_for, flash, redirect
# from sqlalchemy import Text
# from sqlalchemy.engine import Engine
from app.models.quiz_model import Quiz
from app.models.login_model import Login
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
            return 504
            
        
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

""" 

Serviço de tratamento para requisições no Endpoint de login.
Realiza validação de login.

"""

@bp.route("/contato", methods=["POST"])
def registrar_contato():
    
    nome_form, email_form, mensagem_form, telefone_form = None
    
    if request.method == 'POST':
        
        # nome_form = request.form('nome')
        # email_form = request.form('email')
        # mensagem_form = request.form('mensagem')
        # telefone_form = request.form('telefone')
        contato = request.json()
        
        nome_form = contato['nome']
        email_form = contato['email']
        mensagem_form = contato['mensagem']        
        telefone_form = contato['telefone']
        
        novo_contato = Contato(nome=nome_form,email=email_form,mensagem_form=mensagem_form,telefone=telefone_form)
        novo_contato_resposta = {}
        
        try:
            
            db.session.add(novo_contato)
            db.session.commit()
            
            novo_contato_resposta['nome'] = novo_contato.nome
            novo_contato_resposta['email'] = novo_contato.email
            novo_contato_resposta['mensagem'] = novo_contato.mensagem
            novo_contato_resposta['telefone'] = novo_contato.telefone
            print(jsonify(novo_contato_resposta))
            return jsonify(novo_contato_resposta), 201
        
        except Exception as exception:
            db.session.rollback()
            print(exception)
            return 500
        
    else:
        return 405

""" 

Serviço de tratamento para requisições no Endpoint de login.
Realiza validação de login.

"""

@bp.route("/login", methods=["POST"])
def validar_login():
    
    email_form = None
    senha_form = None
    
    if request.method == 'POST':
        # email_form = request.form('email')
        # senha_form = request.form('senha')
        form = request.get_json()
        email_form = form['email'] 
        senha_form = form['senha']
        
    else:
        return make_response({ "mensagem": "Login inválido!" }), 401
    
    try:
        
        login = Login.query.first()
        
        if email_form == login.email:
            
            if senha_form == login.senha:
                return make_response({ "mensagem": "Login validado!" }), 202
            
        else:
            return make_response({ "mensagem": "Login inválido!" }), 401
        
    except Exception as exception:
        print(exception)
        return make_response({ "mensagem": "Login inválido!" }), 405