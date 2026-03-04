def reverse_string(text):
    ans  = ""
    for ch in text:
        ans = ch + ans
    return ans

name = input("enter the string:")

result = reverse_string(name)
print(result)