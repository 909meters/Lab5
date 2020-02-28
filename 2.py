import re

n = input()
txt = "The most handsome"
x = re.findall(n, txt)
print(x)