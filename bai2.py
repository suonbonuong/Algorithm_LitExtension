# import time
# read csv -> 
import mysql.connector
import csv
# read csv file 
f = open('customer.csv')
data = csv.reader(f)

# connect database 
mydb = mysql.connector.connect(host="127.0.0.1", user='root', port=3306,
                               passwd='DanGerous11@', db='mydatabase')


# create table 
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS customerss")
# mycursor.execute("CREATE DATABASE mydatabase")
create_table = """CREATE TABLE customerss (customerid VARCHAR(255),
                               firstname VARCHAR(255),
                               lastname VARCHAR(255),
                               companyname VARCHAR(255),
                               billingaddress1 VARCHAR(255),
                               billingaddress2 VARCHAR(255),
                               city VARCHAR(255),
                               stat VARCHAR(255),
                               pastalcode VARCHAR(255),
                               country VARCHAR(255),
                               phonenumber VARCHAR(255),
                               emailaddress VARCHAR(255),
                               createdate VARCHAR(255))"""
mycursor.execute(create_table) 

   
data = list(data)
for row in data[1:]:
    mycursor.execute('INSERT INTO customerss(customerid,firstname,lastname,companyname,billingaddress1,billingaddress2,city,stat,pastalcode,country,phonenumber,emailaddress,createdate) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")', row)
mydb.commit()
mycursor.close()
print('Done')
f.close()
