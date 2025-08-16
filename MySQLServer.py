import mysql.connector
from mysql.connector import Error  # Import the Error class for catching exceptions
try:
    # Attempt to connect to the MySQL server
# Replace with your connection details
       mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="songa1936",
            )
       if mydb.is_connected():
          mycursor = mydb.cursor()
          # Execute SQL statements using the execute() method on the cursor
          mycursor.execute("CREATE DATABASE IF NOT  EXISTS  alx_book_store")
          print("Database 'alx_book_store' created successfully!")
          # Close connection to the databasse  
          mycursor.close()
          mydb.close()
except Error as e:
    print("Error while connecting to MySQL:", e)
