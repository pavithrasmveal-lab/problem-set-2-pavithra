l=list(map(int,input("Enter inputs:").split()))  #get input
target=int(input("Enter a number:"))   #get target value
flag=False     
for i in range(2,len(l)):#for sub list length
    for j in range((len(l)-i)+1):  
        sum=0
        for k in range(j,j+i):   #for possible sublist for length i
            sum=sum+int(l[k])     
        if(sum==target):      #checking for target value
            print(f"The smallest length:{i}")#print output
            print(f"The subarray:{l[j:j+i]}")
            flag=True         
            break         #break the inner loop
    if (flag):
        break          #break the outer loop
