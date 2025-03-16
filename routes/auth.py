from flask import request, jsonify, Blueprint, url_for, redirect, flash, session
from flask_login import login_user, login_required, logout_user
from models import db
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        flash("Username dan password harus diisi!", "error")
        return redirect(url_for("index"))  # Redirect kembali ke halaman register/login

    if User.query.filter_by(username=username).first():
        flash("Username sudah terdaftar!", "error")
        return redirect(url_for("index"))  # Redirect kembali ke halaman register/login

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=True)
    flash("Registrasi berhasil! Selamat datang.", "success")
    return redirect(url_for("home"))  # Redirect ke halaman utama setelah sukses

@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        flash("Username dan password harus diisi!", "error")
        session["flash"] = {"message": "Username dan password harus diisi!", "category": "error"}
        return redirect(url_for("index"))

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        login_user(user, remember=True)
        flash("Login berhasil!", "success")
        session["flash"] = {"message": "Login berhasil!", "category": "success"}
        return redirect(url_for("home"))

    flash("Username atau password salah!", "error")
    session["flash"] = {"message": "Username atau password salah!", "category": "error"}
    return redirect(url_for("index"))

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))