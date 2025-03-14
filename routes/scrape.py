import json
from flask import request, jsonify, Blueprint
from flask_login import login_required, current_user
from models import db
from models.conversation import Conversation
from scraper.scraper import scrape_data

scrape_bp = Blueprint("scrape", __name__)

@scrape_bp.route("/run", methods=["POST"])
@login_required
def run_scraping():
    data = request.json
    query = data.get("query")

    if not query:
        return jsonify({"error": "Query tidak boleh kosong"}), 400

    response = scrape_data(query)

    response_str = json.dumps(response, ensure_ascii=False)

    new_conversation = Conversation(user_id=current_user.id, message=query, response=response_str)

    db.session.add(new_conversation)
    db.session.commit()

    return jsonify({"message": "Scraping berhasil!", "data": response}), 200

@scrape_bp.route("/conversations", methods=["GET"])
@login_required
def get_conversations():
    conversations = Conversation.query.filter_by(user_id=current_user.id).all()
    return jsonify([conv.to_dict() for conv in conversations])