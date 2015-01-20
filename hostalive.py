#!/usr/bin/python

import socket
import sys
import time
import argparse

RETRIES=100
TIMEOUT_SECONDS=10
SLEEP_SECONDS=10

parser = argparse.ArgumentParser(description='Check if host/service is alive.')
parser.add_argument('hostname',metavar='hostname',type=str,nargs=1,help='name of server (short or FQDN)')
parser.add_argument('port',metavar='portnumber',type=int,nargs=1,help='port number for TCP connection')
parser.add_argument('--retries',metavar='retries',type=int,nargs=1,default=[RETRIES],help='number of retries (default is %d)' % RETRIES)
parser.add_argument('--timeout',metavar='timeout',type=int,nargs=1,default=[TIMEOUT_SECONDS],help='seconds to wait for TCP connection (default is %d). Along with --sleep, keep this to a sane high value.' % TIMEOUT_SECONDS)
parser.add_argument('--sleep',metavar='sleep',type=int,nargs=1,default=[SLEEP_SECONDS],help='seconds to wait before retrying TCP connection (default is %d). Along with --timeout, keep this to a sane high value.' % SLEEP_SECONDS)
parser.add_argument('--keepalive',dest='keepalive',action='store_true',help='will continue trying connections even after a successful connection.')
parser.set_defaults(keepalive=False)
args = parser.parse_args()

hostname = args.hostname[0]
port_number = args.port[0]
retries = args.retries[0]
timeout_seconds = args.timeout[0]
sleep_seconds = args.sleep[0]
keepalive = args.keepalive

try:
    server_address=socket.gethostbyname(hostname)
except socket.error as ex:
    sys.stderr.write("Could not resolve hostname!\n")
    quit(1)


socketid = None


while(retries):
    print("Trying to connect to %s - %s on port %d ..." % (hostname,server_address,port_number))
    retries=retries-1
    try:
        socketid = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketid.settimeout(timeout_seconds)
    except socket.error as ex:
        sys.stderr.write( "Could not create socket!\n")
        sys.stderr.write(ex.message)
        quit(1)

    try:
        socketid.connect((server_address,port_number))
        print("Connected!")
        socketid.close()
    except socket.error as ex:
        print("Connect failed")
        socketid = None
    if (keepalive and retries) or (socketid == None and retries):
        print("Sleeping %d seconds before retrying..." % sleep_seconds)
        time.sleep(sleep_seconds)
        continue
    socketid = None
    quit(0)

quit(1)
