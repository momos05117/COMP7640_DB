from logging.config import valid_ident
from sqlite3 import connect
import mysql.connector
import os

# mysql connection
connection = mysql.connector.connect(host='127.0.0.1',
                                     user='root',
                                     passwd='',
                                     database='management')
cursor = connection.cursor()


def adminMainMenu():
    print(' — — — — MENU — — — -')
    print(' 1. Show All Shops')
    print(' 2. Show All Items in each shop')
    print(' 3. Add A Shop')
    print(' 4. Add A Item')
    print(' 5. Search Item')
    print(' 6. Cancel Order')
    print(' 7. Exit')
    print(' — — — — — — — — — — ')


def customerMainMenu():
    print(' — — — — MENU — — — -')
    print(' 1. Show All Shops')
    print(' 2. Show All Items')
    print(' 3. Search Item')
    print(' 4. Cancel Order')
    print(' 5. Item Purchase')
    print(' 6. Exit')
    print(' — — — — — — — — — — ')


def adminOptions():
    choice = int(input("Please enter your choice[MENU 1-7] : "))
    if choice == 1:
        os.system('cls')
        adminMainMenu()
        print("\n===================================================\n")
        allshops()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 2:
        os.system('cls')
        adminMainMenu()
        print("\n===================================================\n")
        allitems()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 3:
        os.system('cls')
        adminMainMenu()
        print("\n===================================================\n")
        addshop()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 4:
        os.system('cls')
        adminMainMenu()
        print("\n===================================================\n")
        additem()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 5:
        os.system('cls')
        adminMainMenu()
        print("\n===================================================\n")
        searchitem()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 6:
        os.system('cls')
        adminMainMenu()
        print("\n===================================================\n")
        cancelorder()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 7:
        os.system('cls')
        print("\n===================================================\n")
        exit()
        print("\n====================BYE!===========================\n")
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        adminMainMenu()
        print("\n===================================================\n")
        adminOptions()


def customerOptions():
    choice = int(input("Please enter your choice : "))
    if choice == 1:
        os.system('cls')
        customerMainMenu()
        print("\n===================================================\n")
        allshops()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 2:
        os.system('cls')
        customerMainMenu()
        print("\n===================================================\n")
        allitems()
        print("\n===================================================\n")
        customerOptions()
    elif choice == 3:
        os.system('cls')
        customerMainMenu()
        print("\n===================================================\n")
        addshop()
        print("\n===================================================\n")
        customerOptions()
    elif choice == 4:
        os.system('cls')
        customerMainMenu()
        print("\n===================================================\n")
        additem()
        print("\n===================================================\n")
        customerOptions()
    elif choice == 5:
        os.system('cls')
        customerMainMenu()
        print("\n===================================================\n")
        searchitem()
        print("\n===================================================\n")
        customerOptions()
    elif choice == 6:
        os.system('cls')
        customerMainMenu()
        print("\n===================================================\n")
        cancelorder()
        print("\n===================================================\n")
        customerOptions()
    elif choice == 7:
        os.system('cls')
        print("\n===================================================\n")
        exit()
        print("\n====================BYE!===========================\n")
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        customerMainMenu()
        print("\n===================================================\n")
        customerOptions()

# exit the system and back to login


def exit():
    print("Logout Successful!")
    login()

# show all the shop in db


def allshops():
    print('---Show All Shops---')
    print("\nId\tShop Name\tRating\t\tLocation")
    print("=============================================================")
    cursor.execute('SELECT * FROM `shoplist`;')
    records = cursor.fetchall()
    for r in records:
        print(f'{r[0]}\t{r[1]}\t{r[2]}\t\t{r[3]}')

# show all the item in each shop by user input shop id


def allitems():
    shopid = input('Input the shop ID:')
    print('---Show All Items In the shop---')
    print("\nId\tItem Name\tPrice\t\tQty.")
    print("=============================================================")
    sql = "SELECT iid,iname,price,qty FROM `itemlist` WHERE sid='"+shopid+"';"
    cursor.execute(sql)
    records = cursor.fetchall()
    for r in records:
        print(f'{r[0]}\t{r[1]}\t\t{r[2]}\t\t{r[3]}')
    print('---Successfully Showed---')

# add the shop


def addshop():
    print('---Add A New Shop---')
    sid = input('Enter Shop ID:')
    sname = input('Enter Shop Name:')
    rating = input('Please rate this Shop from 1 to 5:')
    location = input('Enter Shop Location:')
    sql = 'INSERT INTO `shoplist`(`sid`,`sname`,`rating`,`location`) VALUES (%s,%s,%s,%s)'
    val = (sid, sname, rating, location)
    cursor.execute(sql, val)
    connection.commit()
    print('---Successfully Added---')

# add the item


def additem():
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
    val = (iid, iname, price, kw1, kw2, kw3, qty, sid, compid)
    cursor.execute(sql, val)
    connection.commit()
    print('---Successfully Added---')

# search the item in db


def searchitem():
    print('---Search Item---')
    iname = input('Enter Item Name: ')
    sql = "SELECT * FROM itemlist WHERE iname LIKE '%"+iname+"%'"
    cursor.execute(sql)
    records = cursor.fetchall()
    for r in records:
        print(r)

    print('---Sucessfully Search---')

# cancel order by order ID


def cancelorder():
    print('---Cancel Order---')
    oid = input('Enter Order ID: ')
    sql = "DELETE FROM orderlist WHERE oid LIKE '%"+oid+"%'"
    cursor.execute(sql)
    connection.commit()

    print('---Sucessfully Canceled ---')

# item purchase


def itempurchase():
    print('---Item Purchase---')
    oid = input('Enter Order ID: ')
    sql = "SELECT itemlist.iname, orderlist.cid FROM itemlist INNER JOIN orderlist ON itemlist.compid IN(orderlist.compid1,orderlist.compid2, orderlist.compid3 ) WHERE orderlist.oid like '%"+oid+"%'"
    cursor.execute(sql)
    records = cursor.fetchall()
    for r in records:
        print(r)

    print('---Purchase List End ---')

# login function for admin role or customer role


def login():
    userid = ''
    username = input(
        "Input your user ID to login : ")
    sql = "SELECT cid from clientlist WHERE cid like '"+username+"'"
    cursor.execute(sql)
    records = cursor.fetchall()
    for r in records:
        userid = r[0]

    if not userid:
        print("No user id!")
    elif userid == 'admin':
        print("Welcome to login!")
        adminMainMenu()
        adminOptions()
    else:
        print("Welcome "+userid)
        customerMainMenu()
        customerOptions()


if __name__ == '__main__':
    login()
