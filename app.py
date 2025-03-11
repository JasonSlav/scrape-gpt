from flask import Flask
from config import Config
from extensions import db, cors, migrate
from routes import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

# Inisialisasi ekstensi
db.init_app(app)
cors.init_app(app)
migrate.init_app(app, db)

# 🔹 Konfigurasi CORS agar mendukung Cookie (credentials: "include")
cors.init_app(app, supports_credentials=True)

# Daftarkan blueprint
app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True)