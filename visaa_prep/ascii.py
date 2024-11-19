s=input()
result=""
for i in s:
    if i.islower():
        result+=i.upper()
    if i.isupper():
        result+=i.lower()
print(result)
