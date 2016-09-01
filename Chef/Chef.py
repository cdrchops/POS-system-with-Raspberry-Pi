# Python 2.7
# Chef.py

import time

import Communication
import UserInterface
import PrintMethods
import xmlMethods
import dbSQLite3
import Audio
import KitchenDisplay

gSpiceLevel = ["Mild", "Medium", "Hot"]
gCookLevel = ["Rare", "Medium", "Well Done"]

gCurrOrderId = 0

class OrderItem:
  name = ""
  spiceLevel = "Medium" # ("Mild", "Medium", "Hot")
  cookLevel = "Medium" # ("Rare", "Medium", "Well Done")
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
  global gCurrOrderId

  # Start Comminucation
  Communication.init()

  # Database Init
  dbSQLite3.init()
  gCurrOrderId = dbSQLite3.getMaxOid()

  # Pause (2 Seconds)
  time.sleep(2)

  # Kitchen Display
  KitchenDisplay.startDisplay()


def closeAndExit():
  # Stop Comminucation
  Communication.deinit()


def waitForOrderDetails():
  global gCurrOrder

  # Receive Order
  orderXmlStr = Communication.recvData()
  gCurrOrder = Order()
  xmlMethods.xmlStr2order(orderXmlStr, gCurrOrder)

  # Print Order
  PrintMethods.printOrderDetails(gCurrOrder)

  orderId = genearteOrderId()
  dbSQLite3.insertMaxOid(orderId)

  # Send OrderId
  Communication.sendData(str(orderId))

  # Insert Order
  dbSQLite3.insertOrder(orderId, gCurrOrder)

  return gCurrOrder


def sendOrderComplete():

  #Communication.sendData("Order Completed")
  print "1"


def waitForBillRequest():
  global gCurrOrderId

  # Receive Order
  orderXmlStr = Communication.recvData()

  # Generate Bill
  bill = generateBill()

  # Print Bill
  PrintMethods.printBillDetails(bill)

  # Insert Bill
  dbSQLite3.insertBill(gCurrOrderId, bill)

  # Send Bill
  billXmlStr = xmlMethods.bill2xmlStr(bill)
  Communication.sendData(billXmlStr)


def genearteOrderId():
  global gCurrOrderId

  gCurrOrderId = gCurrOrderId + 1

  return gCurrOrderId


def generateBill():
  global gCurrOrder

  bill = Bill()

  bill.tableNum = gCurrOrder.tableNum
  bill.numGuests = gCurrOrder.numGuests
  bill.numItems = gCurrOrder.numItems
  bill.grandTotal = 0

  if bill.numItems > 0:
    bill.item_1.name = gCurrOrder.item_1.name
    bill.item_1.quantity = gCurrOrder.item_1.quantity
    bill.item_1.price = 12.99
    bill.item_1.totalPrice = (bill.item_1.price * bill.item_1.quantity)
    bill.grandTotal = (bill.grandTotal + bill.item_1.totalPrice)

  if bill.numItems > 1:
    bill.item_2.name = gCurrOrder.item_2.name
    bill.item_2.quantity = gCurrOrder.item_2.quantity
    bill.item_2.price = 10.99
    bill.item_2.totalPrice = (bill.item_2.price * bill.item_2.quantity)
    bill.grandTotal = (bill.grandTotal + bill.item_2.totalPrice)

  if bill.numItems > 2:
    bill.item_3.name = gCurrOrder.item_3.name
    bill.item_3.quantity = gCurrOrder.item_3.quantity
    bill.item_3.price = 13.99
    bill.item_3.totalPrice = (bill.item_3.price * bill.item_3.quantity)
    bill.grandTotal = (bill.grandTotal + bill.item_3.totalPrice)

  return bill


def audioSupport():
  Audio.record(10, "sampleAudio.wav")
  Audio.play("sampleAudio.wav")


def test():
  # Database Init
  global gCurrOrderId

  dbSQLite3.init()
  gCurrOrderId = dbSQLite3.getMaxOid()
  print gCurrOrderId

  orderId = genearteOrderId()
  dbSQLite3.insertMaxOid(gCurrOrderId)
  print gCurrOrderId

  orderId = genearteOrderId()
  dbSQLite3.insertMaxOid(gCurrOrderId)
  print gCurrOrderId

  orderId = genearteOrderId()
  dbSQLite3.insertMaxOid(gCurrOrderId)
  print gCurrOrderId

  gCurrOrderId = dbSQLite3.getMaxOid()
  print gCurrOrderId


if __name__ == "__main__":
  main()


