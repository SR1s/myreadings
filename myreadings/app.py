#encoding=utf-8
import sys, os
reload(sys)  
sys.setdefaultencoding('utf8')

from flask import Flask, g, request, render_template, flash, redirect, url_for

from myreadings.models import Item, Note, User, db

from myreadings.views.User import user

from config.local_config import \
    (MYSQL_HOST, MYSQL_HOST_S, MYSQL_PORT, 
     MYSQL_USER, MYSQL_PASS, MYSQL_DB)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  \
        'mysql://%s:%s@%s:%s/%s' % \
        (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
app.debug = True
app.secret_key = 'guesswhatkeyitis'
db.init_app(app)
app.register_blueprint(user, url_prefix="/user")

@app.route('/')
def index():
    notes = Note.query.order_by(Note.add_date.desc()).all()
    items = list()
    for note in notes:
        item = Item.query.filter_by(id=note.item_id).first()
        note.mixinItem(item)
        items.append(note)
    return render_template("index.html", items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        link = request.form['link']
        title = request.form['title']
        description = request.form['description']

        item = Item(link, title)
        db.session.add(item)
        db.session.commit()

        note = Note(description, 1, item.id)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for("hello"))
    return render_template("add.html")

@app.route('/u/<int:user_id>')
def user(user_id):
    return str(user_id)

@app.route('/view')
def view():
    return render_template("view.html")

@app.route("/note/add", methods=['POST',])
def add_note():
    pass

if "__main__" == __name__ :
    app.run()
