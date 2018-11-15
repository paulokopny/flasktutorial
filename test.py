from flask import Flask
from flask import render_template
import db
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/userpage/<username>')
def userpage(username):
    user_data = db.get_user(username)
    return render_template('userpage.html', user=user_data)


app.run()
