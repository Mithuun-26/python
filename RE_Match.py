import re
text="Python is Hard"
x=re.match(r"Python",text)
print(x.group())
