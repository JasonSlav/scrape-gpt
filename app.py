from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, current_user
from config import Config
from models import db
from routes.auth import auth_bp
from routes.scrape import scrape_bp
import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
CORS(app, supports_credentials=True)

login_manager = LoginManager(app)
login_manager.login_view = "index"

@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    return User.query.get(int(user_id))

@app.route("/navbar")
@login_required
def navbar():
    return render_template("navbar.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
@login_required
def home():
    return render_template("home.html", username=current_user.username)

@app.route("/chat")
@login_required
def chat():
    return render_template("chat.html", username=current_user.username)

@app.route("/history")
@login_required
def history():
    return render_template("history.html", username=current_user.username)

@app.errorhandler(405)
def method_not_allowed(e):
    return redirect(url_for('index'))

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(scrape_bp, url_prefix="/scrape")

if __name__ == "__main__":
    app.run(debug=True)