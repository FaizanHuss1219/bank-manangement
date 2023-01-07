'''import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='root',database='bankmgnt')
cur=conn.cursor()

conn.autocommit = True

print('1:CREATE BANK ACCOUNT')
print('2:TRANSACTION')
print('3:CUSTOMER DETAILS')
print('4:TRANSACTION DETAILS')
print('5:DELETE DETAILS')
print('6:QUIT')

n=int(input('Enter Your Choice:'))

if n==1:
    acc_no=int(input('Enter your Account Number:'))
    acc_name=input('Enter your Account Name:')
    ph_no=int(input('Enter your Phone Number:'))
    add=(input('Enter your Address:'))
    cr_amt=int(input('Enter your Credit Number:'))
    v_SQLInsert="INSERT  INTO customer_details values (" +  str (acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " +add + " ',"+ str (cr_amt) + " ) "
    cur.execute(v_SQLInsert)
    print('=======ACCOUNT CREATED SUCCESFULLY=======')
    conn.commit()

if n==2:
    acct_no=int(input('Enter your Account Number:'))
    cur.execute('select * from customer_details where acct_no:'+str (acct_no))
    data=cur.fetchall()
    count=cur.rowcount
    conn.commit()
    if count ==0:
        print('Account Number Invalid......Try Again...')
    else:
        print('1:WITHDRAW AMOUNT')
        print('2:ADD AMOUNT')
        x=int(input('Enter your Choice:'))
        if x==1:
            amt=int(input('Enter the Withdrawl Amount:'))
            cur.execute('update customer_details set cr_amt=cr_amt-'+str(amt) +' where acct_no=' +str(acct_no))
            conn.commit()
            print('=====Account Updated Successfully=====')
        if x==2:
            amt=int(input('Enter amount to be added:'))
            cur.execute('update customer_details set cr_amt=cr_amt+'+str(amt) +' where acct_no=' +str(acct_no))
            conn.commit()
            print('=====Account Updated Successfully=====')

if n==3:
    acct_no=int(input('Enter your Account Number:'))
    cur.execute('select * from customer_details where acct_no:'+str(acct_no))
    if cur.fetchone() is None:
        print('invalid Account Number')
    else:
        cur.execute('select * from customer_details where acct_no:'+str(acct_no))
        data=cur.fetchall()
        for row in data:
            print('ACCOUNT NO=',acct_no)
            print('ACCOUNT NAME=',row[1])
            print('PHONE NUMBER=',row[2])
            print('ADDRESS=',row[3])
            print('CREDIT ACCOUNT=',row[4])

if n== 4:
     acct_no=int(input('Enter your account number='))
     print()
     cur.execute('select * from customer_details where  acct_no='+str(acct_no) )
     if cur.fetchone() is  None:
         print()
         print('Invalid Account number')
     else:
         cur.execute('select * from transactions where acct_no='+str(acct_no) )
         data=cur.fetchall()
         for row in data:
            print('ACCOUNT NO=',acct_no)
            print()
            print('DATE=',row[1])
            print()
            print(' WITHDRAWAL AMOUNT=',row[2])
            print()
            print('AMOUNT ADDED=',row[3])
            print()'''









import datetime as dt
import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='root',database='bankmgnt')
cur = conn.cursor()

      

conn.autocommit = True
c = 'y'
while c == 'y':
    
                         print()
                         print('1.CREATE BANK ACCOUNT')
                         print()
                         print('2.TRANSACTION')
                         print()
                         print('3.CUSTOMER DETAILS')
                         print()
                         print('4.TRANSACTION DETAILS')
                         print()
                         print('5.DELETE ACCOUNT')
                         print()
                         print('6.QUIT')

                         print()
                         n=int(input('Enter your CHOICE='))
                         print()

                         if n == 1:

                                    acc_no=int(input('Enter your ACCOUNT NUMBER='))
                                    print()
                                    acc_name=input('Enter your ACCOUNT NAME=')
                                    print()
                                    ph_no=int(input('Enter your PHONE NUMBER='))
                                    print()
                                    add=(input('Enter your place='))
                                    print()
                                    cr_amt=int(input('Enter your credit amount='))
                                    V_SQLInsert="INSERT  INTO customer_details values (" +  str (acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " +add + " ',"+ str (cr_amt) + " ) "
                                    cur.execute(V_SQLInsert)
                                    print()
                                    print('=====Account Created Succesfully=====')
                                    conn.commit()
    

                         if n == 2:
                              acct_no=int(input('Enter Your Account Number='))
                              cur.execute('select * from customer_details where acct_no='+str (acct_no) )
                              data=cur.fetchall()
                              count=cur.rowcount
                              conn.commit()
                              if count == 0:
                                   print()
                                   print('Account Number Invalid Sorry Try Again Later')
                                   print()
                              else:
                                   print()
                                   print('1.WITHDRAW AMOUNT')
                                   print()
                                   print('2.ADD AMOUNT')
                                   print()

                                   print()
                                   x=int(input('Enter your CHOICE='))
                                   print()
                                   if x == 1:
                                        amt=int(input('Enter withdrawl amount='))
                                        cr_amt=0
                                        cur.execute('update customer_details set   cr_amt=cr_amt-'+str(amt) +  ' where acct_no=' +str(acct_no) )
                                        V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),amt,cr_amt) 
                                        cur.execute(  V_SQLInsert)
                                        conn.commit()
                                        print()
                                        print('=====TRANSACTION SUCESSFULL=====')
                                        
                                        

                                   if x== 2:
                                         amt=int(input('Enter amount to be added='))
                                         cr_amt=0
                                         cur.execute('update customer_details set  cr_amt=cr_amt+'+str(amt) +  ' where acct_no=' +str(acct_no) )
                                         V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),cr_amt,amt)
                                         cur.execute(  V_SQLInsert)
                                         conn.commit()
                                         print()
                                         print('=====Account Updated Succesfully=====')

                         if n == 3:
                              acct_no=int(input('Enter your account number='))
                              print()
                              cur.execute('select * from customer_details where acct_no='+str(acct_no) )
                              if cur.fetchone() is  None:
                                   print()
                                   print('Invalid Account number')
                              else:
                                   cur.execute('select * from customer_details where acct_no='+str(acct_no) )
                                   data=cur.fetchall()
                                   for row in data:
                                        print('ACCOUNT NO=',acct_no)
                                        print()
                                        print('ACCOUNT NAME=',row[1])
                                        print()
                                        print('PHONE NUMBER=',row[2])
                                        print()
                                        print('ADDRESS=',row[3])
                                        print()
                                        print('cr_amt=',row[4])
                         if n == 4:
                               acct_no=int(input('Enter your account number='))
                               print()
                               cur.execute('select * from customer_details where acct_no='+str(acct_no) )
                               if cur.fetchone() is  None:
                                   print()
                                   print('Invalid Account number')
                               else:
                                   cur.execute('select * from transactions where acct_no='+str(acct_no) )
                                   data=cur.fetchall()
                                   for row in data:
                                        print('ACCOUNT NO=',acct_no)
                                        print()
                                        print('DATE=',row[1])
                                        print()
                                        print('WITHDRAWAL AMOUNT=',row[2])
                                        print()
                                        print('AMOUNT ADDED=',row[3])
                                        print()
                         if n == 5:
                                print('DELETE YOUR ACCOUNT')
                                acct_no=int(input('Enter your account number='))  
                                cur.execute('delete from customer_details where acct_no='+str(acct_no) )
                                print('=====-ACCOUNT DELETED SUCCESSFULLY=====') 
                                print()
                         if n==6:
                                print('DO YOU WANT TO CONTINUE(Y/N)')
                                print()
                                c=input('Enter your Choice= ')

else:
    print('THANK YOU VISIT AGAIN............')
    quit()







