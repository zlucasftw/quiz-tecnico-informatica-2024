from flask import Blueprint, jsonify, make_response, session, url_for, flash, redirect, request, render_template
from app.models.login_model import Login

bp_login = Blueprint("login", __name__, template_folder='../templates/')

@bp_login.route("/login", methods=["GET"])
def template_login():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        return make_response("Erro", 404)

@bp_login.route("/login", methods=["POST"])
def validar_login():
    
    email_form = None
    senha_form = None
    
    if request.method == 'POST':
        # email_form = request.form('email')
        # senha_form = request.form('senha')
        # form = request.get_json()
        email_form = request.form['email']
        senha_form = request.form['senha']
        
        # return redirect('http://127.0.0.1:5500/login.html', 401)
        # return jsonify({ "mensagem": "Login inválido!" }), 401
        
        try:

            login = Login.query.first()

            if email_form == login.email:

                if senha_form == login.senha:
                    return render_template("home.html")
                    # return jsonify({ "mensagem": "Login validado!" }), 202
                else:
                    return render_template("login.html")

            else:
                return render_template("login.html")
                # return redirect('http://127.0.0.1:5500/login.html', 401)
                # return jsonify({ "mensagem": "Login inválido!" }), 401

        except Exception as exception:
            raise exception
            # return render_template("login.html")
            # print(exception)
            # return jsonify({ "mensagem": "Login inválido!" }), 405
    else:
        return render_template("login.html")
        # return jsonify({ "mensagem": "Login inválido!" }), 405