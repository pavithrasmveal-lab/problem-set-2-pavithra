l=list(map(int,input("Enter inputs:").split())) #get input list
flag=False
for i in range((len(l)-1),1,-1):    #sub list length from large to small
    for j in range((len(l)-i)+1):    
        count0=0  #to count zero
        count1=0  #to count one
        for k in range(j,j+i):  #to maintain possible sublist
            if(l[k]==0):      #check for zero and increament
                count0+=1  
            else:
                count1+=1        #check for one and increament
        if(count0==count1):     #check count1 and count0 equal
            print(f"The longest subarray with eaual one and zero :{i}")
            flag=True
            break  #breaks inner loop
    if (flag):
        break  #break outer loop
