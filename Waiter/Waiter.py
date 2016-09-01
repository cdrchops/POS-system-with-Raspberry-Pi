# Python 2.7
# Waiter.py

import time

import Communication
import UserInterface
import PrintMethods
import xmlMethods
import dbSQLite3
import Audio

gSpiceLevel = ["Mild", "Medium", "Hot"]
gCookLevel = ["Rare", "Medium", "Well Done"]

class OrderItem:
  name = ""
  spiceLevel = "." # ("Mild", "Medium", "Hot")
  cookLevel = "." # ("Rare", "Medium", "Well Done")
  quantity = 0

class Order:
  date = time.strftime("%m/%d/%Y")
  time = time.strftime("%H:%M:%S")
  tableNum = 0
  numGuests = 0
  numItems = 0
  item_1 = OrderItem()
  item_2 = OrderItem()
  item_3 = OrderItem()

class BillItem:
  name = ""
  quantity = 0
  price = 0.00
  totalPrice = 0.00

class Bill:
  date = time.strftime("%m/%d/%Y")
  time = time.strftime("%H:%M:%S")
  tableNum = 0
  numGuests = 0
  numItems = 0
  item_1 = BillItem()
  item_2 = BillItem()
  item_3 = BillItem()
  grandTotal = 0.00


def main():

  # Start Comminucation
  Communication.init()

  # Pause (2 Seconds)
  # time.sleep(2)

  # Start User Interface
  UserInterface.startDisplay()


def closeAndExit():
  # Stop Comminucation
  Communication.deinit()


def orderDetails(data):
  global gCurrOrder

  index = 0
  gCurrOrder = Order()
  gCurrOrder.tableNum = 10

  if (data[0] + data[2] + data[4] != 0):
    # Food
    if (data[0] != 0):
      index = index + 1
      name = "F_Item1"
      quantity = data[0]
      spice = "."
      cook = gCookLevel[data[1] - 1]
      fillFoodDetails(index, name, quantity, spice, cook)

    if (data[2] != 0):
      index = index + 1
      name = "F_Item2"
      quantity = data[2]
      spice = gSpiceLevel[data[3] - 1]
      cook = "."
      fillFoodDetails(index, name, quantity, spice, cook)

    if (data[4] != 0):
      index = index + 1
      name = "F_Item3"
      quantity = data[4]
      spice = "."
      cook = "."
      fillFoodDetails(index, name, quantity, spice, cook)
  else:
    # Drinks
    if (data[5] != 0):
      index = index + 1
      name = "D_Item1"
      quantity = data[5]
      fillDrinksDetails(index, name, quantity)

    if (data[6] != 0):
      index = index + 1
      name = "D_Item2"
      quantity = data[6]
      fillDrinksDetails(index, name, quantity)

    if (data[7] != 0):
      index = index + 1
      name = "D_Item3"
      quantity = data[7]
      fillDrinksDetails(index, name, quantity)

  sendOrder2Chef()


def sendOrder2Chef():
  global gCurrOrder
  global gOrderId

  # Print Order
  PrintMethods.printOrderDetails(gCurrOrder)

  # Create Xml String
  orderXmlStr = xmlMethods.order2xmlStr(gCurrOrder)
  Communication.sendData(orderXmlStr)


def waitForOrderComplete():

  # Wait for Order Complete
  orderIdStr = Communication.recvData()


def sendBillRequest():

    Communication.sendData("Bill Request")
 

def fillFoodDetails(index, name, quantity, spice, cook):
  global gCurrOrder

  if index == 1:
    gCurrOrder.item_1.name = name
    gCurrOrder.item_1.spiceLevel = spice
    gCurrOrder.item_1.cookLevel = cook
    gCurrOrder.item_1.quantity = quantity
    gCurrOrder.numItems = gCurrOrder.numItems + 1
  elif index == 2:
    gCurrOrder.item_2.name = name
    gCurrOrder.item_2.spiceLevel = spice
    gCurrOrder.item_2.cookLevel = cook
    gCurrOrder.item_2.quantity = quantity
    gCurrOrder.numItems = gCurrOrder.numItems + 1
  elif index == 3:
    gCurrOrder.item_3.name = name
    gCurrOrder.item_3.spiceLevel = spice
    gCurrOrder.item_3.cookLevel = cook
    gCurrOrder.item_3.quantity = quantity
    gCurrOrder.numItems = gCurrOrder.numItems + 1


def fillDrinksDetails(index, name, quantity):
  global gCurrOrder

  if index == 1:
    gCurrOrder.item_1.name = name
    gCurrOrder.item_1.quantity = quantity
    gCurrOrder.numItems = gCurrOrder.numItems + 1
  elif index == 2:
    gCurrOrder.item_2.name = name
    gCurrOrder.item_2.quantity = quantity
    gCurrOrder.numItems = gCurrOrder.numItems + 1
  elif index == 3:
    gCurrOrder.item_3.name = name
    gCurrOrder.item_3.quantity = quantity
    gCurrOrder.numItems = gCurrOrder.numItems + 1


def getOrderDetailsStr():
  global gCurrOrder
  global gOrderId

  # Wait for Order Id
  orderIdStr = Communication.recvData()
  gOrderId = int(orderIdStr)

  if (gCurrOrder.item_1.name[0] == 'F'):
    food = True
  else:
    food = False

  orderStr = ("======================================================" + "\n" 
  "   Order Id	: " + str(gOrderId) + "\n\n"
  "	Date	: " + gCurrOrder.date + "\n"
  "	Time	: " + gCurrOrder.time + "\n"
  "	Table	: " + str(gCurrOrder.tableNum) + "\n"
  "	Items	: " + str(gCurrOrder.numItems) + "\n")

  if gCurrOrder.numItems > 0:
    orderStr = orderStr + (
    "   Item 1 :" + "\n"
    "	Name	: " + gCurrOrder.item_1.name + "\n"
    "	Quantity	: " + str(gCurrOrder.item_1.quantity) + "\n")
    if (food == True):
      orderStr = orderStr + (
      "	Spice	: " + gCurrOrder.item_1.spiceLevel + "\n"
      "	Cook	: " + gCurrOrder.item_1.cookLevel + "\n")

  if gCurrOrder.numItems > 1:
    orderStr = orderStr + (
    "   Item 2 :" + "\n"
    "	Name	: " + gCurrOrder.item_2.name + "\n"
    "	Quantity	: " + str(gCurrOrder.item_2.quantity) + "\n")
    if (food == True):
      orderStr = orderStr + (
      "	Spice	: " + gCurrOrder.item_2.spiceLevel + "\n"
      "	Cook	: " + gCurrOrder.item_2.cookLevel + "\n")

  if gCurrOrder.numItems > 2:
    orderStr = orderStr + (
    "   Item 3 :" + "\n"
    "	Name	: " + gCurrOrder.item_3.name + "\n"
    "	Quantity	: " + str(gCurrOrder.item_3.quantity) + "\n")
    if (food == True):
      orderStr = orderStr + (
      "	Spice	: " + gCurrOrder.item_3.spiceLevel + "\n"
      "	Cook	: " + gCurrOrder.item_3.cookLevel + "\n")

  orderStr = orderStr + "======================================================"

  return orderStr


def getBillDetailsStr():
  global gOrderId

  # Receive Bill
  billXmlStr = Communication.recvData()
  bill = Bill()
  xmlMethods.xmlStr2bill(billXmlStr, bill)

  # Print Bill
  PrintMethods.printBillDetails(bill)

  billStr = ("======================================================" + "\n" 
  "   Order Id	: " + str(gOrderId) + "\n\n"
  "	Date	: " + bill.date + "\n"
  "	Time	: " + bill.time + "\n"
  "	Table	: " + str(bill.tableNum) + "\n"
  "	Items	: " + str(bill.numItems) + "\n"
  "	G Total	: $" + str(bill.grandTotal) + "\n")

  if bill.numItems > 0:
    billStr = billStr + (
    "   Item 1 :" + "\n"
    "	Name	: " + bill.item_1.name + "\n"
    "	Quantity	: " + str(bill.item_1.quantity) + "\n"
    "	Price	: $" + str(bill.item_1.price) + "\n"
    "	Total	: $" + str(bill.item_1.totalPrice) + "\n")

  if bill.numItems > 1:
    billStr = billStr + (
    "   Item 1 :" + "\n"
    "	Name	: " + bill.item_2.name + "\n"
    "	Quantity	: " + str(bill.item_2.quantity) + "\n"
    "	Price	: $" + str(bill.item_2.price) + "\n"
    "	Total	: $" + str(bill.item_2.totalPrice) + "\n")

  if bill.numItems > 2:
    billStr = billStr + (
    "   Item 1 :" + "\n"
    "	Name	: " + bill.item_3.name + "\n"
    "	Quantity	: " + str(bill.item_3.quantity) + "\n"
    "	Price	: $" + str(bill.item_3.price) + "\n"
    "	Total	: $" + str(bill.item_3.totalPrice) + "\n")

  billStr = billStr + "======================================================"

  return billStr



if __name__ == "__main__":
  main()



