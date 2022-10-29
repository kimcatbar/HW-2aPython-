def sort_dictionary(aDict):
    sorted_names =[]#list of name
    sorted_phonenum =[]#list of phonenumbers
    dict_copy=sorted(aDict.items(), key=lambda x: x[1][1])#sort by age
    for i in dict_copy:
        sorted_names.append(i[0])#add names to list
        sorted_phonenum.append(i[1][0])#add phone numbers to list 
    complete_list_tuple = list(zip(sorted_names,sorted_phonenum))#zip creates a list(of tuples)
    return complete_list_tuple
