from flask_restful import Resource, abort
from flask import jsonify, request

from data import db_session
from data.users import User


class LoginResource(Resource):
    @staticmethod
    def get():
        name = request.json["name"]
        password = request.json["password"]
        session = db_session.create_session()
        user = session.query(User).filter(User.name == name).first()
        if user is None:
            abort(404, message=f"User [{name}] is not found")
        if not user.check_password(password):
            abort(401, message=f"[{name}]'s user password is incorrect")
        return jsonify({"level_amount": user.level_amount, "time": user.time})
