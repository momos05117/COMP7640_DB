COMP7640 Database Systems and Administration - Group Project

Below would show the steps for running the project:

Basic requirements:
- Python 3.5 Installed
- MySQL Installed

_____________________________________________________________________________
Step 1: Create "management" database after login to MySQL

mysql> CREATE DATABASE management;

_____________________________________________________________________________
Step 2: Import the SQL file "Mysql_DB_EX.sql" to management database

% mysql -u root management < Mysql_DB_EX.sql

_____________________________________________________________________________
Step 3: Run the Python file "Interface.py"

% python3 interface.py

There are two types of users, admin and customer

For admin login:
Input your user ID to login : admin

For customer login:
Input your user ID to login : [customer ID] e.g. C1, C2, C3

After login, you may then follow the instructions shown on command line to run the programme.

_____________________________________________________________________________


Below is the demo of admin:

Input your user ID to login : admin

After login, the meun would be shown as follow:
Welcome to login!
 — — — — MENU — — — -
 1. Show All Shops
 2. Show All Items in each shop
 3. Add A Shop
 4. Add A Item
 5. Search Item
 6. Cancel Order
 7. Exit
 — — — — — — — — — —

Function 1:
Please enter your choice[MENU 1-7] : 1
---Show All Shops---

Function 2:
Please enter your choice[MENU 1-7] : 2
Input the shop ID:S1
---Show All Items In the shop---

Function 3:
Please enter your choice[MENU 1-7] : 3
Enter Shop ID:S4
Enter Shop Name:Food shop
Please rate this Shop from 1 to 5:5
Enter Shop Location:Aberdeen
---Successfully Added---

Function 4:
Please enter your choice[MENU 1-7] : 4
Enter Item Code:I2  
Enter Item Name:Burger
Enter the price of this items:500
Enter the 1st characteristic of this item:big
Enter the 2nd characteristic of this item:meat
Enter the 3rd characteristic of this item:fast food
Enter the quantity of this item:40
Enter Shop ID:S6
---Successfully Added---

Function 5:
Please enter your choice[MENU 1-7] : 5
Enter keyword of Item: meat
---Sucessfully Search---

Function 6:
Please enter your choice[MENU 1-7] : 6
Enter Order ID: S2001
Please input the order ID that you want to cancel or press enter to skip :S2001
---Sucessfully Canceled ---

Function 7:
Please enter your choice[MENU 1-7] : 7
Logout Successful!

_____________________________________________________________________________


Below is the demo of customer:

Input your user ID to login : C1

After login, the meun would be shown as follow:
Welcome C1
 — — — — MENU — — — -
 1. Show All Shops
 2. Show All Items
 3. Search Item
 4. Show Order
 5. Cancel Order
 6. Item Purchase
 7. Exit
 — — — — — — — — — — 

Function 1:
Please enter your choice[MENU 1-7] : 1
---Show All Shops---

Function 2:
Please enter your choice[MENU 1-7] : 2
Input the shop ID:S3
---Show All Items In the shop---

Function 3:
Please enter your choice[MENU 1-7] : 3
Enter keyword of Item: meat
---Sucessfully Search---

Function 4:
Please enter your choice[MENU 1-7] : 4
---Show Your All Ordered---

Function 5:
Please enter your choice[MENU 1-7] : 5
Enter Order ID: S1001
Please input the order ID that you want to cancel or press enter to skip :S1001
---Sucessfully Canceled ---

Function 6:
Please enter your choice[MENU 1-7] : 6
Enter Shop ID: S1
Enter Item ID: I1
Enter the Qty you want to buy:3
Please confirm the order that you want item:Apple,Qty:3,Price:10 [Y/N]: Y
Purchase Succfully. Order ID:S4001

Function 7:
Please enter your choice[MENU 1-7] : 7
Logout Successful!