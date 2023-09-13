import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = '56743'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class TaskTwo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, name, username):
        self.name = name
        self.username = username


with app.app_context():
    db.create_all()


def check(name):
    word_list = list(name)
    check = None
    for i in word_list:
        try:
            value = int(i)
        except ValueError:
            check = True
        else:
            check = False
            break
    return check


@app.route('/api/<int:id>', methods=['GET'])
def read_task(id):
    try:
        user = db.session.execute(db.select(TaskTwo).filter_by(
            id=id)).scalar_one()  # Use TaskTwo.query.get to retrieve a record by its primary key
        # return jsonify(response=f'No Result with id={id} Found', status_code=404), 404

    except Exception as e:
        return jsonify(response=str(e), status_code=500), 500
    else:
        return jsonify(id=user.id, name=user.name, username=user.username), 200


@app.route('/api', methods=['POST'])
def create():
    try:
        data = request.get_json()
        name = data.get('name')
        random_int = randint(1, 1001)
        if check(name):
            username = f'{name}{random_int}'
            user = TaskTwo(name=name, username=username)
            db.session.add(user)
            db.session.commit()
            return jsonify(response=f'{name} created successfully', id=user.id,
                           name=user.name, username=user.username, status_code=200), 200
        else:
            return jsonify(response=f'{name} contains an integer, not allowed', status_code=400), 400
    except Exception as e:
        return jsonify(response=str(e), status_code=500), 500


@app.route('/api/<int:id>', methods=['PUT'])
def update_task(id):
    try:
        data = request.get_json()
        name = data.get('name')
        username = data.get('username')
        user = TaskTwo.query.get(id)
        if user is None:
            return jsonify(response=f'user with id = {id} not found', status_code=404), 404
        if check(name):
            if username:
                user.username = username
            user.name = name
            db.session.commit()
            updated = TaskTwo.query.get(id)
            return jsonify(response='User update', id=updated.id, name=updated.name, username=updated.username,
                           status_code=200), 200
        else:
            return jsonify(response=f'{name} contains an integer, not allowed', status_code=400), 400
    except Exception as e:
        return jsonify(response=str(e), status_code=500), 500


@app.route('/api/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        user = db.session.execute(db.select(TaskTwo).filter_by(id=id)).scalar_one()
        if user is None:
            return jsonify(response=f'{id} does not exist', status_code=404), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify(response=f'user with id={id} has been deleted', status_code=204), 204
    except Exception as e:
        return jsonify(response=str(e), status_code=500), 500


if __name__ == '__main__':
    app.run(debug=True)
