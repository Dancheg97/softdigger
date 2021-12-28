import re

x = re.sub(r'[^a-zA-Z ]+', '', 'happy t00 go 129.129')

print(x)
