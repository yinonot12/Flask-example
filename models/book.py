from . import db

class Book(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    author=db.Column(db.String(200), nullable=False)
    year_published=db.Column(db.String(10), nullable=False)
    genere=db.Column(db.String(10), nullable=False)
    





