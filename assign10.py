
file=open("sensor_data.txt","r")
distance=[]
for line in file:
    line=line.strip()
    if line.startswith('#') or line=="":
        continue
    distance.append(float(line))
total_readings=len(distance)
maximum_reading=max(distance)
minimum_reading=min(distance)
apporach=0
backoff=0
for i in range(1,len(distance)-1):
    if(distance[i-1]>distance[i]):
        apporach+=1
    if(distance[i]<distance[i+1]):
        backoff+=1
file.close()
print("Total readings :",total_readings)
print("Maximum distance:",maximum_reading)
print("Minimum distance:",minimum_reading)
print("No of Approach:",apporach)
print("No of backoff:",backoff)
