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

global userid


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
    print(' 4. Show Order')
    print(' 5. Cancel Order')
    print(' 6. Item Purchase')
    print(' 7. Exit')
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
        customerMainMenu()
        print("\n===================================================\n")
        allshops()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 2:
        customerMainMenu()
        print("\n===================================================\n")
        allitems()
        print("\n===================================================\n")
        customerOptions()
    elif choice == 3:
        customerMainMenu()
        print("\n===================================================\n")
        searchitem()()
        print("\n===================================================\n")
        customerOptions()
    elif choice == 4:
        customerMainMenu()
        print("\n===================================================\n")
        showorder()
        print("\n===================================================\n")
        customerOptions()
    elif choice == 5:
        customerMainMenu()
        print("\n===================================================\n")
        cancelorder()
        print("\n===================================================\n")
        customerOptions()
    elif choice == 6:
        customerMainMenu()
        print("\n===================================================\n")
        itempurchase()
        print("\n===================================================\n")
        customerOptions()
    elif choice == 7:
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
    sql = 'INSERT INTO `itemlist`(`iid`,`iname`,`price`,`kw1`,`kw2`,`kw3`,`qty`,`sid`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (iid.upper(), iname, price, kw1, kw2, kw3, qty, sid.upper())
    cursor.execute(sql, val)
    connection.commit()
    print('---Successfully Added---')

# search the item in db


def searchitem():
    print('---Search Item---')
    iname = input('Enter keyword of Item: ')
    sql = "SELECT iid,sname,iname,CONCAT(COALESCE(`kw1`,''),' ',COALESCE(`kw2`,''),' ',COALESCE(`kw3`,'')) as descri,price,qty FROM itemlist LEFT JOIN shoplist ON itemlist.sid=shoplist.sid WHERE iname LIKE '%" + \
        iname+"%' OR kw1 LIKE '%"+iname+"%' OR kw2 LIKE '%" + \
        iname+"%' OR kw3 LIKE '%"+iname+"%'"
    cursor.execute(sql)
    records = cursor.fetchall()
    print("\nId\tShop Name\tItem Name\tItem Description\tPrice\t\tQty.")
    print("=======================================================================================")
    for r in records:
        print(f'{r[0]}\t{r[1]}\t{r[2]}\t\t{r[3]}\t\t{r[4]}\t\t{r[5]}')

    print('---Sucessfully Search---')

# cancel order by order ID


def cancelorder():
    print('---Cancel Order---')
    oid = input('Enter Order ID: ')
    sql = "SELECT oid,shoplist.sname,itemlist.iname,itemlist.price,orderlist.qty FROM orderlist LEFT JOIN itemlist ON itemlist.iid=orderlist.iid AND itemlist.sid=orderlist.sid LEFT JOIN shoplist ON orderlist.sid=shoplist.sid WHERE orderlist.oid like '%"+oid+"%'"
    cursor.execute(sql)
    records = cursor.fetchall()
    print("\nOrder Id\tShop Name\tItem Name\tPrice\t\tQty.")
    print("=======================================================================================")
    for r in records:
        print(f'{r[0]}\t\t{r[1]}\t{r[2]}\t\t{r[3]}\t\t{r[4]}')
    confirm_cancel_oid = input(
        "\nPlease input the order ID that you want to cancel or press enter to skip :")
    if confirm_cancel_oid != "":
        sql = "UPDATE orderlist SET recstat='C' WHERE oid ='"+confirm_cancel_oid+"'"
        cursor.execute(sql)
        connection.commit()
        print('---Sucessfully Canceled ---')
    else:
        customerMainMenu()
        customerOptions()

# item purchase


def itempurchase():
    global userid
    print('---Item Purchase---')
    sid = input('Enter Shop ID: ')
    iid = input('Enter Item ID: ')
    chk_shop_stock_sql = "SELECT iid,sid,iname,price FROM itemlist WHERE sid= '" + \
        sid+"' AND iid='"+iid+"'"
    cursor.execute(chk_shop_stock_sql)
    records = cursor.fetchall()
    if len(records) == 0:
        print('---No Item Record. Input Again---')
        itempurchase()
    else:
        for r in records:
            item_name = r[2]
            item_price = r[3]
        qty = input("Enter the Qty you want to buy:")
        confirm_to_buy = input("\nPlease confirm the order that you want item:" +
                               item_name+",Qty:"+str(qty)+",Price:"+str(item_price)+" [Y/N]: ")
        if confirm_to_buy == 'Y' or confirm_to_buy == 'y':
            get_max_oid_sql = "select max(oid),UPPER(concat(left(max(oid),2),lpad(right(oid,3)+001,3,0))) AS max from orderlist where sid like '"+sid+"%'"
            cursor.execute(get_max_oid_sql)
            records = cursor.fetchall()
            if len(records) == 0:
                max_oid = sid+"001"
            else:
                for r in records:
                    max_oid = r[1]
            insert_sql = "INSERT INTO orderlist VALUES(%s,%s,%s,%s,%s,NOW(),'N')"
            val = (max_oid, userid.upper(),
                   sid.upper(), iid.upper(), qty)
            cursor.execute(insert_sql, val)
            connection.commit()
            print('Purchase Succfully. Order ID:')
            print(max_oid)
        else:
            customerMainMenu()
            customerOptions()


def showorder():
    print('---Show Your All Ordered---')
    sql = "SELECT oid,shoplist.sname,itemlist.iname,itemlist.price,orderlist.qty FROM orderlist LEFT JOIN itemlist ON itemlist.iid=orderlist.iid AND itemlist.sid=orderlist.sid LEFT JOIN shoplist ON orderlist.sid=shoplist.sid WHERE orderlist.cid ='"+userid+"'"
    cursor.execute(sql)
    records = cursor.fetchall()
    print("\nOrder Id\tShop Name\tItem Name\tPrice\t\tQty.")
    print("=======================================================================================")
    for r in records:
        print(f'{r[0]}\t\t{r[1]}\t{r[2]}\t\t{r[3]}\t\t{r[4]}')
# login function for admin role or customer role


def login():
    global userid
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
