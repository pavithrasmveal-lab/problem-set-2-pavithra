#maximum sum of fixed window ,given a list and integer ,find maximum sum of any contiguous sublist of size k

def max_sum(l,k):
    maximum_sum_temp=0    #store maximum sum
    for i in range(((len(l)-k)+1)):
        sum_l=0           # to calculate sum for every iteration
        for j in range(i,i+k):        #to run in length of substring
            sum_l=sum_l+int(l[j])    # perform addition
        if(maximum_sum_temp<sum_l):     
            maximum_sum_temp=sum_l    # update maimum sum
            a=i
    return maximum_sum_temp,a     #return maximum sum and the which position
l=list(map(int,input("Enter inputs:").split()))  #get input list from user
k=int(input("Enter length of substring:"))    # get length for substring
maximum_sum_temp,a=max_sum(l,k)         #fuction call
print(f"The substring with maximum sum is:{l[a:a+k]}")  #print the substring
print(f"The maximum sum is:{maximum_sum_temp}")    #print the maximum sum
 

