from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from Adapters.database import init_db
from Models.school_model import db
from Controllers.schoolcontroller import SchoolController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS


init_db(app)

@app.route('/')
def hello():
    return "Hello, Flask!"


@app.route('/schools', methods=['GET'])
def get_schools():
    return SchoolController.get_schools()

@app.route('/schools', methods=['POST'])
def add_schools():
    return SchoolController.add_school()

@app.route('/schools/<int:school_id>', methods=['GET'])
def get_school(school_id):
    return SchoolController.get_school(school_id)

@app.route('/schools/<int:school_id>', methods=['DELETE'])
def delete_school(school_id):
    return SchoolController.delete_school(school_id)

if __name__ == '__main__':
    app.run(debug=True)
