from flask import jsonify, make_response, request



# Dummy user data
users = {
    'user1': {'username': 'user1', 'password': 'pass1'},
    'user2': {'username': 'user2', 'password': 'pass2'}
}
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return make_response(jsonify({'message': 'Username or password missing'}), 400)

    user = users.get(username)
    if not user or user['password'] != password:
        return make_response(jsonify({'message': 'Invalid credentials'}), 401)

    response = make_response(jsonify({'message': 'Logged in successfully'}), 200)
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.set_cookie('username', username)  # Set cookie
    return response

def check_login():
    username = request.cookies.get('username')
    if username:
        return jsonify({'logged_in': True, 'username': username})
    else:
        return jsonify({'logged_in': False}), 401
    
def logout():
    response = make_response(jsonify({'message': 'Logged out successfully'}), 200)
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.set_cookie('username', '', expires=0)  # Delete cookie
    return response