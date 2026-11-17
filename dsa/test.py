import re
p = re.compile(r"^\d{3}$")       # exactly 3 digits, nothing else
print(p.match("123"))            # ?
print(p.match("1234"))           # ?
print(p.match("052"))            # ?