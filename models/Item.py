from flask.ext.sqlalchemy import SQLAlchemy
from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(255), unique=True)
    title = db.Column(db.String(255))

    def __init__(self, link, title):
        self.link = link
        self.title = title

    def __repr__(self):
        return '<Item: %s : %s>' % \
                (self.title, self.link)