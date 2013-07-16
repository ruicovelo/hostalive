#!/usr/bin/python

import socket
import sys
import time


USAGE="Usage: <hostname> <port>"
SLEEP_SECONDS=5
RETRIES=3
TIMEOUT=5

if (len(sys.argv) != 3):
    print USAGE
    quit(1)

hostname = sys.argv[1]
try:
    port_number = int(sys.argv[2])
except ValueError:
  print USAGE
  quit(1)

server_address=socket.gethostbyname(hostname)
while(RETRIES):
    RETRIES=RETRIES-1
    try:
        socketid = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketid.settimeout(TIMEOUT)
    except socket.error as ex:
        print "Could not create socket"
        quit(1)
    try:
        socketid.connect((server_address,port_number))
    except socket.error as ex:
        print "Connect failed"
        print "Sleeping %d seconds..." % SLEEP_SECONDS
        time.sleep(SLEEP_SECONDS)
        continue
    print "Connected."
    socketid.close()
    socketid = None
    break




