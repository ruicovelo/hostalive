hostalive
=========

Tool to check if a given host/service is reachable.


This was part of a relearning experience using C and UNIX sockets. I discovered I could also have a python script to the same exact thing so I added the python script for better portability. 


So far this is yet another one-tcp-port-scanner (if you can call it a "port scanner").
"There are many like it but this one is mine".

It's a basic example of UNIX sockets programming. 

This kind of tool is also popular because "ping" says very little about a server availability.
Therefore is common for sysadmins to use telnet to check if a given port (read "service") is available
for troubleshooting or when waiting for a reboot to finish. 

Instead of re-running telnet all the time, lazy sysadmins like me write this kind of tools to retry a TCP connection
to a given port until successful.


# USAGE
<pre>
usage: hostalive.py [-h] [--retries retries] [--timeout timeout]
                    [--sleep sleep]
                    hostname portnumber

Check if host/service is alive.

positional arguments:
  hostname           name of server (short or FQDN)
  portnumber         port number for TCP connection

optional arguments:
  -h, --help         show this help message and exit
  --retries retries  number of retries (default is 100)
  --timeout timeout  seconds to wait for TCP connection (default is 10). Along
                     with --sleep, keep this to a sane high value.
  --sleep sleep      seconds to wait before retrying TCP connection (default
                     is 30). Along with --timeout, keep this to a sane high
                     value.

</pre>


## Example:

(I do this when I reboot a server and want to check if it get's back online)

./hostalive.py hostname 22 && ssh user@hostname || echo "Oh noz!!"

or why not:

./hostalive.py hostname 22 && espeak "Host is back online"; ssh user@hostname


