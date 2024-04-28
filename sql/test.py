import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password = "admin",
    database = "python_test"
)

print(mydb)

# Create a database 
mycursor = mydb.cursor()

# **Create database**
# mycursor.execute("CREATE DATABASE python_test")
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)

# **Create table**
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


# **Insert data**
# sql = "INSERT INTO customers (name, address) VALUES (%s,%s)"
# val = ("John", "Highway 21")
# **Multiple Values**
val = [
    ("John", "Lowstreet 4"),
    ("Ivan", "New York"),
    ("Melisa", "Brooklyn"),
]
# mycursor.execute(sql, val)
# mycursor.executemany(sql, val)

# mydb.commit()
# print(mycursor.rowcount, "record inserted")
# print("1 record inserted, ID: ", mycursor.lastrowid)

# ** Select From**

# mycursor.execute("SELECT * FROM customers WHERE address='Brooklyn'")
# mycursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'")
# mycursor.execute("SELECT name, address FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# myresult = mycursor.fetchone()
# print(myresult)

# **Prevent SQL Inyection**

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("New York",)

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# **Sort the result**

sql = "SELECT * FROM customers ORDER BY name" # ASC or DESC
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# **Delete a record**

sql = "DELETE FROM customers WHERE address = %s"
adr = ('Lowstreet 4',)

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# **Delete a Table**

sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)

# **Update a record**

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# **LIMIT AND OFFSET**

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2") # Starts from the third record and foward
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# **Join Table**
# sql = "SELECT \
#     users.name AS user, \
#     products.name AS favorite \
#     FROM users \
#     INNER JOIN products ON users.fav = products.id"
# sql = "SELECT \
#     users.name AS user, \
#     products.name AS favorite \
#     FROM users \
#     LEFT JOIN products ON users.fav = products.id"
sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    RIGHT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)