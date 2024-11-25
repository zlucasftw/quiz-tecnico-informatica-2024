# from typing import Literal
# from flask import Blueprint, jsonify, render_template, request, make_response, session, url_for, flash, redirect
# from flask.wrappers import Response
# from sqlalchemy import Text
# from sqlalchemy.engine import Engine
# from app.models.login_model import Login
# from werkzeug.utils import secure_filename
# from datetime import datetime
# from app import db

# bp_login = Blueprint("bp_login", __name__, template_folder='../templates/bp_login')

# @bp_login.route("/login", method="POST")
# def validar_login():
    
#     email_form = None
#     senha_form = None
    
#     if request.method == 'POST':
#         # email_form = request.form('email')
#         # senha_form = request.form('senha')
#         form = request.get_json()
#         email_form = form['email'] 
#         senha_form = form['senha']
        
#     else:
#         return make_response({ "mensagem": "Login inválido!" }), 401
    
#     try:
        
#         login = Login.query.first()
        
#         if email_form == login.email:
            
#             if senha_form == login.senha:
#                 return make_response({ "mensagem": "Login validado!" }), 202
            
#         else:
#             return make_response({ "mensagem": "Login inválido!" }), 401
        
#     except Exception as exception:
#         return make_response({ "mensagem": "Login inválido!" }), 401