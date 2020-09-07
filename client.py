import socket
import sys
import time
while True:
    time.sleep(1)
    host=socket.gethostname()
    file=open("/var/log/secure", "r")
    count=0
    for line in file:
        if 'Failed' in line or 'Accepted' in line:
            count=count+1
    sys.stdout = open("/var/www/html/index.html", 'w')
    print(str(count) + " SSH attempts happened on " + host)
