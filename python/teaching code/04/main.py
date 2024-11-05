import mysql.connector
from mysql.connector import Error

host = "localhost"  # ชื่อโฮสต์ (เช่น 'localhost')
db = "company"  # ชื่อฐานข้อมูลที่ต้องการใช้
user = "root"  # ชื่อผู้ใช้งานฐานข้อมูล
pwd = "keep1234"  # รหัสผ่านของผู้ใช้งาน
table = "employees"

try:
    # สร้างการเชื่อมต่อไปยังฐานข้อมูล
    connection = mysql.connector.connect(
        host=host,
        database=db,
        user=user,
        password=pwd,
    )

    if connection.is_connected():
        # ตรวจสอบว่าการเชื่อมต่อสำเร็จ
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)

        # สร้างตัวชี้เพื่อใช้รันคำสั่ง SQL
        cursor = connection.cursor()

        # รันคำสั่ง SQL ตัวอย่างเพื่อดึงข้อมูลจากตาราง
        cursor.execute("SELECT * FROM " + table)  # แทนที่ 'your_table' ด้วยชื่อตารางของคุณ
        records = cursor.fetchall()

        print("Total number of rows in table: ", cursor.rowcount)
        
        # print(records[1])

        # แสดงข้อมูลที่ได้
        for row in records:
            for col in row:
                print(col)
                
            print('')

except Error as e:
    print("Error while connecting to MySQL", e)
    # print(e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
