import time

# Connect to the database
db_conn = db_connect()

# Set the duration in seconds    
duration = 10
 
# Start the timer
start_time = time.time()

# Check if the duration has been exceeded
while (time.time() - start_time) < duration:
    # Continue with the database operation.
 
# Close the database connection
db_conn.close()