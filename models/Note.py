from app import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer)
    item_id = db.Column(db.Integer)
    add_date = db.Column(db.DateTime)
    last_edit = db.Column(db.DateTime) 