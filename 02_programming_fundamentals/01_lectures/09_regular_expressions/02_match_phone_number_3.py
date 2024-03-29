import re

data = input()
pattern = r"(^|(?<=\s))(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
phones = re.finditer(pattern, data)
phones = [p.group(0) for p in phones]
print(', '.join(phones))
