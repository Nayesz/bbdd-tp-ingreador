from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')
db=SQLAlchemy(app)
db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

