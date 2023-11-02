from flask import Flask, request, jsonify
import logging
from service.credential_check_service import check_username_and_password

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    username: str = body['username']
    logging.debug(f'username: {username}')
    password: str = body['password']

    success: bool = check_username_and_password(username, password)
    logging.debug(f'success: {success}')

    response = jsonify({"success": success})

    return response


if __name__ == '__main__':
    app.run(debug=True, port=5001)
