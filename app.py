import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, make_response, Blueprint
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "bismillahucl")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:0963@127.0.0.1/flask")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
cors = CORS(app, supports_credentials=True)

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

auth_bp = Blueprint("auth", __name__)

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
        login_user(user, remember=True)
        response = make_response(jsonify({"message": "Login Sukses!"}), 200)
        return response
    return jsonify({"error": "Username atau password salah"}), 401

@auth_bp.route("/protected", methods=["GET"])
@login_required
def protected():
    return jsonify({"message": f"Halo, {getattr(current_user, 'username', 'User')}! Ini adalah halaman proteksi."})

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout berhasil!"}), 200

@auth_bp.route('/upload', methods=['POST'])
@login_required
def upload_link():
    user_id = user_id
    data = request.json
    new_link = UploadedLink(user_id=load_user(user_id), link=data['link'])
    db.session.add(new_link)
    db.session.commit()
    return jsonify({"message": "Link uploaded"})

app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True)