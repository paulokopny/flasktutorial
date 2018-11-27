from flask import Flask
from flask import render_template
from flask import request
import db
app = Flask(__name__)

import sqlite3



@app.route('/')
def hello_world():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users")
    users = list(c.fetchall())

    conn.close()
    return render_template('page01.html', users=users)


@app.route('/search')
def search_for_person():
    q = request.args.get('query')
    users = db.get_users_by_name(q)
    return render_template('search_results.html', q=q, users=users)




app.run()
