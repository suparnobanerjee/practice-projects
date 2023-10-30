import re
text = "Hello this is the number 82, and this is a phone number 9244522195 and this is also a phone number (92)-1353-4621 and this also +91 2245 5731"
pattern = '\d{10}|\(\d{2}\)-\d{4}\-\d{4}|\+\d{2}\ \d{4}\ \d{4}'
matches = re.findall(pattern,text)
print(matches)