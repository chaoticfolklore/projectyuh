#SHOP FOR SCHOOL NOTES 

#MODULES USED IN THE PROJECT

import csv #used to perform functions on CSV files 

import random #used in functions 'notes_additem()', 'account()', and 'checkout()' 

import os #used to check if files exist or not 
os.system('cls') #used to add color to introductory print statements 

import datetime #used in funtion 'checkout()' for billing

#FILES USED IN THE PROJECT

#stores details of notes 
notes="items.csv"
csvfile=open(notes, 'a', newline='')
csvfile.close()

#stores billing records 
bill="billing.csv"
csvfile=open(bill, 'a', newline='')
csvfile.close()

#stores customer details 
cust="customer.csv"
csvfile=open(cust, 'a', newline='')
csvfile.close()

#list used by customers of purchases
cart=[]

#-----------------------------------------------------------------------------------------------------------------
#records in file 'notes': product_id, grade, subject, chapter_no, chapter_name, no_of_pages, description, price

#FUNCTIONS FOR FILE 'notes'
#------------------------------------------------

#DISPLAY ITEMS
def notes_displayall():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                 PRODUCTS AVAILABLE")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if os.path.isfile(notes):
        file=open(notes, 'r')
        csvobj=csv.reader(file)
        for line in csvobj:
            print(line, end="\n\n")
        file.close()
    else:
        print("File doesn't exist")

#ADD ITEMS
def notes_additem():
    l=[]
    while True:
        
        #generate product_id
        id=open(notes, 'r')
        obj=csv.reader(id)
        product_id=random.randint(0, 1000)
        for line in obj:
            while line[0]==product_id:
                product_id=random.randint(0, 1000)
            
            
        grade=input("Enter grade:")
        subject=input("Enter subject:")
        chapter_no=input("Enter chapter number:")
        chapter_name=input("Enter chapter name:")

        found=0

        id.seek(0)
        for line in obj:
            if grade==line[1] and subject==line[2] and chapter_no==line[3] and chapter_name==line[4]:
                found=1
                
        if found==1:
            print("\nRecord already exists\n")
        else:
            no_of_pages=float(input("Enter number of pages:"))
            description=input("Enter description:")
            price=float(input("Enter price:"))
            l.append([product_id, grade, subject, chapter_no, chapter_name, no_of_pages, description, price])
            
            choice=input("Do you want to add more records? (y/n)")
            if choice in "nN":
                break

        id.close()  
    file=open(notes, 'a', newline='')
    csvobj=csv.writer(file)
    csvobj.writerows(l)
    file.close()

#DELETE ITEM
def notes_deleteitem():
    csvfile=open(notes, 'r')
    csvobj=csv.reader(csvfile)
    notes_displayall()
    a=input("\nEnter product ID:")
    found=0
    l=[]
    for line in csvobj:
        if a!= line[0]:
            l.append(line)
        else:
            found=1
    if found==1:
        print("\nRecord deleted")
    else:
        print("\nRecord not found")
    csvfile.close()
    csvfile=open(notes,'w', newline='')
    csvobj=csv.writer(csvfile)
    csvobj.writerows(l)
    csvfile.close()

#EDIT ITEM
def notes_edititem():
    csvfile=open(notes,'r')
    csvobj=csv.reader(csvfile)
    notes_displayall()
    search=input("\nEnter product ID to edit:")
    found=0
    edit=[]
    for line in csvobj:
        if search==line[0]:
            line[6]=input("Enter description:")
            line[7]=float(input("Enter price:"))
            found=1
        edit.append(line)
    if found==1:
        print("\nRecord edited")
    else:
        print("\nRecord not found")
    csvfile.close()
    csvfile=open(notes, 'w', newline='')
    csvobj=csv.writer(csvfile)
    csvobj.writerows(edit)
    csvfile.close()

#SEARCH ITEM
def notes_searchitem():
    while True:
        print('\n~~~~~~~~~~~~~~~~~~~')
        print('    SEARCH USING')
        print('~~~~~~~~~~~~~~~~~~~')
        print('1: Product ID')
        print('2: Grade')
        print('3: Subject')
        print('0: Go back')

        choice=int(input("\nEnter choice:"))

        if choice==1:
            csvfile=open(notes, 'r')
            csvobj=csv.reader(csvfile)
            search=input("Enter the product ID:")
            search=search.strip()
            found=0
            print('\n~~~~~~~~~~~~~~~~~~~~~~~')
            print('     SEARCH RESULTS')
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
            for line in csvobj:
                if line[0]==search:
                    print("\nProduct ID:", line[0])
                    print("Grade:", line[1])
                    print("Subject:", line[2])
                    print("Chapter number:", line[3])
                    print("Chapter name:", line[4])
                    print("Number of pages:", line[5])
                    print("Description:", line[6])
                    print("Price:", line[7])                   
                    found=1
            if found==0:
                print("\nItem(s) NOT found")

        elif choice==2:
            csvfile=open(notes, 'r')
            csvobj=csv.reader(csvfile)
            search=input("Enter grade:")
            search=search.strip()
            found=0
            print('\n~~~~~~~~~~~~~~~~~~~~~~~')
            print('     SEARCH RESULTS')
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
            for line in csvobj:
                if line[1]==search:
                    print("\nProduct ID:", line[0])
                    print("Grade:", line[1])
                    print("Subject:", line[2])
                    print("Chapter number:", line[3])
                    print("Chapter name:", line[4])
                    print("Number of pages:", line[5])
                    print("Description:", line[6])
                    print("Price:", line[7])                   
                    found=1
            if found==0:
                print("\nItem(s) NOT found")

        elif choice==3:
            csvfile=open(notes, 'r')
            csvobj=csv.reader(csvfile)
            search=input("\nEnter the subject:")
            search=search.strip()
            found=0
            print('\n~~~~~~~~~~~~~~~~~~~~~~~')
            print('     SEARCH RESULTS')
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
            for line in csvobj:
                if line[2]==search:
                    print("\nProduct ID:", line[0])
                    print("Grade:", line[1])
                    print("Subject:", line[2])
                    print("Chapter number:", line[3])
                    print("Chapter name:", line[4])
                    print("Number of pages:", line[5])
                    print("Description:", line[6])
                    print("Price:", line[7])                   
                    found=1
            if found==0:
                print("\nItem(s) NOT found")
                
        elif choice==0:
            break
        
        else:
            print("Invalid entry")
            
#SORT ITEMS BY GRADE
def notes_sortitem():
    print("\nSORTING RECORDS BY GRADE..")
    csvfile=open(notes,'r')
    csvobj=csv.reader(csvfile)
    l=[]
    for line in csvobj:
        l.append(line)
    for i in range(len(l)):
        for j in range(0,len(l)-1-i):
            if l[j][1]<l[j+1][1]:
                  l[j],l[j+1]=l[j+1],l[j]
    csvfile.close()

    csvfile=open('notes_sorted.csv', 'w', newline='')
    csvobj=csv.writer(csvfile)
    csvobj.writerows(l)
    csvfile.close()
    print("\nRecords sorted!")
    csvfile=open('notes_sorted.csv', 'r')
    csvobj=csv.reader(csvfile)
    for i in csvobj:
        print(i)
    csvfile.close()

#-----------------------------------------------------------------------------------------------------------------
#records in file 'bill': bill_no, userID, date_purchased, notes_purchased, payment_method, payment_account, total

#FUNCTIONS FOR FILE 'billing'
#------------------------------------------------

#DISPLAY BILLING
def billing_displayall():
    if os.path.isfile(bill):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                         BILLING RECORDS")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        file=open(bill, 'r')
        csvobj=csv.reader(file)
        for line in csvobj:
            print(line, end='\n\n')
        file.close()
    else:
        print("File doesn't exist")

#SEARCH RECORDS WITH BILL NUMBER
def billing_searchbill():
    with open(bill, 'r') as csvfile:
        csvobj=csv.reader(csvfile)
        search=input("\nEnter the bill number to search:")
        found=0
        print('\n~~~~~~~~~~~~~~~~~~~~~~~')
        print('     SEARCH RESULTS')
        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        for line in csvobj:
            if line[0]==search:
                print("\n",line)
                found=1
        if found==0:
            print("\nRecord(s) NOT found")

#SEARCH RECORDS WITH USERNAME
def billing_searchuser():
    with open(bill, 'r') as csvfile:
        csvobj=csv.reader(csvfile)
        search=input("\nEnter the username to search:")
        found=0
        print('\n~~~~~~~~~~~~~~~~~~~~~~~')
        print('     SEARCH RESULTS')
        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        for line in csvobj:
            if line[1]==search:
                print("\n",line)
                found=1
        if found==0:
            print("\nRecord(s) NOT found")
            
#SEARCH RECORDS WITH MONTH OF PURCHASE
def billing_searchmonth():
    with open(bill, 'r') as csvfile:
        csvobj=csv.reader(csvfile)
        search=input("\nEnter the month number:")
        found=0
        print('\n~~~~~~~~~~~~~~~~~~~~~~~')
        print('     SEARCH RESULTS')
        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        for line in csvobj:
            a=line[3].split()
            if search==(a[0][5]+a[0][6]) or search==a[0][6]:
                print("\n",line)
                found=1
        if found==0:
            print("\nRecord(s) NOT found")
    
#SORT ITEMS BY USER
def billing_sortitem():
    print("\nSORTING RECORDS BY USER..")
    csvfile=open(bill,'r')
    csvobj=csv.reader(csvfile)
    l=[]
    for line in csvobj:
        l.append(line)
    for i in range(len(l)):
        for j in range(0,len(l)-1-i):
            if l[j][1]>l[j+1][1]:
                  l[j],l[j+1]=l[j+1],l[j]
    csvfile.close()

    csvfile=open('billing_sorted.csv', 'w', newline='')
    csvobj=csv.writer(csvfile)
    csvobj.writerows(l)
    csvfile.close()
    print("\nRecords sorted!")
    csvfile=open('billing_sorted.csv', 'r')
    csvobj=csv.reader(csvfile)
    for i in csvobj:
        print(i)
    csvfile.close()

#------------------------------------------------------------------------------
#records for file 'cust': username, user_ID, name, surname, country, email_id
    
#FUNCTIONS FOR CUSTOMERS SIDE
#------------------------------------------------

#DISPLAY ALL PRODUCTS FOR CUSTOMER
def cust_displayall():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                 PRODUCTS AVAILABLE")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if os.path.isfile(notes):
        file=open(notes, 'r')
        csvobj=csv.reader(file)
        for line in csvobj:
            print("\nProduct ID:", line[0])
            print("Grade:", line[1])
            print("Subject:", line[2])
            print("Chapter number:", line[3])
            print("Chapter name:", line[4])
            print("Number of pages:", line[5])
            print("Description:", line[6])
            print("Price:", line[7])
        file.close()
    else:
        print("File doesn't exist")

#CREATE OR LOGIN TO ACCOUNT
def account():
    global username
    global user_ID
    print('\n~~~~~~~~~~~~~~~~~~~~~')
    print('         MENU')
    print('~~~~~~~~~~~~~~~~~~~~~')
    print("1: Login to account")
    print("2: Create account")

    choice=int(input("\nEnter choice:"))

    new=[]

    if choice==1:
        username=input("\nEnter username:")
        username=username.strip()
        user_ID=input("Enter user ID:")
        user_ID=user_ID.strip()
        csvfile=open(cust, 'r')
        csvobj=csv.reader(csvfile)
        for line in csvobj:
            if line[0]==username and line[1]==user_ID:
                print("\nLOGIN SUCCESSFUL!")
                return 1
        csvfile.close()
        
    elif choice==2:
        username=input("Enter username:")
        csvfile=open(cust, 'r')
        csvobj=csv.reader(csvfile)
        a=0
        
        for line in csvobj:
            if username==line[0]:
                a=1
                break
        csvfile.close()
            
        if a==1:
            print("\nOops, Username already exists!")
            return 3

        else:
            csvfile=open(cust, 'r')
            csvobj=csv.reader(csvfile)
            obj=csv.reader(csvfile)
            user_ID=random.randint(0, 100000)
            for line in csvobj:
                while line[0]==user_ID:
                    user_ID=random.randint(0, 100000)
            print("Your user ID is:", user_ID)
            csvfile.close()
        
            name=input("Enter your name:")
            surname=input("Enter your surname:")
            country=input("Enter country of residence:")
            email_id=input("Enter email id:")

            new.append([username, user_ID, name, surname, country, email_id])

            print("\nACCOUNT CREATED")
        
            csvfile=open(cust, 'a', newline='')
            csvobj=csv.writer(csvfile)
            csvobj.writerows(new)
            csvfile.close()

            return 2

#ADDING TO CART
def add_to_cart():
    p=input("\nEnter product ID:")
    csvfile=open(notes, 'r')
    csvobj=csv.reader(csvfile)
    found=0
    for line in csvobj:
        if p==line[0]:
            if line not in cart:
                cart.append(line)
                found=1
                print("\nItem ADDED to cart")
            else:
                found=3
    if found==3:
        print("\nItem is already in cart")
        
    elif found==0:
        print("\nItem not found")

#DELETING FROM CART
def delete_from_cart():
    p=input("\nEnter product ID:")
    found=0
    for line in cart:
        if p==line[0]:
            cart.remove(line)
            found=1
    if found==1:
        print("\nProduct REMOVED from cart")
    else:
        print("\nItem not found in cart")

#CHECKOUT
def checkout():
    global username
    global user_ID
    a=account()
    if a==1:
        billing=[]
        csvfile=open(bill, 'r')
        csvobj=csv.reader(csvfile)
        bill_no=random.randint(0, 10000000)
        for line in csvobj:
            while line[0]==bill_no:
                bill_no=random.randint(0, 10000000)
        csvfile.close()
        
        date_purchased =datetime.datetime.now()
        notes_purchased=cart
        payment_method=input("Enter payment method (paypal/credit card/debit card:")
        payment_account=input("Enter payment account:")

        total=0
        for line in cart:
            total=total+float(line[7])
            
        print("Total cost:", total)

        confirm=input("Do you confirm this purchase? (y/n)")
        confirm=confirm.upper()

        if confirm=="Y":
            print("\nPURCHASE SUCCESSFUL!")
            print("You'll receive the notes on your email ID. Thank you for shopping!")
            billing.append([bill_no, username, user_ID, date_purchased, notes_purchased, payment_method, payment_account, total])
            
        
        csvfile=open(bill, 'a', newline='')
        csvobj=csv.writer(csvfile)
        csvobj.writerows(billing)
        csvfile.close()
        cart.clear()
        
    elif a==2:
        print("\nYou can use your account!")
        
    elif a==3:
        print("\nTry a different username")
    
    else:
        print("\nInvalid username and password\n")
        
#DISPLAY BILL RECORDS FOR CUSTOMER
def display_bills():
    global username
    with open(bill, 'r') as csvfile:
        csvobj=csv.reader(csvfile)
        found=0
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("              YOUR BILLING RECORDS")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for line in csvobj:
            if line[1]==username:
                print("\nBill number:", line[0])
                print("Purchase date:", line[3])
                print("Notes purchased:", line[4])
                print("Payment method:", line[5])
                print("Payment account:", line[6])
                print("Total paid:", line[7])
                found=1
        if found==0:
            print("Record(s) NOT found")

#DISPLAY PURCHASED ITEMS
def display_purchased():
    global username
    with open(bill, 'r') as csvfile:
        csvobj=csv.reader(csvfile)
        found=0
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("               YOUR PURCHASE RECORDS")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for line in csvobj:
            if line[1]==username:
                print(line[4])
                found=1
        if found==0:
            print("\nRecord(s) NOT found")

#DISPLAY AND EDIT CUSTOMER ACCOUNT DETAILS
def display_cust():
    global username
    while True:
        print('\n~~~~~~~~~~~~~~~~~~~')
        print('       MENU')
        print('~~~~~~~~~~~~~~~~~~~')
        print('1: Profile details')
        print('2: Edit profile details')
        print('0: Exit\n')

        choice=int(input("Enter choice:"))

        if choice==1:
            csvfile=open(cust, 'r')
            csvobj=csv.reader(csvfile)
            found=0
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("             YOUR ACCOUNT DETAILS")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for line in csvobj:
                if line[0]==username:
                    found=1
            if found==1:
                print("Username:",line[0])
                print("User ID:", line[1])
                print("Name:",line[2])
                print("Surname:",line[3])
                print("Country:", line[4])
                print("Email ID:", line[5])
            else:
                print("Account not found")
            csvfile.close()

        elif choice==2:
            csvfile=open(cust,'r')
            csvobj=csv.reader(csvfile)
            found=0
            edit=[]
            for line in csvobj:
                if line[0]==username:
                    line[2]=input("Enter name:")
                    line[3]=input("Enter surname:")
                    line[4]=input("Enter country:")
                    line[5]=input("Enter Email ID:")
                    found=1
                edit.append(line)
            if found==1:
                print("\nDetails updated")
            csvfile.close()
            csvfile=open(cust, 'w', newline='')
            csvobj=csv.writer(csvfile)
            csvobj.writerows(edit)
            csvfile.close()

        elif choice==0:
            break
        
        else:
            print("\nInvalid entry")

#DELETE CUSTOMER ACCOUNT
def delete_account():
    global username
    csvfile=open(cust, 'r')
    csvobj=csv.reader(csvfile)
    found=0
    l=[]
    for line in csvobj:
        if username!=line[0]:
            l.append(line)
        else:
            found=1
    if found==1:
        print("\nACCOUNT DELETED\n")
    else:
        print("\nERROR in deleting account")

    csvfile.close()
    csvfile=open(cust,'w', newline='')
    csvobj=csv.writer(csvfile)
    csvobj.writerows(l)
    csvfile.close()
    
#------------------------------------------------------------------------------  
#MAIN STARTS HERE
#------------------------------------------------------------------------------

print("\u001b[34;1m\t\t\t\tSHOP FOR SCHOOL NOTES\u001b[37m")
print("\u001b[34;1m\t\t\t\t~~~~~~~~~~~~~~~~~~~~~\u001b[37m")
#timer loop
print("\u001b[32mLoading..\u001b[37m")
for i in range(100000000):
    pass

print('\u001b[32mConnected successfully!\u001b[37m')
user=input("Enter user:")
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
                print("4: Edit item")
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
                    notes_edititem()
                    
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
                print("1: Display Billing records")
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
                        print("2: Search by username")
                        print("3: Search by month")
                        print("0: Go back\n")
            
                        s=int(input("Enter choice:"))
                        
                        if s==1:
                            billing_searchbill()
                        elif s==2:
                            billing_searchuser()
                        elif s==3:
                            billing_searchmonth()
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
        cust_displayall()

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
                if not cart:
                    print("\nNo items in cart")
                for i in cart:
                    print(i)
                    
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
                print("3: View purchase records")
                print("4: Delete account")
                print("0: Go back\n")

                a=int(input("Enter choice:"))

                if a==1:
                    display_cust()

                elif a==2:
                    display_bills()

                elif a==3:
                    display_purchased()

                elif a==4:
                    delete_account()
                
                elif a==0:
                    break

                else:
                    print("\nInvalid entry")
                    
        elif a==2:
            print("\nYou may use your account")
            
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

                















                    
        
