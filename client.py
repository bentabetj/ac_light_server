#!/usr/bin/idle3
# -*-coding:Utf-8 -*

import socket
import serial
import sys



connx_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connx_server.connect(('192.168.1.82',58))

etat=sys.argv[1];

connx_server.send(etat)

connx_server.close()