from app import db
from app import app

app.test_request_context().push()
db.drop_all(app=app)
db.create_all(app=app)
