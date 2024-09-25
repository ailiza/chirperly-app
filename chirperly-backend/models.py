from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()  # We'll initialize this later in `app.py`

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # ... other user fields (e.g., password, email)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    # ... other contact fields

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    is_scheduled = db.Column(db.Boolean, default=False)
    scheduled_time = db.Column(db.DateTime, nullable=True) 
    # ... other message fields (e.g., sentiment)