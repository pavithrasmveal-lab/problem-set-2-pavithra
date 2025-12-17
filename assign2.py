l=list(map(int,input("Enter inputs:").split()))  # get input list from user
maximum_sum_temp=0               #store maximum sum
k=int(input("Enter length of substring:"))     # get length for substring
for i in range(((len(l)-k)+1)):
    sum_l=0           # to calculate sum for every iteration
    for j in range(i,i+k):      #to run in length of substring
        sum_l=sum_l+int(l[j])    # perform addition
    if(maximum_sum_temp<sum_l):     # update maimum sum
        maximum_sum_temp=sum_l
        a=i
print(f"The substring with maximum sum is:{l[a:a+k]}")  #print the substring
print(f"The maximum sum is:{maximum_sum_temp}") #print the maximum sum
 
