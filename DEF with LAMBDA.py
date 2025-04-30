abc_efg=24
ABC_EFG=9.76
print(abc_efg+ABC_EFG)
print(abc_efg,type(abc_efg),ABC_EFG,type(ABC_EFG))

d=20
qwe=3.900
w=2+10j
print(d+qwe)
print('o',d)
print(67//d*qwe+d)
print(id(w),w,type(w))
print(w,type(w))
a=[-3,-2,-1,0]
b=[-3,-2,-1,0,1,2,3,]
print(a+b)
print(a,type(b),b,type(a))
print(a,type(a),b,type(b))
print(b,type(a),a,type(b))
nz=''' 
      %s support the team of new zealand
      
      '''
print(nz% ('''new zealanders'''))
print(nz,type(nz))
print(len('''new zealand'''))
print('''new'''[2])

t=('qwerty',23,56+4j)
print(t)
print(56+4j,type(56+4j))
print('qwerty',type('qwerty'))
print('q',27*23)
print(56+4j in t)
print('qwerty' in t)
print('qwerty' not in t)
print(23/56+4j)
print(23-56+4j)
q=['kane williamson',22,45+8j]
w=['virat kohli',32,4+4j]
print(q)
print(w)
print(w[0])
print(len('kane williamson'))
print('kane willison'[5:14])
name='pratham'
last_name=('patel')
age=21
print(name,last_name,age)
List1=[1,2,3,4,5,6,7,8,9,10]
List1[6]=36,50
print(List1)

fruit_lists=['apple','pineapple','watermelon','kiwi']
# add one item in fruit_lists
fruit_lists.append('coconut')
print(fruit_lists)
# replace the fruit in fruit_lists
fruit_lists[3]="orange"
print(fruit_lists)
print(min('apple'))
print(max('apple'))
print(len(fruit_lists))

num_lists=[10,100,1000,1020,2040,3050,6660]
num_lists[2]=500
print(num_lists)
print(max(num_lists))
a=200
b=300
c=400
print(a+max(num_lists))
print(a+c/b*max(num_lists))
print(min(num_lists))
print(a%c*b/a-min(num_lists))
print(max(a,b,c))

cricket_lists=['bat','pads','balls','bags','helmets']
cricket_lists.append('gloves')
print(cricket_lists)
cricket_lists[2]='football'
print(cricket_lists)
print((cricket_lists))

instagram_lists=['ronaldo','virat kohli','selena gomez']
print(max(instagram_lists))
print(len(instagram_lists))
print('ronaldo'[0])
print('ronaldo'[1:4])
print('ronaldo'[5:8])

name="virat kohli"
ms='Ms Dhoni'
print(name)
print(len(name))
print(len("virat"))
print(len("kohli"))
print(name[0])
print(name[0:4])
print(name[6:9])
print(max('virat'))
print(min('virat'))
print(name+" "+ms)


v="virat kohli"
print(max(v))
print(v[0:5])
print(len('kohli'))
print('K'in 'kohli')
print('v' not in  'virat')
print(v[2:5])
print(v[0::4])
print(v[::-2])

star_lists=["ms dhoni","virat kohli","saniya mirza","babar azam","lionel messi"]
print(len(star_lists))
print(max(star_lists))
print(min(star_lists))
star_lists[2]='ronaldo'
print(star_lists)
star_lists.append('micheal jordan')
print(star_lists)

nba_lists=["lebron james","micheal jordan","larry page","steph curry","dwayne smith"]
print(len(nba_lists))
print("lebron james"[0:6])
print('lebron james'[7:10])
nba_lists.append('kyle kuzma')
print(nba_lists)
print('kyle kuzma'[1:3])
print(id('kyle'))
print(id('kuzma'))
print(id('kyle kuzma'))


a=23.45
b=25
c=100
d=56+7j
print(a+b)
print('a',67)
print(a<b)
print(b<a)
print(type(a))
print(type(b))
print(a+b)
print(a/c+d*b)
print(a,type(a),b,type(b),c,type(c),d,type(d))
print(b//c+d-a*a)
print(c<b or c<a)
print(c&b)
print(b|c)
print(b^c)
print(bin(b^c))
print(id(c^b))
print(a//b+c*d)
print(type(d))

a=23
b=45
c=50
d=60
print(a<c and b<d)
print(a+c//d-b*a)
print(a==b or c!=d)
print(a+40,c-30,b//20,d**3)
print(a==b or b!=d or c==a)

a=24
b=50
c=100
d=75
print(a+b//c*d-a+b*d)
print(a<b and a>c and b<c and b<d or d<a or a>d)
print(a==b,c!=d,b>=d)
print(a+100,b-100)
print(id(a),id(b),id(c),id(d))
print(a,type(a))
print(a*2)
print(b//a)
print(a&b)
print(b|c,bin(b|c))
print(75+ b)
print(a==b,a!=b)
print(b,type(a),c,type(d),d,type(a),a,type(c))
print(a^b,c%b,a|d,d%b)
print(a//b+c-d/a*d//45+4j)

a=-5,-4,-3,-2,-1
b=0,1,2,3,4,5
c=a+b
print(c)
print(a<b and a>b)
print(a<b or a>b)
print(0,1,2,3,4,5 not in a)

o="%s out of the t20 world cup"
print(o%"new zealand team")
print(o[::2])
print(o[-1::-5])
print('new zealand'[::-1])
print(o[6:12])
print('new zealand'[0:3].upper())
print('new zealand',type('new zealand'))
print('s' in 'new zealand')
print('n'not in 'new zealand')

u=1,2,3
a=-5,-4,-3
print(u is a)
print(-5 in a)


a=90
b=78
c=45
d=34
print(a>c or b<d)
print(a//b+c**d%a+c)
print(a&b,bin(a|b))
print(a|b,b^c,c&d,d|a)
print(a==b and b!=c and c==d and d!=a)
print(a==b or b!=c or c==d or d!=a)
print(a is b)
print(id(a),id(b),id(c),id(d))
print(type(a),type(c))
print(bin(b),bin(d))
e=b%a+c//d+45
print(e)

d="%s development"
print(d%("ANDROID"))
print(d[6])
print("android"[0:3])
print("android"[-1::-2])
print("android"[::4])
print(type("android"))
print(id("android"))

w="web"
s="site"
print(w+s)
print(w[0:3])
print(s[0:3])
print('w',34)
print(w,45)

p=[23,45,1,00,54,90,100,50500]
p[3]=500
print(len(p))
print(p)
print(max(p))
print(min(p))

k="kane williamson"
m="ms dhoni"
s=7
print(k[0:3],m[3])
print(bin(s))

a=99
print(a%3)
a="apple"
b=2
print('apple''b'" "*3)


p="pratham"
print(p[1:4:6])
print(p[1:5])
print(p[-1::-5])
print(type(p))

shopping_lists=["clothes","toys","foods","electronics","grocery"]
shopping_lists[4]='croma'
print(shopping_lists)
print(len(shopping_lists))
print(shopping_lists[0:2])
print(max(shopping_lists))
print(min(shopping_lists))
shopping_lists[2]="bikes"
shopping_lists.append("drinks")
print(shopping_lists)
print(type(shopping_lists))
shopping_lists[1]="cheese"
print(shopping_lists)
del shopping_lists[2]
print(shopping_lists)


star_list=["andrew garfield","brad pitt","emma stone","ryan gosling"]
print(len(star_list))
print(max(star_list))
print(min(star_list))
star_list.append("tom hardy")
star_list[1]="tom holland"
print(star_list)
del star_list[1:3]
print(star_list)

w="%s is the warzone in the middle east regions"
print(w% "syria")

bucket_lists=["toys","video games","graphic card","games","computer"]
print(len(bucket_lists))
print(max(bucket_lists))
print(min(bucket_lists))
bucket_lists.append("cars")
print(bucket_lists)
print("graphic cards".upper())
bucket_lists[3]="GAMES"
print(bucket_lists)

a=87+4j
b=45.98
c=500
print(a+c//b)
print(a*b)
print(c%b)
print(c<b)
print(type(c))
print(type(b))
print(type(a))

a=-5,-4,-3,-2,-1
b=0,1,2,3,4,5
c=a+b
print(c)
print(c[0:4])

A_list=["ronaldo","virat kohli","roger federe","ms dhoni"]
A_list[2]="Elon Musk"
print(A_list)
A_list.append("Dj Snake")
print(A_list)
print(len(A_list))
print(max(A_list))
print(min(A_list))
print(A_list[0:5])
B_list=["Selena gomez","ludacris","The Rock","ronaldo"]
B_list.append("Vin Diesel")
print(B_list)
print(len(B_list))
print(max(B_list))
print(min(B_list))
print(B_list[0:4])
c_list=A_list+B_list
print(c_list)
c_list[3]="Lebron James"
print(c_list)
print("Lebron James".upper())
c_list.append("Lionel Messi")
print(c_list)
print("ronaldo".upper(),"Elon Musk".upper(),"lionel messi".upper())
print("ronaldo"[0:3])
print("lionel messi"[3:6])
print("liomel messi" in B_list)
print("ronalod"not in c_list)
print("roanldo"== B_list)


print("code yug")
print("code yug"[4:3:2])
print("code yug"[:-4:-1])
print("code yug"[-1:-5:-3])
print("code yug"[0:0])

u_lists=[-3,-2,-1,0]
a_lists=[1,2,3,4]
b_lists=u_lists+a_lists
print(u_lists+a_lists)
u_lists[2]=8
print(u_lists)
print(len(b_lists))
print(max(b_lists))
print(min(b_lists))
print(2 in b_lists)
print(-3 not in c_list)
print(-20 in b_lists)


print("my name is pratham.",end=" ")
print("patel")
print("virat\nwilliamson")
print("lebron\\james")
print("virat","kohli","steve","smith.", sep="-")
print("my","name","is",sep="_",end="*")
print("pratham","patel.",sep="_",end="*")

#print("kane.",end=" ")
#print("williamson")
#print("viv\nrichards")
#print("pratham","patel","is","going","to","trip",sep="-")
#print("shah","rukh","khan","released","his","movie","pathan",sep="^")
#print("cyber","security",sep="</>")
#print("call","of","duty","modern","warfare",sep=":")
#print("0","1","2","3","4","5","6","7","8","9","10",sep="*")
#print("a","b","c",sep="#")
#print("1","2","3",sep="/",end="+")
#print("a","b","c",sep="/",end="+")
#print("/18")
#print("c","o","m","p","u","t","e","r",sep="[",end="*")
#print("10","20","30","40","50","60","70","80","90",sep="]",end="*")



a_list=[4,8,12,16]
a_list[1:4]=[20,24,28]
print(a_list)

sample_list=[10,20,30,40,50]
print(sample_list[-2])

s_list=[10,20,30,40,50,]
print(sample_list[-4:-1])

#numbers=[0,1,2,3,4,5,6,7,8,9]
#subset1=numbers[2:9]


#u=int(input("Enter the value: "))
#a=int(input("Enter the value: "))
#print(u+a)
#print("Sum:",sum)

#abc=int(input("Enter the value: "))
#efg=int(input("Enter the value: "))
#product=abc*efg
#print("Product:", product)


p="my {} is {}".format("name","Pratham.")
print(p)

w="welcome {a} to {b}".format(a=50,b=10)
print(w)
print(bool(50 in b),bool(10 in a))
print(50 in a,10 in b)

i=" %s is %d years old."
print(i %("pratham",21))

a=chr(67)
print(a)
b=ord('q')
print(b)


p=[2,5,10,100,900,6,7,8,9,3,1,0]
print(sorted(p))
print(p.reverse())

aw=[3,4,1,0,9,56,8,45,29,89,56,783,5839,9500,20058498594940304]
q=sorted(aw)
print(q)

# i="20.5"
# print(int(i))

v=7
if v%2==0:
    print("even")
else:
    print("odd")
t="programming"
print("gram" in t)
print(list(t))

def greet():
    return "high"
print(greet())

print(f"the life of %r"%"pratham")
arr=[1,3,5,7]
r=0
for l in arr:
    r+=1
    d=r
    len(arr)
    print(d)
print()
c=True+2
print(c)
cc=False+2
print(cc)
print(bin(False))
print(bin(True))
print(bin(5))
l=8
print(l//3)

f=[1,2,"none",45,"none",212]
pref=[]
for i in f:
    if i is not "none":
        pref.append(i)
else:
    pref.append(0)
    print(pref)

r=(0.1,0.2,0.3,(1,2,3,(10,20,30)))
# for k in r[3][0:2]:
#     print(k)
if 1 in r[3]:
    print('pass')
else:
    print("fail")

g=[0.1,0.2,0.3,[1,2,3,[10,20,30]]]
if 30 in g[3][3]:
    print("true")
else:print("false")
print()
if g[1]<g[3][3][1]:
    print("pass".capitalize())
else:print("fail".capitalize())
print()
if g[3][3][0]<g[3][1]:
    print("pass".upper())
elif g[3][3][0]>=g[1]:
    print("middle".upper())
    print(f"{g[3][3][0]}>={g[1]}")
else:print("fail".upper())

j=lambda a,b:a if(a>b)else b
print(max(5,10))
g=lambda c,d:c if(c<d)else c
print(max(10,20))

a=[[2,3,4],[1,2,3,45,3],[3,9,1,13]]
for l in a[1]+a[2]:
    print(l)

# c=int(input("columns: "))
# r=int(input("rows: "))
# for u in range(c):
#     for l in range(r):
#         print(,end=" ")
#         print(" ")

# d=int(input("c: ")) $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# f=int(input("g: "))
# for l in range(d):
#     for t in range(l):
#      print(l*t,end=" ")

##  THE BREAK STATEMENT ####
print("the break statement")
for l in range(1,6):
    if l==3:
        print("inside the loop.",l)
        print("outside the loop")
## CONTINUE STATEMENT ###
print("\nThe continue instruction:")
for k in range(1,6):
    if k==3:
        continue
print("Inside the loop.",k)
print("Outside the loop.")



for i in range(0, 11):
    if i % 2 != 0:
        print(i)

z = 0
y = 10
x = y < z and z > y or y < z and z < y

my_list =  [x * x for x in range(5)]


def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(my_list))

x = 1
y = 2
x, y, z = x, x, y
z, y, x = x, y, z

print(x, y, z)

k=[[1,3,5],[2,4,6]]
for i in k[0]:
    print(i*2)

print(1%11)
print(11%1)


### prime number ###
# r=int(input("r: "))
# for k in range(2,r):
#     if r%k==0:
#         print("not prime")
#     else:
#         print("it is prime")

# y=13
# if y==1:
#     for j in range(2,y):
#         if y%j==0:
#             print("it is prime")
#         else:
#             print("it is not prime")

# v=[1,2,3,4,5,6,7,8,9,10,11]
# if v==1:
#     print("it is not prime number")
# if v>1:
#     for t in range(2,v):
#         if v%t==0:
#             print("it is not a prime number")
#             break
#     else:
#          print("it is a prime number")
f=5
for k in range(2,f):
    if f%k==0:
        print("true".upper())
        break
    else:
        print("false".upper())
def c(a):
    return (4/3)*(3.14)*(a**3)
print(c(2))

def cheque(num,low,high):
    if num in range(low,high+1):
        print("{} is in the range between {} and {}".format(num,low,high))
    else:
        print("the number is outside the range.".upper())
cheque(15,11,20)

def g(n,l,h):
    return n in range(l-1,h)
print(g(10,5,15))

def g(t):
    s=[]
    for u in t:
      if u not in s:
            s.append(u)
    return s
# print(g([1,1,1,1,2,2,3,3,3,3,4,5]))
print(g([10,10,10,10,22,22,33,33,33,33,33,54,50]))

def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

def op(hj):
    total=1
    for j in hj:
        total*=j
    return total
print(op([1,2,3,-4]))

# class Glasses: ####################################     P R O B L E M    ###########
#     pass
# class Shader:
#     def printShadeIndex(self):
#         print("HIGH")
# class Sunglasses(Glasses,Shader):
#     pass
# obj=Sunglasses
# obj.printShadeIndex()
# print(obj.Sunglasses)
# print(obj.printShadeIndex)

class MemoryDevice:
    def printPhysicalSize(self):
        print("medium")
class SDCard(MemoryDevice):
    def printPhysicalSize(self):
        print("small")
sdCard=SDCard()
sdCard.printPhysicalSize()

print(2+3*4)
print(f"{2} + {3} =={2+3}")
print(f"{3}*{4}=={3*4}")
print()
print(4-3)
print(f"{4}*{3}=={4*3}")
print(f"{4}*{3}-{3}=={4*3-3}")

nc=5
nr=4
for r in range(nc):
    for t in range(nr):
       print(r*t,end=" ")
    print(":")

fruit="7"
fru=fruit+"0"
eggs=int(fru)+3
print(float(eggs))

a=9/9.9
b=9*9.9
print(a//b)

def test(x,lst=None):
    if lst is None:
        lst=[]
    lst.append(x)
    return lst
print(test(1))
print(test(2))
print(test(2,[10,20]))
print(test(4))

def find_hcf(x,y):
    while(y):
        x,y=y,x%y
    return x
a,b=2,3
hcf=find_hcf(a,b)
lcm=(a*b)//hcf
print(f"the HCF of {a} and {b} is {hcf}")
print(f"the lcm of {a} and {b} is {lcm}")

a=[1,2,3]
b=a.copy()
a+=[4,5]
print(a)
print(b)
print(a,b)

o=[10,20,30]
p=o
p.append(40)
print(o)
print(p)

a=5
b=-a
c=~a
print(a,b,c)

def rto(a,*b,n):
    return a+b[0]*n
print(rto(10,20,30,40,50,n=10))

def mini(a,w,i):
    return a-w-i
print(mini(10,20,90))
print(mini(-0.1,-0.5,-0.4))
print(mini(-10,-9,-0.4))
# print(max(mini(10,-10,-0.1)))

print(float("-10.94"))
print(int("98"))
# print(int("90.111"))
print(int(90.232))

def coal(x):
    for t in str(x).capitalize().split():
        print(t)
kaol=["coal","gold","mines","silver","diamond"]
print(coal(kaol))

# def mines(g):#############      JOL JAAAL PROBLEM    ######
#     print(mines(g))
    # print(type(mines(g)))
        # print(str(mines(gold)).capitalize())
# gold=["one","two","three","four"]
# mines(gold)

# def trucks(t):              #############      JOL JAAAL PROBLEM    ######
#     return trucks(q)
# q=["sports","books","games"]
# print(trucks(q))

def mice(x):
    for u in x:
        if u%2==0:
            print(u)
f=[90,28,94,2,48,98,78,94,8,2,74,84,74,8,74,3]
mice(f)

def com(c):
    return "tata".join(c)
print(com("motors\n"),print(com("ev\n"),print("services\n"),print(com("play\n"))))

def ser(app="company"):
    print(app+" is a food delivery service app.")
ser("zomato".capitalize())
ser("swiggy".capitalize())
ser("uber eats".capitalize())

def h(c,/):
    print(c)
h(3)
print()
# print("i want {chocolates[2]}".format(chocolates="m&m","hersheys","bounty"))  JOL JAAL PROBLEM
# print("i want {choco[0]}".format(choco="hershey","bounty"))

# print("i have a {toys}".format(toys="cars"))
# print("i have a {games}".format(games="racing",))

def car(*bonus):
    x=2
    for k in bonus:
        x*=k
        print(x)
car(2,4)
# car(1,3)
car(6,8)
car(8,10)

s={c:c**2
for c in range(3)}
print(s)
print(type(s))
print(s.values())
print()

f={l:l**2
for l in range(5)}
print(f)
print(f.keys())
print(f.values())
print()

def chap(**mibas):
    print(mibas)
    print(type(mibas))
chap(s="sports",m="movies",g="games")

def card(*i):
    print(i)
    print(type(i))
# j("fortnite","pubg","warzone")
card("laptop","mobile","switch")

g={pic:pic*2
for pic in range(5)}
print(g)
# print(g[:])
# print(p)
# for p in range(5):
#     print(p)

## HOW TO SORTED TWO LISTS ##
# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next
# class answer:
#     def merge(selfself,list1:optional[ListNode],list2:optional[ListNode]):

# def new(land):
#     return land[4].capitalize() + land[-4:0].upper()
# d=lambda land[0:4].upper() + land[-4:0].upper()
# print(d)

#a=3
#b=2
#a*=b
#b*=a
#print(b)

g=[1,2,3,4,5000]
print(g[0]+g[2])
g.insert(1,100)
print(g)
g.index(4)
print(g.index(5000))
l=[]
d={"p":"pratham",
   "o":"om",
   "r":"rushit",
   "m":"mann"}
l.append(d)
print(l)
print(type(l))
print(g.append(l))
print(g.append(d))
g.append(100)
print(g)

h=range(1,10,2)
for f,d in enumerate(h):
    print(f,d)
dog=range(11,20)
cat=range(10,15)
# for k,g,f in enumerate(zip(dog,cat)):
#     print(k,g,f)
for j,l in enumerate(zip(dog,cat)):
    print(j,l)
for s,i in enumerate(zip(dog,cat)):
    print(s,i)

bell=range(1,5)
ball=range(5,10)
for g,m in enumerate(zip(bell,ball)):
    print(f"{g}*{m}=={g*m}")
for v,m in enumerate(bell):
    print(v,m)
# d=[1,2,3,4,5,
#    [10,20,30,40,50,
#     [100,200,300,400]]]

def haveli(a,b,c=10,d=3):
    return a+b-c/d
# print(a+b+c+d)
# haveli(100,200)
print(haveli(100,200))

def bhoot(a,b,c=10,d=100):
    print(a+b+c+d)
    print(chr(a))
bhoot(100,200)

j=[]
def gram(n):
    for k in n:
        j.append(k)
        if k not in j:
         print(k)
c=[1,2,3,24,2,98,9,42,82,42]
gram(c)

def cinema(movies):
    for i in movies:
        print(sorted(str(i).upper()))
        print(i.count("a"))
    for t in movies:
        print(t)
ticket=["meta","whatsapp","facebook","twiiter"]
cinema(ticket)

f=[]
def usha(bajaj):
    for b in bajaj:
        f.append(bajaj.keys())
        # print()
        f.append(bajaj.values())
        # print()
        print(f"i want items in append {f.append(bajaj.items())}")
        # print()
        print(f)
        # print()
d={"r":"rushit",
   "m":"mann",
   "j":"jeet"}
usha(d)

d=[]
# def sports(players):
    # for s in players:
    #     d.append(players.values())
    #     print(d)
    # for sd in players:
    #     d.append(players[5])
# g={1:"one",
#    2:"two",
#    3:"three",
#    4:"four",
#    5:"five"}
# sports(g)

c=[]
def hell(heaven):
    for u in heaven:
        c.append(heaven["s"].upper().split()+heaven["b"].capitalize().split())
        print(c)
azure={"s":"sports",
       "c":"cars",
       "t":"trucks",
       "b":"bikes"}
hell(azure)

f=[80,13,89,324]
print(str(f).split())

def force(friction):
    for kinetic in friction["a"].upper():
        print(list(kinetic))
    for magnetic in friction.values():
        print(sorted(str(magnetic).upper()))
        print()
        # print(reversed(magnetic))
c={"a":"america",
   "b":"belgium",
   "c":"cuba",
   "d":"dubai"}
force(c)

f=100000
print(f"the decimal stays away from me.{f:.>100}")
print(f"the float stays away from me.{f:/^100} and {f:\^100}")

for j in range(5):
    for k in range(j):
        print(j*k,end=" ")
    print()

for a in range(3):
    for t in range(4):
        print(a*t,end=" ")
    print()

y=90
if y<100 or y>40:
    print("the")
else:print("that")
h=40
if y<100 or h>50:
    print("true")
else:
    print("no")
if y<120 and h>50:
    print("yes")
else:print("no")

y={"you":"youtube",
   "true":"truecaller",
   "app":"whatsapp",
   "goo":"google"}
for k in str(y.keys()).upper():
    print(list(k))
for g in str(y.keys()).upper():
    print(set(y))
y["facebook"]="mark"
print(y)
k="kaggle"
g="google"
# k.find("g")
print(k.find("a"))
print(k.join("google"))
print(k.partition("g"))
print(list(g).__mul__(3))
print(list(g).__mul__(5))
por=[90,242]
print(por.__hash__)
print(por.__contains__(90))

number=[1,2,3,4,5]
for k in number:
    print(k.as_integer_ratio())
for n in number:
    print(n.numerator.denominator)
for x in number[0:2]:
    print(x,"is numbers and integers")

bills=["electricity","water","tax","petrol"]
for j in bills:
    print(list(j).__mul__(3))
for n in bills:
    print(list(str(n).split()))
for z in bills:
    print(str(z).partition("t"))
c="i am a python"
for k in c.split():
    if len(k):
        print(k[-1])
for n in c.split():
    if len(k):
        print(k[-1])

class answer(object):
    def land(self,s):
        words=s.split()
        if words:
            return len(words[-1])
        else:return 0
ans=answer()
s="my name is python"
result=ans.land(s)
print(result)

f="fly me to the moon"
for k in f.split():
    if len(k):
        print(k[-1])
    else:print(0)
for j in f.split():
    if len(k[-1]):
        print(len(k))
    else:print(0)

a="art is craft"
for u in a.split():
    if a:
        print(len(a[1]))
    else:print("no")

m="man sits on chair"
for j in m.split():
    if len(j):
        print(j[-1].upper())
    else:print("no")
for d in m.split():
    if len(d[-1]):
        print(len(d))
    else:print("c")

n="mr puff bakes puff"
for j in n.split():
    if len(j[-1]):
        print(len(j))
    else:print("g")
for y in n.rpartition("f"):
    if y:
        print(y)
for l in n.rsplit("f"):
    print(l)

c="santa comes on christmas"
for l in c.partition("c").__mul__(2):
    print(l)
# for x in c.replace("comes","goes"):
#     print("hi")
for t in c:
    print(c.replace("christmas","diwali"))

i="isro and nasa join company"
for h in i:
    print(i.zfill(30))
for u in i.partition("joi"):
    if u.split():
        print(u)
    else:print("v")

def bisleri(water):
    for u in water:
        print(u)
g=[10.23,89322,984343]
bisleri(g)
d=[903,20,24,2]
print(d.__iadd__([90,3]))
print(d.__imul__(8))
# print(d.__gt__(2))

print(803.85+597.43)

for u in range(5):
    for k in range(u):
        print("#",end=" ")
    print()

# c=int(input("R: "))
# r=int(input("C: "))
# symbol=input("enter the symbol to use: ")
# for j in range(r):
#     for n in range(c):
#         print(symbol,end=" ")
#     print()

# e={"w":"weekend",
#    "s":"starboy",
#    "b":"blinding lights"
#    }
# while e['w']:
#     if len(e.values())>5:
#         print("true")
#     else:print("false")

# f=[1,2,3,4,5]
# while f<f[2]:

t="tesla"
u=[]
for x in t:
    u.extend("solar")
    print(u)
for c in t:
    u.append(c)
    print(u)

r="rivian"
f=[]
for k in r:
    f.count("i")
    print(f)
rav="rivian"
# rav.count("i")
# print(rav)
print(rav.count("i"))

k=(1,2,3)
f=[]
for y in k:
    f.append(y)
    print(f)

# e={"g":"google","m":"microsoft","i":'ibm'}
# c=()
# o=[]
# for t in e:
#     o.reverse(t)
#     print(o)
    # o.insert("t","tesla")
    # print(o)
    # c.__new__(4)
    # c.__mul__(2)
    # print(c)
f=[c for c in "cisco"]
print(f)
# g=[v for v in range(len(0,5))]
# print(g)
f=[v for v in range(0,5)]
print(f)

e=[g for g in range(0,20) if g%2==0]
print(e)
f=[i for i in range(10) if i//2==0]
print(f)
d=[s for s in range(10) if s%3==2]
print(d)
z=[x for x in range(10) if x+4==0]
print(z)
e=[q for q in range(15) if q%3==0]
print(e)
c=[c for c in range(40) if c%4==0]
print(c)
d=[d for d in range(20) if d//3==0]
print(d)

mu=[k*2 for k in range(5)]
print(mu)
print(f"multiplication of mu:{mu}")
sq=[v**2 for v in range(5)]
print(sq)
print(f"the square of sq is :{sq}")
cub=[r**3 for r in range(5)]
print(cub)
print(f"the cube of cub:{cub}")
d=[0,1,8,27,64]
sq_rt=[p**0.5 for p in d]
print(sq_rt)
print(f"the square_root of sq_rt is :{sq_rt}")

e=["true".upper() if d%2==0 else "false" for d in range(0,10)]
print(e)

e=[]
k=e
for i in [1,3,5]:
    for w in [2,4,6]:
        e.append(i+w)
        print(k)
v=5
c=4
for u in range(v):
    for k in range(c):
        print(u*k,end=" ")
    print()

v=3
c=2
for u in range(v):
    for k in range(c):
        print(u*k,end=" ")
    print()

v=4
c=3
f="#"
for u in range(v):
    for k in range(c):
        print(f,end=" ")
    print()

 # f=[a,n for n in range(5),for a in range(6)]
d=[c+b for c in [10,20,40]for b in [11,13,15]]
print(d)

g=[0,1,2,3,4,5]
f=[10,20,30,40,50]
for t in g:
    for a in f:
       if t%2==0:
           if a%2==0:
               print(t,a)
           else:print("fail")
g = [0, 1, 2, 3, 4, 5]
f = [10, 20, 30, 40, 50]
for t in g:
    for a in f:
        if t % 2 == 0:
            if a%3==0:
                print(t, a)
            else:
                print("fail")
gf=[0,1,2,3,4,5]
fg=[10,20,30,40,50]
for c in gf:
    for s in fg:
       if c%3==0:
           if s%4==0:
               print(c,s)
           else:print("v")
           
t={"c":"canada",
   "t":"toronto",
   "d":"denmark","b":"belgium"}
f=[s for s in t.values()]
print(str(f).upper())
# c=[str(d["c"][0]) for d in f]
# print(c)
o=[d for d in t.values()]
print(o)
i=["apple","samsung","lava","vivo","nokia","blackberry"]
d=[x[0] for x in i]
print(sorted(d))
p=[c[0:3] for c in i]
print(p)
u=["spacex","blue origin","amazon","walmart"]
v=[f[0:3]+" "+f[-3:] for f in u]
print(str(v).upper())
g=[b[0:3] for b in u]
print(g)
e=[w for w in u]
# print(e.count(u.count("a")))
print(u[2].count("a"),u[-1].count("a"))
# print(type(u[2].count("a"),u[-1].count("a"),u[0].count("a")))

# d=[c for c in range(len(0,10))]
# print(d)

# j=[144,256,188,280,556,550,9233]
# f=[]
# for k in j:
#     f.append(pow(j,0.5))
#     print(f)
g={"d":"denmark",
   "b":"belgium",
   "a":"america",
   "c":"canada"}
for ke,va in g.items():
    print(va,ke)
    print(ke)
s=["number","float","integer","value"]
x=[x.split("|") for x in s]
print(x)
d={"a":"apple","b":"ball"}
f={"c":"cat","d":"dell"}
print(d|f)
q=[-1,-3,0,4,-5.24,0,45,3]
c=[d for d in q if d<0]
print(c)
x=[a for a in q if a>0]
print(x)

p=[[0,1,2],
   [3,4,5],[6,7,8
        ]]
g=[c[0] for c in p]
print(g)
x=[[0,1,2],[3,4,5],[6,7,8]]
z=[d[0]**2 for d in x]
print(z)
p=[q[1]+10 for q in x]
print(p)

r=[[1,3,5],[2,4,6],[3,5,7],[6,8,10]]
c=[x[0]*x[2] for x in r]
print(c)

e={"a":"alpha","b":"belt","c":"chikoo","d":"dragon"}
# x=[i for i in e.update({"a":"apple"})]
c=[v for v in e.values()]
print(c)

b=["a","app","d","len","cop"]
l=["asus","macbook","dell","lenovo","copilot"]
t={}
for j,k in zip(b,l):
    t[j]=k
print(t)

def game(a,b):
    print(a+b)
game(10,20)
# def gta(g,t,a):
#     return g**t**a**0.5
# print(gta(100,200,300))

def samp():
    print("hello")
samp()
def rto():
    print("vehicle stops at red light")
rto()

def samp1(name):
    print("skull".upper()+name)
samp1("candy".upper())

def sneakers():
    print("shoes are always called {s}".format(s="sneakers"))
sneakers()

# def num(o,p):
#     return o+p
# num(10,20)
# def xerox(name):
#     return int(name)
# print(xerox("name has been given"))
# c=[d for d in q if d>0  if d<0]
# print(c)

def chec(nu):
    for y in nu:
        if y%2==0:
            print("yes")
        else:print(y)
s=[10,309,48,94,74,7,36,83,34]
chec(s)

def li(comp):
    return [x**2 for x in comp]
s=[1,3,5,7,9]
print(li(s))

def asd(cv):
    print(["pass"if v%4==0 else "fail" for v in cv])
c=[19,18,24,79,2,48,74,975,79,4,53,94975,937,95]
asd(c)

t=[19,18,24,79,2,48,74,975,79,4,53,94975,937,95]
f=["odd"if g%2==0 else g for g in t]
print(f)

def cheque(correct):
    for t in correct:
        if t%4==0:
            return "access"
        else:return "denied"
print(cheque([1,2,3]))
print(cheque([1,3,5]))
print(cheque([2,4,6]))
print(cheque([12,16,28]))

def fun(x):
    return x+2
e=fun
def fun(x):
    return x*3
print(e(5))

def c(f,*args):
    print("first letters:",s)
    for england in args:
        print("next letter:",england)
c("h","e","l","l","o")

def x(z):
    return z*10
print(x(2))

## how to want some indexes [characters] of word from string in a list:-
def v(o):
    for k in o:
        print(k[3])
x=["list","array","tuple","dictionary"]
v(x)
print(

)
def c(x):
    for i in x:
        print(i[2].upper())
d={"a":"america","b":"belgium","c":"canada"}
c(d.values())

def z(i,o,p):
    return i**o//p
print(z(20000,14,5))

s=lambda x:x**2
print(s(12))
r=lambda c:c[0:4]
print(r("manipulation"))
print((lambda j:j**3)(2))

def s(a):
    return lambda q:q*a
q=s(10)
print(q(20))

def t(u,i):
    return lambda k,l:k*u*l*i
s=t(2,3)
d=t(10,20)
print(s(1,3))
print(d(2,4))

def fiji(cu,ba):
    return lambda pa,ri:pa**ri
z=fiji(1,3)
d=fiji(2,5)
print(z(-4,-2))
print(d(-3,-1))

d="print something"
j=lambda d:d[6:].upper()
print(j(d))

def fun(j,k):
    if j>k and j<k:
        return "yes,please"
    else:return "no,thank yu"
x=fun(10,40)
print(x)

def plus(a,b):
    c=a+b
    d=a-b
    e=a//b
    f=a**b
    print(c,e,f,d)
plus(9.8,8.32)

gv=-0.45
def c(lv):
    return lv+gv
print(c(-0.15))

def asd(q,o):
    q=10
    o=84
    x=q/o
    return x
print(asd(10,-9.45))

# def intro(x):
#     x=input("x: ")
#     print(x)
# intro("cars")

def rto(cars,models,cylinders):
    print("vin diesel has:-",cars)
    print("the car model is:-",models)
    print("the car has ",cylinders,"nitro boosters")
rto("dodge".upper(),"charger".upper(),"2")

def laptop(name,type,fans):
    print("the name of laptop is:-",name)
    print("the type of laptop is:-",type)
    print("the laptop has",fans,"fans.")
laptop("asus".upper(),"gaming".upper(),4)

# def rtx(g,t):
#     g=int(input("g: "))
#     t=int(input("t: "))
#     if g>t:
#         print("ooh yeah")
#     else:print("oh shit")
# rtx(10,90)

# "password checker"
# def pass_chq(p):
#     p=str(input("p: "))
#     if p=="cr@m2le_world" or p:
#         print("access".upper())
#     else:print("denied".upper())
# pass_chq("stable")

black=lambda v:v*3
print(black(10))
chec=lambda h,k:"yes"if h>k else "no"
print(chec(9,12))

foo=lambda j:j%4==0
print(foo(25))
daru=lambda age:"permisson_granted"if age>=30 else "permission_denied"
print(daru(10))

# def jerk(age):
#     age=int(input("i: "))
#     c=lambda a:"permission_granted"if a>=30 else "permission_denied"
#     print(c)
# jerk(10)

q=[1,2,3,4,5]
cub=list(map(lambda q:q*3,q))
print(cub)

label=["strings","lists","tuples","dictionaries"]
c=list(map(lambda v:v[0:4],label))
print(c)

t=[-5,-4,-3,-2,-1]
d=list(map(lambda f:f*f,t))
print(d)

q=["keyboard","monitor","units","cards"]
f=tuple(map(lambda c:c[0:3].upper().split(),q))
print(f,type(f))

r={"n":"nadal","r":"roger","j":"novijck","h":"hengry"}
x=list(map(lambda d:d[0:4],r.values()))
print(x)
print(

)
i=(["pandas","numpy","stats"],["ones","twos","threes"],["strings","dictionaries","lists"])
for n in i:
    print(n)
for g,k,l in i:
    print(g[0:4])
    print()

# r=int(input("r: "))
# if r>=100:
#     print("yes")
# else:print("no")
def t(asd):
    for j,k,l in asd:
        print(l[0:3].upper().split())
        print(type(l))
        # print(k.upper().split()+" "+l.upper().split())
    # for f,g,h in asd:
    #     print(f.
g=(["ones","twos","threes"],["sets","reps","chips"],["cars","bikes","planes"])
t(g)

person=("strings",7,"str")
name,legit,ty=person
print(f"name:{name}")
print(f"legit:{legit}")
print(f"ty:{ty}")

o=[("mouse",1),("monitor",27),("keyboard",50)]
for name,nu in o:
    print(f"quality:{name} | quantity:{nu}")

f=(1,2,3,4,5)
fi,s,*t=f
print(f"first:{fi}")
print(f"second:{s}")
print(f"third:{t}")

# def ios(i,*o,s):
#     print(f"i means:{i}")
#     print(f"o means:{o}")
#     print(f"s means:{s}")
# rtp=(1,2,3,4,5,6)
# ios(rtp)

def sqr(lt):
    return lt**2
g=[1,3,5,7,9]
for u in map(sqr,g):
    print(u)
# f=map(lambda s:s**2,g)
# print(f)
def ras(keri):
    if len(keri)%2==0:
        return "even"
    else:return keri[0]
v=["andy","tom","rock"]
print(list(map(ras,v)))

e=[10,90,4977,8734,47,37,35,93]
k=list(filter(lambda g:g%2==0,e))
print(k)
print()

# " how to get last three digits from strings in lists by use lambda function"
r=["arrays","numpys","docks","cars"]
f=list(map(lambda rg:rg[-3::].upper(),r))
print(f)
print()

def ke(c):
    return c+5
s=lambda c:c*2
print(ke(3))
print(

)
def yt(fc):
    t=lambda fc:fc+10
    return t(fc)+10
print(yt(80))
print(

)

#######    "3/2/2025    #####"

e=lambda t:t*2
print(e(5))

def rt(a,b,c):
    return lambda g,h,i:g*h+i
r=rt(10,20,30)
print(r(100,200,300))

def ty(o):
    print(list(filter(lambda i:i%5==0,o)))
f=[10,29,97,784,66,84,55,7,95,79,6,97,57,93,75]
ty(f)
print(

)
y={"b":"bmw","m":"mercendes","p":"pagani","t":"tesla"}
r=list(filter(lambda t:t,y.values()))
print(r)
# g=map(lambda i:i,y.update({"a":"apple"}))
# print(g)
print(

)
i=[98,453,45,24,2,324,23,2,232]
r=list(map(lambda k:k/len(i),i))
print(r)
e=[1,2,3,4,5,6,7,8,9,10]
w=list(map(lambda r:sum(e)/len(e),e))
print(w)
print(

)
# t=(1,2,3,4,5)
# op=list(filter(lambda e:sum(e)/len(e),t))
# ops=list(filter(lambda r:r/len(t),t))
# opsd=list(lambda e:sum(t)/len(t),t)
# print(op)
# print(ops)
# print(opsd)

# f=["sql","pandas","numpy","python","java"]
# d=list(filter(lambda x:x["p"]==0,f))
# print(d)

h="sql pandas numpy python java"
for i in h.split():
    if i[0]=="p":
        print(i)

####    " how to get last alphabet in strings from lists by use filter method" ####
f=["america","china","belgium","spain","bali"]
d=list(filter(lambda k:k[-1]=="a",f))
print(d)
print(

)
# "DOUBT " "how to guess if strings have length but match with s"
d=["tesla","byd","toyota","tata","citrogen"]
s=list(map(lambda w:len(d[1])==len(d[1]),d))
print(s)
print(

)
# e=["tesla","byd","toyota","tata","citrogen"]
# if e==e.index(e[2]):
#     print("yes")
# else:print("no")

# d=["canada","cuba","spain","russia"]
# if d[1]==len(d[1]):
#     print("true")
# else:print("false")

# w=["food","cars","trucks"]
# print(w.index("trucks"))

q=["tesla","byd","toyota","tata","citrogen"]
t=list(filter(lambda g:g.count("a"),q))

###   "how to know how many alphabets in strings in lists and lenght of strings in lists by use map function."  ###
tiles=list(map(lambda g:g.count("a") and len(g),q))
print(t)
print(tiles)
print(

)
w={"a":"apple","m":"macbook","i":"iphone","s":"samsung"}
r=list(map(lambda k:k.count("a"),w.values()))
print(r)
o=list(map(lambda u:u.count("a")and len(w),w.values()))
# p=list(map(lambda u:u.count("a")and len(w.values()),str(w.values())))
print(o)
# print(p)
print(

)
a=["bikes","cars","mountains","tribes"]
wasd=tuple(map(lambda r:r.count("i"),a))
print(wasd)
ios=tuple(map(lambda p:p.count("i")and len(p),a))
print(ios)
print(

)
qw={"s":"squares","r":"rectangle","t":"triangle","c":"circles"}
rt=list(map(lambda ux:ux.count("i")and len(ux),qw.values()))
print(rt)
d=list(filter(lambda ui:ui.count("angle") and len(ui),qw.values()))
print(d)
print(

)

# r=["medis","fortis","zydus",1,2,3,4] ######
# if r<0:
#     print(r)
# else:print("r")

t=[8,975,97,55.5,85,75,779,55,7]
u=set(filter(lambda k:sum(t)/len(t),t))
s=set(map(lambda o:str(t.count(55)),t))
sr=tuple(map(lambda o:str(t.count(55)),t))
# srk=tuple(filter(lambda o:o,t.count(55)))
print(u)
print(s)
print(sr)
# print(srk)
print(

)
q=[90,49,79,3,35,85,97,35,37,57,95,73,9,37,53,9]
t=tuple(filter(lambda g:g%2==0 or g%7==0,q))
print(t)

# def job(a,b,c,d):
#     return lambda d,r,o,y:d+r-o*y//bin(r)
# qw=job(100,200,300,400)
# print(qw(10,20,30,40))

# def qw(i,o):
#     print(lambda r,t:r+t)
# qw(10,20)
def rto(i,o):
    return lambda f,g:f+g
s=rto(10,20)
print(s(90,12))

a=bin(20)
print(a)
print(type(a))
print(

)
#####   "4/2/25"  #####
t=["tesla","taxes","tata","totla","tetris"]
s=sorted(t,key=lambda f:len(f))
print(s)
print(

)
r=[82,84,89,73,8,75,85,45,8,63,3,67,57,36,87]
e=tuple(filter(lambda w:w%2==0 and w%4==0,r))
print(e)
print()
# a=[79,78,97,8,7677,643,736,486,387,48,34]
# t=dict(filter(lambda ww:w%2==0 and ww%8==0,a))
# t=complex(filter(lambda e:e%2==0 and e%8==0,a))
# print(t)

r=[94,97,40,48,94,84,82,8,482,4,98,94,8]
t=tuple(filter(lambda h:h//2 and h//4,r))
print(t)
print()

####  "4/2/25" ####
t=["stairs","bricks","stones","cements","cases"]
f=tuple(map(lambda y:y[1].split() and len(t[1]),t))
# s=set(sorted(t,key=lambda k:t.split() and len(t)))
print(f)
# print(s)
print()

def per(f,g,h):
    return lambda i,o,p:i**o//p
r=per(20000,10,5)
print(r(30000,20,10))

# f=10
# g=20
# v=(list(lambda k,l:bin(k)+hex(l),f,g))
# t=list(lambda x,c:bin(x)+hex(c),f)
# print(v)

r=lambda j,k,l:bin(j)+oct(k)+hex(l)
print(r(100,200,300))
print(type(r))
print()

d=[10,3,8284,28,942,24,84,0.1,0.2,0.3]
c=list(map and filter(lambda j:j>=50,d))
print(c)
b=tuple(filter(lambda x:x%4==0,d))
print(b)
print()

# c=([1,3,5],[2,4,6],[7,9,11],[8,10,12])
# for t in enumerate(c[0]):
#     print(f"{enumerate(c)}:----{t}")
# for t,c,v,b in enumerate(c):
#     print(f"{enumerate(c)}:---{c}")

e=[(1,2,3),(4,5,6),(7,8,9)]
for k,n in enumerate(e[0]):
    print(f"{k}:---{n}")
print()
x=([0.1,0.2,0.3],[1.1,1.2,1.3],[2.1,2.2,2.3])
for i,m in enumerate(x):
    print(f"{i:.<10}:{m:}")
    for k,j in enumerate(x[0]):
        print(f"{k:|<10}  {n:.>20}")
    # print(f"{i:.<10f} and  {m:.>10f}")

####   "8/2/25"  ####
e=[[[[[10,20,30,40,],[1.1,1.2,1.3,1.4],[2,4,6,8,10]]]]]
print(e[0][0][0][0])
print(e[0][0][0][1])
print(e[0][0][0][2])




































