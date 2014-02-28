from myreadings.models import db
from datetime import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer)
    item_id = db.Column(db.Integer)
    add_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_edit = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, content, user_id, item_id):
        self.content = content
        self.user_id = user_id
        self.item_id = item_id

    def __repr__(Note):
        return '<Item: %s By %s - %s>' % \
                (self.content, self.item_id, self.add_date)