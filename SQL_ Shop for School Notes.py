#THREE TABLES CREATED IN MYSQL: notes, billing, customer_details
'''
mysql> use project;
Database changed

1. TABLE 'notes'
===================

mysql> create table notes(product_id int(35) primary key,
grade int(3), subject varchar(50), chapter_no int(3), chapter_name varchar(50),
no_of_pages int(50), description varchar(150), price decimal(5,2));
Query OK, 0 rows affected (0.03 sec)

mysql> desc notes;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| product_id   | int(35)      | NO   | PRI | NULL    |       |
| grade        | int(3)       | YES  |     | NULL    |       |
| subject      | varchar(50)  | YES  |     | NULL    |       |
| chapter_no   | int(3)       | YES  |     | NULL    |       |
| chapter_name | varchar(50)  | YES  |     | NULL    |       |
| no_of_pages  | int(50)      | YES  |     | NULL    |       |
| description  | varchar(150) | YES  |     | NULL    |       |
| price        | decimal(5,2) | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
8 rows in set (0.00 sec)

2. TABLE 'billing'
===================

mysql> create table billing(bill_no int(35) primary key, userID int(35),
date_purchased date, notes_purchased varchar(100), payment_method varchar(35),
payment_account varchar(50), total decimal(10,2));
Query OK, 0 rows affected (0.03 sec)

mysql> desc billing;
+-----------------+---------------+------+-----+---------+-------+
| Field           | Type          | Null | Key | Default | Extra |
+-----------------+---------------+------+-----+---------+-------+
| bill_no         | int(35)       | NO   | PRI | NULL    |       |
| userID          | int(35)       | YES  |     | NULL    |       |
| date_purchased  | date          | YES  |     | NULL    |       |
| notes_purchased | varchar(100)  | YES  |     | NULL    |       |
| payment_method  | varchar(35)   | YES  |     | NULL    |       |
| payment_account | varchar(50)   | YES  |     | NULL    |       |
| total           | decimal(10,2) | YES  |     | NULL    |       |
+-----------------+---------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

3. TABLE 'customer_details'
============================

mysql> create table customer_details(username varchar(35), userID int(35) primary key, name varchar(35), surname varchar(35),
country varchar(50), email_id varchar(100));
Query OK, 0 rows affected (0.13 sec)

mysql> desc customer_details;
+----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| username | varchar(35)  | YES  |     | NULL    |       |
| userID   | int(35)      | NO   | PRI | NULL    |       |
| name     | varchar(35)  | YES  |     | NULL    |       |
| surname  | varchar(35)  | YES  |     | NULL    |       |
| country  | varchar(50)  | YES  |     | NULL    |       |
| email_id | varchar(100) | YES  |     | NULL    |       |
+----------+--------------+------+-----+---------+-------+
6 rows in set (0.00 sec)
'''

#MODULES/VARIABLES USED IN THE PROJECT
import mysql.connector as m #used to establish connection between python and mySQL

import datetime #used in funtion 'checkout()' for billing

import random #used to generate product_id, bill_no and userID

#used to add colour to introductory print statements
import os 
os.system("cls")

cart=[] #used by customers for purchases

#-----------------------------------------------------------------------------------------------------------------
#records in table 'notes': product_id, grade, subject, chapter_no, chapter_name, no_of_pages, description, price

#FUNCTIONS FOR TABLE 'notes'
#------------------------------------------------

#DISPLAY RECORDS
def notes_displayall():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                 PRODUCTS AVAILABLE")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    cursor=con.cursor()
    cursor.execute("select *from notes")
    resultset=cursor.fetchall()
    for i in resultset:
        print("\nProduct ID:",i[0],)
        d={"Grade": i[1],"Subject": i[2],"Chapter number":i[3],"Chapter name": i[4],"No of pages": i[5],"Description":i[6],"Price": i[7]}
        print(d)
    

#ADD RECORDS
def notes_additem():
    while True:
        cursor=con.cursor()

        #generate book_id
        cursor.execute("select product_id from notes")
        resultset=cursor.fetchall()
        product_id=random.randint(0, 10000)
        for i in resultset:
            while i==product_id:
                product_id=random.randint(0, 10000)
        print("Product ID:", product_id)

        grade=int(input("Enter grade:"))
        subject=input("Enter subject:")
        chapter_no=int(input("Enter chapter number:"))

        cursor.execute("select grade, subject, chapter_no from notes")
        resultset=cursor.fetchall()
        l=(grade, subject, chapter_no)
        found=0
        for i in resultset:
            if i==l:
                found=1
                
        if found==1:
            print("Record already exists")
        else:
            chapter_name=input("Enter chapter name:")
            no_of_pages=int(input("Enter number of pages:"))
            description=input("Enter description:")
            price=float(input("Enter price:"))
            cursor.execute("insert into notes values({}, {}, '{}', {}, '{}', {}, '{}', {})".format(product_id, grade, subject, chapter_no, chapter_name, no_of_pages, description, price))
            con.commit()

        ch=input("\nDo you want to continue? (y/n):")
        if ch in "Nn":
            break

#DELETE RECORDS
def notes_deleteitem():
    cursor=con.cursor()
    delete=int(input("\nEnter product ID to delete:"))
    cursor.execute("select* from notes where product_id={}".format(delete))
    resultset=cursor.fetchall()
    if not resultset:
        print("\nRecord not found")
    else:
        cursor.execute("delete from notes where product_id=%d"%delete)
        print("\nRecord deleted successfully!")
        con.commit()

#EDIT RECORDS: DESCRIPTION AND PRICE
def notes_updateitem():
    while True:
        print('\n~~~~~~~~~~~~~~~~~~~')
        print('       MENU')
        print('~~~~~~~~~~~~~~~~~~~')
        print('1: Update description')
        print('2: Update price')
        print('0: Go back')
        ch=int(input("\nEnter choice:"))

        if ch==1:
            cursor=con.cursor()
            update=int(input("\nEnter product ID to edit:"))
            cursor.execute("select product_id from notes where product_id={}".format(update))
            resultset=cursor.fetchall()
            if not resultset:
                print("\nRecord not found")
            else:
                desc=input("Enter new description:")
                cursor.execute("update notes set description='{}' where product_id={}".format(desc, update))
                print("\nRecord updated successfully!")
                con.commit()
                
        elif ch==2:
            cursor=con.cursor()
            update=int(input("\nEnter product ID to edit:"))
            cursor.execute("select product_id from notes where product_id={}".format(update))
            resultset=cursor.fetchall()
            if not resultset:
                print("\nRecord not found")
            else:
                price=float(input("Enter new price:"))
                cursor.execute("update notes set price={} where product_id={}".format(price, update))
                print("\nRecord updated successfully!")
                con.commit()

        elif ch==0:
            break

        else:
            print("Invalid entry")

#SEARCH RECORDS: BY PRODUCT ID, GRADE AND SUBJECT
def notes_searchitem():
    while True:
        print('\n~~~~~~~~~~~~~~~~~~~')
        print('    SEARCH USING')
        print('~~~~~~~~~~~~~~~~~~~')
        print('1: Product ID')
        print('2: Grade')
        print('3: Subject')
        print('0: Go back')
        ch=int(input("\nEnter choice:"))

        if ch==1:
            cursor=con.cursor()
            search=int(input("\nEnter the product ID to search:"))
            cursor.execute("select *from notes where product_id=%d"%search)
            resultset=cursor.fetchall()
            print('\n~~~~~~~~~~~~~~~~~~~~~~~')
            print('     SEARCH RESULTS')
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
            if not resultset:
                print("\nRecord not found")
            for i in resultset:
                print("\nProduct ID:",i[0],)
                d={"Grade": i[1],"Subject": i[2],"Chapter number":i[3],"Chapter name": i[4],"No of pages": i[5],"Description":i[6],"Price": i[7]}
                print(d)
            
        elif ch==2:
            cursor=con.cursor()
            search=int(input("\nEnter grade to search:"))
            cursor.execute("select *from notes where grade=%d"%search)
            resultset=cursor.fetchall()
            print('\n~~~~~~~~~~~~~~~~~~~~~~~')
            print('     SEARCH RESULTS')
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
            if not resultset:
                print("\nRecord not found")
            for i in resultset:
                print("\nProduct ID:",i[0],)
                d={"Grade": i[1],"Subject": i[2],"Chapter number":i[3],"Chapter name": i[4],"No of pages": i[5],"Description":i[6],"Price": i[7]}
                print(d)
        
        elif ch==3:
            cursor=con.cursor()
            search=input("\nEnter subject to search:")
            cursor.execute("select *from notes where subject='{}'".format(search))
            resultset=cursor.fetchall()
            print('\n~~~~~~~~~~~~~~~~~~~~~~~')
            print('     SEARCH RESULTS')
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
            if not resultset:
                print("\nRecord not found")
            for i in resultset:
                print("\nProduct ID:",i[0],)
                d={"Grade": i[1],"Subject": i[2],"Chapter number":i[3],"Chapter name": i[4],"No of pages": i[5],"Description":i[6],"Price": i[7]}
                print(d)
                
        elif ch==0:
            break

        else:
            print("Invalid entry")

#SORT RECORDS BY GRADE
def notes_sortitem():
    cursor=con.cursor()
    cursor.execute("select *from notes order by grade asc")
    resultset=cursor.fetchall()
    print("\nSORTING RECORDS BY GRADE..")
    for i in resultset:
        print("\nGrade:",i[1],)
        d={"Product ID": i[0],"Subject": i[2],"Chapter number":i[3],"Chapter name": i[4],"No of pages": i[5],"Description":i[6],"Price": i[7]}
        print(d)

#-----------------------------------------------------------------------------------------------------------------
#records in table 'billing': bill_no, userID, date_purchased, notes_purchased, payment_method, payment_account, total

#FUNCTIONS FOR TABLE 'billing'
#------------------------------------------------

#DISPLAY RECORDS (NATURAL JOIN)
def billing_displayall():
    cursor=con.cursor()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                         BILLING RECORDS")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    cursor.execute("select *from customer_details natural join billing")
    resultset=cursor.fetchall()
    for i in resultset:
        u={'User ID': i[0], 'Username':i[1], 'Name': i[2], 'Surname': i[3], 'Country': i[4], 'Email ID': i[5]}
        print("\nUser details:", u)
        print('Bill number:', i[6])
        d={'Date purchased': i[7],'Notes purchased': i[8],'Payment method': i[9],'Payment account': i[10],'Total': i[11]}
        print("Bill details:",d)

#SEARCH BY BILL NUMBER
def billing_searchbill():
    cursor=con.cursor()
    search=int(input("\nEnter bill number to search:"))
    cursor.execute("select *from billing where bill_no=%d"%search)
    resultset=cursor.fetchall()
    print('\n~~~~~~~~~~~~~~~~~~~~~~~')
    print('     SEARCH RESULTS')
    print('~~~~~~~~~~~~~~~~~~~~~~~~')
    if not resultset:
        print("\nRecord not found")
    for i in resultset:
        print('\nBill number:', i[0])
        d={'User ID': i[1],'Date purchased': i[2],'Notes purchased': i[3],'Payment method': i[4],'Payment account': i[5],'Total': i[6]}
        print(d)

#SEARCH BY USER ID
def billing_searchuser():
    cursor=con.cursor()
    search=int(input("\nEnter user ID to search:"))
    cursor.execute("select *from billing where userID=%d"%search)
    resultset=cursor.fetchall()
    print('\n~~~~~~~~~~~~~~~~~~~~~~~')
    print('     SEARCH RESULTS')
    print('~~~~~~~~~~~~~~~~~~~~~~~~')
    if not resultset:
        print("\nRecord not found")
    for i in resultset:
        print('\nBill number:', i[0])
        d={'User ID': i[1],'Date purchased': i[2],'Notes purchased': i[3],'Payment method': i[4],'Payment account': i[5],'Total': i[6]}
        print(d)

#SORT RECORDS BY MONTH
def billing_sortitem():
    cursor=con.cursor()
    cursor.execute("select*from billing order by date_purchased asc")
    resultset=cursor.fetchall()
    print("\nSORTING RECORDS BY DATE..")
    for i in resultset:
        print("\n", i)

#------------------------------------------------------------------------------
#records for table customer_details: username, user_id, name, surname, country, email_id
    
#FUNCTIONS FOR CUSTOMERS SIDE
#------------------------------------------------

#DISPLAY CART
def display_cart():
    cursor=con.cursor()
    print('\n~~~~~~~~~~~~~~~~~~~~~~~')
    print('           CART')
    print('~~~~~~~~~~~~~~~~~~~~~~~~')
    if not cart:
        print("No products in cart")
    else:
        for i in cart:
            cursor.execute("select* from notes where product_id=%d"%i)
            resultset=cursor.fetchall()
            for i in resultset:
                print("\nProduct ID:",i[0],)
                d={"Grade": i[1],"Subject": i[2],"Chapter number":i[3],"Chapter name": i[4],"No of pages": i[5],"Description":i[6],"Price": i[7]}
                print(d)
    

#ADD TO CART
def add_to_cart():
    cursor=con.cursor()
    add=int(input("\nEnter product ID to add to cart:"))
    cursor.execute("select* from notes where product_id=%d"%add)
    resultset=cursor.fetchall()
    if not resultset:
        print("\nProduct not found")
    else:
        cart.append(add)
        print("\nProduct ADDED to cart!")

#DELETE FROM CART
def delete_from_cart():
    cursor=con.cursor()
    delete=int(input("\nEnter product ID to delete from cart:"))
    if delete in cart:
        cart.remove(delete)
        print("\nProduct REMOVED from cart")
    else:
        print("Product NOT FOUND in cart")

#CREATE OR LOGIN TO ACCOUNT/ ADD RECORDS TO TABLE 'customer_details'
def account():
    global username
    global userID
    
    print('\n~~~~~~~~~~~~~~~~~~~~~')
    print('         MENU')
    print('~~~~~~~~~~~~~~~~~~~~~')
    print("1: Login to account")
    print("2: Create account")
    ch=int(input("\nEnter choice:"))

    if ch==1:
        cursor=con.cursor()
        username=input("\nEnter username:")
        username=username.strip()
        userID=int(input("Enter user ID:"))
        cursor.execute("select*from customer_details where username='{}' and userID={}".format(username, userID))
        resultset=cursor.fetchall()
        if resultset:
            print("\nLOGIN SUCCESSFUL!")
            return 1
        
    elif ch==2:
        cursor=con.cursor()

        username=input("Enter username (35 characters):")
        cursor.execute("select*from customer_details where username='{}'".format(username))
        resultset=cursor.fetchall()
        if resultset:
            print("\nOops! Username already exists")
            return 3
        
        else:
            cursor.execute("select userID from customer_details")
            resultset=cursor.fetchall()
            userID=random.randint(0, 100000)
            for i in resultset:
                while i==userID:
                    userID=random.randint(0, 100000)
            print("Your user ID is:", userID)

            name=input("Enter your name:")
            surname=input("Enter your surname:")
            country=input("Enter your country of residence:")
            email_id=input("Enter your email ID:")

            cursor.execute("insert into customer_details values('{}',{},'{}','{}','{}','{}')".format(username, userID,name,surname,country,email_id))
            con.commit()
            print("\nACCOUNT CREATED!")
            return 2

#CHECKOUT/ ADD RECORDS TO TABLE 'billing'
def checkout():
    global username
    global userID
    a=account()

    if a==1:
        cursor=con.cursor()
        cursor.execute("select bill_no from billing")
        resultset=cursor.fetchall()
        bill_no=random.randint(0, 100000)
        for i in resultset:
            while i==bill_no:
                bill_no=random.randint(0, 100000)
        print("Your bill number is:", bill_no)
        date_purchased=datetime.date.today()
        notes_purchased=cart
        payment_method=input("Enter payment method (paypal/credit card/debit card):")
        payment_account=input("Enter payment account:")

        total=0
        for i in cart:
            cursor.execute("select price from notes where product_id=%d"%i)
            resultset=cursor.fetchall()
            for j in resultset[0]:
                total+=float(j)
        print("Total cost:", total)

        confirm=input("Do you confirm this purchase? (y/n):")
        if confirm in "yY":
            cursor.execute("insert into billing values({},{},'{}','{}','{}','{}',{})".format(bill_no, userID, date_purchased, notes_purchased, payment_method, payment_account, total))
            con.commit()
            print("\nPURCHASE SUCCESSFUL!")
            print("You'll receive the notes on your email ID. Thank you for shopping!")
            cart.clear()

    elif a==2:
        print("\nYou can use your account!")
        
    elif a==3:
        print("\nTry a different username")
    
    else:
        print("\nInvalid username or password\n")

#DISPLAY/EDIT ACCOUNT DETAILS
def display_cust():
    global userID
    while True:
        print('\n~~~~~~~~~~~~~~~~~~~')
        print('       MENU')
        print('~~~~~~~~~~~~~~~~~~~')
        print('1: View account details')
        print('2: Edit account details')
        print('0: Exit\n')
        ch=int(input("Enter choice:"))

        if ch==1:
            cursor=con.cursor()
            cursor.execute("select *from customer_details where userID={}".format(userID))
            resultset=cursor.fetchall()
            for i in resultset:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("             YOUR ACCOUNT DETAILS")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                u={'User ID': i[0], 'Username':i[1], 'Name': i[2], 'Surname': i[3], 'Country': i[4], 'Email ID': i[5]}
                print(u)

        elif ch==2:
            cursor=con.cursor()
            country=input("Enter country:")
            email=input("Enter email ID:")
            cursor.execute("update customer_details set email_id='{}', country='{}' where userID={}".format(email, country, userID))
            con.commit()
            print("Information updated successfully!")

        elif ch==0:
            break

        else:
            print("Invalid entry")

#DISPLAY BILLING RECORDS OF CUSTOMER 
def display_bills():
    global userID
    cursor=con.cursor()
    cursor.execute("select*from billing where userID={}".format(userID))
    resultset=cursor.fetchall()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              YOUR BILLING RECORDS")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in resultset:
        print('\nBill number:', i[0])
        d={'User ID': i[1],'Date purchased': i[2],'Notes purchased': i[3],'Payment method': i[4],'Payment account': i[5],'Total': i[6]}
        print(d)

#DELETE CUSTOMER ACCOUNT/DELETE RECORDS FROM TABLE 'customer_details'
def delete_account():
    global userID
    cursor=con.cursor()
    cursor.execute("delete from customer_details where userID={}".format(userID))
    con.commit()
    print("Account DELETED")
        
#------------------------------------------------------------------------------  
#MAIN STARTS HERE
#------------------------------------------------------------------------------

con=m.connect(host='localhost', user='root', passwd='root', database='project')
if con.is_connected():
    print("\u001b[34;1m\t\t\t\tSHOP FOR SCHOOL NOTES\u001b[37m")
    print('\t\t\t\t~~~~~~~~~~~~~~~~~~~~~')
    #timer loop
    print("\u001b[32mLoading..\u001b[37m")
    for i in range(100000000):
        pass
    print('\u001b[32mConnected successfully!\u001b[37m')
    
    
user=input("Enter user (admin/customer):")
user=user.upper()

if user=="ADMIN":
    password=input("Enter password:")
    while password=="notes123":
        print('\n~~~~~~~~~~~~~~~~~~~')
        print('       MENU')
        print('~~~~~~~~~~~~~~~~~~~')
        print('1: Notes menu')
        print('2: Billing records')
        print('0: Exit\n')

        choice=int(input("Enter your choice(1/2, 0 to exit):"))
        
        if choice==1:
            while True:
                print('\n~~~~~~~~~~~~~~~~')
                print('      MENU')
                print('~~~~~~~~~~~~~~~~')
                print("1: Display items")
                print("2: Add item")
                print("3: Delete item")
                print("4: Update item")
                print("5: Search item")
                print("6: Sort items")
                print("0: Go back\n")

                n=int(input("Enter choice(1-6, 0 to go back):"))

                if n==1:
                    notes_displayall()
                    
                elif n==2:
                    notes_additem()
                    
                elif n==3:
                    notes_deleteitem()
                    
                elif n==4:
                    notes_updateitem()
                    
                elif n==5:
                    notes_searchitem()
                    
                elif n==6:
                    notes_sortitem()
                    
                elif n==0:
                    break
                
                else:
                    print("\nInvalid entry")

        elif choice==2:
            while True: 
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('            MENU')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print("1: Display billing records")
                print("2: Search record")
                print("3: Sort records")
                print("0: Go back\n")

                billing=int(input("Enter choice (1-3, 0 to exit):"))

                if billing==1:
                    billing_displayall()
                    
                elif billing==2:
                    while True:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~")
                        print('          MENU')
                        print("~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("1: Search by bill number")
                        print("2: Search by user ID")
                        print("0: Go back\n")
            
                        s=int(input("Enter choice:"))
                        
                        if s==1:
                            billing_searchbill()
                        elif s==2:
                            billing_searchuser()
                        elif s==0:
                            break
                        else:
                            print("\nInvalid entry")
                
                elif billing==3:
                    billing_sortitem()
                    
                elif billing==0:
                    break
                else:
                    print("\nInvalid entry")
                    
        elif choice==0:
            break

        else:
            print("\nInvalid entry")

while user=="CUSTOMER":
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('           MENU')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('1: Display available notes')
    print('2: Shop notes')
    print('3: Go to cart')
    print('4: Account details')
    print('0: Logout\n')

    option=int(input("Enter choice (1-4, 0 to logout):"))

    if option==1:
        notes_displayall()

    elif option==2:
        while True:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
            print('          MENU')
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            print('1: Search for notes')
            print('2: Add a product to cart')
            print('0: Go back\n')

            shop=int(input("Enter choice:"))

            if shop==1:
                notes_searchitem()

            elif shop==2:
                add_to_cart()

            elif shop==0:
                break
            
            else:
                print("\nInvalid entry")

    elif option==3:
        while True:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print('            MENU')
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print('1: View products in cart')
            print('2: Add a product to cart')
            print('3: Delete product from cart')
            print('4: Checkout')
            print('0: Go back\n')

            a=int(input('Enter your choice:'))
            
            if a==1:
                display_cart()
                    
            elif a==2:
                add_to_cart()

            elif a==3:
                delete_from_cart()

            elif a==4:
                checkout()
                    
            elif a==0:
                break

            else:
                print("\nInvalid entry")

    elif option==4:
        a=account()
        if a==1:
            while True:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('          MENU')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("1: Account details")
                print("2: View billing records")
                print("3: Delete account")
                print("0: Go back\n")

                a=int(input("Enter choice:"))

                if a==1:
                    display_cust()

                elif a==2:
                    display_bills()

                elif a==3:
                    delete_account()
                
                elif a==0:
                    break

                else:
                    print("\nInvalid entry")
                    
        elif a==2:
            print("You may use your account!")
            
        elif a==3:
            print("\nTry another username")

        else:
            print("\nInvalid username or user ID")


    elif option==0:
        break

    else:
        input()

#-----------------------------------------------------------------------
#END OF CODE
#-----------------------------------------------------------------------

