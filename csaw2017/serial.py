#!/usr/bin/env python
import socket
import sys

# connect with server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4239
s.connect(("misc.chal.csaw.io", port))

# ommit the first prompt
string = "8-1-1 even parity. Respond with '1' if you got the byte, '0' to retransmit."
skip = len(string.encode('utf-8'))
s.recv(skip + 1)

# 11 bits = 1 start bit - 8 data bits - 1 parity bit - 1 stop bit
# Each binary is 11 bits + \n = 12 characters
flag = ''
while True:
	binary = s.recv(12)
	data = binary[1:10]
	d = binary[1:9]
	ones = 0
	for c in data:
		if c == "1":
			ones = ones + 1
	if (ones%2 == 0):
		print binary
		d2 = chr(int(d, 2))
		flag = flag + d2
		print flag
		s.send('1'+'\r\n')
	else:
		s.send('0'+'\r\n')

