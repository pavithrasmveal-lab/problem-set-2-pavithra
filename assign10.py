#Robot sensor program
file=open("sensor_data.txt","r") #open file in read mode
distance=[]    #list formation
for line in file:
    line=line.strip()
    if line.startswith('#') or line=="":  #to ignore line start with #
        continue
    distance.append(float(line))   #add remaing readings
total_readings=len(distance)       # for total_readingd
maximum_reading=max(distance)      #for maximum
minimum_reading=min(distance)     #for minimum
apporach=0
backoff=0
for i in range(1,len(distance)-1):
    if(distance[i-1]>distance[i]):  #previous>currrent =approach
        apporach+=1
    if(distance[i]<distance[i+1]): #current<next=backoff
        backoff+=1
file.close()     #close file 
#output display
print("Total readings :",total_readings)   
print("Maximum distance:",maximum_reading)
print("Minimum distance:",minimum_reading)
print("No of Approach:",apporach)
print("No of backoff:",backoff)

