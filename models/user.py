from . import db 

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(15),nullable=False)
    phone_number=db.Column(db.String,primary_key=True)
    city=db.Column(db.String(10),nullable=True)
    age=db.Column(db.Integer,nullable=True)
