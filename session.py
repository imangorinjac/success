from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///session.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "random string"
db = SQLAlchemy(app)


class Folder(db.Model):

    __tablename__ = "folder"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    files = db.relationship("File", backref="files")

    def __repr__(self):
        return f"Folder({self.name})"


class File(db.Model):

    __tablename__ = "file"

    id = db.Column(db.Integer, primary_key=True)
    folder_id = db.Column(db.Integer, db.ForeignKey("folder.id"))
    name = db.Column(db.String(50))
    size = db.Column(db.Integer)

db.create_all()

def __repr__(self):
        return f"File({self.folder_id}, {self.name}, {self.size})"
