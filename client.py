import sys
import time
while True:
    time.sleep(1)
    file=open("/var/log/secure", "r")
    count=0
    for line in file:
        if 'Failed' in line or 'Accepted' in line:
            count=count+1
#    sys.stdout = open('file', 'w')
    sys.stdout = open("/var/www/html/index.html", 'w')
    print("No of SSH attempts on server: ",count)
