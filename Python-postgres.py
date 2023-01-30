
--Creating tables using Python in Postgres

--Creating Connection

import psycopg2

try:
    conn = psycopg2.connect("host=localhost dbname=Sankar_S user=postgres password=12345Welcome$")
except psycopg2.Error as e:
    print("Error: Could not make connection to DB")
    print(e)
    
--Creating cursor to Execute SQL commands

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not make connection to DB")
    print(e)
    
conn.set_session(autocommit=True)

--Creating tables

try:
    cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS (student_id int, name varchar, age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e:
    print("Issue in creating table")
    print(e)
    
--Inserting records into table

try:
    cur.execute("INSERT INTO STUDENTS (student_id, name, age, gender, subject, marks) \
                VALUES (%s,%s,%s,%s,%s,%s)", \
                (1, 'Sankar', 23, 'Male', 'Maths', 95))
except psycopg2.Error as e:
    print("Issue in inserting records")
    print(e)

try:
    cur.execute("INSERT INTO STUDENTS (student_id, name, age, gender, subject, marks) \
                VALUES (%s,%s,%s,%s,%s,%s)", \
                (1, 'Ram', 35, 'Male', 'English', 80))
except psycopg2.Error as e:
    print("Issue in inserting records")
    print(e)
    
    
-- Fetching data from DB

try:
    cur.execute("SELECT * FROM STUDENTS;")
except psycopg2.Error as e:
    print(e)
    
row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()
    
 --Closing the connection
 
 cur.close()
conn.close()