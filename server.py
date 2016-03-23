#!/usr/bin/idle3
# -*-coding:Utf-8 -*

import socket
import sys
import serial

ser = serial.Serial('/dev/ttyACM0',9600)

connx_pri = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connx_pri.bind(('192.168.1.82', 58))
connx_pri.listen(5)
connx_pri.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

data=''
while data != '0':
  connx_client, infos_connx=connx_pri.accept()
  data=connx_client.recv(1024)
  if data=='1': 
    ser.write('1')

  elif data=='2':
    ser.write('2')





