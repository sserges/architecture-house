from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())
