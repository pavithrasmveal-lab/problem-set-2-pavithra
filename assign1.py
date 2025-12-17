list1=[]    #create first list 
list2=[]    #crate second list
s1=int(input("enter size of list1:"))#get size of list1
#to read elements in list1
list1=list(map(int,input("Enter elements:").split()))
#it will work for all except last element
for i in range(0,s1-1):     
    list2.append(list1[i]+list1[i+1])
#append the last element
list2.append(list1[s1-1])
#display of output
print("The original list:",list1)   
print("The changed one:",list2)

