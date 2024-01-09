import mysql.connector

# connection

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python"
)

# Cursor
cursor = con.cursor()

# Execute query
query = "DELETE FROM python.assessments WHERE (id = 3);"
cursor.execute(query)

# fetch
rows = cursor.fetchall()

# print
for row in rows:
    print(row)

# close
cursor.close()
con.close()
