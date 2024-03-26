'''
a=1
sum=0

while (a<=100):
    sum += a
    a = a + 1

print("sum =",sum)
'''
n=int(input("Number: "))
result=''

while(n!=0):
    m=n%2
    result=str(m)+result
    n=n//2
print(result)