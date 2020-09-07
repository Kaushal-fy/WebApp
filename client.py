file = open("/var/log/secure", "r")
data = file.read()
occurrences = data.count("Accepted")
print('Number of occurrences of the word :', occurrences)
