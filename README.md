hostalive
=========

Tool to check if a given host/service is reachable.


Getting back on the horse using C and UNIX sockets. 

_update_: I dared to ask myself if it could be done in python using low level library... python version added.

So far this is yet another one-tcp-port-scanner (if you can call it a "port scanner").
"There are many like it but this one is mine". Seriously... there are lots of examples of tools like this
because this is a good example of the code required to connect to a specified TCP port.

This kind of tool is also popular because "ping" says very little about a server availability.
Therefore is common for sysadmins to use telnet to check if a given port (read "service") is available
for troubleshooting of just waiting for a reboot to finish. 

Instead of rerunning telnet all the time, lazy sysadmins like me write this kind of tools to retry a TCP connection
to a given port until successful.

My goal is to add a few of my own features.
