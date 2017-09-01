from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///solidareasy.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    token = db.Column(db.String(120), unique=True)

    def __init__(self, username, email, token):
        self.username = username
        self.email = email
        self.token = token

    def __repr__(self):
        return '<User %r>' % self.username
if __name__ == '__main__':
	db.create_all()