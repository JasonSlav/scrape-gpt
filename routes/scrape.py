import json
from flask import request, jsonify, Blueprint
from flask_login import login_required, current_user
from models import db
from models.conversation import Conversation
from scraper.scraper import scrape_data
from scraper.preprocess import preprocess_conversation

scrape_bp = Blueprint("scrape", __name__)

@scrape_bp.route("/run", methods=["POST"])
@login_required
def run_scraping():
    data = request.json
    url = data.get("url")
    description = data.get("description")

    if not url:
        return jsonify({"error": "URL tidak boleh kosong"}), 400

    response = scrape_data(url)
    if "error" in response:
        return jsonify({"error": response["error"]}), 400

    response_str = json.dumps(response, ensure_ascii=False)
    preprocessed = preprocess_conversation(response_str)

    new_conversation = Conversation(
        user_id=current_user.id,
        link=url,
        response=response_str,
        preprocessed=preprocessed,
        description=description
    )

    db.session.add(new_conversation)
    db.session.commit()

    return jsonify({"message": "Scraping berhasil!", "data": response}), 200

@scrape_bp.route("/conversations", methods=["GET"])
@login_required
def get_conversations():
    conversations = Conversation.query.filter_by(user_id=current_user.id).with_entities(
        Conversation.id, Conversation.created_at, Conversation.link, Conversation.description
    ).all()
    
    return jsonify([
        {
            "id": conv.id,
            "created_at": conv.created_at.isoformat() if conv.created_at else None,
            "link": conv.link,
            "description": conv.description
        }
        for conv in conversations
    ])

@scrape_bp.route("/conversations/<int:conversation_id>", methods=["GET"])
@login_required
def get_conversation_detail(conversation_id):
    conversation = Conversation.query.filter_by(id=conversation_id, user_id=current_user.id).first_or_404()
    return jsonify(conversation.to_dict())