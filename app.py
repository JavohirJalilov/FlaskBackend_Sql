from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))

@app.route('/')
def home():
    return 'Home Page'

@app.route('/add')
def add_user():
    user1 = User(username='Jalilov',email='javohirjalilov777@gmail.com')
    user2 = User(username='Diyor',email='diyorbekjumanov@gmail.com')
    db.session.add(user1)
    db.session.add(user2)
    bd.session.commit()
    return f'{type(user1)}'

if __name__ == '__main__':
    app.run(debug=True)