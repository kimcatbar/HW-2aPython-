def swap_list(aList):
    x = len(aList) - 1 #last postition
    y = x//2 #index in middle 
    aList[x],aList[y]= aList[y],aList[x]
    return aList 
    #print(aList)
