def longsubstring(l):
    maxi=0     
    for i in range(len(a)):  #run upto length of list
        count1=0        
        for j in range(len(str(a[i]))): #to get the string length in a list
            count1+=1
        if(maxi<=count1):  #check for maximum substing
            maxi=count1
    return maxi
string=input("Enter a string:")  #getinput string
a=string.split() #string convert to list 
maxi=longsubstring(a)  #function call
print(f"The length of longest contiguous substring with no space:{maxi}")
