# class dog():
#     def __init__(self,breed):
#         self.breed=breed
# my_dog=(breed="pug")
# print(my_dog.breed)

# class   @property
# def (self):
#     return

class Person:
    def __init__(self,name,age):
        self.name=name.upper()
        self.age=age
        def __getName(self):
            return self.name.upper()
        def getAge(self):
            return self.age

# p=Person("pratham",23)
p1=Person("pratham",23)
print(p1.name)
print(p1.age)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # def __getName(self):
        #     return self.name
        # def getAge(self):
        #     return self.age
p1=Person("pratham",23)
print(len(p1.name))

class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed.upper()
d=Dog("bruno","labradog")
print(d.breed)
print(d.name)
print(sorted(d.breed))

class Car:
    def __init__(self,name,model,plate):
        self.name=name
        self.model=model
        # self.plate=plate
c=Car("toyota".title(),"corolla",9242-2423-3423)
print(c.name)
# print(c.plate)
print(c.model)

class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
ca=Car("morris garages","gloster")
print(ca.model)
print(sorted(ca.model))

class Card:
    def __init__(self,name,company,num):
        self.name=name
        self.name=f"the company : {name.upper()} length {len(name)}"
        self.company=company
        self.company=f"the name : {company.upper()} and lenght {len(company)}"
        self.num=num
r=Card("nvidia","graphic card",3060)
print(r.name)
print(r.company)
print(r.num)

class Sum_two_num:
    def __init__(self,one,two):
        self.one=one
        self.two=two
v=Sum_two_num(10,20)
print(v.one+v.two)

class FIN:
    def __init__(self,one,two,three,four):
        self.one=one
        self.two=two
        self.three=three
        self.four=four
d=FIN(12,0.4,10,50000)
print(d.one+d.three-d.two**d.four)
print(d.one-d.two**d.three//d.four)
print(d.four%d.three**d.two+d.one)
print(id(d.one+d.two+d.three+d.four))
# print(chr(12+0.4+10+50000))

class show:
    def __init__(self,name,type):
        self.name=name.upper()
        self.type=type
g=show("ben 10","teen")
print(g.name)
print(g.type)

class FIND:
    def __init__(self,n,v,nu,val):
        self.n=n
        self.v=v
        self.nu=nu
        self.val=val
h=FIND(10,20,30,40)
print(bin(h.n+h.v+h.nu+h.val))
print(chr(h.n*h.v*h.nu*h.val))
print(oct(h.v*h.n+h.nu-h.val))
print(hex(h.v*h.n+h.nu-h.val))
# print(sum(bin(h)))
# print(sum(chr(h)))

class Classroom:
    def __init__(self,students,type,clss):
        self.students=students
        self.type=type
        self.clss=clss
o=Classroom(50,"wood",5)
print(o.type.upper())
print(o.clss)
print(o.students+10)

class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def __str__(self):
     return f"{self.name}({self.gender})"
po=Person("donald trump",78)
print(po)

class Components:
  def __init__(self,m,f):
    self.m=m
    self.f=f
  def sen(self):
     print(f"{self.m} and {self.f} are components of computers.")
h=Components("motherboard","fan")
h.sen()

# class Sumproduct: ################################3            PROBLEM         ##################################
#     def  __int__(self,m,n):
#         self.m=m
#         self.n=n
    # def n(self):
    #     return f"{self.m*self.n}"
# f=Sumproduct(1,2)
# print(f)

class Compass:
  def __init__(self,name,type):
    self.name=name
    self.type=type
  def combine(self):
      print(f"{self.name.title()} has a {self.type} color compass.")
r=Compass("doremon","red")
r.combine()

# class TV:
#     pass
# obj=TV()
# obj.price=200
# print(self.price)

print("hello world!")

class Man():
    def __init__(head,name,age,height,weight):
        head.name=name
        head.age=age
        head.height=height
        head.weight=weight
a=Man("pratham",23,"183cm","78kg")
print(a.height,a.name,a.age,a.weight)
# print(a.name+a.height+a.age+a.weight)

class Game:
    def __init__(self,name,type,background):
        self.name=name
        self.type=type
        self.background=background
w=Game("fortnite".title(),"comedy\n                   survival","avengers".title())
d=Game("warzone".title(),"action","open-ground")
print(f"type of game: {w.type}")
print(f"type of game: {d.type}".upper())
print(w.background+d.background)
print(w.name.upper()+" "+d.name.upper())

######  METHODS  #####

class Fees:
    def __init__(self,prices,quantity):
        self.prices=prices
        self.quantity=quantity
    def details(self):
        print(f"apples have {self.prices} prices of  {self.quantity} quantity.")
das=Fees(50,10)
das.details()

# class Quantity:
#     def __init__(self,name,lines,weight):
#         self.name=name
#         self.lines=lines
#         self.weight=weight
#     def details(self):
#         print(f"{self.name} have {self.lines}\n"
#               f"{self.weight}")
#         print(self.lines+self.weight)
# guava=Quantity("grapes",10,50)
# print(guava.weight)
# print(guava.lines)

class Quantity:
    def __init__(self,name,lines,weight):
        self.name=name
        self.lines=lines
        self.weight=weight
    def details(self):
        print(f"{self.name} have {self.lines}\n"
              f"              {self.weight} paisa.")
        # print(self.lines+self.weight)
guava=Quantity("grapes",10,50)
# print(guava.weight)
# print(guava.lines)
guava.details()

class Process:
    def __init__(self,start_date,end_date):
        self.start_date=start_date
        self.end_date=end_date
    def system(self):
        return (f"accounting years has started on {self.start_date}\n"
                f"        finished on this {self.end_date}.")
# io=Process(1-4-2024,31-3-2025)
io=Process("1-4-2024","31-3-2025")
# io.system()
print(io.system().upper())

class FORMULAS:
    def __init__(self,addition,sub,expo,divi):
        self.addition=addition
        self.sub=sub
        self.expo=expo
        self.divi=divi
    def Addition(self):
        print(f"the addition of two numbers: {self.addition+self.addition}")
    def subtract(self):
        return f"the subtract of two integers: {self.sub+self.sub}"
    def mu(self):
        print(f"the multiplication of complexes:{self.expo*self.expo}")
        print(f"i want .two decimal of self.expo :{self.expo*self.expo:.2f}".upper())
    def son(self):
        return f"the divison of float numbers: {self.divi//self.divi}"
g=FORMULAS(10,100,3.2,-5)
g.Addition()
print(g.subtract())
g.mu()
print(g.son())


class Name():
    def __init__(self,company,employees):
        self.company=company
        self.employyees=employees
    def daata(self):
        return f"the {self.company} has {self.employyees} staff."
k=Name("tesla",500000)
print(k.daata())

# class staff: #####################     PROBLEM      #############
#     def saras(self):
#         self.name=str(input("Name: "))
#         self.age=int(input("Age: "))
#         self.gender=str(input("Gender: "))
#     def show(self):
#         print("First Name:",self.name)
#         print("AGE: ",self.age)
#         print("gender:",self.gender)
# j=staff()
# jai=saras()
# juice=show()

class fist():
    k=10
    g=0.10
p=fist()
print(p.k+p.g)
print(p.k-p.g)

# class wool:  ########     INPUT FUNCTION IN CLASS   #####
#     g=int(input("n: "))
#     v=complex(input("c: "))
# o=wool()
# print(o.g+o.v)

class test:
    def __init__(self,x):
        self.x=x
        x=10
l=test(100)
print(l.x)

class dog:
    dogs_count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("welcome to this world {}!".format(self.name))
        dog.dogs_count+=1
    def __del__(self):
        print("Goodbye {} :(".format(self.name))
        dog.dogs_count-=1
a=dog("max",1)
print("number of dogs:{}".format(dog.dogs_count))
b=dog("charlie",7)
del a
c=dog("spot",4.5)
print("number of dogs:{}".format(dog.dogs_count))
del b
del c
print("number of dogs:{}".format(dog.dogs_count))

def scope_test():
    def do_local():
        spam="local spam"
    def do_nonlocal():
        nonlocal spam
        spam="nonlocal spam"
    def do_global():
        global spam
        spam="global spam"
    spam="test spam"
    do_local()
    print("after local assignment:",spam)
    do_nonlocal()
    print("after non local assignment:",spam)
    do_global()
    print("after global assignment:",spam)
scope_test()
print("in global scope:",spam)

class student:
    name="jane"
    course="javascript"
net=student()
print(net.name+net.course)
print(net.course[4:]+net.name)

class plus:
    def __init__(self,lee,jet_lee):
        self.lee=lee
        self.jet_lee=jet_lee
f=plus([1,2,3,4,5],[10,20,30,40,50])
print(f.jet_lee[0:3]+f.lee[::-2])

class ios:
    def __init__(self,name,last):
        self.name=name
        self.last=last
    def fox(self):
        return self.name+self.last
u=ios(["jio","airtel","starlink"],["oil","gold","silver"])
print(u.fox())

# class gold:
#     def __init__(self,mark,weight):
#         self.mark=mark.split()
#         self.weight=weight.split()
# trade=gold(["russian","indian","chinese"],["american","european","japanese"])
# print(trade.mark.upper().split()+trade.weight.upper().split())
# print(trade.mark+trade.weight)

# class mark:
#     def __init__(self,one,two):
#         self.one=one
#         self.two=two
#     def  g(self):
#         print(self.one.upper())
        # return self.one.split()+self.two.split()
# r=mark(["gold","silver"],["diamond","bitcoin"])
# print(r.g())

class circle():
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*self.pi
    def get_circumference(self):
        return self.radius*self.pi*2
o=circle(100)
print(o.pi)
print(o.radius)
print(o.area)
print(o.get_circumference())

class test:
    def __init__(self,x):
        self.x=x
        x=10
l=test(100)
print(l.x)

class sys:
    def __init__(self,f):
        self.f=f
        f=4.5
g=sys(90)
print(g.f)

class plus:
    def __init__(self,k,l):
        self.k=k
        self.l=l
        k=1.0
        l=9.0
f=plus(8.9,2.3)
print(f.k**f.l)
print(f.k//f.l)
print(f.k+f.l)

class daigram:
    def __init__(self,di,pi):
        self.di=di
        self.pi=pi
        di=2.3
        pi=1.3
g=daigram(1.2,2.4)
print(g.di*g.pi)
print(g.pi**g.di)

class strike:
    def __init__(self,youtube,facebook):
        self.youtube=youtube
        self.facebook=facebook
        youtube=-12
        facebook=-10
    def fy(self):
        return self.youtube**self.facebook
og=strike(-2,-4)
print(og.fy())
print(id(og.fy()))

class pharm:
    def __init__(self,i,o):
        self.i=i
        self.o=o
        i=20
        o=10
    def compare(self):
        if self.i==self.o:
            print("pass".upper())
        else:print("fail".upper())
f=pharm(0.1,0.2)
print(f.compare())

class pie():
    def __init__(self,gram):
        self.gram=gram
    def kg(self):
        for k in self.gram:
            print(k)
gr=pie([10,20,30,45,32,3])
print(gr.kg())

class counter():
    count=0
    def __init__(self):
        self.count+=1
a=counter()
b=counter()
print(a.count,b.count,counter.count)
print()
# class ui():
#     count=0
#     def __init__(self,j):
#         self.j=j
#     def v(self):
#         return self.count+self.j
# d=ui(10)
# print(d.v())

class ios():
    def __init__(self,i,o,s):
        self.i=i
        self.o=o
        self.s=s
    def war(self):
        for h in self.i:
            print(h)
    def zone(self):
        for t in self.o:
            print(t)
    def telecom(self):
        for r in self.s:
            print(r)
    def keyboard(self):
        return self.i[0]+self.o[-1]+self.s[-4]
f=ios([1,2,3,4,5],[10,20,30,40,50],[100,200,300,400,500])
print(f.war())
print(f.zone())
print(f.telecom())
print(f.keyboard())

class div:
    def __init__(self,v):
        self.v=v
        v=[10,20,30,40,50,23,2,2,32,42]
    def cu(self):
        for j in self.v:
            if j%2==0:
                print(j)
f=div([19,0,3,28,9,4,38,94,2,44,2])
print(f.cu())
print()

# class glass:
#     def __init__(self,m):
#         self.m=m
#         m=[1,90,32,58,9,4,35,37,8,43,53]
#     def asd(self):
        # if self.asd()%2==0:
        #     print(self.asd())
        # if self.m%2==0:
        #     print(self.m)
# m=glass([19,0,32,8,9,24,88,9,42,44,89,42])
# print(m.asd())

class fid:
    def __init__(self,k):
        self.k=k
        k="donald trump is smart guy."
    def h(self):
        for i in self.k.split():
            if len(i)%2==0:
                print(i.upper())
j=fid("vladimir putin is a kgb agent.")
print(j.h())

class glass:
    def __init__(self,sq,cub):
        self.sq=sq
        self.cub=cub
f=glass("half water","half glass")
print(f.sq[0:4])
print(f.cub[5:10])
print(f.sq[0:4]+f.cub[5:10])
print(f.cub[6:8].upper()+f.sq[5:7].upper())

# class sq():
#     def __init__(self,j):
#         self.j=j
#         j=(90,28,9,24,2,23,24)
#     def lo(self):
#         return list(map(lambda g:g%2!=0,self.j))
# f=sq({10,2,0,32,3,8,9,24,22,88,42})
# print(f.j)
# print()
# print(f.lo())

class sq():
    def __init__(self,j):
        self.j=j
        j=(90,28,9,24,2,23,24)
    def lo(self):
        return list(map(lambda g:g%2!=0,self.j))
f=sq({10,2,0,32,3,8,9,24,22,88,42})
print(f.j)
print()
print(f.lo())

f=(90,29,48,4,29,42,8,42,92,42)
d=list(map(lambda v:v%2!=0,f))
print(d)

g=(90,24,8,2,48,28,9,48,4,2,82,3,5,7)
h=list(filter(lambda b:b%2!=0,g))
p=list(filter(lambda s:s%2==0,g))
print(h)
print(p)

class cheque:
    def __init__(self,j):
        self.j=j
        j="NTPC green energy"
    def b(self):
        if "ntpc" in self.j:
            print("pass".upper())
        else:print("fail".upper())
f=cheque("NTPC green energy")
print(f.j)
print(f.b())

class finish:
    def __init__(self,k):
        self.k=k
    def h(self):
        if "adani" in self.k:
            print("true".upper())
        else:print("false".upper())
            # print(self.k)
        # else:print("ports".upper())
d=finish("adani ports")
w=finish("Adani ports")
print(d.k)
print()
print(d.h())
print()
print(w.k)
print()
print(w.h())

class room:
    def __init__(self,jm,kl):
        self.jm=jm
        self.kl=kl
    def rto(self):
        return self.jm==self.kl
p=room(256,257)
o=room(258,258)
print(p.rto())
print()
print(o.rto())

class orient:
    def __init__(self,n):
        self.n=n
    def moj(self):
        return list(filter(lambda g:g%2==0,self.n))
r=orient([1,90,28,9,48,9,44,4,3,4,9,4,39,4,83,84,49,34])
print(r.moj())
print(r.n.count(9))
print()

class dairy:
    def __init__(self,jk,cement):
        self.jk=jk
        self.cement=cement
    def gk(self):
        return chr(self.jk+self.cement*self.jk//self.cement)
    def oz(self):
        return hex(self.jk+self.cement*self.jk//self.cement)
    def og(self):
        return oct(self.jk+self.cement*self.jk//self.cement)
    def fo(self):
        return float(self.jk+self.cement*self.jk//self.cement)
f=dairy(100,100)
print(f.gk())
print(f.oz())
print(f.og())
print(f.fo())
print(f.gk())
print(f.gk()+f.oz()+f.og()+f.gk())
# print(bin(f.gk()+f.oz()+f.og()+f.gk()))

class kai:
    def __init__(self,e,n):
        self.e=e
        self.n=n
    def q(self):
        for u in self.e:
            print(u)
    def r(self):
        for t in self.n:
            print(t)
    def t(self):
        for s,d in zip(self.e,self.n):
            print(f"{s}:{d}")
    def sd(self):
        for a,z in enumerate(zip(self.n[0].upper())):
            print(f"{a}:|:|:{z}")
f=kai([0,1,2,3,4,5],["tata","adani","musk","jeff","tim","gates"])
print(f.t())
print(f.sd())

class game:
    def __init__(self,i):
        self.i=i
    def rti(self):
        return self.i.insert(1,10)
g=game([90,8,8,34,24,2,2,2,2])
print(g.rti())
print(g.i)
print(g.i.insert(1,1000))

d=[10,90,34,99,3449,99]
d.insert(1,100)
print(d)
f=[0.9,0.3,0.8,0.3]
f.append(d)
print(f)

# count=0
# f="figi"
# for j in f:
#     print(f"{count}:{j}")
#     count+=1

class glasses():
    def __init__(self,dock,docker):
        self.dock=dock
        self.docker=docker
    def iti(self):
        print(list(map(lambda j,k: k.upper().split()[0:4] + j.upper().split()[0:7], self.dock, self.docker)))
        # return self.dock[0:5]+self.docker[6:10]
d=glasses(["donald trump"],["european union"])
print(d.iti())

t=["union","set","tuple","dictionary"]
class dockey:
    def __init__(self,t):
        self.t=t
    def wtf(self):
        return list(t[2])
tv=dockey(t)
print(tv.wtf())

war=["america","russia","japan","india","canada"]
zone=["north korea","china","sudan","cuba","sweden"]
class formula:
    def __init__(self,war,zone):
        self.war=war
        self.zone=zone
    def cod(self):
        return set(war[1].upper())
    def pubg(self):
        return set(zone[-1].upper())
    def fort(self):
        for u in enumerate(zip(self.war[1].upper(),self.zone[-1].upper())):
            print(list(u))
black=formula(war,zone)
# print()
print(black.cod())
# print()
print(black.pubg())
# print()
print(black.fort())
print()

f=[90,38,93,8,7,4,2,3,1]
class radi():
    def __init__(self,f):
        self.f=f
    def radar(self):
        print(tuple(sorted(self.f)))
        print(tuple(reversed(self.f)))
        return tuple(reversed(self.f))
        # return set(reversed(self.f))
iop=radi(f)
print(iop.radar())

sd=[100,89,320,200,400,23,1,23,4,78,13,25,27]
class find():
    def __init__(self,sd):
        self.sd=sd
    def doremon(self):
        print(set(filter(lambda risk:risk%2==0,self.sd)))
        return list(map(lambda beta:beta%2==0,self.sd))
w=find(sd)
print(w.sd)
print(w.doremon())

d={1,8,9,12,33,2,4,2,5,6}
fry={1,8,9,23,4,2,132,1}
class make():
    def __init__(self,d,fra):
        self.fry=fry
        self.d=d
    def pan(self):
        print(f"the unity of all numbers of d and fry:{self.d|self.fry}")
    def egg(self):
        print(f"the repeat numbers of d and fry:{self.d & self.fry}")
    def omlet(self):
        print(f"the single numbers of d and fry:{self.d^self.fry}")
r=make(d,fry)
print(r.pan())
print(

)
print(r.egg())
print(

)
print(r.omlet())

# e=("android","ios","set","tuple") #####      APPEND PROBLEM IN CLASS AND OBJECTS   #######
# d={"walmart":{
#     "g":"grocery",
#     "c":"clothes",
#     "d":"drinks",
#     "s":"stationery",
#     "v":"video games"
# }}
# x=[]
# class games():
#     def __init__(self,e,d,x):
#         self.e=e
#         self.d=d
#         self.x=x
#     def ubuntu(self):
        # return x.append(e)
        # return x.append(self.e) $$$$
    # def linux(self):
    #     return x.append(self.d)
    # def micro(self):
    #     return x.append(self.e+self.d)
# h=games(e,d,x)
# print(h.ubuntu())
# print(h.linux())
# print(h.ubuntu())

# creta=("android","ios","set","tuple")   #####      APPEND PROBLEM IN CLASS AND OBJECTS   #######
# swift={
#     "g":"grocery",
#     "c":"clothes",
#     "d":"drinks",
#     "s":"stationery",
#     "v":"video games"
# }
# inox=[]

# class mouse():
#     def __init__(self,creta,swift):
#         self.creta=creta
#         self.swift=swift
#         self.inox=inox
#     def mean(self):
#         print(self.inox.append(self.creta))
#         print(inox.append(creta))
    # def less(self):
    #     print(inox.append(swift))
    # def red(self):
    #     inox.append(creta)
# g=mouse(creta,swift)
# o=mouse(creta,swift)
# print(g.mean())
# print(g.red())


g=("cricket","golf","football","basketball")
c=[]
class jack:
    def __init__(self,g,c):
        self.g=g
        self.c=c
c.append(g[0].upper())
print(c)

class handle():
    def __init__(self,g,c):
        self.g=g
        self.c=c
    def tube(self):
        return list(reversed(self.g))
    def pipe(self):
        return list(reversed(self.g[0].upper()))
    def fill(self):
        return list(sorted(self.g,key=lambda l:l))
water=handle(g,c)
print(water.tube())
print()
print(water.pipe())
print()
print(water.fill())
print()

q=["mouse",'pad',"mice","gloves","desktop"]
ol=("mouse",'pad',"mice","gloves","desktop")
for h in str(q).split():
    print(h[0])
print([word[0:4]for word in str(ol).upper().split()])



k={"king","spade","diamond","queen"}
f=[]
# for d in f:
#     for a in k:
#      print(d.append(a))
f.append(k)
print(sorted(f))

g=["mumbai","banglore","pune","delhi","gurugram"]
s=list(map(lambda t:t.upper().split(),g[0]))
print(s)

class go():
    def __init__(self,g):
        self.g=g
    def sd(self):
        print(list(map(lambda g:g.upper().split(),self.g[-1])))
        # print(tuple(map(lambda v:v.split(),self.g[-4])))
    def a(self):
        print(tuple(map(lambda h:h.split(),self.g[-1])))

f=go(g)
print(f.sd())
# print(type(f.sd()))
print(f.a())
print(type(f.a()))

# o={0.8,0.8,0.4,0.1,.03,0,30,50.45}
# print(set(o))

sport_names=["cricket","football","rubgy","basketball"] ################         PROB    ############
sport_players=["virat kohli","neymar","tom brady","lebron james"] ######       LEM     ######
#
class deck:
    def __init__(self,sport_names,sport_players):
        self.sport_names=sport_names
        self.sport_players=sport_players
    def block(self):
        for t in str(self.sport_names).split():
            print([alpha[0:3]for alpha in str(self.sport_names).upper().split()])
    def cade(self):
        for y in str(self.sport_players).split():
            print([beta[::-2]for beta in str(self.sport_players).upper().split()])
t=deck(sport_names,sport_players)
print(t.block())
print(t.cade())

# f="donald trump"
# for k in f[0:4].upper().split():
#     print(k)
# for u in f[0:3]:
#     print(u.upper()*5)


r=['kohli',"dhoni","dhawan","sharma"]
class dock:
    def __init__(self,r):
        self.r=r
    def radint(self):
        for u in self.r[0][0:3]:
            print(u.upper()*5)
    def raduis(self):
        for j in self.r[1][0:4] and self.r[-1][-3:]:
            print(j.upper()*5)
    def radium(self):
        for l in self.r[1][0:3]+self.r[2][0:3]:
            print(l.upper()*3)
t=dock(r)
print(t.radint())
print()
print(t.raduis())
print()
print(t.radium())
# for t in r[1][0:3]+r[2][0:3]:
    # print(t.upper()*3)

d=[19,8,9,34,89,45,38,89,24,24,9,3,42]
class fin():
    def __init__(self,d):
        self.d=d
    def rock(self):
        print(tuple(filter(lambda k:k%2==0,self.d)))
    def paper(self):
        print(set(filter(lambda d:d%2!=0,self.d)))
    def scissor(self):
        print(set(filter(lambda c:c%3==0 and c%3!=0,self.d)))
        print(set(filter(lambda a:a%3==0 or a%3!=0,self.d)))
bata=fin(d)
print(bata.rock())
print()
print(bata.paper())
print()
print(bata.scissor())

f=[90,89,453,{90,3,23,23,2},{"i"
                             :"integrated",
                             "o":"operating",
                             "s":"system"},(-9,28,8,4)]
class pubg:
    def __init__(self,f):
        self.f=f
    def rtu(self):
        for t in f[4].values():
            print(t.upper())
    def sd(self):
        for j in f[4]["o"]:
            print(j.upper().split())
d=pubg(f)
print(d.rtu())
print()
print(d.sd())

s={"sports":{"c":"cricket",
             "f":"football",
             "b":"basketball",
             "r":"rubgy"}}
for i in s["sports"].values():
    print(i)
class iron:
    def __init__(self,s):
        self.s=s
    def license(self):
        for r in enumerate(s["sports"]["f"].upper()):
            print(r)
    def paper(self):
        for w in enumerate(s["sports"]["c"].upper()):
            print(w)
    def sign(self):
        for y in enumerate(s["sports"]["c"]):
            print(y)
c=iron(s)
print(c.license())
print()
print(c.paper())
print()
print(c.sign())
print()

g=0
d={"d":"donald",
   "t":"trump",
   "c":"china",
   "i":"india",
   "a":"angular"}
# for k,l in enumerate["d"]["t"]):
#     print(f"{g}:{k}:{l}")
#     g+=1
for u in zip(d["d"],["a"]):
    print(f"{g}:{u}")
    g+=1

class scooter:
    def __init__(self,brand:str,power_rating:str)->None:
        self.brand=brand
        self.power_rating=power_rating

eng:scooter=scooter("bajaj".title(),"b+".upper())
print(eng)
print()
print(eng.brand)
print(eng.power_rating)

fran=scooter=scooter("vespa".title(),"c+".upper())
print(fran)
print(fran.brand)
print(fran.power_rating)

# class bike:                           ###############         JOL JAAAL ( PROBLEM)    ############
#     def __init__(self,brand,speed:int):
#         self.brand=brand
#         self.speed=speed
#         self.turned_on:bool=False
#     def turned_on(self)->None:
#         if self.turned_on:
#             print(f"{self.brand} has increse speed around {self.speed}\nit should be penalty.")
#         else:
#             self.turned_on=True
#             print(f"{self.brand} has decrease speed about.then,\nthere is no penalty.")
#     def turn_off(self)->None:
#         if self.turn_off():
#             print(f"{self.brand} gives average about {self.speed}")
#         else:
#             self.turned_on()
# mug:bike=bike("jawa",120)
# print(mug.turned_on)

s=[0,89,37,8,43,63,7,43]
class cheque:
    def __init__(self,s):
        self.s=s
    def checker(self):
        if s[0]==s[1]:
            print("true")
        else:print("false")
sf:cheque=cheque(s)
sf.checker()

print("{} and {}".format("mario","pokemon"))
f="{1} and {0}"
print(f.format("stumble","guys"))
c="{2} and {0}"
print(c.format("fall","guys","stumble"))

g=[0,89,24,78,97,23,79,8,3,99]
f=(90,8,92,9,7,78,8,47,97,64)
print(len(g))
print(len(f))
class bat():
    def __init__(self,g,f):
        self.g=g
        self.f=f
    def war(self):
        print(list(filter(lambda j:j%2==0,self.g)))
    def zone(self):
        print(list(filter(lambda l:l%3==0,self.f)))
        # return set(filter(lambda c:c%2==0 and c%3==0,self.g,self.f))
r=bat(g,f)
print(r.war())
print()
print(r.zone())

cuba=[90,89,48,79,77,47,83,4,77,23]
fiji=(90,87,84,78,38,97,7,99,37,3)
class build():
    def __init__(self,cuba,fiji):
        self.cuba=cuba
        self.fiji=fiji
    def kill(self):
        return set(map(lambda j,b:j**0.5+b**0.5,cuba[0:5],fiji[0:4]))
    print("i want .two decimal :{w:.2f}".format(w=23.439483943))
    # print(f"i want two decimla:{(map(lambda j,b:j**0.5+b**0.5,cuba[0:5],fiji[0:4])):2.f}")
    # print(f"i want .two decimal:{set(map(lambda j,b:j**0.5+b**0.5,cuba[0:5],fiji[0:4]))}")
wall=build(cuba,fiji)
print(wall.kill())

f={"s":"sports",
   "c":"cricket",
   "f":"football",
   "b":"basketball",
   "r":"rubgy"}
class pencile:
    def __init__(self,f):
        self.f=f
    def scale(self):
        for r in enumerate(self.f.values()):
            print(r)
    # def card(self):
    #     return list(map(lambda f:str(f in self.f.values)))
        # return list(map(lambda c:c in self.f.values.upper().split(),self.f))
axe=pencile(f)
print(axe.scale())
# print(axe.card())

spor={"c":"cricket",
      "f":"football",
      "b":"basketball",
      "r":"rubgy"}
# d=str(map(lambda g:g.upper().split(),spor.values()))# print(d)
class ship():
    def __init__(self,spor):
        self.spor=spor
    def water(self):
        for u in str(self.spor).upper().split():
            print(u)
    def rubber(self):
        for j in spor["c"]:
            print(list(j.upper()))
    def stand(self):
        for r in enumerate(zip(spor["f"].upper(),spor["c"].upper())):
            print(list(r))
spray=ship(str(spor).upper().split())
print(spray.water())
print(spray.rubber())
print(spray.stand())

games={"w":"warzone",
   "f":"fortnite",
   "p":"pubg",
   "b":"battlefield",
   "c":"counter"}

class line:
    def __init__(self,games):
        self.games=games
    def cover(self):
        x = 0
        for u, in games["f"].upper():
            print(f"{x}:{u}")
            x+=1
    def drive(self):
        p=0
        for k in games["c"].upper():
            print(list(f"{p}:{k}"))
            print(tuple(f"{p}:{k}"))
            p-=1
    def drove(self):
        e=chr(250)
        for t in games["p"].upper():
            print(list(f"{e}{t}"))
            e+=chr(70)
            # print(list(k))
    def mouse(self):
        r=-10
        for j in games["b"].upper():
            print(list(f"{r}:{j}"))
            r-=20
    def wired(self):
        q=-5
        for u in games["w"].upper():
            print(set(f"{q}!{u}"))
            q+=4
    def pad(self):
        a=-10
        for c in games["p"].upper():
            print(tuple(f"{a}~{c}"))
            a+=2
h=line(games)
print(h.cover())
print(h.drive())
print()
print(h.mouse())
print()
print(h.wired())
print()
print(h.pad())
# print(h.drove())

# print(-2+2)
d={2,4,6,8,10,12,14,16,18,20}
class flight():
    def __init__(self,d):
        self.d=d
    def eco(self):
        e=-15
        for sd in d:
            print(list(f"{e}/{sd}"))
            e+=2
    def bus(self):
        p=-5
        for w in d:
            print(tuple(f"{p}{w}"))
            p*=2
    def van(self):
        z=-5
        for w in d:
            print(set(f"{z}{w}"))
            z*=2
q=flight(d)
print(q.eco())
print()
# print(q.bus(),print(),print(q.van()))
print(q.bus())
print()
print(q.van())
print()

class boxes():
    def __init__(self,food):
        self.food=food
    def ios(self):
        for u in self.food:
            print(u)
toys=["games","ring","balls","cars"]
h=boxes(toys)
print(h.ios())
print()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(type(p1))
print(p1)

t={"m":"movies",
   "t":"toys",
   "g":"games",
   "s":"shops"}
class truck:
    def __init__(self,t):
        self.t=t
    def you(self):
        for s in t["m"].upper().split():
            print(s)
d=truck(t)
print(d.you())

e=["movies","games","shops"]
class r:
    def __init__(self,e):
        self.e=e
    def rty(self):
        for t in str(e[0]).upper().split():
            print(list(t.upper()))
g=r(e)
print(g.rty())
print()

r=["sports","movies","games","choice"]
class dec():
    def __init__(self,r):
        self.r=r
    # def turtle(self):
    #     for n in list(str(chr(r[0][1])).upper()):
    #         print(n)
    def fish(self):
        return r[0][1]
    def mouse(self):
        for i in list(str(ord(r[1][0].upper()))):
            print(i)
    def catch(self):
        v=-5
        for k in zip(r[0].upper(),r[1].upper(),r[2].upper(),r[3].upper()):
            print(set(f"{v}:{k}"))
            v+=2
    # def fire(self):  ###      problem   ####
    #     return ord(r[0]),ord(r[0])
t=dec(r)
# print(t.turtle())
print(ord(t.fish()))
print(t.mouse(),print())
print(t.catch())
# print(t.fire())

class game():
 pass
class fridge():
    def __init__(self):
        self.handle=handle
        print("fridge".upper())
        # print("fridge".upper().join("handle".upper()))
class oven():
    def __init__(self):
        self.handle=handle
        print("microwave".upper())
k=fridge()
l=oven()
print(k.handle)
print(k.handle)

class fridge():
    def __init__(self,handle,color):
        self.handle=handle
        self.color=color
    def hill(self):
        print(f"{self.handle} has {self.color}.")

# class pc_design:
#     def __init__(self,cover,graphic_card):
#         self.cover=cover
#     def gpu(self,graphic_card):
#         self.graphic_card=graphic_card
#     def m(self,monitor):
#         self.monitor=monitor
#     def mother(self,mother_board):
#         self.mother_board=mother_board
#     def electricity(self,power_supply):
#         self.power_supply=power_supply
#     def ram(self,memory_ram):
#         self.memory_ram=memory_ram
#     def cpu(self,c_p_u):
#         self.c_p_u=c_p_u
#     def o_s_sys(self,system):
#         self.system=system
#     def other_gaming_things(self,things):
#         self.things=things
#     def wires(self,cables):
#         self.cables=cables
#     def screw(self,screws):
#         self.screws=screws
#     def store(self,stor,age):
#         self.stor=stor
#         self.age=age
#     def mous(self,gaming_mouse):
#         self.gaming_mouse=gaming_mouse
#     def board(self,gaming_keyboard):
#         self.gaming_keyboard=gaming_keyboard
#
# c=pc_design("Ant Esports Elite 1100 Mid-Tower Computer Case")
# print(f"i have bought {self.cover} from amazon") #####
# g=pc_design

class pc_design:
    def  __init__(self,graphic_card,case,cpu,memory,mother_board,power_supply,system,cables,screws,storage_ram,keyboard,mouse,SD):
        self.grahic_card=graphic_card
        self.case=case
        self.cpu=cpu
        self.memory=memory
        self.mother_board=mother_board
        self.power_supply=power_supply
        self.system=system
        self.cables=cables
        self.screws=screws
        self.storage_ram=storage_ram
        self.keyboard=keyboard
        self.mouse=mouse
        self.SD=SD
    def installation(self):
        print(f"At first step,i have bought {self.case} case from Amazon.\n             And i started install {self.cpu} in {self.mother_board}.\nAlso, i installed"
              f"  {self.SD} .\n             After,i put {self.memory} in above cpu in the motherboard.\nThen i tested run outside the case.\n"
              f"             in additionally,i connected the {self.power_supply} backside of {self.case} and i attached the {int(self.screws)} screws with power supply\n"
              f"Also, after completed the three step.\n             i started the installation of {self.grahic_card} on the motherboard\nand completing the "
              f"installation of gpu.\n             moreover, i bought 2 TB {self.storage_ram} from game stop and i installed  of {self.storage_ram}\nbeside the {self.power_supply}.\n"
              f"             secondly,i connected the {self.keyboard} and {self.mouse} upside or above\nthe {self.case}.".title())

encrypt=pc_design("nvidia geforce rtx 3050","Ant Esports Elite 1100 Mid-Tower","Intel Core i5-12400F Desktop Processor",memory="G Skill Trident Z5 ",mother_board="MSI PRO H510M-B Motherboard",power_supply="Ant Esports VS400L",
                  system="Corsair Vengeance i7500",cables="wires",screws=4,storage_ram="Crucial Pro DDR5 RAM 32GB Kit (2x16GB)",keyboard="HyperX Alloy Origins 65 Mechanical Gaming Keyboard",mouse="Razer DeathAdder Essential Wired Gaming Mouse",SD="SAMSUNG EVO Plus 128GB SD")
encrypt.installation()
print(
)
# coin=pc_design(memory="G Skill Trident Z5 ",mother_board="MSI PRO H510M-B Motherboard",power_supply="Ant Esports VS400L")
# bit=pc_design(system="Corsair Vengeance i7500",cables="wires",screws=4,storage_ram="Crucial Pro DDR5 RAM 32GB Kit (2x16GB)")
# doge=pc_design(keyboard="HyperX Alloy Origins 65 Mechanical Gaming Keyboard",mouse="Razer DeathAdder Essential Wired Gaming Mouse",SD="SAMSUNG EVO Plus 128GB SD")

# print(f"At first step, i have bought {self.case},{self.grahic_card},{self.storage_ram},{self.}")

# class deck():
    # def __init__(self,esteem):
    #     self.glass=glass
    #     self.esteem=esteem*self.glass
# r=deck(10,20)
# print(r.esteem)

###  "9/2/25"  ###
class guns:
    def __init__(self):
        self.name="m416"
        self.ammos=5.56
        self.type_gun="assult rifle"
my_guns=guns()
print(f"the gun name is :{my_guns.name}")
print(f"the type of ammos :{my_guns.ammos}")
print(f"the type of gun is :{my_guns.type_gun}")
print()

class pc_games:
    def __init__(self):
        self.name="fortnite"
        self.type="survival"
        self.availability="pc","xbox","ps4"
g=pc_games()
print(f"the name of game is :{g.name}")
print(f"the type of game is :{g.type}")
print(f"the game is available in :{g.availability}")

# class fruits_quantity:
#     def __init__(self,name,quantity):
#         self.name="apple"
#         self.quantity=30
# frt=fruits_quantity()
# print(f" 1) the name of fruit is :{frt.name}\n      the quantity of fruit is :{frt.quantity}")
# frt.quantity=50
# frt.name="banana"
# print(f"2) the name of fruit is :{frt.name} and the quantity of fruit is :{frt.quantity}")

class fruit:
    def __init__(self):
        self.name="apple"
        self.color="red"
my_fruit=fruit()
my_fruit.color="green"
my_fruit.name="watermelon"
print(my_fruit.color)
print(my_fruit.name)

class shoes:
    def __init__(self,name,color):
        self.name="nike"
        self.color="red"
s=shoes("adidas","black")
print(s.name.upper())
print(s.color.upper())
print()

class cars:
    def __init__(self,name,color):
        self.name="mustang"
        self.color="green"
    def details(self):
        print("my car name is "+self.name+" and "+"my color of car is "+self.color)
c=cars("lamborghini".upper(),"yellow".upper())
# print(c.name and c.color)
print(c.details())
print()

class table:
    def __init__(self,type,color,legs):
        self.type=type
        self.color=color
        self.legs=legs
    def det(self):
        print("the type of table is "+self.type.title()+'. the color of table is '+self.color.title()+". the table has "+str(self.legs)+" legs.")
j=table("wooden","brown",4)
j.det()
print()

class mul:
    def __init__(self):
        self.ons=4
        self.tws=6
        self.thrs=10
    def multi(self):
        print(self.ons**self.tws+self.thrs**0.5)
f=mul()
f.multi()
print()

import random
class setts:
    def __init__(self):
        self.name="cricket"
        self.things="bat_ball"
        self.players=11
c=setts()
# v=random.sample(c)
print(c.name,c.things,c.players)
print()

class games:
    def __init__(self,name,door):
        self.name=name
        self.door=door
g=games("cricket","outdoor")
a=games("carrom","indoor")
m=games("ludo","indoor & outdoor")
print(g.name)
print(g.door)
print(a.door+" "+a.name)
print(m.name+" "+m.door)
print()

# class info:
#     def __init__(self):
#         self.name=name
#         self.type=type
#         self.made=made
#         self.available=available
# c=info("pubg","survival","c++","mobile")
# print(c.name)
# print(c.type)
print()
class info:
    def __init__(self,name,type,made,available):
        self.name=name
        self.type=type
        self.made=made
        self.available=available
d=info("pubg","survival","c++","mobile")
print(d.name)
print(d.type)
print(d.available)
print(d.made)
print()
# c=info("pubg","survival","c++","mobile"))

# class bottle():
#     def __init__(self,volume,type_):
#         self.volume=volume
#         self.type=type
#     def pour(self):
#         print("pouring....")
#     def fill(self):
#         print("filling....")
#     def recycle(self):
#         print("recycling....")
# f=bottle()
# f.recycle()
print()

class games():
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def g(self):
        return self.name
    def a(self):
        return self.name+" "+self.type
x=games("warzone","action_survival")
print(x.g())
print(x.a())
print()

class laptops:
    def __init__(self,name,type):
        self.name="asus"
        self.type="gaming"
lap=laptops("dell","creators")
print(lap.name)
print(lap.type)
print()

# class lam:
#     def __init__(self):
#         self.name=name
#     def ert(self):
#         return list(filter(lambda c:c**2,g))
# g=lam([10,20,30,40,50])
# print(g.ert())
print()

class creta:
    def __init__(self,name):
        self.name=name
    def yt(self):
        for k in enumerate(self.name):
            print(k)
            # print(f"{k}:::{self.name}")
# c=creta([10,904,242,323,2,112,1])
i=creta([1,3,5,7,9,11])
# c.yt()
i.yt()
print()

# class desk:
#     def __init__(self,name,keys):
#         self.name=name
#         self.keys=keys
#     def dlf(self):
#         return list(lambda g,h:g**h,self.name,self.keys)
#     pass
# h=desk([110,20,304,0],[10,24,20,803,23,43])
# print(h.dlf())

# class sqrt:
#     def __init__(self,name):
#         self.name=name
#     def srt(self):
#         pass
#         print(list(lambda x:x**2,self.name))
# c=sqrt([10,304,323,42])
# c.srt()


# class deck:
#     def __init__(self,deck):
#         self.deck=deck
#     def rti(self):
#         pass
#         return list(lambda f:f+f)
# c=deck([10,24,24,3,4,2312])
# c.rti()

####   "11/2/25"  ####
class magnet:
    def __init__(self):
        self.one=1
        self.two=2
    def rto(self):
        return self.one+self.two
v=magnet()
print(v.rto())
print()

class games():
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def g(self):
        return self.name
    def a(self):
        return self.name+" "+self.type
x=games("warzone","action_survival")
print(x.g())
print(x.a())
print()
# class staff:
#     def laptop(self,name,type,role,salary):
#         self.name=name
#         self.type=type
#         self.role=role
#         self.salary=salary
#     def la(self):
#         return self.name+self.type
#     def pt(self):
#         return self.role+self.salary
#     def op(self):
#         return f"the person name is :{self.name}\n{self.name} is a :{self.type}\n.{self.name} does a :{self.role}\n.and {self.name} has {self.salary} salary."
# w=staff("corey","male","manager",25000)
# t=staff("cor)
# print(w.op())

print()
class gta:
    def __init__(self,name,game):
        self.name="gta"
        self.game="survival"
    def gt(self):
        return self.name+" "+self.game
f=gta("pubg","action_survial")
print(f.gt())
print(

)
class staff:
    def __init__(self,name,gender,role):
        self.name=name
        self.gender=gender
        self.role=role
    def ops(self):
        print(self.name+self.gender+self.role)
    def fra(self):
        print(f"the name of person is: {self.name}\n.{self.name} is a : {self.gender}\n.{self.name} does {self.role}")
s=staff("corey","male","analyst")
taf=staff("alex","male","manager")
print(s.fra())
print()
print(taf.fra())
print()

class ui:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def full_name(self):
        return "{} and {}".format(self.first,self.last)
emp_1=ui("core","manages")
emp_2=ui("ios","apple")
# print(emp_1.first)
# print(emp_2.last)
print(emp_2.full_name())
print()

import random
class games:
    def __init__(self,name):
        self.name=name
    def h_t(self):
        print(random.choice(self.name))
# o=["H","T","HH","TT"]
s=games(["H","T","HH","TT"])
s.h_t()
import random
class random_dice_numbers:
    def __init__(self,numbers):
        self.numbers=numbers
    def yt(self):
        print(random.choice(self.numbers))
q=random_dice_numbers([1,2,3,4,5,6])
q.yt()
# h=range(1,6)
print()

class robot:
    def __init__(self,given_name,given_color):
        self.name=given_name
        self.color=given_color
    def intro_self(self):
        print("my name is "+self.name+" "+self.color)
s=robot("pogo","brown")
s.intro_self()
f=robot("china","red")
f.intro_self()
# s=robot()
# s.name="tom"
# s.color="red"
# s.intro_self()
# print()
# ss=robot()
# ss.name="doremon"
# ss.color="blue"
# ss.intro_self()
# print()
# cam=robot()
# cam.name="pogo"
# cam.color="black"
# cam.intro_self()
print()

# class animal:
#     def __init__(self,name):
#         self.name=name
#         self.is_alive=True
#     def eat(self):
#         print(f"{self.name} is eating.")
#     def sleep(self):
#         print(f"{self.name} is sleeping.")
# class dog(animal):
#     pass
# class cat(animal):
#     pass
# class mouse(animal):
#     pass
# Dogs=dog("bruno")
# cats=cat("gini")
# mices=mouse('mushak')
# print(Dogs.name)
# print(Dogs.is_alive)
# print(cats.is_alive)
# mices.sleep()

class bike:
    def __init__(self,name,number):
        self.name=name
        self.is_engine_start=True or False
        self.number=int(number)
    def petrol(self):
        print(f"{self.name} is filling the petrol.")
    def gears(self):
        print(f"{self.name} has changed the gear at {self.number}.")
class jawa(bike):
    pass
class pulsar(bike):
    pass
class royal_enfield(bike):
    pass
j=jawa("jawa350",4)
p=pulsar("pulsar200",5)
r=royal_enfield("hunter_350",6)
print(j.name)
print(j.is_engine_start)
j.gears()
r.gears()
p.petrol()
print()

####   12/2/25  ####

class shots:
    def __init__(self,name,type_shots):
        self.name=name
        self.type_shots=type_shots
    def n1(self):
        return f"{self.name} hits {self.type_shots} ."
    def n2(self):
        return f"{self.name} hits {self.type_shots}."
    def n3(self):
        return f"{self.type_shots} hit by {self.name}"
class virat_kohli(shots):
    pass
class Ms_dhoni(shots):
    pass
class Rohit_sharma(shots):
    pass
vk=shots("virat_kohli","cover drive")
ms=shots("Dhoni","helicopter")
rs_45=shots("rohit_sharma","flick shot")
print(vk.name)
print(ms.type_shots)
print(vk.n1())
print(ms.n3())
print(rs_45.n2())
print()

class cars:
    def __init__(self,alpha,name,origin):
        self.alpha=alpha
        self.name=name
        self.origin=origin
    def info(self):
        return f"{self.alpha} : {self.name} == {self.origin}."
    def infostic(self):
        return f"{self.alpha} : {self.name} == {self.origin}."
    def infostop(self):
        return f"{self.alpha} : {self.name} == {self.origin}."
class america(cars):
    pass
class germany(cars):
    pass
class japan (cars):
    pass
# class italy(cars):
#     pass
# class uae(cars):
#     pass
ra=cars("r".title(),"rivian".upper(),"america".upper())
bm=cars("b".upper(),"bmw".upper(),"germany".upper())
j=cars("t".upper(),"toyota".upper(),"japan".upper())
lam=cars("l".upper(),"lamborghini".upper(),"italy".upper())
ferr=cars("f".upper(),"ferrai".upper(),"uniter arab emirates".upper())
cit=cars("c".upper(),"citrogen".upper(),"france".upper())
print(ra.info())
print(bm.infostic())
print(j.infostop())
print(lam.info())
print(ferr.infostic())
print(cit.infostop())
print()

class bikes:
    def __init__(self,name,color,speed,country):
        self.name=name
        self.color=color
        self.speed=int(speed)
        self.nation=country
class tri(bikes):
    def __init__(self,name,color,speed,country):
        super().__init__(name,color,speed,country)
class ja(bikes):
    def __init__(self,name,color,speed,country):
        super().__init__(name,country,speed,color)
class harley(bikes):
    def __init__(self,name,color,speed,country):
        super().__init__(name,color,speed,country)
class royal(bikes):
    def __init__(self,name,color,speed,country):
        super().__init__(name,color,speed,country)
trp=tri("triumph".upper(),"black".title(),"160","america")
print(trp.name)
print(trp.color)
j=ja('jawa'.upper(),"brown".upper(),189,"indian")
print(j.name)
print(j.color)
print(j.speed)
print(j.nation)
print()

# class food:
#     def __init__(self,states,food):
#         self.states=states
#         self.food=food
#     def infor(self):
#         super().__init__(states,food)
#     def ui(self):
#         return f"{self.states} has it's own {self.food}."

class youtube:
    def __init__(self,videos,type,creators):
        self.videos=videos
        self.type=type
        self.creators=creators
    def inf(self):
        return f"{self.creators} made {self.videos} of {self.type}"
class des(youtube):
    pass
class lik(youtube):
    pass
class comm(youtube):
    pass
ap=youtube("technical skill","educational","alex")
r=youtube("gameplay","game","lakers")
f=youtube("electronics product","product_based","unbox therapy")
print(ap.inf())
print(f.inf())
print(r.inf())
print()

class deck:
    def __init__(self,name,age,role):
        self.i=name
        self.o=age
        self.s=role
    def per(self):
        return f"{self.i} made {self.o} and upload  on {self.s}."
class lic(deck):
    pass
class dis(deck):
    pass
class com(deck):
    pass
lix=deck("coding ninjas","coding",role="youtube")
print(lix.per())

class dock:
    def a(self):
        print("bro code")
class b(dock):
    def ballb(self):
        print("sundas khalid")
class op(b):
    def cf(self):
        print("google")
c=op()
c.a()
c.ballb()
c.cf()
print()

class dock:
    def a(self):
        print("bro code")
class b:
    def ballb(self):
        print("sundas khalid")
class op(b):
    def cf(self):
        print("google")
class hello(op,b):
    def rt(self):
        print("microsoft")
he=hello()
he.ballb()
he.cf()
he.rt()
print()

# class movies:
#     def __init__(self,name,genre,rating):
#         self.name=name
#         self.genre=genre
#         self.rating=rating
# class ji:
    # def ui(self):

        # return f"{self.name} and {self.genre} and {self.rating}."
# class dir:
#     def ux(self):
        # return f"{self.name} and {self.genre} and {self.rating}."
# class pro(ji,dir):
#     def com(self):
        # return
print()

print("13/2/25")

class com:
    def __init__(self,founders,companies,what_makes):
        self.founders=founders
        self.companies=companies
        self.what_makes=what_makes
    def fgh(self):
        return f"{self.founders} made {self.what_makes} == {self.companies}."
class you(com):
    pass
class fac(com):
    pass
class goo(com):
    pass
o=com("larry illson","oracle","database models")
f=com("mark zuckerberg","facebook","social media app")
m=com("bill gates","microsoft","operating system")
print(m.fgh().upper())
print(o.fgh().upper())
print(f.fgh().upper())

class employee:
    num_of_emps=0
    raise_amt=1.05
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+" "+last+"@email.com"
        self.pay=pay

        employee.num_of_emps+=1
    def full_name(self):
        return "{} {}".format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt= amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split("-")
        return cls(first,last,pay)

emp_1=employee("corey","schafer",50000)
emp_2=employee("tom","cruise",10000)


# employee.set_raise_amt(10.20)
# emp_1.set_raise_amt(10.30)
# emp_2.set_raise_amt(10.50)

# print(employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
emp_str_1="john-doe-70000"
emp_str_2="steve-smith-3000"
emp_str_3="jane-deo-90000"
new_emp_1=employee.from_string(emp_str_1)

# first,last,pay=emp_str_1.split("-")
# new_emp_1=employee(first,last,pay)
# new_emp_2=employee(first,last,pay)
print(new_emp_1.email)
print(new_emp_1.pay)
# print(new_emp_2.email)
# print(new_emp_2.num_of_emps)
print()

print("17/2/25")

class person:
    name="pratham"
    age=int(22)
    occupation="i'm student"
a=person()
print(a.occupation)
class solo(person):
    name="yono"
    age=int(1)
    role="progamming"
b=solo()
print(b.role)
print()

class game:
    name="gta6"
    creator="rockstar production"
    launch="fall 2025"
    def inf(self):
        print(f"{self.creator} will launch {self.name}"
              f" in {self.launch}".upper())
i=game()
i.inf()
print()

class game:
    name="gta6"
    creator="rockstar production"
    launch="fall 2025"
    def inf(self):
        print(f"{self.creator} will launch {self.name}"
              f" in {self.launch}".upper())
class sg(game):
    name="rainbow six x"
    created_by="ubisoft"

k=sg()
k.inf()
print(k.created_by)
print(k.name)
print()

class year:
    name="fifa 2015"
    creator="electronic access"
    launch="mid 2015"
    def acc(self):
        return f"{self.creator} released {self.name} in {self.launch}."
class hole(year):
    name="pes 2016"
    creator="unity 3d"
    launch="summer 2016"
    def giver(self):
       return f"{self.creator} launched {self.name} in {self.launch}."

y=year()
print(y.acc())
o=hole()
print(o.acc())
print(o.giver().upper())

class vehicles:
    name="tesla"
    model="model x"
    def jk(self):
        return f"{self.model} is belong to {self.name} "
v=vehicles()
print(v.jk())
b=vehicles()
b.name="bmw"
b.model="B5"
print(b.jk())
print()

class myroom:
    def __init__(self,value):
        self.value=value
    def show(self):
        print(f"value is {self.value}")
    @property
    def vas(self):
        print(10*self.value)
m=myroom(100)
m.show()
m.vas
p=myroom(900)
p.vas
print()

class myroom:
    def __init__(self,value):
        self.value=value
    def show(self):
        print(f"value is {self.value}")
    @property
    def vas_scale_measure(self):
        print(10*self.value)

    @vas_scale_measure.setter
    def vas_scale_measure(self,new_number):
        self.value=new_number+20
        # print(10 * self.value)
obj=myroom(20)
obj.vas_scale_measure=50
obj.vas_scale_measure
obj.show()
# obj.vas_scale_measure
# obj.vas_scale_measure=50
print()

class room:
    def __init__(self,numb):
        self.numb=numb
    @property
    def expo_nent(self):
        return self.numb*1
    @expo_nent.setter
    def expo_nent(self,new_numb):
        self.numb=new_numb+10
j=room(5)
j.expo_nent=4
print(j.expo_nent)
print()

class vehi:
    def __init__(self,name,seats):
        self.name=name
        self.seats=int(seats)
        self.shit=int(self.seats+self.seats)
    @property
    def bus_1(self):
        print(f"{self.seats}+{self.seats}=={self.shit}")
        print("{} has {} seats ".format(self.name,self.seats))
        # return f"{self.name} has {self.seats}"
    @bus_1.setter
    def bus_1(self,mini_bus):
        return f"{self.seats}+{self.seats}=={self.seats+self.seats}"
        # return f"{self.seats} in {self.name}."
B=vehi("minibus",10)
print(B.bus_1)
k=vehi("small",20)
k.bus_1
p=vehi("truck",2)
p.bus_1
print()

# class gems:
#     def __init__(self,name,type):
#         self.name="battlefield hardline"
#         self.type="action"
#     @property
#     def sec_gem(self):
#         print(f"{self.name} is a {self.type} game.")
#     @sec_gem.setter
#     def sec_gem(self,name,type,created_by):
#         self.name="rainbow six siege"
#         self.type="multiplayer"
#         self.created_by="electronic arts"
#         print(f"{self.created_by} created {self.name} is a type of {self.type} .")
#     @property
#     def third_gem(self):
#         print(f"{self.name} made by {self.type}.")
#     @third_gem.setter
#     def giving(self):
#         print(self.name,self.type)
# a=gems
# a.third_gem

class choco:
    def __init__(self,name,origin):
        self.name=name
        self.origin=origin
    @property
    def cho(self):
        print(f"{self.name} made in {self.origin}.")
    @cho.setter
    def cho(self,type):
        print(f"{self.name} is {self.type} made in {self.origin}")
g=choco("hershey","american")
g.cho

# r=90
# class dig:
#     d=90
#     p=r+d
# t=dig()
# print(t)
# print()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __str__(self):
#     return f"{self.name}({self.age})"
# p1 = Person("John", 36)
# print(p1)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def myfunc(self):
#     print("Hello my name is " + self.name)
# p1 = Person("John", 36)
# p1.myfunc()

# class example:
#     def __init__(self):
#         print("i am the first constructor.")
#     def __int__(self):
#         print("i am the second constructor.")
#     def init

# h=["america","russia","india","china"]  ####################  YES ################
# g=["sudan","sweden","germany","brazil"]  ####################  YES ################
# class joke:
#     def __init__(self,h,g):
#         self.h=h
#         self.g=g
#     def v(self):
#         return self.h.append(self.g)
# k=joke(h,g)
# print(k.v())

# class doremon():####################  YES ################
#     def __init__(self,h,g):
#         self.g=g
#         self.h=h
#     def cements(self):
#         return tuple(map(lambda r,t:t.upper().split()+r.upper().split(),self.h[0],self.g[0]))
# y=doremon(h,g)
# print(y.cements())
print()
print("######   20/2/25  ######")

class staff:
    def __init__(self,name,role,company,hole):
        self.name=name
        self.role=role
        self.company=company
        self.hole=print(f"{self.name} has {self.role}"
                        f" in {self.company}.")
p=staff("alex","video creator","youtube","op")
p.hole
print()







