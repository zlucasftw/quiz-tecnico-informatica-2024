from flask import Blueprint, jsonify, make_response, session, url_for, flash, redirect, request
from app.models.quiz_model import Quiz
from app.models.categoria_model import Categoria 
from app.models.pergunta_model import Perguntas
from app import db
from flask import current_app as app

bp_quiz = Blueprint("quiz", __name__, template_folder='../templates/')

@bp_quiz.route('/quiz', methods=['GET'])
def listar_quiz():
    
    if request.method == 'GET':
        
        try:
        
            quiz = Quiz.query.all()
            # quiz = app.session.query(Quiz, Categoria, Perguntas).join(Categoria, Categoria.id == Quiz.categoria_id).join(Perguntas, Perguntas.id == Quiz.pergunta_id).all()
            # print(quiz)
            info_quiz = []

            for q in quiz:
                info_quiz.append(Quiz.to_dict(q))
            
            if not info_quiz:
                return jsonify({"Erro": "Não encontrado"}), 404
        
            return jsonify(info_quiz)
        
        except Exception as exception:
            return jsonify({"Erro": "Erro no servidor"}), 500
    else:
        return jsonify({"Erro": "Erro no servidor"}), 500

@bp_quiz.route('/quiz', methods=['POST'])
def cadastrar_quiz():
    
    if request.method == 'POST':
        # quiz = {}        
        # quiz['quantidade'] = request.form('quantidade')
        # quiz['titulo'] = request.form('titulo')
        # quiz['perguntas'] = request.form('perguntas')
        # quiz['id_categoria'] = request.form('id_categoria')
        quiz = request.get_json()
        quiz_titulo = quiz['titulo']
        quiz_url_imagem = quiz['url_imagem']
        quiz_quantidade_perguntas = quiz['quantidade_perguntas']
        quiz_categoria_id = quiz['categoria_id']
        quiz_pergunta_id = quiz['pergunta_id']
        
        novo_quiz = Quiz(titulo=quiz_titulo,url_imagem=quiz_url_imagem,quantidade_perguntas=quiz_quantidade_perguntas, categoria_id=quiz_categoria_id, pergunta_id=quiz_pergunta_id)
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
        
        except Exception as exception:
            
            db.session.rollback()
            return jsonify({ "Erro": "Servidor" }), 500
            
        
        # quiz = jsonify(perguntas)
        # if quiz is not None:
        #     return quiz
        # else:
        #     make_response(404)
        
    else:
        make_response(404)
    

        
    