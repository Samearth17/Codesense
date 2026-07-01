import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_data_from_db(table_name):
    
    # connect to the database
    connection = psycopg2.connect(
        user='username',
        password='password',
        host='host',
        port='5432',
        database='testdb'
    )
    cursor = connection.cursor()
    
    # retrieve data from the table
    sql = f"""SELECT column1, column2, column3 FROM {table_name}"""
    cursor.execute(sql)
    records = cursor.fetchall()
    
    # close the connection
    connection.close()

    return records

@app.route('/data/<table_name>', methods=['GET'])
def get_data(table_name):
    # retrieve data from the db
    data = get_data_from_db(table_name)

    # build response
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run()