# Python 2.7
# dbSQLite3.py

import sqlite3

DB_FILE_NAME = "projectDB.db"


def init():
  global dbHandle

  # Connect to DB
  dbHandle = sqlite3.connect(DB_FILE_NAME)

  # Create Table
  createOrderTable()
  createBillTable()
  createMaxOidTable()


def createOrderTable():
  global dbHandle

  cursor = dbHandle.cursor()
  
  # Drop Order Table
  #try:
  #  cursor.execute('''DROP TABLE ORDERS''')
  #except sqlite3.OperationalError:
  #  pass

  # Create Table
  try:
    cursor.execute('''CREATE TABLE ORDERS
      ( ORDER_ID   INT  NOT NULL,
        DATE       TEXT NOT NULL,
        TIME       TEXT NOT NULL,
        TABLE_NUM  INT  NOT NULL,
        NUM_GUESTS INT  NOT NULL,
        NUM_ITEMS  INT  NOT NULL,
        IT1_NAME   TEXT NOT NULL,
        IT1_SL     TEXT NOT NULL,
        IT1_CL     TEXT NOT NULL,
        IT1_QUANT  INT  NOT NULL,
        IT2_NAME   TEXT,
        IT2_SL     TEXT,
        IT2_CL     TEXT,
        IT2_QUANT  INT,
        IT3_NAME   TEXT,
        IT3_SL     TEXT,
        IT3_CL     TEXT,
        IT3_QUANT  INT
      );''')
  except sqlite3.OperationalError:
    pass

  # Commit
  dbHandle.commit()


def createBillTable():
  global dbHandle

  cursor = dbHandle.cursor()
  
  # Drop Order Table
  #try:
  #  cursor.execute('''DROP TABLE BILLS''')
  #except sqlite3.OperationalError:
  #  pass

  # Create Table
  try:
    cursor.execute('''CREATE TABLE BILLS
      ( BILL_ID    INT           NOT NULL,
        DATE       TEXT          NOT NULL,
        TIME       TEXT          NOT NULL,
        TABLE_NUM  INT           NOT NULL,
        NUM_GUESTS INT           NOT NULL,
        NUM_ITEMS  INT           NOT NULL,
        GRD_TOTAL  DECIMAL(5,2)  NOT NULL,
        IT1_NAME   TEXT          NOT NULL,
        IT1_QUANT  INT           NOT NULL,
        IT1_PRICE  DECIMAL(5,2)  NOT NULL,
        IT1_TPRICE DECIMAL(5,2)  NOT NULL,
        IT2_NAME   TEXT,
        IT2_QUANT  INT,
        IT2_PRICE  DECIMAL(5,2),
        IT2_TPRICE DECIMAL(5,2),
        IT3_NAME   TEXT,
        IT3_QUANT  INT,
        IT3_PRICE  DECIMAL(5,2),
        IT3_TPRICE DECIMAL(5,2)
      );''')
  except sqlite3.OperationalError:
    pass

  # Commit
  dbHandle.commit()


def createMaxOidTable():
  global dbHandle

  cursor = dbHandle.cursor()
  
  # Drop Order Table
  #try:
  #  cursor.execute('''DROP TABLE MAXOID''')
  #except sqlite3.OperationalError:
  #  pass

  # Create Table
  try:
    cursor.execute('''CREATE TABLE MAXOID
      ( MAX_ORDER_ID   INT  NOT NULL );''')
  except sqlite3.OperationalError:
    pass

  # Commit
  dbHandle.commit()



def insertOrder(orderId, od):
  global dbHandle

  cursor = dbHandle.cursor()

  # Delete Entry
  try:
    cursor.execute('''DELETE FROM ORDERS WHERE ORDER_ID = {val}'''.format(val = orderId))
  except sqlite3.OperationalError:
    pass

  # Add Entry
  if od.numItems == 1:
    cursor.execute('''INSERT INTO ORDERS
      ( ORDER_ID, DATE, TIME, TABLE_NUM, NUM_GUESTS, NUM_ITEMS, 
      IT1_NAME, IT1_SL, IT1_CL, IT1_QUANT) VALUES(?,?,?,?,?,?,?,?,?,?)''', 
      (orderId, od.date, od.time, od.tableNum, od.numGuests, od.numItems, 
      od.item_1.name, od.item_1.spiceLevel, od.item_1.cookLevel, od.item_1.quantity))

  if od.numItems == 2:
    cursor.execute('''INSERT INTO ORDERS
      ( ORDER_ID, DATE, TIME, TABLE_NUM, NUM_GUESTS, NUM_ITEMS, 
      IT1_NAME, IT1_SL, IT1_CL, IT1_QUANT, IT2_NAME, IT2_SL, IT2_CL, IT2_QUANT)
      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (orderId, od.date, od.time, od.tableNum, od.numGuests, od.numItems, 
      od.item_1.name, od.item_1.spiceLevel, od.item_1.cookLevel, od.item_1.quantity, 
      od.item_2.name, od.item_2.spiceLevel, od.item_2.cookLevel, od.item_2.quantity))

  if od.numItems == 3:
    cursor.execute('''INSERT INTO ORDERS
      ( ORDER_ID, DATE, TIME, TABLE_NUM, NUM_GUESTS, NUM_ITEMS, 
      IT1_NAME, IT1_SL, IT1_CL, IT1_QUANT, IT2_NAME, IT2_SL, IT2_CL, IT2_QUANT, IT3_NAME, IT3_SL, IT3_CL, IT3_QUANT)
      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (orderId, od.date, od.time, od.tableNum, od.numGuests, od.numItems, 
      od.item_1.name, od.item_1.spiceLevel, od.item_1.cookLevel, od.item_1.quantity, 
      od.item_2.name, od.item_2.spiceLevel, od.item_2.cookLevel, od.item_2.quantity,
      od.item_3.name, od.item_3.spiceLevel, od.item_3.cookLevel, od.item_3.quantity))

  # Commit
  dbHandle.commit()


def insertBill(billId, bd):
  global dbHandle

  cursor = dbHandle.cursor()

  # Delete Entry
  try:
    cursor.execute('''DELETE FROM BILLS WHERE BILL_ID = {val}'''.format(val = billId))
  except sqlite3.OperationalError:
    pass

  # Add Entry
  if bd.numItems == 1:
    cursor.execute('''INSERT INTO BILLS
      ( BILL_ID, DATE, TIME, TABLE_NUM, NUM_GUESTS, NUM_ITEMS, GRD_TOTAL, 
      IT1_NAME, IT1_QUANT, IT1_PRICE, IT1_TPRICE) VALUES(?,?,?,?,?,?,?,?,?,?,?)''', 
      (billId, bd.date, bd.time, bd.tableNum, bd.numGuests, bd.numItems, bd.grandTotal, 
      bd.item_1.name, bd.item_1.quantity, bd.item_1.price, bd.item_1.totalPrice))

  if bd.numItems == 2:
    cursor.execute('''INSERT INTO BILLS
      ( BILL_ID, DATE, TIME, TABLE_NUM, NUM_GUESTS, NUM_ITEMS, GRD_TOTAL, 
      IT1_NAME, IT1_QUANT, IT1_PRICE, IT1_TPRICE, IT2_NAME, IT2_QUANT, IT2_PRICE, IT2_TPRICE)
      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (billId, bd.date, bd.time, bd.tableNum, bd.numGuests, bd.numItems, bd.grandTotal, 
      bd.item_1.name, bd.item_1.quantity, bd.item_1.price, bd.item_1.totalPrice, 
      bd.item_2.name, bd.item_2.quantity, bd.item_2.price, bd.item_2.totalPrice))

  if bd.numItems == 3:
    cursor.execute('''INSERT INTO BILLS
      ( BILL_ID, DATE, TIME, TABLE_NUM, NUM_GUESTS, NUM_ITEMS, GRD_TOTAL, 
      IT1_NAME, IT1_QUANT, IT1_PRICE, IT1_TPRICE, IT2_NAME, IT2_QUANT, IT2_PRICE, IT2_TPRICE, IT3_NAME, IT3_QUANT, IT3_PRICE, IT3_TPRICE)
      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (billId, bd.date, bd.time, bd.tableNum, bd.numGuests, bd.numItems, bd.grandTotal, 
      bd.item_1.name, bd.item_1.quantity, bd.item_1.price, bd.item_1.totalPrice, 
      bd.item_2.name, bd.item_2.quantity, bd.item_2.price, bd.item_2.totalPrice,
      bd.item_3.name, bd.item_3.quantity, bd.item_3.price, bd.item_3.totalPrice))

  # Commit
  dbHandle.commit()

def insertMaxOid(maxOid):
  global dbHandle

  cursor = dbHandle.cursor()

  # Delete Entry
  try:
    cursor.execute('''DELETE FROM MAXOID WHERE MAX_ORDER_ID = {val}'''.format(val = maxOid-1))
  except sqlite3.OperationalError:
    pass

  # Add Entry
  cursor.execute('''INSERT INTO MAXOID ( MAX_ORDER_ID ) VALUES(?)''', (maxOid,))

  # Commit
  dbHandle.commit()


def getMaxOid():
  global dbHandle

  cursor = dbHandle.cursor()

  try:
    cursor.execute('''SELECT MAX_ORDER_ID FROM MAXOID''')
    entry = cursor.fetchall()
  except sqlite3.OperationalError:
    entry = 0
    pass

  if not entry:
    entry = 0
  else:
    entry = entry[0][0]

  return entry


def printOrder(orderId):
  global dbHandle

  cursor = dbHandle.cursor()

  cursor.execute('''SELECT * FROM ORDERS WHERE ORDER_ID = {val}'''.format(val = orderId))
  entry = cursor.fetchall()
  print entry


def prinBill(billId):
  global dbHandle

  cursor = dbHandle.cursor()

  cursor.execute('''SELECT * FROM BILLS WHERE BILL_ID = {val}'''.format(val = billId))
  entry = cursor.fetchall()
  print entry


def printOrderTable():
  global dbHandle

  cursor = dbHandle.cursor()

  cursor.execute('''SELECT * FROM ORDERS''')
  entries = cursor.fetchall()

  print "================================================="

  print "ID     Date     Time   Table Guests Items"
  for entry in entries:
    print str(entry[0]) + "  " + entry[1] + " " + entry[2] + "   " + str(entry[3]) + "     " + str(entry[4]) + "      " + str(entry[5])

  print "================================================="


def printBillTable():
  global dbHandle

  cursor = dbHandle.cursor()

  cursor.execute('''SELECT * FROM BILLS''')
  entries = cursor.fetchall()

  print "================================================="

  print "ID     Date     Time   Table Guests Items ToTal"
  for entry in entries:
    print str(entry[0]) + "  " + entry[1] + " " + entry[2] + "   " + str(entry[3]) + "     " + str(entry[4]) + "      " + str(entry[5]) + "   $" + str(entry[6])

  print "================================================="


