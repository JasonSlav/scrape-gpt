from flask import request, jsonify, Blueprint
from flask_login import login_user, login_required, logout_user
from models import db
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username dan password harus diisi"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username sudah terdaftar"}), 400

    new_user = User(username=data["username"])
    new_user.set_password(data["password"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User berhasil didaftarkan"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()
    
    if user and user.check_password(data.get("password")):
        login_user(user, remember=True)
        return jsonify({"message": "Login Sukses!"}), 200
    
    return jsonify({"error": "Username atau password salah"}), 401

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout berhasil!"}), 200