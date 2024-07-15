import mysql.connector # pip install mysql-connector-python
from faker import Faker # pip install faker
import random

# MySQL 연결 설정
db_connection = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "20153681",
	database = "testdatabase"
)

cursor = db_connection.cursor()
fake = Faker()

# users 테이블에 데이터 삽입
for _ in range(100): # '_' 이 값을 굳이 사용은 하지 않을거고 99까지 반복을 할꺼야
	username = fake.user_name()
	email = fake.email()
	sql = "INSERT INTO users (username, email) VALUES(%s, %s)" # 데이터를 넣어줘 users테이블에 (이 필드에) string 데이터를 넣을꺼야, 어떤 데이터를 넣을건데 username, email 값을 넣을거야
	values = (username,email)
	cursor.execute(sql,values) # 쿼리를 실행해줘

# user_id 불러오기
cursor.execute("SELECT user_id FROM users") # 커서에 결과가 담김
valid_user_id = [row[0] for row in cursor.fetchall()] #fetchall에서 데이터를 불러오고 row 데이터에 들어옴 그중에서 [0] 데이터를 가져와서 유저아이디로 사용 하겠다. 리스트에 담음

# 100개의 주문 더미 데이터 생성

for _ in range(100):
    user_id = random.choice(valid_user_id)  # 담긴 리스트 중에 하나를 랜덤으로 선택
    product_name = fake.word()  # 단어를 랜덤으로 만드는 함수
    quantity = random.randint(1, 10)

    try:
        sql = "INSERT INTO orders(user_id, product_name, quantity) VALUES(%s, %s, %s)"  # 데이터를 넣어줘 orders 라는 테이블인데 어떤걸 넣고 싶은데 ? -> user_id, product_name, quantity 넣고 싶은 값은 뭔데 (%s)
        values = (user_id, product_name, quantity)  # 필요한 값은? 컬럼명과 변수 명을 동일하게 해야 편하다
        cursor.execute(sql, values)
    except: # 유효하지 않은 user_id로 인한 오휴 처리
        
        pass

db_connection.commit() # 변경 내용 커밋
cursor.close() #  연결 해제
db_connection.close() 

