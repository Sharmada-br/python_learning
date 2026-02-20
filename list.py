def function1(data):
    return_list =[]
    for val in data:  
        if val % 2 != 0:
            return_list.append(val)
    return return_list
print(function1([1, 2, 3, 4, 5, 6]))