def sort_dictionary(aDict):
    sorted_names =[]
    sorted_phonenum =[]
    dict_copy=sorted(aDict.items(), key=lambda x: x[1][1])
    for i in dict_copy:
        sorted_names.append(i[0])
        sorted_phonenum.append(i[1][0])
    complete_list_tuple = list(zip(sorted_names,sorted_phonenum))
    return complete_list_tuple
