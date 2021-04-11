def firstDuplicate(a):
    s1=set()
    s2=list()
    L=0
    
    for i in range(0,len(a)):
        s1.add(a[i])
        s2.append(a[i])
        L=len(s1)
        L2=len(s2)
        if L==L2 :
            continue
        elif L2>L:
            return a[i]
            pass
    return -1        
            
        
        

