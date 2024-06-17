import re

s = "dog cat cat dog"
s = re.sub('[^a-z]','',s)
print(s)