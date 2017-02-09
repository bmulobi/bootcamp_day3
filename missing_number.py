def find_missing(list1, list2):
    
    if len(list1) == 0 and len(list2) == 0:
        return 0
        
    set1 = set(list1)
    set2 = set(list2)
    
    if len(list(set1 - set2)) == 0 and len(list(set2 - set1)) == 0:
        return 0
    
    if len(set1) > len(set2):
        num = list(set1 - set2)
        return int(num[0])
        
    else:
        num = list(set2 - set1)
        return int(num[0])   

a = find_missing([1,2,3],[1,2])        
print(a)