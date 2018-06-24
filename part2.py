#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For SI 507 Waiver, fall 2018
@author: oshinnayak, onayak @umich.edu

"""
import sys
import sqlite3


# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>


 
def create_connection(db_file):
    
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def customers(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT Id AS 'ID', CompanyName AS 'Customer Name'  from Customer ")
 
    rows = cur.fetchall()
 
    print("ID", " Customer Name")
    for row in rows:
        print(str(row[0]), str(row[1]))
 
 
def employees(conn):

    cur = conn.cursor()
    cur.execute("SELECT Id AS 'ID', (FirstName || \" \" ||  LastName)  AS 'Employee Name' from Employee")
 
    rows = cur.fetchall()

    print("ID", "Employee Name")
    for row in rows:
        print(str(row[0])+"  "+ str(row[1]))

 
def orders(conn,cust=None,emp=None):

    cur = conn.cursor()
    if cust is not None:
    	cur.execute("SELECT O.Orderdate from 'Order' AS O JOIN Customer AS C on O.CustomerId= C.Id WHERE C.Id= (?) ",(cust,) )
    	rows = cur.fetchall()
    if emp is not None:
    	cur.execute("SELECT O.Orderdate from 'Order' AS O JOIN Employee AS E on O.EmployeeId= E.Id WHERE E.LastName= (?) ",(emp,) )
    	rows = cur.fetchall()

    print("Order dates")

    for row in rows:
        print(str(row[0]))

 
def main():
    database = "Northwind_small.sqlite"
    # create a database connection
    conn = create_connection(database)
    if (len(sys.argv) > 1):
            with conn:
                if sys.argv[1] == "customers":
                     customers(conn)
                elif (sys.argv[1] == "employees"):
                    employees(conn)
                elif (sys.argv[1] == "orders"):
                    if (sys.argv[2][0]=="c"):
                        orders(conn, sys.argv[2][5:],None)
                    elif (sys.argv[2][0]=="e"):
                        orders(conn,None, sys.argv[2][4:])
                else:
                    print("Please correct arguments")

    else:
        print("Please correct arguments")
    
    	
    
if __name__ == '__main__':
    main()
    

