def vowels(string):
    vowels = "aieou"
    count = 0

    for char in string:
        if char.lower() in vowels:
          count += 1
    return count
name = input("enter the string:")

result = vowels(name)
print(result)



