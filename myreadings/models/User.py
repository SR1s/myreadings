from myreadings.models import db
from 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    sina_id = db.Column(db.String(255))

    def __init__(self, username, email, password, sina_id=None):
    	self.username = username
    	self.email = email
    	self.password = password
    	if sina_id:
    		self.sina_id = sina_id