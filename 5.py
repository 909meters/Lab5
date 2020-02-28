import re

txt = "The most handsome"
n = input()
x = re.search(n, txt)
print(x)