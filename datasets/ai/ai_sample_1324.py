@app.route('/users/api/v1.0/users')
def get_users():
 users = [
 {
 'id': 1,
 'name': 'John Smith',
 'email': 'john.smith@example.com'
 },
 {
 'id': 2,
 'name': 'Jane Doe',
 'email': 'jane.doe@example.com',
 }
 ]
 return jsonify({'users': users})