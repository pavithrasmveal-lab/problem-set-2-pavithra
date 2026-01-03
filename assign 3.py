
#Given a list of integers, window size k, and value x, count how many contiguous windows of size k have an average ≥ x.

def averagecount(l,sub,avg):
    count=0      #to keep the output count
    for i in range((len(l)-sub)+1):
        sum1=0      #temporary variable to sum and avergae
        avg1=0
        for j in range(i,i+sub):   #to run in length of sublist
            sum1=sum1+int(l[j])
            avg1=sum1/sub
        if(avg1>=avg):    #check for average and increament count
            count+=1
    return count
        
l=list(map(int,input("Enter inputs:").split()))  #get input list
sub=int(input("Enter substring size:"))  #get length of sublist
avg=int(input("Enter average size:"))  # get average value
count=averagecount(l,sub,avg)
print(f"The count is:{count}")

