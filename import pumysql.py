import pumysql

connection = pymysql .connect(
        host ='127.0.0.1',
        user='root',
        password='oz-password',
        db='classicmodels',
        charset='utf8mb4',
        cursorclass=pymysql. cursors. DictCursor
)
cursor =connection.cursor()

sql = "SELECT * FROM customers"
sursor.execute(sql)

customers = cursor.fetchone()
print("customers : ", customers)
print("customers : ", customers[1])
print("customers : ", customers[2])
print("customers : ", customers[3])