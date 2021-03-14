from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(80),unique=True)

    def __repr__(self):  
        return f'username: {self.username} email: {self.email}'

@app.route('/')
def home():
    return 'Home Page'

@app.route('/add')
def add_user():
    user1 = User(username='Jalilov',email='javohirjalilov777@gmail.com')
    user2 = User(username='Diyor',email='diyorbekjumanov@gmail.com')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    return 'ok'

@app.route('/read')
def read_user():
    users = User.query.get(1)
    return str(users)

@app.route('/delete')
def delete():
    users = User.query.first()
    db.session.delete(users)
    db.session.commit()
    return 'delete'

if __name__ == '__main__':
    app.run(debug=True)