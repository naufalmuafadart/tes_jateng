from flask import Flask, request
from dotenv import load_dotenv
import helper.database.db_user as db_user
import helper.database.db_auth as db_auth
import helper.database.db_card as db_card
import helper.bearer as bearer_helper
import helper.json_web_token as json_web_token
import os

load_dotenv()

app = Flask(__name__)

@app.route('/login')
def login():
    phone_number = request.json['phone_number']
    password = request.json['password']
    try:
        access_token, refresh_token, _id = db_user.check_login(phone_number, password)
        db_auth.insert(_id, refresh_token)
        return {
            'status': 'success',
            'message': 'success login',
            'data': {
                'access_token': access_token,
                'refresh_token': refresh_token
            },
        }
    except Exception as e:
        return {
            'status': 'fail login',
            'message': str(e)
        }, 400

@app.route('/logout')
def logout():
    headers = request.headers
    bearer = headers.get('Authorization')
    try:
        token = bearer_helper.validate_bearer(bearer)
        payload = json_web_token.verify_token(token, True)
        user_id = payload['id']
        db_auth.delete(user_id)
        return {
            'status': 'success',
            'message': 'success logout',
            'data': user_id,
        }
    except Exception as e:
        return {
            'status': 'fail logout',
            'message': str(e)
        }, 400

@app.route('/addCard', methods=['POST'])
def add_card():
    headers = request.headers
    bearer = headers.get('Authorization')
    number = request.json['number']
    holder = request.json['holder']
    month_expired = request.json['month_expired']
    year_expired = request.json['year_expired']
    security_code = request.json['security_code']
    try:
        token = bearer_helper.validate_bearer(bearer)
        payload = json_web_token.verify_token(token, True)
        user_id = payload['id']
        db_card.insert(user_id, number, holder, month_expired, year_expired, security_code)
        return {
            'status': 'success',
            'message': 'success add card',
        }
    except Exception as e:
        return {
            'status': 'fail add card',
            'message': str(e)
        }, 400


@app.route('/getCardList')
def get_card_list():
    headers = request.headers
    bearer = headers.get('Authorization')
    try:
        token = bearer_helper.validate_bearer(bearer)
        payload = json_web_token.verify_token(token, True)
        user_id = payload['id']
        data = db_card.get_by_user_id(user_id)
        return {
            'status': 'success',
            'message': 'success get cards list',
            'data': data
        }
    except Exception as e:
        return {
            'status': 'fail add card',
            'message': str(e)
        }, 400

@app.route('/getCardDetail/<_id>')
def get_card_detail(_id):
    headers = request.headers
    bearer = headers.get('Authorization')
    try:
        token = bearer_helper.validate_bearer(bearer)
        payload = json_web_token.verify_token(token, True)
        data = db_card.get_by_id(_id)
        return {
            'status': 'success',
            'message': 'success get card detail',
            'data': data
        }
    except Exception as e:
        return {
            'status': 'fail add card',
            'message': str(e)
        }, 400

app.run(debug=True, host=os.getenv('APP_HOST'), port=os.getenv('APP_PORT'))
