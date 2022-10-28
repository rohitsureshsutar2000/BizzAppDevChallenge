#Read a file from a URL in Python

import urllib.request

url = input("Enter Url:-\n")

file = urllib.request.urlopen(url)

for line in file:
    decoded_line = line.decode("utf-8").strip()
    print(decoded_line)


#  Url like
#               http://textfiles.com/adventure/aaow.sol