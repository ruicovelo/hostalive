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
try:
    server_address=socket.gethostbyname(hostname)
except socket.error as ex:
  sys.stderr.write("Could not resolve hostname!\n")
  quit(1)


while(RETRIES):
    print "Trying to connect to %s - %s on port %d ..." % (hostname,server_address,port_number)
    RETRIES=RETRIES-1
    try:
        socketid = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketid.settimeout(TIMEOUT)
    except socket.error as ex:
        sys.stderr.write( "Could not create socket!\n")
        quit(1)
    try:
        socketid.connect((server_address,port_number))
    except socket.error as ex:
        print "Connect failed"
        print "Sleeping %d seconds..." % SLEEP_SECONDS
        time.sleep(SLEEP_SECONDS)
        socketid = None
        continue
    print "Connected."
    socketid.close()
    socketid = None
    break




