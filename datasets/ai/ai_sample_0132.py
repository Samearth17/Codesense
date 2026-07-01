import psycopg2
from datetime import datetime, timedelta
import schedule
import time

conn = psycopg2.connect(
 host="localhost", 
 database="db", 
 user="user", 
 password="password"
)

def refresh_data():
 cur = conn.cursor()
 query = 'REFRESH TABLE "TableName";'
 cur.execute(query)
 conn.commit()

# run the refresh_data job every 5 minutes
schedule.every(5).minutes.do(refresh_data)

while True:
 schedule.run_pending()
 time.sleep(1)