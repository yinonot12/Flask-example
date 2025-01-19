from flask import Flask,request,jsonify 
from flask_cors import CORS
from models import db
from models.user import user 
from models.book import book 
from models.loans import loans

app=Flask(__name__)
CORS(app,resource={r"/*": {"origins": "*"}})


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///library.db'
db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True) #start the flask app with
