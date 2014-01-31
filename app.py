#encoding=utf-8

from flask import Flask, g, request, render_template, flash, redirect, url_for
import MySQLdb

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

import imp
try:
    imp.find_module("sae")
    from sae.const import (MYSQL_HOST, MYSQL_HOST_S, MYSQL_PORT, 
                           MYSQL_USER, MYSQL_PASS, MYSQL_DB)
except ImportError:
    from config.local_config import (MYSQL_HOST, MYSQL_HOST_S, MYSQL_PORT, 
                                     MYSQL_USER, MYSQL_PASS, MYSQL_DB)

app = Flask(__name__)
app.debug = True
app.secret_key = 'guesswhatkeyitis'


@app.before_request
def before_request():
    g.db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS,
                           MYSQL_DB, port=int(MYSQL_PORT), charset="utf8") #Define charset to avoid chinese decode error

#请求结束时关闭数据库连接
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/')
def hello():
    sql = """SELECT `title`, `link`, `description` FROM `items` ORDER BY `id` desc; """
    c = g.db.cursor()
    c.execute(sql)
    items = list(c.fetchall())
    #js = json.loads(items)
    #return json.dumps(items,ensure_ascii=False)
    return render_template("index.html", items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        link = request.form['link']
        title = request.form['title']
        description = request.form['description']
        sql = """INSERT `items`(`link`, `title`, `description`) VALUES ('%s', '%s', '%s')""" % (link, title, description)
        c = g.db.cursor()
        c.execute(sql)
        flash('添加成功')
        return redirect(url_for("hello"))
    return render_template("add.html")

if "__main__" == __name__ :
    app.run()
