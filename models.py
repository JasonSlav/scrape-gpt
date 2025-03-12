from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    conversations = db.relationship('Conversation', backref='user', lazy=True)

class Conversation(db.Model):
    conversation_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    title = db.Column(db.String(255), nullable = False)
    link = db.Column(db.Text, nullable = False)
    text = db.Column(db.Text, nullable = False)
    lowercased_text = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.TIMESTAMP, server_default = db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, server_default = db.func.current_timestamp(), onupdate = db.func.current_timestamp())