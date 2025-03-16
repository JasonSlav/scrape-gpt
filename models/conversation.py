from datetime import datetime, timezone
from sqlalchemy import event
from models import db

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    link = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    preprocessed = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "link": self.link,
            "response": self.response,
            "preprocessed": self.preprocessed,
            "description": self.description,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

@event.listens_for(Conversation, "before_insert")
def before_insert(mapper, connection, target):
    print(f"New Conversation Created: {target.link}")

@event.listens_for(Conversation, "before_update")
def before_update(mapper, connection, target):
    print(f"Conversation Updated: {target.link}")