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
    
    if quiz is None:
        return jsonify({"Erro": "Não encontrado"}), 404
    
    info_quiz = []
    
    for info in quiz:
        info = dict(info)
        info_quiz.append(info)
        
    print(info_quiz)
    
    if not info_quiz:
        return jsonify({"Erro": "Não encontrado"}), 404
    else:
        return jsonify(info_quiz)
    # if info_quiz:
    # else:
    #     return 404
    
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
    
    nome_form, email_form, mensagem_form, telefone_form = None, None, None, None
    
    if request.method == 'POST':
        
        # nome_form = request.form('nome')
        # email_form = request.form('email')
        # mensagem_form = request.form('mensagem')
        # telefone_form = request.form('telefone')
        contato = request.get_json()
        
        nome_form = contato['nome']
        email_form = contato['email']
        mensagem_form = contato['mensagem']
        telefone_form = contato['telefone']
        
        emails = Contato.query.all()

        for email in emails:
        
            if email.email == email_form:
                return jsonify({ "Erro": "Contato já enviado!" }), 400
        
        novo_contato = Contato(nome=nome_form,email=email_form,mensagem=mensagem_form,telefone=telefone_form)
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
            db.session.close()
            print(exception)
            return 500
        
    else:
        return 405

@bp.route("/contato", methods=["GET"])
def listar_contatos():
    
    try:
        
        contatos = Contato.query.all()
        
        # if contatos is None:
        #     return jsonify({ "Erro": "Erro no servidor" }), 500
        
        contato_resposta = []
        
        for contato in contatos:
            contato = dict(contato)
            contato_resposta.append(contato)
        
        # print(contato)
        
        # if not contato:
        #     return jsonify({ "Erro": "Não encontrado" }), 404
        # else:
        return jsonify(contato_resposta), 302
    
    except Exception as exception:
        return jsonify({ "Erro": "Erro no servidor" }), 500

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
        return jsonify({ "mensagem": "Login inválido!" }), 401
    
    try:
        
        login = Login.query.first()
        
        if email_form == login.email:
            
            if senha_form == login.senha:
                return jsonify({ "mensagem": "Login validado!" }), 202
            
        else:
            return jsonify({ "mensagem": "Login inválido!" }), 401
        
    except Exception as exception:
        print(exception)
        return jsonify({ "mensagem": "Login inválido!" }), 405

