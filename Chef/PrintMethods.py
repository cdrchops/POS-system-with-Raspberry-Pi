# Python 2.7
# PrintMethods.py

def printOrderDetails(orderDetails):
  print "================================================="
  print "Order Details:"
  print "  Date       : " + orderDetails.date
  print "  Time       : " + orderDetails.time
  print "  Table Num  : " + str(orderDetails.tableNum)
  print "  Num Guests : " + str(orderDetails.numGuests)
  print "  Num Items  : " + str(orderDetails.numItems)

  if orderDetails.numItems > 0:
    print ""
    print "  Item 1 :"
    print "    Name        : " + orderDetails.item_1.name
    print "    Spice Level : " + orderDetails.item_1.spiceLevel
    print "    Cook Level  : " + orderDetails.item_1.cookLevel
    print "    Quantity    : " + str(orderDetails.item_1.quantity)

  if orderDetails.numItems > 1:
    print ""
    print "  Item 2 :"
    print "    Name        : " + orderDetails.item_2.name
    print "    Spice Level : " + orderDetails.item_2.spiceLevel
    print "    Cook Level  : " + orderDetails.item_2.cookLevel
    print "    Quantity    : " + str(orderDetails.item_2.quantity)

  if orderDetails.numItems > 2:
    print ""
    print "  Item 3 :"
    print "    Name        : " + orderDetails.item_3.name
    print "    Spice Level : " + orderDetails.item_3.spiceLevel
    print "    Cook Level  : " + orderDetails.item_3.cookLevel
    print "    Quantity    : " + str(orderDetails.item_3.quantity)

  print "================================================="


def printBillDetails(billDetails):
  print "================================================="
  print "Bill Details:"
  print "  Date       : " + billDetails.date
  print "  Time       : " + billDetails.time
  print "  Table Num  : " + str(billDetails.tableNum)
  print "  Num Guests : " + str(billDetails.numGuests)
  print "  Num Items  : " + str(billDetails.numItems)
  print "  Grand Total: " + "$" + str(billDetails.grandTotal)

  if billDetails.numItems > 0:
    print ""
    print "  Item 1 :"
    print "    Name        : " + billDetails.item_1.name
    print "    Quantity    : " + str(billDetails.item_1.quantity)
    print "    Price       : " + "$" + str(billDetails.item_1.price)
    print "    Total Price : " + "$" + str(billDetails.item_1.totalPrice)

  if billDetails.numItems > 1:
    print ""
    print "  Item 2 :"
    print "    Name        : " + billDetails.item_2.name
    print "    Quantity    : " + str(billDetails.item_2.quantity)
    print "    Price       : " + "$" + str(billDetails.item_2.price)
    print "    Total Price : " + "$" + str(billDetails.item_2.totalPrice)

  if billDetails.numItems > 2:
    print ""
    print "  Item 3 :"
    print "    Name        : " + billDetails.item_3.name
    print "    Quantity    : " + str(billDetails.item_3.quantity)
    print "    Price       : " + "$" + str(billDetails.item_3.price)
    print "    Total Price : " + "$" + str(billDetails.item_3.totalPrice)

  print "================================================="


