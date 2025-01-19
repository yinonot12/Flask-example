from datetime import datetime
from . import db

class Loan(db.Model):
    id = db.Column(db.Integer, Primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable = False)
    book_id = db.Column(db.Integer, db.ForeignKey('Book.id'), nullable = False)
    loan_date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)