
def swap_list(aList):
    x = len(aList) - 1 #last postition
    y = x//2 #index in middle 
    if y < 0:#if list only has one elememt since o//2 = 0 
        return aList
    else:
        aList[x],aList[y]= aList[y],aList[x]
        return aList 
