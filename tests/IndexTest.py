import os
import unittest
import tempfile
from myreadings import app, db

class IndexTest(unittest.TestCase):
    def setUp(self):
        self.db_fd, db_path = tempfile.mkstemp()
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + db_path
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.test_request_context():
            db.drop_all(app = app)
            db.create_all(app = app)

    def tearDown(self):
        os.close(self.db_fd)
        #os.unlink(app.config['SQLALCHEMY_DATABASE_URI'])

    def test_add_note(self):
        rv = self.app.post('/add', data=dict(
            link="link",
            title="title",
            description="description"),
            follow_redirects=True
        )
        self.assertTrue('link' in rv.data)
        self.assertTrue('title' in rv.data)
        self.assertTrue('description' in rv.data)