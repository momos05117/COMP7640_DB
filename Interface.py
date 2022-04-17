from logging.config import valid_ident
from sqlite3 import connect
import mysql.connector
import os 

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     passwd='passw0rd',
                                     database='management')

def displayMainMenu():
    print(' — — — — MENU — — — -')
    print(' 1. Show All Shops')
    print(' 2. Show All Items')
    print(' 3. Add A Shop')
    print(' 4. Add A Item')
    print(' 5. Search Item')
    print(' 6. Cancel Order')
    print(' 7. Exit')
    print(' — — — — — — — — — — ')

def exit():
    n = int(input(' Press 7 to exit : '))
    if n == 7:
       os.system('cls') # For Windows
       run()
    else:
       print('Invalid Option')
       exit()

def allshops():  
    cursor = connection.cursor()
    print('---Show All Shops---')
    cursor.execute('SELECT * FROM `shoplist`;')
    records = cursor.fetchall()
    for r in records:
        print(r)
    print('---Successfully Showed---')
    exit ()

def allitems():
    cursor = connection.cursor()
    print('---Show All Items---')
    cursor.execute('SELECT * FROM `itemlist`;')
    records = cursor.fetchall()
    for r in records:
        print(r)
    print('---Successfully Showed---')
    exit ()

def addshop():
    cursor = connection.cursor()
    print('---Add A New Shop---')
    sid = input('Enter Shop ID:')
    sname = input('Enter Shop Name:')
    rating = input('Please rate this Shop from 1 to 5:')
    location = input('Enter Shop Location:')

    sql = 'INSERT INTO `shoplist`(`sid`,`sname`,`rating`,`location`) VALUES (%s,%s,%s,%s)'
    val = (sid,sname,rating,location)
    cursor.execute(sql,val)
    connection.commit()
    
    print('---Successfully Added---')
    exit ()

def additem():
    cursor = connection.cursor()
    print('---Add A New Item---')
    iid = input('Enter Item Code:')
    iname = input('Enter Item Name:')
    price = input('Enter the price of this items:')
    kw1 = input('Enter the 1st characteristic of this item:')
    kw2 = input('Enter the 2nd characteristic of this item:')
    kw3 = input('Enter the 3rd characteristic of this item:')
    qty = input('Enter the quantity of this item:')
    sid = input('Enter Shop ID:')
    compid = (iid+sid)
    
    sql = 'INSERT INTO `itemlist`(`iid`,`iname`,`price`,`kw1`,`kw2`,`kw3`,`qty`,`sid`,`compid`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (iid,iname,price,kw1,kw2,kw3,qty,sid,compid)
    cursor.execute(sql,val)
    connection.commit()
    
    print('---Successfully Added---')
    exit ()

def searchitem():
    cursor = connection.cursor()
    print('---Search Item---')
    iname = input ('Enter Item Name: ')
    sql = "SELECT * FROM itemlist WHERE iname LIKE '%"+iname+"%'"
    cursor.execute(sql)
    records=cursor.fetchall()
    for r in records:
        print(r)

    print('---Sucessfully Search---')
    exit ()

def cancelorder():
     cursor = connection.cursor()
     print('---Cancel Order---')
     iid = input ('Enter Item Code: ')
     sid = input ('Enter Shop ID: ')
     compid = iid+sid
     sql = "DELETE FROM itemlist WHERE compid LIKE '%"+compid+"%'"
     cursor.execute(sql)
     connection.commit()

     print('---Sucessfully Canceled ---')
     exit ()


def run ():
    displayMainMenu()
    n = int(input('Enter Option: '))
    if n == 1:
        os.system ('cls')
        allshops()
    elif n ==2:
        os.system ('cls')
        allitems()    
    elif n==3:
        os.system ('cls')
        addshop()    
    elif n==4:
        os.system ('cls')
        additem()
    elif n==5:
        os.system ('cls')
        searchitem()
    elif n==6:
        os.system ('cls')
        cancelorder()  
    elif n==7:
        os.system ('cls')
        print(' — — — Thank You — — -')
    else:
        os.system ('cls')
        run()

if __name__ == '__main__':
   run()