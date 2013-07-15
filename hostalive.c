#include <stdlib.h>
#include <stdio.h>
#include <netinet/in.h>
#include <fcntl.h>
#include <netdb.h>
#include <sys/socket.h>
#include <unistd.h>



int main (int argc, const char *argv[]) {
  int socketid;
	struct sockaddr_in server_address;
	struct hostent* hostinfo;
	const char *hostname;
	int port_number;
	int tries=10;			// number of tries to connect
	int timeout=5;			// connecting timeout in seconds
	int sleep_seconds=30;	// sleep before retry
	fd_set fdset;			// file descritor set for monitoring the socket
    struct timeval tv;		// time out struct

	
//TODO: validate arguments
//TODO: get executable name for usage information
//TODO: configurable timeout
//TODO: configurable tries
//TODO: configurable sleep

	if (argc != 3){
		fprintf(stderr,"Usage: <hostname> <port>\n");
		return 1;
	}else {
		hostname = argv[1];
		port_number = strtol(argv[2],(char **)NULL,10);
	}

	
	
	server_address.sin_family = AF_INET;
	
	printf("Resolving %s ...\n",hostname);
	hostinfo = gethostbyname (hostname);
	if (hostinfo == NULL){
		fprintf(stderr,"Could not resolve IP address for %s\n",hostname);
		return 1;
	}else {
		server_address.sin_addr = *((struct in_addr *) hostinfo->h_addr);	 
	}
	
	server_address.sin_port = htons(port_number);
	
	while(tries--){
		socketid = socket(PF_INET,SOCK_STREAM,0);
		
		// setting socket to non-blocking so I can control the timeout
		fcntl(socketid, F_SETFL, O_NONBLOCK);

		if (socketid != -1){
			printf("Trying to connect...\n");
			connect(socketid,(struct sockaddr *)&server_address,sizeof(struct sockaddr_in));
		
			FD_ZERO(&fdset);			// clear set
			FD_SET(socketid, &fdset);	// assign set to socket
			tv.tv_sec = timeout;		// prepare timeout struct for select
			tv.tv_usec = 0;
			
			// monitoring socket state with select usint the file descriptor set and timeout
			if (select(socketid + 1, NULL, &fdset, NULL, &tv) == 1)
			{
				// something happend to socket
				int socket_error;
				socklen_t len = sizeof socket_error;
				
				// getting socket state
				getsockopt(socketid, SOL_SOCKET, SO_ERROR, &socket_error, &len);
			
				if (socket_error == 0) {
					printf("Connected.\n");
					close(socketid);
					//TODO: run something
					return 0;				
				}else {
					perror("Connect");
				}
			}
			else {
				printf("Timeout... Sleeping %d seconds... \n",sleep_seconds);
				sleep(sleep_seconds);
			}

		
		}else {
			fprintf(stderr,"Could not create socket...\n");
			return -1;
		}
	}

    return 0;
}
