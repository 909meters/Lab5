import re

txt = "The most handsome"
n = int(input())
x = re.split("\s", txt, n)
print(x)