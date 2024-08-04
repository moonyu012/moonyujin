import pymysql
import pymysql.cursors

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '20153681',
    db= 'airbnb',
    charset='utf8mb4', # 이모지 개념 설정
    cursorclass = pymysql.cursors.DictCursor
)
#with 작업의 시작과 끝을 정의 작업이 끝난 후 자동으로 정리를 수행
with connection.cursor() as cursor: # cursor의 역할 SQL쿼리 실행과 경과를 가져올때 사용
    # 문제1: 새로운 제품 추가
     sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s,%s,%s)"
     cursor.execute(sql, ('Python Book', 10000, 10)) # 데이터 베이스에 전달
     connection.commit() # 전달한걸 반영하겠다.
    
    # #문제2: 고객 목록 조회
     cursor.execute("SELECT * FROM Products")
     for book in cursor.fetchall(): # 가져온 행을 돌면서 처리
         print(book)

    # # 문제3: 제품 재고 업데이트
     sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
     cursor.execute(sql,(1, 1))
     connection.commit()

    # 문제4: 고객별 총 주문 금액 계산
     sql = "SELECT customerID, SUM(totalAmount) AS totalAmount FROM Orders GROUP BY customerID"
     cursor.execute(sql)
     datas = cursor.fetchall()
     print(datas)
    
    # 문제 5 : 고객 이메일 업데이트
     sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
     cursor.execute(sql,('update@update.com', 1))
     connection.commit()

    # 문제 6 : 주문 취소
     sql = "DELETE FROM Orders WHERE orderID = %s"
     cursor.execute(sql,(15))
     connection.commit()

    # 문제 7 : 특정 제품 검색
     sql = "SELECT * FROM Products WHERE productName LIKE %s"
     cursor.execute(sql,('%Book%'))
     datas = cursor.fetchall()

     for data in datas:
         print(data['productName'])

    # 문제 8 : 특정 고객의 주문 데이터 조회
     sql = "SELECT * FROM Orders WHERE customerID = %s"
     cursor.execute(sql,(1))
     datas = cursor.fetchall()

     for data in datas:
         print(data)
    
    # 문제 9: 가방 많이 주문한 고객
     sql = """
        SELECT customerID, COUNT(*) as orderCount 
        FROM Orders GROUP BY customerID 
        ORDER BY orderCount DESC LIMIT 1
        """
     cursor.execute(sql)
     data = cursor.fetchall()
     print(data)


    
cursor.close()
