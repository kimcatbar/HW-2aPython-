
def swap_list(aList):
    x = len(aList) - 1 #last postition
    y = x//2 #index in middle 
    if y <= 1:#if list is empty 
        return aList
    else:
        aList[x],aList[y]= aList[y],aList[x]
        return aList 
