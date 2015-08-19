#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="chappie", user="chappie", password="chappie15", host="chappie.cxrfold0ewxa.us-east-1.rds.amazonaws.com", port="5432")

print ("Opened database successfully")

cursor = conn.cursor()

name = "minions"
age = 2
address = "South Pole"
email = "minions@minions.com"


query = ('insert into customer (cust_name, cust_age, cust_address, cust_email) values (%s, %s, %s, %s)')
data = (name, age, address, email)
cursor.execute(query, data)

cursor.execute('SELECT * FROM customer')
rows = cursor.fetchall()
for row in rows:
   print (row)
   
print ("Operation done successfully")
conn.close()
