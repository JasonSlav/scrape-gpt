from flask import request, jsonify, Flask, make_response, Blueprint
from extensions import db
from models import User
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
auth_bp = Blueprint("auth", __name__)
login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username dan password harus diisi"}), 400

    user = User.query.filter_by(username=data["username"]).first()
    if user:
        return jsonify({"error": "Username sudah terdaftar"}), 400

    new_user = User(username=data["username"])
    new_user.set_password(data["password"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User berhasil didaftarkan"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        response = make_response(jsonify({"message": "Login Sukses!"}), 200)
        return response
    return jsonify({"error": "Username atau password salah"}), 401

@auth_bp.route("/protected", methods=["GET"])
@login_required
def protected():
    return jsonify({"message": f"Halo, {current_user.username}! Ini adalah halaman proteksi."})
    
@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout berhasil!"}), 200
