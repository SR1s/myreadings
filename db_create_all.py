from app import db
from app import app

app.test_request_context().push()
db.create_all(app=app)
