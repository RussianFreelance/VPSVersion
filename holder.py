# A script just for container hang, hold in running mode
import time
import os

os.system("echo Script started")
index = 0
while 1:
  if index % 20 == 0:
    os.system("echo ping")
  index += 1
  time.sleep(2)
