import time

file = open(r'/var/log/secure', 'r')

while True:

    line = file.readline()
    if 'Failed' in line or 'Accepted' in line:
        time.sleep(1)
        print 'Found ',line
