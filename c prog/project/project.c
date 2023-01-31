option=""

// Options Menu repeatedly displays available options till program exit.

while(option != "E"){
    print ("\n===== OPTIONS MENU =====")
    print("A --> Add Items")
    print("D --> Delete Items")
    print("C --> Change Items")
    print("L --> List of Items")
    print("B --> Proceed to Billing Module")
    print("P --> Print old bill")
    print("E --> Exit")
         
    option=input("Select an option :")
    
    // Option to Add items prompts the user to enter item code, item name, quantity,
    // rate. It uses mysql connector to connect to items table and inserts the 
    // specified item details
    
    if option=="A":
        new_item_no=input("Enter the new item Code to be added :")
        new_item_name=input("Enter the new item to add to list: ")
        new_item_rate=input("Enter the unit rate : ")
        new_item_qty=input("Enter the new item quantity : ")
        
        import mysql.connector as sql
        conn=sql.connect(host="localhost",user="root",password="root123",database="market")
        
        if conn.is_connected() == False:
            print("Connection to the database failed")
        cursor=conn.cursor()
        cursor.execute("insert into items(item_no,item_name,quantity,unit_price) values({},'{}',{},{})".format(new_item_no,new_item_name,new_item_qty,
        new_item_rate))
        conn.commit()
        print("Item Code: ",new_item_no, "Item Name :", new_item_name," added.")
        print("\n")
        cursor.execute("select * from items")
        result=cursor.fetchall()
        for row in result:
             print(row)
        conn.close();
   
    // Option to delete items prompts the user to enter item name to be deleted
    // It uses mysql connector to connect to items table and deletes the 
    // specified item details
        
    if option=="D":
        del_item=input("Enter item to delete from the list: ")
        print ("Delete item = ",del_item)
        import mysql.connector as sql
        conn=sql.connect(host="localhost",user="root",password="root123",database="market")
        
        if conn.is_connected() == False:
            print("Connection to the database failed")
        cursor=conn.cursor()
        cursor.execute("delete from items where item_name = '{}'".format(del_item))
        conn.commit()
        print("Item",del_item,"deleted from the list")
        print("\n")
        cursor.execute("select * from items")
        result=cursor.fetchall()
        for row in result:
             print(row)
        conn.close();
      
    // Option to change items prompts the user to enter item name whose details is 
    // to be changed.
    // It asks the user what to change - (Q)uantity or per unit (R)ate of the item
    // It uses mysql connector to connect to items table and updates the 
    // specified  details based on the changes requested
        
    if option=="C":
        chng_item=input("Please enter the item you want to change: ")
        chng=input("Do you want to update the Quantity or Rate for this item- enter Q/R: ")
        
        if chng=="Q":
            chng_qty=input("Please specify revised quantity for this item: ")
            import mysql.connector as sql
            conn=sql.connect(host="localhost",user="root",password="root123",database="market")
            
            if conn.is_connected() == False:
                print("Connection to the database failed")
            cursor=conn.cursor()
            cursor.execute("update items set quantity={} where item_name = '{}'".format(chng_qty,chng_item))
            conn.commit()
            print("Quantity for",chng_item,"changed to",chng_qty)
            print("\n")
            cursor.execute("select * from items")
            result=cursor.fetchall()
            for row in result:
                 print(row)
            conn.close();
        
        if chng=="R":                
            chng_rate=input("Enter the new rate for this item: ")        
            import mysql.connector as sql
            conn=sql.connect(host="localhost",user="root",password="root123",database="market")
            
            if conn.is_connected() == False:
                print("Connection to the database failed")
            cursor=conn.cursor()
            cursor.execute("update items set unit_price={} where item_name = '{}'".format(chng_rate,chng_item))
            conn.commit()
            print("Rate for",chng_item,"changed to Rs.",chng_rate)
            print("\n")
            cursor.execute("select * from items")
            result=cursor.fetchall()
            for row in result:
                 print(row)
            conn.close();  
            
    // Option to display list of items and  details from items table     
    
    if option=="L":
        print ("\n Item No, Item, Quantity, Unit Price:")
        print ("======================================")
        
        import mysql.connector as sql
        conn=sql.connect(host="localhost",user="root",password="root123",database="market")
        
        if conn.is_connected() == False:
            print("Connection to the database failed")
        cursor=conn.cursor()
        cursor.execute("select * from items")
        result=cursor.fetchall()
        for row in result:
             print(row)
        conn.close(); 
        
    // Option to display previously generated bills from bills table
    // Prompts the user to provide old bill number available in bills table
  
    if option=="P":
        old_b_no=input("Please provide old bill number : ")
        print("\n************* FINAL BILL **************")
                
        print("\n Bill Number:",old_b_no," Date: 01/01/01")
        print("=======================================\n")
        print(" Item   Qty    Rate  Amount")
        print("----------------------------")
        
        import mysql.connector as sql
        conn=sql.connect(host="localhost",user="root",password="root123",database="market")
            
        if conn.is_connected() == False:
            print("Connection to the database failed")
        cursor=conn.cursor()
        cursor.execute("select bill_item,bill_qty,bill_rate,bill_amt from bills where bill_no={}".format(old_b_no))            
        result=cursor.fetchall()
        for row in result:
             print(row)
        print("\nTotal Bill Amount (Rs)")
        print("=====================")
        cursor.execute("select sum(bill_amt) from bills where bill_no={}".format(old_b_no))
        result=cursor.fetchone()
        for row in result:
             print(row)
        conn.close();
        
        // capture the total bill amount from SQL query output in list format to integer
        // If total bill amount is greater than Rs. 1000, a 10% discount is added to 
        // the final bill amount
        
        tot_bill=result[0]
        if tot_bill >= 1000:
            tot_bill=0.9*tot_bill
            print("Congrats!! You are eligible for 10% discount\n")
            print("Your Final Bill Amount = ",tot_bill)
        print("\n ******** Thank You, Visit Again ********")   

    // Option to invoke billing module. 
        
    if option=="B":
        print("Proceeding to Billing Module ....")
        ans="y"
        import random
        b_amt=0
        // uses randint function to generate a random integer as a bill number
        b_no=random.randint(1,99999)
        b_rate=0
        b_qty=0
        new_qty=0
        
        // Iteratively ask for item to be billed, till user does not want to
        // add any more items
        
        while ans=="y"or ans=="Y":
            b_item=input("Enter item to bill : ")
            b_qty=int(input("How many do you need : "))
            
            import mysql.connector as sql
            conn=sql.connect(host="localhost",user="root",password="root123",database="market")
            
            if conn.is_connected() == False:
                print("Connection to the database failed")
            cursor=conn.cursor()
            cursor.execute("select quantity from items where item_name='{}'".format(b_item));
            result=cursor.fetchone()
            result=int(result[0])
            
            // Check available quantity in items table. Alerts the user if adequate
            // stock for the item is not available, displays available stock for the 
            // user to revise the quantity to bill.
            
            if result < b_qty:
                print("Insufficient number of", b_item,"in stock to bill. Available = ",result)
                conn.close();
                ans=input("Do you want to buy more items - y/n - ")
            else:
                // if adequate quantity is available, then update item table with 
                // the remaining quantity of the item
                new_qty=result-b_qty
                cursor.execute("select unit_price from items where item_name='{}'".format(b_item));
                b_rate=cursor.fetchone()
                
                // covert billing rate fetched from sql query in list form to integer
                b_rate=int(b_rate[0])
                print(b_rate)
                
                // billing amount = billing rate * quantity
                b_amt=b_rate*b_qty
                cursor.execute("update items set quantity = {} where item_name='{}'".format(new_qty,b_item))
                conn.commit();
                
                // insert billing details into bills table
                cursor.execute("insert into bills(bill_no,bill_item,bill_qty,bill_rate,bill_amt) values({},'{}',{},{},{})".format(b_no,b_item,b_qty,b_rate,b_amt))
                conn.commit();
                conn.close();
                ans=input("Do you want to buy more items - y/n - ")
        
        conn.close();
          
        // Once there are no more items to bill, the final bill with bill number,
        // today's date, billing details from bills table is displayed
        
        print("\n************* FINAL BILL **************")
                
        from datetime import date
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        print("\n Bill Number: ",b_no," Date:", d1)
        print("=======================================\n")
        print(" Item   Qty    Rate  Amount")
        print("----------------------------")
        
        import mysql.connector as sql
        conn=sql.connect(host="localhost",user="root",password="root123",database="market")
            
        if conn.is_connected() == False:
            print("Connection to the database failed")
        cursor=conn.cursor()
        cursor.execute("select bill_item,bill_qty,bill_rate,bill_amt from bills where bill_no={}".format(b_no))            
        result=cursor.fetchall()
        for row in result:
             print(row)
        print("\nTotal Bill Amount (Rs)")
        print("=====================")
        
        // calculate total bill amount for the current bill number by 
        // summing up item wise bill amount 
      
        cursor.execute("select sum(bill_amt) from bills where bill_no={}".format(b_no))
        result=cursor.fetchone()
        for row in result:
             print(row)
        conn.close();
        
        // Get the total bill amount from SQL query output in list format to integer
        // If total bill amount is greater than Rs. 1000, a 10% discount is added to 
        // the final bill amount
        
        tot_bill=result[0]
        if tot_bill >= 1000:
            tot_bill=0.9*tot_bill
            print("Congrats!! You are eligible for 10% discount\n")
            print("Your Final Bill Amount = ",tot_bill)
        print("\n ******** Thank You, Visit Again ********")