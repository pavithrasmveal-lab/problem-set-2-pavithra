#new list generation given a list(m) and output(n) a new list of same length but i-th element is defined as n[i]=m[i]+m[i+1] except last element
def new_list(list1):
    list2=[]     #output list
    for i in range(0,len(list1)-1):    #it will work for all except last element 
        list2.append(list1[i]+list1[i+1])
    list2.append(list1[len(list1)-1])  #append the last element
    return list2          #return output
list1=list(map(int,input("Enter inputs:").split())) #input list
list2=new_list(list1)      #function call
print("The original list:",list1)    #display output
print("The changed one:",list2)
