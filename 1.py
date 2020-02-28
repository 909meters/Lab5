import re

txt = "The most handsime"
x = re.search("^The.*handsome$", txt)
if (x):
    print("YES! We have a match!")
else:
    print("No match")