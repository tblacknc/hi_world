

def sortit(array):
    a = 0
    temp = 0
    l1 = 0
    for a in array:
        # a = number being compared
        if l1 + 1 != len(array):
            if a > array[l1 + 1]:
                temp = array[l1 + 1]
                array[l1 + 1] = a
                array[l1] = temp
                sortit(array)   
            l1 += 1  
    return array   
            
print(sortit([1,3, 5, 2]))
print(sortit([1,3,5,3,1,3,5,3,6,8,5,9,3,5,3,1,3,5,3,6,8,3,5,3,1,3,5,3,6,8,5,9,3,5,3,1,3,5,3,6,8,5,9]))

