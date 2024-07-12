import mysql.connector

#connect to sql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="<password>"
)

#create cursor
mycursor = mydb.cursor()

#create db
mycursor.execute("CREATE DATABASE car_rental")

#select car_rental db
mycursor.execute("USE car_rental")

#cars table
mycursor.execute("CREATE TABLE cars ("
                 "car_id INT AUTO_INCREMENT PRIMARY KEY, "
                 "make VARCHAR(50), "
                 "model VARCHAR(50), "
                 "year DATE);")

#admin table
mycursor.execute("CREATE TABLE admins ("
                 "admin_id INT AUTO_INCREMENT PRIMARY KEY, "
                 "name VARCHAR(50), "
                 "email VARCHAR(50), "
                 "password VARCHAR(50), "
                 "phone INT);")

#customer table
mycursor.execute("CREATE TABLE customers ("
                 "customer_id INT AUTO_INCREMENT PRIMARY KEY, "
                 "name VARCHAR(50), "
                 "email VARCHAR(50), "
                 "password VARCHAR(50), "
                 "phone INT);")

#orders table
mycursor.execute("CREATE TABLE orders ("
                 "order_id INT AUTO_INCREMENT PRIMARY KEY, "
                 "customer_id INT, "
                 "car_id INT, "
                 "from_date DATE, "
                 "to_date DATE, "
                 "status VARCHAR (20), "
                 "FOREIGN KEY (customer_id) REFERENCES customers(customer_id), "
                 "FOREIGN KEY (car_id) REFERENCES cars(car_id));")