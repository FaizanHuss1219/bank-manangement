import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='root',database='bankmgnt')
cur = conn.cursor()
cur.execute('create table customer_details(acct_no int primary key,acct_name varchar(25),phone_no int(100),address varchar(25),cr_amt float)')
