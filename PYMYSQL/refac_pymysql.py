import pymysql

def excute_query(connection, query, args=None):
    with connection.cursor() as cursor:  # with 안에서 유지
        cursor.execute(query, args or ())
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        else:
            connection.commit()

def main():
    connection = pymysql.connect(
        host='localhost',
        user='username',
        password='password',
        db='db_name',
        charset='utf8mb4',  # 이모지 개념 설정
        cursorclass=pymysql.cursors.DictCursor  # 딕셔너리 형태로 데이터를 보내라  기본값은 튜플임
    )
    
    try:
        # SELECT 연산
        result = excute_query(connection, "SELECT * FROM table_name")
        print("SELECT 연산 결과:")
        for row in result:
            print(row)
        
        # INSERT 연산
        excute_query(connection, "INSERT INTO table_name (column1, column2) VALUES (%s, %s)", ('data1', 'data2'))
        print("INSERT 연산 수행됨.")
        
        # UPDATE 연산
        excute_query(connection, "UPDATE table_name SET column1=%s WHERE column2=%s", ('new_data1', 'criteria'))
        print("UPDATE 연산 수행됨.")
        
        # DELETE 연산
        excute_query(connection, "DELETE FROM table_name WHERE column_name=%s", ('criteria',))
        print("DELETE 연산 수행됨.")
    
    finally:
        # 데이터베이스 연결 종료
        connection.close()

if __name__ == "__main__":
    main()


