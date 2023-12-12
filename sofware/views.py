from flask import Blueprint, request, json, jsonify
from .models import Users
from sofware import db

views = Blueprint('views', __name__)


@views.route('/register', methods=["POST"])
def register():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        telephone = request.form.get("telephone")
        mail = request.form.get("email")
        password = request.form.get("password")

        user = Users.query.filter_by(email=mail).first()

        if user is None:
            # Si l'étudiant n'existe pas, créez-en un nouveau
            new_user = Users(fullname=fullname, telephone=telephone, email=mail, password=password)

            db.session.add(new_user)
            db.session.commit()

            return jsonify(["Register success"])
        else:
            return jsonify(["User already exists"])

@views.route('/login', methods=["GET", "POST"])
def login():
    d = {}
    if request.method == "POST":
        mail = request.form["email"]
        password = request.form["password"]

        login = Users.query.filter_by(email=mail, password=password).first()

        if login is None:
            # acount not found

            return jsonify(["Wrong Credentials"])
        else:
            # acount found

            return jsonify(["success"])