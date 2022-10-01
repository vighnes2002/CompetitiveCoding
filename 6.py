arr=[55,88,99,98,68,25]
first=0
runnerup=0

for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    if arr[i]>arr[j]:
      arr[i],arr[j]=arr[j],arr[i]
print(arr)
print("Runner up: ",arr[len(arr)-2])

