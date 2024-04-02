def Squares(n):
    return n**2
numbers =[1,3,5,9]
print(list(map(Squares,numbers)))

Squares=lambda n:n**2
numbers=[1,3,5,9]
print(list(map(Squares,numbers)))

print(list(map(lambda n:n**2,[1,3,5,9])))
