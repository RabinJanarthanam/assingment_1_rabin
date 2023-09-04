number=(1,2,3,4,5,6,7,8,9)
even=0
odd=0
for num in number:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("no of even number:",even)
print("no of odd number:",odd)
