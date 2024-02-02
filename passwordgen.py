import random
import string
from typing import List, Any

s1 = string.ascii_lowercase
print(s1)
s2= string.ascii_uppercase
print(s2)
s3= string.digits
print(s3)
s4= string.punctuation
print(s4)

plen = int(input("Enter password length\n"))
s = []
s = list(s1) + list(s2) + list(s3) + list(s4)
print(s)
random.shuffle(s)
print(s)
print("" . join(s[0:plen]))
