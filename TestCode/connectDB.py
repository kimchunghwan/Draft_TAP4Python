import pymssql

# MSSQL
conn = pymssql.connect(host='localhost', user='root', password='eisan$2016', database='EISAN')
cursor = conn.cursor()
cursor.execute(
    "select * from tap")
rows = cursor.fetchall()

for row in rows:
    print(str(row))


# 디비 관련해서 테스트 툴에 필요한 기능은 아래와 같다.
# 엑셀 -> 데이터 , 데이터 -> 엑셀로 변환하는 처리도 필요하겠지
# truncate 혹은 테이블 초기화

# insert
# update
# select
# run sql
# db diff
# 그리고 필요한것이
