# Python 2.7
# communication.py

import threading
import Queue
from socket import *

TARGET_IP = "10.0.0.15" # i.e. of the Order placement system
PORT = 5000
BUFFER_SIZE = 1024
TIME_OUT = 1
RETRY_COUNT = 60
QUEUE_SIZE = 10

sendLock = threading.Lock()
sendFullCondVar = threading.Condition(sendLock)
sendEmptyCondVar = threading.Condition(sendLock)
sendQueue = Queue.Queue(maxsize = QUEUE_SIZE)

recvLock = threading.Lock()
recvFullCondVar = threading.Condition(recvLock)
recvEmptyCondVar = threading.Condition(recvLock)
recvQueue = Queue.Queue(maxsize = QUEUE_SIZE)


def init():
  global task_1, task_2

  task_1 = threading.Thread(target = startServer)
  task_1.start()

  task_2 = threading.Thread(target = startClient)
  task_2.start()


def deinit():
  global task_1, task_2

  sendData("exit")

  task_2.join()
  task_1.join()


def sendData(data):
  # Acquire (sendLock)
  sendLock.acquire()

  # Wait (Full)
  while(sendQueue.full()):
    sendFullCondVar.wait()

  # Put Data
  sendQueue.put(data)
  sendEmptyCondVar.notify()

  # Release (sendLock)
  sendLock.release()


def recvData():
  # Acquire (recvLock)
  recvLock.acquire()

  # Wait (Empty)
  while(recvQueue.empty()):
    recvEmptyCondVar.wait()

  # Get Data
  data = recvQueue.get()
  recvFullCondVar.notify()

  # Release (recvLock)
  recvLock.release()

  return data


def startServer():
  host = ""
  port = PORT
  buffSize = BUFFER_SIZE

  address = (host, port)
  serverSocket = socket(AF_INET, SOCK_DGRAM)
  serverSocket.bind(address)

  retryCount = 0
  while (retryCount < RETRY_COUNT):
    print "Ch1: Attempt " + str(retryCount + 1) + "/" + str(RETRY_COUNT)
    try:
      serverSocket.settimeout(TIME_OUT)
      (data, address) = serverSocket.recvfrom(buffSize)
      if data == "req:connect":
        data = "res:connected"
        serverSocket.sendto(data, address)
        break
    except timeout:
      retryCount = retryCount + 1
      pass

  if (retryCount == RETRY_COUNT):
    print "Ch1: Connection Failed"
  else:
    print "Ch1: Connection Successful"

    serverSocket.settimeout(None)
    serverSocket.setblocking(1)

    while True:
      (data, address) = serverSocket.recvfrom(buffSize)
      if data == "exit":
        break

      # Acquire (recvLock)
      recvLock.acquire()

      # Wait (Full)
      while(recvQueue.full()):
        recvFullCondVar.wait()

      # Put Data
      recvQueue.put(data)
      recvEmptyCondVar.notify()

      # Release (recvLock)
      recvLock.release()

  serverSocket.close()


def startClient():
  host = TARGET_IP
  port = PORT
  buffSize = BUFFER_SIZE

  address = (host, port)
  clientSocket = socket(AF_INET, SOCK_DGRAM)

  retryCount = 0
  while (retryCount < RETRY_COUNT):
    print "Ch2: Attempt " + str(retryCount + 1) + "/" + str(RETRY_COUNT)
    try:
      data = "req:connect"
      clientSocket.settimeout(TIME_OUT)
      clientSocket.sendto(data, address)
      (data, address) = clientSocket.recvfrom(buffSize)
      if data == "res:connected":
        break
    except timeout:
      retryCount = retryCount + 1
      pass

  if (retryCount == RETRY_COUNT):
    print "Ch2: Connection Failed"
  else:
    print "Ch2: Connection Successful"

    clientSocket.settimeout(None)
    clientSocket.setblocking(1)

    while True:
      # Acquire (sendLock)
      sendLock.acquire()

      # Wait (Empty)
      while(sendQueue.empty()):
        sendEmptyCondVar.wait()

      # Get Data
      data = sendQueue.get()
      sendFullCondVar.notify()

      # Release (sendLock)
      sendLock.release()

      clientSocket.sendto(data, address)
      if data == "exit":
        break

  clientSocket.close()


