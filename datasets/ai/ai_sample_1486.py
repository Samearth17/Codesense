import flask
import mysql.connector

app = flask.Flask(__name__)
mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    passwd = "yourpassword"
)  

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method == 'GET':
        # return all user records
        cursor = mydb.cursor() 
        query = "SELECT * FROM users"
        cursor.execute(query)
        results = cursor.fetchall()
        return jsonify(results)
    
    if request.method == 'POST':
        # add a new user record
        data = request.get_json()
        sql_query = "INSERT INTO users (name, age, email") VALUES (%s, %s, %s)"
        val = (data['name'], data['age'], data['email'])
        cursor.execute(sql_query, val)
        mydb.commit()
        return jsonify({'message': 'user added successfully'})
    
    if request.method == 'PUT':
        # edit an existing user record
        data = request.get_json()
        sql_query = "UPDATE users SET name = %s, age = %s, email = %s WHERE id = %s" 
        val = (data['name'], data['age'], data['email'], data['id'])
        cursor.execute(sql_query, val)
        mydb.commit()
        return jsonify({'message': 'user record updated successfully'})

    if request.method == 'DELETE':
        # delete a user record
        data = request.get_json()
        sql_query = "DELETE FROM users WHERE id = %s" 
        val = (data['id'],)
        cursor.execute(sql_query, val)
        mydb.commit()
        return jsonify({'message': 'user record deleted successfully'})