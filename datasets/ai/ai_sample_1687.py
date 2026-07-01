import flask

app = flask.Flask(__name__)

@app.route('/api/v1/users', methods=['POST'])
def add_user(): 
    data = request.get_json()
    
    #connect to database
    db_connection = create_engine('mysql+pymysql://user:password@localhost/dbname')
    conn = db_connection.connect()

    #execute query
    query = 'INSERT INTO users VALUES(name="{name}", age={age}, email="{email}")'.format(
        name=data['name'], 
        age=data['age'],
        email=data['email']
    )
    conn.execute(query)
    conn.close()

    return jsonify({'status': 'ok'})