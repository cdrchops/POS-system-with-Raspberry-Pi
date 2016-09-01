# Python 2.7
# audio.py

import subprocess


def record(length, fileName):

  bashString = "arecord -D plughw:1,0 -d " + str(length) + " -r 16000 " + str(fileName)

  recordProc = subprocess.Popen(bashString, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  # print recodingProc.pid

  recordProc.wait()


def play(fileName):

  bashString = "aplay -r 16000 " + str(fileName)

  playProc = subprocess.Popen(bashString, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  # print playProc.pid

  playProc.wait()
