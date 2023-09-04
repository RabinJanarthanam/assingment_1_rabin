# n=50
# num1=0
# num2=1
# next_number=num2
# while next_number<=n:
#     print(next_number,end=" ")
#     num1,num2=num2,next_number
#     next_number=num1+num2
# print()

num=9
n1,n2=1,1
print("fibonacci series:",n1,n2,end=" ")
for i in range(2,num):
    n3=n2+n1
    n1=n2
    n2=n3
    print(n3,end=" ")
print()
