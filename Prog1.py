#연습문제1
listA=["a","b","c"]
listA.insert(0,"홍길동")
listA.insert(2,"홍길순")
listA.append("홍길")
print(listA)

#연습문제2
listB=[1,2,3]
listB[1]=17
print(listB)
listB.extend([4,5,6])
print(listB)
listB.pop(0)
print(listB)
listB.sort()
print(listB)
listB.sort(reverse=True)
print(listB)
listB.insert(3,25)

#연습문제3
from random import randint
player=50
while(player> 0 and player < 100 ):
    coin1 = randint(1,2)
    coin2 = randint(1,2)
    
    if(coin2==coin1):
        player+=9
        print("맞췄습니다. 현재 당신의 돈은 ",player) 
    else:
        player-=10
        print("틀렸습니다. 현재 당신의 돈은 ",player)

#연습문제4
def GCB(n,m):
    while(n>0):
        ram = m%n
        m=n
        n=ram
    return m

n=int(input("입력1:"))
m=int(input("입력2:"))

if(n>m):
     print(GCB(m,n))
else:
    print(GCB(n,m))

#연습문제 5
string=input("Your word:")
len1=string.find('a')+1
print(string[0:len1])
print(string[len1:])

#연습문제 6
sum=0
for i in '123456':
    sum+=int(i)
print(sum)

#연습문제 7
listA=[]
for i in range(0,49,1):
    listA.append(i)
listB=[i**2 for i in listA]
print(listA)
print(listB)


#연습문제 8
days = {'January':31, 'February':28, 'March':31, 'April':30,    
'May':31, 'June':30, 'July':31, 'August':31,
 'September':30, 'October':31, 'November':30, 
'December':31}

m=input("월 입력:")
print(days[m])
print(sorted(days.keys()))
for month, days_in_month in days.items():
        if days_in_month == 31:
            print(month)

sorted(days.values())
print(days)

m=input("월 입력:")
for month, days_in_month in days.items():
    if month[:3].lower() ==m.lower():
        print(f"{month}의 일 수는 {days_in_month}일입니다.")


#연습문제 9

d = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
     {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
     {'name':'Princess', 'phone':'555-3141', 'email':''},
     {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]


print("전화번호가 8로 끝나는 사용자 이름:")
for user in d:
     if user['phone'].endswith('8'):
         print(user['name'])

print("이메일이 없는 사용자 이름:")
for user in d:
     if not user['email']:
         print(user['name'])

name = input("사용자 이름을 입력하세요: ")
for user in d:
    if user['name'] == name:
        print(f"{name}의 전화번호: {user.get('phone', '정보 없음')}")
        print(f"{name}의 이메일: {user.get('email', '정보 없음')}")
    else:
        print("이름이 없습니다.")


#연습문제 10
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        print(self.name)
    
    def getAge(self):
        print(self.age)

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID
    
    def getID(self):
        return self.employeeID

def parse_string_to_dict(string, delimiter1='&', delimiter2='='):
    result_dict = {}
    pairs = string.split(delimiter1)
    for pair in pairs:
        key, value = pair.split(delimiter2)
        result_dict[key] = value
    return result_dict

data_string = 'led=on&motor=off&switch=off'
data_dict = parse_string_to_dict(data_string)
print(data_dict)

employee = Employee("IoT", 65, 2018)
print("이름:", employee.name)
print("나이:", employee.age)
print("ID:", employee.getID())
