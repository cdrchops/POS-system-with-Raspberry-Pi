# Python 2.7
# xmlMethods.py

import xml.etree.ElementTree as ET


def order2xmlStr(orderDetails):

  orderNode = ET.Element("order")

  ET.SubElement(orderNode, "date").text = orderDetails.date
  ET.SubElement(orderNode, "time").text = orderDetails.time
  ET.SubElement(orderNode, "tableNum").text = str(orderDetails.tableNum)
  ET.SubElement(orderNode, "numGuests").text = str(orderDetails.numGuests)
  ET.SubElement(orderNode, "numItems").text = str(orderDetails.numItems)

  if orderDetails.numItems > 0:
    itemNode = ET.SubElement(orderNode, "item", name = orderDetails.item_1.name)
    ET.SubElement(itemNode, "spiceLevel").text = orderDetails.item_1.spiceLevel
    ET.SubElement(itemNode, "cookLevel").text = orderDetails.item_1.cookLevel
    ET.SubElement(itemNode, "quantity").text = str(orderDetails.item_1.quantity)

  if orderDetails.numItems > 1:
    itemNode = ET.SubElement(orderNode, "item", name = orderDetails.item_2.name)
    ET.SubElement(itemNode, "spiceLevel").text = orderDetails.item_2.spiceLevel
    ET.SubElement(itemNode, "cookLevel").text = orderDetails.item_2.cookLevel
    ET.SubElement(itemNode, "quantity").text = str(orderDetails.item_2.quantity)

  if orderDetails.numItems > 2:
    itemNode = ET.SubElement(orderNode, "item", name = orderDetails.item_3.name)
    ET.SubElement(itemNode, "spiceLevel").text = orderDetails.item_3.spiceLevel
    ET.SubElement(itemNode, "cookLevel").text = orderDetails.item_3.cookLevel
    ET.SubElement(itemNode, "quantity").text = str(orderDetails.item_3.quantity)

  # orderTree = ET.ElementTree(orderNode)
  # orderTree.write("orderSample1.xml")

  orderXmlStr = ET.tostring(orderNode, encoding = "us-ascii", method = "xml")
  return orderXmlStr


def xmlStr2order(orderXmlStr, orderDetails):

  orderNode = ET.fromstring(orderXmlStr)

  # orderTree = ET.ElementTree(orderNode)
  # orderTree.write("orderSample2.xml")

  orderDetails.date = orderNode.find("date").text
  orderDetails.time = orderNode.find("time").text
  orderDetails.tableNum = int(orderNode.find("tableNum").text)
  orderDetails.numGuests = int(orderNode.find("numGuests").text)
  orderDetails.numItems = int(orderNode.find("numItems").text)

  itemNodes = orderNode.findall("item")

  if orderDetails.numItems > 0:
    orderDetails.item_1.name = itemNodes[0].get("name")
    orderDetails.item_1.spiceLevel = itemNodes[0].find("spiceLevel").text
    orderDetails.item_1.cookLevel = itemNodes[0].find("cookLevel").text
    orderDetails.item_1.quantity = int(itemNodes[0].find("quantity").text)

  if orderDetails.numItems > 1:
    orderDetails.item_2.name = itemNodes[1].get("name")
    orderDetails.item_2.spiceLevel = itemNodes[1].find("spiceLevel").text
    orderDetails.item_2.cookLevel = itemNodes[1].find("cookLevel").text
    orderDetails.item_2.quantity = int(itemNodes[1].find("quantity").text)

  if orderDetails.numItems > 2:
    orderDetails.item_3.name = itemNodes[2].get("name")
    orderDetails.item_3.spiceLevel = itemNodes[2].find("spiceLevel").text
    orderDetails.item_3.cookLevel = itemNodes[2].find("cookLevel").text
    orderDetails.item_3.quantity = int(itemNodes[2].find("quantity").text)

  return orderDetails


def bill2xmlStr(billDetails):

  billNode = ET.Element("bill")

  ET.SubElement(billNode, "date").text = billDetails.date
  ET.SubElement(billNode, "time").text = billDetails.time
  ET.SubElement(billNode, "tableNum").text = str(billDetails.tableNum)
  ET.SubElement(billNode, "numGuests").text = str(billDetails.numGuests)
  ET.SubElement(billNode, "numItems").text = str(billDetails.numItems)
  ET.SubElement(billNode, "grandTotal").text = str(billDetails.grandTotal)

  if billDetails.numItems > 0:
    itemNode = ET.SubElement(billNode, "item", name = billDetails.item_1.name)
    ET.SubElement(itemNode, "quantity").text = str(billDetails.item_1.quantity)
    ET.SubElement(itemNode, "price").text = str(billDetails.item_1.price)
    ET.SubElement(itemNode, "totalPrice").text = str(billDetails.item_1.totalPrice)

  if billDetails.numItems > 1:
    itemNode = ET.SubElement(billNode, "item", name = billDetails.item_2.name)
    ET.SubElement(itemNode, "quantity").text = str(billDetails.item_2.quantity)
    ET.SubElement(itemNode, "price").text = str(billDetails.item_2.price)
    ET.SubElement(itemNode, "totalPrice").text = str(billDetails.item_2.totalPrice)

  if billDetails.numItems > 2:
    itemNode = ET.SubElement(billNode, "item", name = billDetails.item_3.name)
    ET.SubElement(itemNode, "quantity").text = str(billDetails.item_3.quantity)
    ET.SubElement(itemNode, "price").text = str(billDetails.item_3.price)
    ET.SubElement(itemNode, "totalPrice").text = str(billDetails.item_3.totalPrice)

  # billTree = ET.ElementTree(billNode)
  # billTree.write("billSample1.xml")

  billXmlStr = ET.tostring(billNode, encoding = "us-ascii", method = "xml")
  return billXmlStr


def xmlStr2bill(billXmlStr, billDetails):

  billNode = ET.fromstring(billXmlStr)

  # billTree = ET.ElementTree(billNode)
  # billTree.write("billSample2.xml")

  billDetails.date = billNode.find("date").text
  billDetails.time = billNode.find("time").text
  billDetails.tableNum = int(billNode.find("tableNum").text)
  billDetails.numGuests = int(billNode.find("numGuests").text)
  billDetails.numItems = int(billNode.find("numItems").text)
  billDetails.grandTotal = float(billNode.find("grandTotal").text)

  itemNodes = billNode.findall("item")

  if billDetails.numItems > 0:
    billDetails.item_1.name = itemNodes[0].get("name")
    billDetails.item_1.quantity = int(itemNodes[0].find("quantity").text)
    billDetails.item_1.price = float(itemNodes[0].find("price").text)
    billDetails.item_1.totalPrice = float(itemNodes[0].find("totalPrice").text)

  if billDetails.numItems > 1:
    billDetails.item_2.name = itemNodes[1].get("name")
    billDetails.item_2.quantity = int(itemNodes[1].find("quantity").text)
    billDetails.item_2.price = float(itemNodes[1].find("price").text)
    billDetails.item_2.totalPrice = float(itemNodes[1].find("totalPrice").text)

  if billDetails.numItems > 2:
    billDetails.item_3.name = itemNodes[2].get("name")
    billDetails.item_3.quantity = int(itemNodes[2].find("quantity").text)
    billDetails.item_3.price = float(itemNodes[2].find("price").text)
    billDetails.item_3.totalPrice = float(itemNodes[2].find("totalPrice").text)

  return billDetails


