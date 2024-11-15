from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class School(db.Model):
    __tablename__ = 'Schools'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)