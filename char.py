text = input("Enter text: ")
alpha = 0
num = 0
char = 0
for ch in text:
    if ch.isalpha():
        alpha+= 1
    if ch.isalnum():
        num+=1
    else:
        char+=1
print(alpha)
print(num)
print(char)
