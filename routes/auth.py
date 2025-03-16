from flask import request, jsonify, Blueprint, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from models import db
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"error": "Username dan password harus diisi"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username sudah terdaftar"}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=True)
    # flash("Register berhasil!", "success")
    return redirect(url_for("home"))

@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"error": "Username dan password harus diisi"}), 400

    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password):
        login_user(user, remember=True)
        # flash("Login berhasil!", "success")
        return redirect(url_for("home"))
    
    flash("Username atau password salah!", "error")
    return redirect(url_for("index"))

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))