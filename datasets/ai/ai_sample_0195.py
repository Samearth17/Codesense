import pymysql
from pymongo import MongoClient
import psycopg2

# connect to MySQL
connection_mysql = pymysql.connect(host='localhost', user='root', password='password', database='db_name')

# connect to MongoDB
client = MongoClient('mongodb://localhost:27017')

# connect to PostgreSQL
connection_postgresql = psycopg2.connect(host='localhost', user='postgres', password='password', dbname='db_name')

# define a query for each database
query_mysql = 'SELECT * FROM table_name'
query_mongodb = {'name': 'John Doe'}
query_postgresql =  'SELECT * FROM table_name WHERE age > 18'

# execute the query and fetch the results
result_mysql = connection_mysql.execute(query_mysql)
result_mongodb = client.db_name.collection_name.find(query_mongodb)
result_postgresql = connection_postgresql.execute(query_postgresql)

# close the connections
connection_mysql.close()
client.close() 
connection_postgresql.close()

# render the results on webpage
def render_page(request):
    return render(request, 'template.html', {
        'data_mysql': result_mysql, 
        'data_mongodb': result_mongodb,
        'data_postgresql': result_postgresql
    })