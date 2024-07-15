import pymysql
import pymysql.cursors

# (1) db connection

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '20153681',
    db= 'classicmodels',
    charset='utf8mb4', # 이모지 개념 설정
    cursorclass = pymysql.cursors.DictCursor   # 딕셔너리 형태로 데이터를 보내라  기본값은 튜플임                       
)

#(2) CRUD
 


# 커서를 이용해서 DB에 접속해서 쿼리를 날릴수 있음
def get_customers():
    cursor = connection.cursor()  # 커서를 만들고
    
    sql = "SELECT * FROM customers"  # 쿼리 실행
    cursor.execute(sql)

    # 1. SELECT * FROM
    customers = cursor.fetchone() # 데이터가 하나만 필요하면 fetchone()
    print("customers : ", customers)
    print("customers : ", customers['customerNumber'])
    print("customers : ", customers['customerName'])
    print("customers : ", customers['country'])
    cursor.close()

    # 2.INSERT INTO
def add_customer():
    cursor = connection.cursor() 
    
    name = 'yujin'
    family_name = 'moon'
    sql = f"INSERT INTO customers(customerNumber,customerName,contactLastName) VALUES({1000},'{name}','{family_name}')" 
    cursor.execute(sql)
    connection.commit()  # 쿼리를 샐행한 결과를 데이터베이스에 반영을 해줘
    cursor.close()


# add_customer()

## 3. UPDATE SET

def update_customer():
    cursor = connection.cursor()
    update_name = 'update_inseop'
    contactLastName = 'update_kim'

    sql = f"UPDATE customers SET customerName='{update_name}',contactLastName='{contactLastName}' WHERE customerNumber=1000"
    cursor.execute(sql) # 이 쿼리를 실행해줘
    connection.commit()
    cursor.close()

# update_customer()

## 4. DELETE FROM

def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 10003"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

delete_customer()