def homogeneous_list_to_heterogeneous_list(data):
    return_list=[]
    for i in data:
        #if type(i)==int or type(i)==float or type(i)==bool or type(i) == dict:
        #if type(i)!=str:
        if type(i) !=str and type(i)!=float:

            return_list.append(i)

    return return_list
print(homogeneous_list_to_heterogeneous_list([1,"hello",3.14,True,"world",{"name":"sharmada"}]))

 
