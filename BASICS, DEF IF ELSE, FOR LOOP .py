
abc=2
abc_1=3
abc_2=4
print(abc*2)
print(abc_1*2)
print(2**3)

a="pratham"
print(a*10)

s="south africa"
print(s[0:5]*2)
print(s[5:12].upper()*10)

d="donald trump"
print(d[6:12].upper()*10)

k='D'
print('D',56)
i=20
print(i+50)
print('i',70)

u_list=[0,2,4,6,8,10,20,30,40]
u_list[0:4]=[100,102,104,106]
print(u_list)

a_list=[100,200,400,600,800]
b_list=[20,40,60,80]
c_list=a_list+b_list
print(c_list)
c_list[0:6]=[1,3,5,7,9]
print(c_list)

sen1="My name is Pratham"
print(sen1[5])

Animal_list=["monkey","lion","gorilla"]
Animal_list.append("tiger")
print(Animal_list)
print(len(Animal_list))
print(Animal_list[1].upper())

"INPUT"

#qwerty=int(input("Enter the number1"))
#reqwty=int(input("Enter the number2"))
#print(qwerty+reqwty)

#name=input("enter your name: ")
#print("hello,"+ name)

#keyboard=float(input("Enter the value: "))
#mouse=float(input("Enter the value: "))
#print(keyboard+mouse)

#order=input("What you want? pizza/burger = ")
#print("you ordered", order)
#i=input("who invented thr microsoft? = ")
#print("bill gates  invented")

j="%s is the president of usa."
print(j%("joe biden").capitalize())

f="%s fights with joe biden."
d="donald trump"
print(f % d.upper())

d="donald trump"
print(d[0:3].upper())

q=23
print(type(q))

s="string"
print(type(s))

d=34+6j
print(type(d))
print(type(34.90))

p="pratham"
print(p.isalpha())

a="pratham345"
print(a.isdigit())

b="567"
print(b.isalnum())

c="viratkohli166"
print(c.isalnum())


j="joe biden is the president of the usa"
print(j[0:9].upper())
print(j[17:27].upper()*20)

abc_list=[0,2,4,6,8,10]
list_123=[1,3,5,7,9,11]
def_list=abc_list+list_123
print(def_list)

def_list[0:6]=[200,400,600,800,1000]
print(def_list)

print("ms","dhoni","hits","six","in","the","stadium.",sep="<")

s="sachin\ntendukar"
print(s)
print(s[0:6].upper())
print(s[0:6].upper()*5)

print(bin(24))
print(type(45+5j))

#laptop=float(input("Enter the value: "))
#computer=float(input("Enter the Value: "))
#print(laptop+computer)

#f=input("who invented the facebook?= ")
#print=input("Mark Zuckerberg invented the facebook.")

c=56+8j
d=44
print(d*c)
x=chr(67)
print(x)
q=chr(65),chr(66),chr(67),chr(68)
print(q)
w=chr(69),chr(70),chr(71),chr(72)
print(w)
e=q+w
print(e)

p=chr(87)
print(p)
a=chr(68),chr(69),chr(70),chr(71),chr(72)
print(a)

r=ord('P'),ord('R'),ord('a'),ord('t'),ord('h'),ord('a'),ord('m')
print(r)

a=ord('p'),ord('P')
print(a)

qwert=ord('A'),chr(100),ord('B'  ),chr(78)
print(qwert)


u=[1,3,5,7,10,11,13,15,17,19,21]
print(sorted(u))


#chr=input("Enter a character: ")
#ascii_value=ord(chr)
#print("ASCII value of",chr,"is",ascii_value)

#chr=input("Enter the character: ")
#ascii_value=ord(chr)
#print("ASCII value of",chr,"is",ascii_value)


#dividend=int(input("Enter the dividend: "))
#divisor=int(input("Enter the divisor: "))
#quotient= dividend / divisor
#remainder= dividend % divisor
#print("Quotient:",quotient)
#print("Remainder:", remainder)

#a=int(input("Enter the value_1: "))
#b=int(input("Enter the value_2: "))
#c=a*b
#print("Product:",c)

#cat=float(input("Enter the value_1: "))
#dog=float(input("Enter the value_2: "))
#sq= cat+dog
#print("Sum:",sq)

#number=int(input("Enter the interger: "))
#print("You entered:", number)

#chr=input("enter the character: ")
#ascii_value=ord(chr)
#print("ASCII value of",chr,"is",ascii_value)


r_1="om {p} the {f}.".format(p="plays",f="football")
print(r_1)
r_2= "sir {1} the {0}.".format("teaches","maths")
print(r_2)

a=45+8j
b=56.09
c=45
print(type(a))
print(bin(c))

u=[0,2,4,6,8,10]
print(u[0:4])

a="the {} inside in the {}".format("rome","europe")
print(a)
print(a.upper())
print(a.title())
print(type(a))
print(a.isalnum())
print(a.isalpha())
print(a.find("rome"))
print(a.index("europe"))

a="apple\nbannana"
print(a)
a= "aadmi {}hae\n{}ped phae.".format("betha","khajur")
print(a)
print("boy","plays","the","game.",sep="/")

sen1="the {1} roaming {0}".format("monkeys","around")
print(sen1)

shop_lists=["clothes","toys","games"]
shop_lists.append("electronics")
print(shop_lists)
print(shop_lists[0:2])
shop_lists[0]="fast food"
print(shop_lists)
del shop_lists[2]
print(shop_lists)

qw=[2,5,8,3,2,1,4,34,56,5,6,78,23,41,90]
print(sorted(qw))
print(qw.pop())
print(qw.count(5))

e=[3,78,90,5,89,54,89,12,90,55,23,5,5,5,4,3,2,45,10,91,34,45]
print(e.count(5))
print(sorted(e))
print(sorted(e),e.index(78))
print(e.index(5))
print(chr(e[2]))
print(chr(e[19]))
print(chr(e[19]))
print(chr(92))
e.extend([46,47])
print(e)
#print(e[3*3])


#a=[0,1,2,3,4,5,6,7,8,9,10]
#print(a[2+5])
#print(a[2*3])
#print(a[4*5])

s_list=[4,8,12,6]
s_list[1:4]=[20,24,28]
print(s_list)

sa_list=[10,20,30,40,50]
print(sa_list[-2])

sd_list=[10,20,30,40,50]
print(sd_list[-4:-1])

w=[10,30,40,679,282,97640,274,23,789,671,2,3,49,43,12,0,12,22]
d=[10,20,40,567,1,3,5,6,8,0,10,30,23,456,6738,748492,452,7484052094,759]
print(sorted(w))
print(sorted(d))
print(w.count(12))
print(d.count(10))
print(w.count(12)+d.count(10))
print(max(w)*max(d))

ui_list=[2,4,6,8,10]
ui_list.append([12,14,16,18,20])
print(ui_list)
print(ui_list[5][0:4])

#s="hello! \n{}".format("pratham")
#print(s)

#print("string","string1","string2","string3","string4.",sep="/")
#print("string append in the",end=" ")
#print("list.",end=" ")
#print("who","is","the","girl","behind","the","tree","????",sep="()",end=" ")
#print("sheena.",end=" ")


p=["the","dog","in","tree","the","tyuiop","qwerty"]
print(sorted(p))
print(p.count("the"))

a=["q","e","t","y","u","i","o","a","g","b","d","e","f","h","g"]
print(sorted(a))
print(a.count('e'))
print(max(a))
print(a.index('a'))

u=[1,3,5,7,9,11,2,4,6,8,10]
print(u[0:4]+u[5:9])
a=u[1:4]
y=u[6:10]
print(sorted(a+y))


a="string1string2string3"
print(a.isdigit())
print(a.isalpha())
print(a.isalnum())

qwerty="56"
print(qwerty.isdigit())
print(qwerty.isalpha())

wer=[2,4,5,7,8,10,48,579,749]
print(wer.index(48))

tyu=[4,8,2,1,0,65,37,97,34,2,6,784]
print(tyu.count(2))
print(sorted(tyu))
tyu.remove(65)
print(tyu)
print(tyu.count(2))
print(tyu[2::])
print(tyu[-2::-2])
print(hex(4))


r="{} kicks the {} in the stadium in the usa.".format("ronaldo".upper(),"football")
print(r)

# q=(int(input("the values: ")))
# w=(int(input("the values: ")))
# c=q*w
# print("Product:",c)

p="pratham"
print(f"{p.title()} is a good boy.")


u="78"
print(hex(78))
print(oct(2))

i="kartik"
p="pratham"
print(f"{i.upper()} is a good boy\n{p.upper()} is a intelligent boy.")

print("red\blue")
print("string\string1")
print("black\white")
print("red","blue are","opposite","color.")



print(chr(100))
print(ord('T'))

print(34&45)
print(34^45)
print(34|45)


# length=int(input("value: "))
# breath=int(input("values: "))
# square=length*breath
# print(f"the square is : {square} cm^2")
#
#
# qw=(input("Enter the number: "))[0:4]
# print(qw)
# we=input("Enter the alpha: ")
# print(we.isalpha())
# print(we.split())
#
#
# per=int(input("enter the per: "))
#
# if per<=80:
#     print("A grade")
# elif per>=60:
#     print("B grade")
# elif per>=40:
#     print("C grade")
# else:
#     print("no other option")



o=45
p=90
print(o+(89-(p)))


x=90
d=45
print(x+d/x-d//76)

" EXERCISES "

def animal_crackers(text):
    for h in text:
        if h[0]=="L":
            return True
        else:
            return  False
d=animal_crackers("Levelheaded Llama")
s=animal_crackers("Crazy Kangaroo")
print(d)
print(s)

def makes_twenty(a,b):
    if  a+b==20:
        return True
    else:return False
f=makes_twenty(10,10)
g=makes_twenty(12,8)
h=makes_twenty(23,10)
print(f)
print(g)
print(h)

def ten_tens(w,e):
    if  w-e==0:
        return True
    else: return  False
q=ten_tens(10,9)
f=ten_tens(20,1)
print(q)
print(f)

def ones_ones(a,b):
    if a+b==20:
        return True
    else: return False
twos=ones_ones(10,10)
tt=ones_ones(15,5)
op=ones_ones(1,2)
print(twos)
print(op)

# def food(name):

print("macdonald".capitalize())

# def almost(n):
#     if n<=10:
#         return True
#     elif n<100:
#         return True
#     elif n<200:
#         return True
#     else: return False
# ball=almost(int(input("numbers: ")))
# print(ball)

# print(abs(num))

" EXERCISE STATEMENTS ASSESSMENT TEST"
st="print only the words that start with s in this sentences"
for l in st.split():
    if l[0]=="s":
        print(l)

for i in range(0,10):
    if i%2==0:
        print(i)

for n in range(1,50):
        if n%3==0:
         print(n)

stt="print every word in this sentences that has an even number of letters"
for a in stt.split():
    if len(a)%2==0:
        print(a,"<--- lenth of the word is even")

# for num in range(1,101):
#     if num%3==0 and num%5==0:
#         print("fizzbuzz")
#     elif num%3==0:
#         print("fizz")
#     elif num%5==0:
#         print("buzz")
#     else:print(num)

std='create a list of the first letters of every word in this string'
for word in std.split():
    print(word[0].upper().split())

print("donald trump meet narendra modi".split())

s=["physics","chemistry","maths"]
d=[1,2,3,4,5,6,7]
print(s[0],d[0:4])

s[1]="history"
s.append("biology")
print(s)
del d[0:3]
print(d)
print(d[::-5])
print(d[::-1])

ti=(20,90,89,23,45,13,12)
print(ti[0:2])
print(ti[::-3])
print(ti[-1::2])
print(ti[-1::1])
print(ti[1:-1])
tp=(100,200,300,400,200)
tpp=ti+tp
print(sorted(tpp))
print(tp.count(200))

def addition(a,b):
    print(a**2,b**2)
    return a+b
sub=addition(1,2)
addition(3,4)
print(sub)

def names(a="apple",b="batle"):
    print(a==b)
names(a="apple",b="apple")

def jammu(kashmir):
    for k in kashmir:
        if k[0]=="r":
            return True
        else: return False
g=jammu("cristiano ronaldo")
f=jammu("ronaldo")
print(g)
print(f)

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def g(c="s"):
    print("tata "+ c)

g("sons")
g("motors")
g("electric")
g("batteries")
g()
g("big basket")

# food="tomatoes"
# price=20.33
# num_of_food=int(input(f"how many {food}s?:  "))
# total=num_of_food*price
#
# print(f"your total food is rupees {total}")


prices=(90,24,89,190,13,89,5,75)
names=("tomatoes","cabbage","onion","potato","olives","spinach","pinapple","watermelon")
for x,c in zip(prices,names):
    print(f"{x}*{c}")

print(int("89"))
print(type(int("100")))
print()

def j(o):
    for k in o:
        if k%2==0:
            print(k)
j(o=[1,2,3,4,5,6,7,8,9,10])

print("the prices of grapes are:-{g:->10}".format(g=10))
print()

print("he said his name was %s."%"fred")
print("he said his name was %r."%"fred")
print()
print(" i once caught a fish %s."%"this     \tbig")
print()
print("i once caught a fish %r."%"this \tbig")
print()
print("i wrote %s programs today."%3.75)
print("i wrote %s in simple way."%3)
print()
print()
print(f"i put some white spaces in numbers:-{10:.5f}")
print()
print("decimal number:-%6.1f"%(15.999))
print("the . numbers after the interger no:-%20.4f"%(100.23353534343))
print()

print("the deci number - {f:.2f}".format(f=500.223))

def macros(vba):
    while vba<20:
        if vba==16:
            break
        print(vba)
        vba=vba+1
print(macros(vba=2))

# def martin(mars):
#         if mars%2==0:
#           print(k)
# print(martin(mars=[10,11,12,13,14,15]))

def v():
    print("donald trump"[0:3])
v()

def r(d):
    for k in d[0:3]:
        print(k.upper()*3)
print(r(d="donald trump"))

def s(o):
    for qw in o[3:7]:
        return qw.upper()*3
print(s(o="zealand"))

def f(p):
    for m in p[3:7]:
        print(m.upper()*4)
print(f(p="zealand"))


#ui_list.extend([45])
#print(ui_list)

print(f"{'wonder':_<10}\n          {'land':->10}")
# print(f"{10:.1.23f}")

def m(o,p):
    p.append(o)
    print(p)
    p.extend(o)
    print(p)
# m(o=[1,2,3,4,5],p=[10,20,30,40,50])
print(m(o=[1,2,3,4,5],p=[10,20,30,40,50]))

# b=[1,2,3,4,5]
# n=[10,20,30,40,50]
# n.append(b)
# print(n)

d=[10,20,30,40,50]
f=[100,200,300,400,500]
f.append(d)
print(f)
f.extend(d)
print(f)

print(f"i put spaces after number:-{190:_<10}")

def squares(o,m):
    return o**m
# print(f"the squares of 2 is :- {o**m}")
print(squares(2,3))

def vb(i,o):
    print(i+o)
vb(10,20)

def c(l,m):
    return l-m
print(c(10,20))


def r(a,b):
    c=a//b
    return c
print(r(a=10,b=10))

# def pratham(*om,r):
#     return om[2]+r
# print(pratham(10,11,12))

def asia(china,india,pakistan):
    return china+india*pakistan
print(asia(4,3.2,12))

def independent_country(india,china,south_korea,japan):
    return india+china-south_korea*japan
print(independent_country(india=1947,china=1962,south_korea=1987,japan=1945))

def LEADERS_OF_STATES(GUJARAT,RAJASTAN,JHARKAND,UTTAR_PRADESH):
    print(GUJARAT-RAJASTAN/JHARKAND*UTTAR_PRADESH)
LEADERS_OF_STATES(GUJARAT=10,JHARKAND=12,UTTAR_PRADESH=19,RAJASTAN=45)

def cars(*bentley,ferrari):
    return bentley[2]+ferrari
print(cars(10,11,120,ferrari=10))

def gopi(*nath):
    print(nath[1]+nath[4])
gopi(10,20,30,40,50)

def bentley(*bmw):
    print(bmw[3]*bmw[1])
bentley(1,2,3,4,5)

def bmw(*ferrari):
    return ferrari[3]/ferrari[2]
print(bmw(10,20,30,40,50))

f=(10,20,30,40,50)
def r(*i):
    print(i[2]*i[1])
r(*f)

g=[10,20,30,40,50]
def v(*d):
    print(d[1]+d[3])
v(*g)

# df={1,2,3,4,5}
# data={10,20,30,1,2,43,21}
# def b(df,data):
#     print(df|data)
# b()

a=(100,200,300,400,500)
def r(*d):
    print(d[3]-d[2]+d[0])
r(*a)

# f=(1,2,3,4,5)
# g=(10,20,30,40,50)
# def h(*u):
#     print(u[2]+i[3])
# h(*f,*g)


# data={10,20,30,1,2,43,21}
# def cvb(*pot):
#     print(pot[1],pot[3])
# cvb(*data)/

kashmir={100,200,300,400,500}
def g(*apple):
    print(apple[2],apple[1])
g(*kashmir)

figi={10,20,30,40,50}
cuba={100,200,30,40,5}
def asd(america,brazil):
    print(america|brazil)
    print(america&brazil)
    print(america^brazil)
asd(america=figi,brazil=cuba)

def gin(d="dubai"):
    print(d+" has skyscraper.")
    print(d+" has so many sheik.")
    print(d+" burj khalifa.")
    print(d+" cops has superfast cars.")
gin()

# def keyboard(**mouse,gpu):
#     return mouse[1]+gpu
# print(keyboard(10,20,30,40,gpu=10))

# def zxc(**code):
#     return code["fd"]+"  chose indian community."
# print(figi="op",)

def ios(**android):
    print(android["s"]+" made setup plant in india")
ios(a="apple",s="samsung")

def sardar(**bhagat):
    return bhagat["t"]+bhagat["three"]
print(sardar(z=0,o=1,t=20,three=300))

def num_sen(**num_sen):
    print("my name is:-"+num_sen["p"]+","+"my roll.no is: "+num_sen["o"])
num_sen(p="pratham".upper(),o="1")
print()
def cars(hood):
    for l in hood:
        return l
dumb=["1","2","3","4","5"]
cars(dumb)
print()
def country(states):
    for j in states:
        print(j)
alphabets=["c","r","i","p"]
country(alphabets)
print()
def war(fights):
    for y in fights:
        print(y)
city=["japan".upper(),"british".upper(),"russia".upper(),"america".upper()]
# print(war(city))
war(city)
print()
old_movies={"s":"sholay",
            "k":"kaala pathar",
            "san":"shaan",
            "d":"don"}
def r(g):
    for a in g.values():
        print(a.upper())
r(old_movies)
print()
def trucks(repairs):
    for k in repairs:
      print(k)
garage=["one","two","three","four","five"]
trucks(garage)
print()

def g(tower):
    for t in tower:
        print(t)
c=["a","b","c","d"]
g(c)

def raj(kgf,fool):
    for k in enumerate(zip(kgf,fool)):
        print(k)
d=("om","power","alex","siri","amazon")
f=(10,20,30,40,50)
raj(d,f)

missile=[1,2,3,4,5]
bomb=[10,20,30,40,50]
for lungi,dhoti in zip(missile,bomb):
    print(f"{lungi} : x : {dhoti}")

def boss(bidi):
    for k in bidi:
        if k%2==0:
            print(k)
d=[10,11,12,13,14,15,16]
boss(d)

t=(90,131,303,2421)
print(t[0:2])
for i in t:
    print(i)
s={10,342,243,222,4}
for l in s:
    print(l)

two=(1,2,3,490,24,24,32,32) # 8
three=(10,3,3,82,2,24,22) #7
four={1,39,34,24,24,23}#5
for k,i,l in zip(two,three,four):
    print(f"{i}:X:{l}:-:{k}")

op=(1,90,24,22,323)
om=(90.2422,44,242,90,44,900,44)
j=[]
jaago=[]
# for v,m in zip(om,op):
#     j.append(op)
#     print(j)
for n,c in zip(om,op):
    j.append(om)
    jaago.append(op)
    print(om.count(44))
for zigo in jaago:
    print(zigo[0:3])

x=(1,2,3,4,5)
c=[90,322,89,24,24,24]
a=[]
for v in x:
    # c.extend(v)
    a.append(v)
    print(a)

h={"a":"aam aadmi party",
   "b":"bhajap",
   "c":"congress",
   "r":"republican"}
def a(c):
    print(h.values())
a(h)

# def d(c):
#     print(h.update({"d":"democratic"}))
# d(h)
def j(o):
    h.update({"d":"democratic"})
    print(h.values())
j(h)

four_s=[10,242,00,2,"904"]
s_400=[90,48,9,44,21]
def russ(c,v):
    four_s.extend(s_400)
    print(four_s)
    print(four_s[0:4])
    print(four_s[2:10:3])
russ(four_s,s_400)

if 00<0:
    print("true")
else:
    print("false")

if 00==0:
    print("yes")
else:
    print("no")

if 00>0:
    print("access")
else:
    print("not access")



for cv in range(5):
    for vc in range(4):
        print(cv,vc)

for k in range(5):
    for g in range(6):
        print(g,end=" ")
        print(" ")

col=5
ro=4
for i in range(col):
    for c in range(ro):
        print(i,c,end=" ")
        print(" ")

# rows=int(input("rows: "))
# columns=int(input("columns: "))
# streaks=input("streaks: ")
# for r in range(rows):
#     for c in range(columns):
#         print(streaks,end=" ")
#     print()

f=5
g=6
for i in range(f):
    for j in range(g):
        print(i,j,end=" ")
        print("*")
        print(" ")

# def dhokla(rose,halwa):
    # return rose[0]==halwa[0]
# print(f"{rose[0]}=={halwa[0]}")
# c=
# b=
# dhokla(khandvi=c,halwa=b)
# dhokla(khandvi="call of duty".title(),halwa="battlefield".title())
# print(dhokla(rose="call of duty".title(),halwa="battlefield".title()))


def airlines(klm,air):
    print(f"{klm[0]} ==== {air[0]}")
    print(f"{klm} : {air}")
airlines("france airways","air newzealand")

def food(fruits,vegetables):
    print(f"{fruits}=={vegetables}")
    return fruits[0]==vegetables[0]
print(food("watermelon","capsicum"))

def sanand(*tata):
    print(f"{tata[0]}=={tata[0]}")
    return tata[0]==tata[2]
print(sanand("harrier","tigor","thiago","nexon","curvv"))

def specific(*pc):
    print(f"i put some spaces [gap] on the index of the pc:-{pc[0]:->40}.")
    print(f"{pc[0]}=={pc[1]}",print(f"{pc[0][0]}=={pc[1][0]}"))
    return pc[0]==pc[1]
print(specific("hardware".title(),"monitor","desktop","mouse"))

if 0.10+0.1==0.11:
    print("true")
else:
    print("false")

def europe(spain,france):
    if spain+france==0.3:
        print("yes "*2)
    else:
        print("no "*2)
# print(f"spain + france=={spain+france}")
print(europe(0.10,0.1))

def city(moscow,mumbai):
    # print("{0}+{1}=={moscow+mumbai}".format(moscow, mumbai))
    print(f"{moscow}+{mumbai}=={moscow+mumbai}")
    if moscow+mumbai==0.3:
        return "access ".upper()*2
    else:
        return "not access ".upper()*2
print(city(moscow=0.12,mumbai=0.15))


# def mice(russia):                         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#     print(f"the capital of russia is :-{russia}".format())
# print(f"{russia[0]}//{russia[1]}=={russia[0]//russia[1]}".format(*russia))

print("{d}  is the 47 president of the usa.".format(d="donald trump"))
print()
print("{tiger[0]}+{tiger[1]} == 0.4".format(tiger=[10,20,30,40,50]))
print()

# print("[cars[t]  motors\n made suv\ncars".format(cars[t=="tata"]))
# print("m[] and m[]".format(m=["narendra","modi"]))

print("the games of {mobile[2]}".format(mobile=["pubg","fornite","warzone"]))
print()
print("the jethalal in {t}".format(t="tarak mehta show"))

def heavy(**trucks):
    print(trucks["f"]+" "+trucks["m"])
heavy(t="tata",md="mahindra",f='force',a="ashok leyland",m="motors")

print("the mixture of trucks is {t} + {m} ".format(t="tata",m="motors"))

def say(**h):
    return h["h"]+" "+h["w"]
print(say(h="hello",w="world"))

def plaza(states,*city):
    print(states.upper())
    print(city)
plaza("gujarat","vadodara".title(),"surat".title(),"rajkot".title())

# def l(countries,**leaders):
#     print(countries)
#     print(leaders)
# print("countries",c="justin tradeu",india="narendra modi")

def k(cycles,**bikes):
    print(cycles)
    print(bikes)
print(k("hero",h="harley davidson",b="bajaj",t="triumph"))

def lead(countries,**leaders):
    print(countries)
    print(leaders)
print(lead("canada",russia="vladimir putin",usa="joe biden",india="narendra modi"))
print(type((lead("canada",russia="vladimir putin",usa="joe biden",india="narendra modi"))))

# def games(**outdoor,indoor):
#     for k in outdoor.values():
#         print(outdoor)
# games(c="cricket",f="football",b="basketball",base="baseball","chess")

def games(indoor,**outdoor):
    print(indoor)
    print(outdoor)
    for v in outdoor.values():
        print(v)
games("chess",c="cricket".upper(),f="foot\n    ball".upper(),b="baske\n    tball".upper())

def components(laptop,**mobile):
    print(laptop)
    print(mobile)
    for i in mobile.keys():
        print(i)
        # for o in mobile.values():
        #     print(o)
        #     for m,n in enumerate(zip(i,o)):
        #         print(m,n)
components("battery",h="hardware",c="charger",s="software",f="fibre")

def suv(**thar):
    print(thar)
    for l in thar.keys():
        for k in thar.values():
            print(f"{l} :|: {k}")
suv(m="mahindra",b="bolero",s="scropio",x="xuv300",xu="xuv500")

def prices(stock,price):
    for s in stock:
        for pr in price:
            # print(s,pr)
            print(f"the mixture of two parameters:-{s} : {pr}")
rupees=("210","100","140","770","510")
naam=("rvnl","suzlon","ashok leyland","tata motors","hindustan zinc")
prices(rupees,naam)

tv_shows=("bigg boss","kbc","friends","cid","fir")
ratings=(6.5,7,8.5,5.6,10,9)
for t in tv_shows:
    for r in ratings:
        # print(f" {t} /\ {r}")
        print(t,r)

def indoor_games(c):
    # for i in c:
    #     print(i)
    for small,prce in c:
        print(f"{small}:{prce}")
u=[("chess",100),("carrom",120),("table tennis",150),("ping pong",200)]
indoor_games(u)

a=2
b=3
a*=b
# b*=a
# print(b)
# print(a)
# print()
print(f"the multiplication of {a}*={b}=={a*b}")
print()

c=3
d=4
c*=d
print(f"the multiplication of {c}*={d}=={c*d}")
print(c)


print(type([([90])]))
e=90
print(type([(e)]))




def swift(charge):
  for spoon,folk in charge:
    print(f"{spoon}\n      {folk}")
apple=[("apple",10),("mango",40),("cherry",20),("kiwi",50)]
print(swift(apple))

d=(10,20,30,21,34,14)
dd=(10.11,12.24,12.21,90.342,9.45,43.1)
for i in d[0:4]:
    print(i)
for a in dd[0:3]:
    print(a)
# for k in i,a:
#     print(f"{k}:{m}")
for j in i,a:
    print(f"{j}:{g}")

# excel=(100,200,300,400,500)
# power=("tomato","onion","potato","ginger","lady finger")
# for u in excel:
#     for r in power:
#         for naksh,raja in u,r:
#             print(f"{naksh} | {raja}")

program=("python","java","c++","c#")
signs=("#","+",".py","%")
# for sun,moon in enumerate(zip(program,signs)):
#     print(f"{sun}:|:{moon}")
# for p in program:
#     for s in signs:
#         print(f"{p}:{s}")
#     for frog,rain in zip(p,s):
#      print(f"{frog}:/|\:{rain}")
for p,s in zip(program,signs):
    print(f"{p}:{s}")
# for i,o,s in enumerate(zip(program,signs)):
#     print(f"{i}:{o}:{s}")

# for j,k,l in zip(enumerate(program,signs)):
#     print(f"{j}:{k}:{l}")

count=0
c="cuban missiles"
for character in c.upper():
    print(f"{count}:{character}")
    count+=2

gin=0
fiji=("usa","india","china","russia")
busy=("elon musk","mukesh ambani","jack ma","vladimir putin")

for i,f in zip(fiji,busy):
    print(f"{gin}:{i}|{f}")
    gin+=5
print()
f=0
plus=[(1,2),(2,3),(3,4),(4,5)]
for p,l,in plus:
    print(f"{f} |{p}+{l}={p+l}")
    f+=1
    print(f"the decimal in plus:-{p+l:.>50f}")
print(f"the total of plus:-{p+l:.<20f}")

print(f"i put ^ on the number:- {w:.^10}".format(w=100))
print(f"i put some standing lines on the biggest number = {300:|^30}")

# co=0
# for j in range(1,5):
#     for k in range(6,10):
#         print(f"{co}!{j}:{k}")
#         co+=1

def v(n):
    for m in n[::-3]:
        print(m)
p=[1,2,3,4,5,6,7,8,9,10]
print(v(p))

print(f"{q:/^20}".format(q=20))
print(f"{s:/^10}".format(s=5))
print(f"{e:/^15}".format(e=20))

print(f"{s:.>20}".format(s=30))
print(f"{r:/>20}".format(r=40))
print(f"{f:\^10}".format(f=60))


def sub(a,b):
    return a-b
print(sub(a=-0.1,b=-0.5))

city=["jaipur","jodhpur","kota","baroda","surat"]
def names(city):
    return len(city)
sort=sorted(city,key=names)
# print(sorted(city,names))
print(sort)

g={"a":1,"b":2}
x=g.pop("a",0)+g.get("c",3)
print(x)
print(g)
print(x,g)

# r=[1,2,3,4,5,(10,20,30,40,50)]
# def collar(tie):
#     for r in tie[5][0:3]:
#         print(r)
# pant=collar(r)
# pant(r)

print(f"the meaning of numbers is :-{25:.^10}")

print(f"the numbers are:{200:\^15}")

print(f"the lines of numbers:{50:/<40}")

print(f"the number has spaces:-{20:24.2f}")

print(f"the numbers has more gaps :{80:15.2f}")

print(f"values has more lines than number:{1:/<10}")

print(f"values of maths has more space :{90:20.4f}")

print(f"the values of accounts has more:{50:.^10}")
print()
print("decimal numbers:%10.2f"%(90.201939))

print("deci values:%20.2f"%(1000.242324))

print("point numbers with width:%20.2f"%(-90.242782))

print(f"the numbers should be in %s way."%("proper"))

print(f"i want numbers are in %s and%s in line"%("\tintergers","\tdecimals"))

print(f"i want numbers\are in %s."%("intergers"))
print()
print(f"i want %snumbers\t."%"\twhole")

print("i caught a fish %s."%"this      \tbig")

print("i saw a %s khalifa in dubai"%"\tburj")

print(f"the height of statue of unity is %d."%100.42424242323232)

print(f"the lenght of triangel is %d."%88.31)

print(f"the\tshare price of tata motors is %d."%782.424)
print()
print(f"the number of strings is %d:"%90.324242)
print()
print("first:%s,second:%5.2f,third:%r"%("hi!",3.1219,"bye!"))
print()
print("i saw %s\tand\t%r."%("taj mahal","qutub minar"))
print()
print("the {} are in either {} nor in {}.".format("numbers","integers","decimals"))

print("tom {1} finished his {0} in {2}.".format("cruise","movie","rome".title()))

print("the value of {} is %d".format("numbers",902.422))
# print("the values of {} is %d".format("share"))
print()

g=3232.302323
print(abs(g))
print(round(g))

book={"a":1,"b":2}
book_1={"c":3,"d":4}
mix=book|book_1
print(mix)

# v={"e":5,"f":6}
# print(list(book).extend(v))
# mix_2=book-book_
# print(mix_2)
v=[1,2,3,4,5]
for l in v:
    l+=2
    print(l)

# sd=[1,2,3]
# card=[10,20,30,40,50]
# for f in sd:
#     sd+=card
#     print(sd)
f=[1,2,3,[10,20,30,[100,200,300,[0.1,0.2,0.3]]]]
# w=[0.10,0.20,0.30]
print(f[3][3][3][1])
for b in f[3][3][3]:
 print(b+0.20)

v=[10,20,30,40]
for k in v:
    print(k+0.10)
print(k+8.20)

e="code"
r="quiz"
print(e+r)
p="python"
print(p[::2])








# x=4
# if x*2==8:
#     print("true")
# else:
#     print("false")






# def jerk(jack):
#     if jack%2==0:
#         return max(jack)
#     else:
#         return min(jack)
# o=jerk(10)
# g=jerk(15)
# print(o,g)



g={"a":"apple",
   "b":"ball",
   "c":"chiku",
   "d":"doll"}
# def cuba(*h):
#     return h[]
# print(*cuba)
def rto(*ios):
    print(ios)
rto(*g.values())

# def vehicle(*motor):
#     print(motor[],motor[])
# vehicle(*g.values())

# g=(90,30,10,30,39,92,49,92)
# print(sorted(g))
# print(set(g))
# print(g.count(30))



# cuban_missile={"usa":"united states of america",
#                "uk":"united kingdom",
#                "i":"india",
#                "c":"china"}
# cuban_missile.update({"r":"russia"})
# print(cuban_missile)

# e=1
# while e<20:
#
#     print(e)

######################################### how to create a file in python ##############################################

# import os
# file="test.txt"
# if os.path.exists(file):
#     print(f"the files access :-{file}")
# else:
#     print("not access")

# import os
# file="C:/Users/hp/OneDrive/Desktop/test.tt"
# if os.path.exists(file):
#     print(f"the access of this file is :-{file}.")
# else:
#     print("not access2")

# def new(car=10,bike=10):
#     return car+bike
# new()

# def b(a=10,d):
#     c=a*b
#     return c
# print(b(12))

s={"s":"sports",
   "b":"bikes",
   "c":"cars",
   "t":"trucks"}
def license(**ux):
    print(ux["s"],ux["b"])
license(**s)
# def card(*id):
#     return id["s"],id["c"]
# print(card(*s.values()))

def choco(v):
    return pow(2,v)
print(choco(10))

# def word(press): #### BREAK POINT ####
#     return breakpoint("power")
# print(word)

# import random
# def doremon(a):
#     g=a+random
#     return g
# doremon(g)



import random
def retail():
    f=random.randint(10,20)
    g=random.randint(30,40)
    h=random.randint(50,60)
    return f,g,h
# f,g,h=retail()
print(retail())
# print(f,g,h)
import random
def color():
    a=random.randint(10,20)
    b=random.randint(30,40)
    c=random.randint(50,60)
    print(a+b+c)
color()


d={"a":1,"b":2,"c":3,"d":4,"e":5}
key="b"
print(d["b"])
d["f"]="6"
print(d)
# print(d.update(3)) ##  update  ##



def Calc_means(a,b,c,d):
    menas=(a*b)/(a+b)
    menards=(c*b)/(c+d)
    return menas,menards
print(Calc_means(10,20,30,40))

def check(aa,bb):
    if aa<bb:
        return "true"
    else:return "false"
print(check(90,23))

def av(g):
    return sum(g)/3
print(av([10,20,30]))

def create(j):
    for k in j:
        print(k)
f=[0,13,42,13,233]
create(f)
# def creta(v):
#     for c in zip(j,v):
#         return c
# x=[1,89,324,13,14]
# f=[90,32,42,422,32,4]
# creta(x,f)

def yoyo(a,b):
    rect=1/2*a*b
    print(rect)
yoyo(19.25,98.42)
# yoyo(b=89.453)
# yoyo()

a="apple"
s="samsung"
print(a[0:3]+s[-4:])

# a=[0.1,0.2,0.3,0.4,0.5,[0.100,[1,2,[100,200,300,[1000,200,300,{"a":1,
#         "b":2,
#         "c":3,
#         "d":4}]],3,],0.200,0.300]]
# a=[0.1,[0.100,[1,2,[100,200,[1000,200,300,{"a":1,
#         "b":2,
#         "c":3,
#         "d":4}]]]]]
# print(a[1][1][2][2][3].keys())
# print(str(a[1][1][2][2][3].keys()).upper())
# print(list(a[1][1][2][2][3].values()))
# f={"z":"zoo"}
# k=list(f)
# print(list(a[1][1][2][2][3].items()).reverse())
# k.append({"f":"frog"})  #####
##### print(list(a[1][1][2][2][3]))
##### b=reversed(a[1][1][2][2][3],key=lambda m:len(m))


v=(1,2,3,4,5,6)
print(sum(v)/6)
i=(9,24,89,290,884,7)
# print(i.__gt__())
# print(i.__add__()) ### CONCATE
# print(i.__new__()
mi=[0,323,12,(90,313,12)]
ci=(903,23,{"A":"america",
            "c":"canada"})
print(mi[3][0]==ci[0])
# print(mi<ci)
l=(90,28,9,42,3)
o=(90,324,13,32,32)
# print(l|o)
# print(o^l)
# print(l&o)
# print(l+o)

# c={"s":"sports",
#    "d":"dance",
#    "m":"music",
# }
# b={"f":"fortnite",
#    "p":"pubg",
#    "for":"forza"}
# print(c|b)
# print(sorted(c|b))
# a=c.values()
# d=b.values()
# print(sorted(c.values()|b.values()))
# print(dict(sorted(c|b)).values())
# print(sorted(b|c))
# print(sorted(a,d))



print(cafe["menu"]["numb"]==cafe["menu"]["numb"]["val"])
if cafe["menu"]["numb"]==cafe["menu"]["numb"]["val"]:
    print("right")
else:print(f"i {'need some changes':.>20}")
# print(f"the lego creates {'block':.>15}")

if cafe["menu"]["numb"][2]>cafe["menu"]["numb"]["val"][30]:
    print(f"yes{'i am right':_>20}")
else:print(cafe)




# h.insert()
# print(h)
# print(type(p))

t=[1,2,3,4,5,6,7,8,9,10]
for u in t:
    if u%2==0:
        print(u)
    else:print(f"odd number:{u:.>5}".upper())
egg=0
for kaggle in t:
    egg=egg+kaggle
print(egg)

ios=[1,2,3,4,5,6,7,8,9,10]
h=5
for c in ios:
    h=h/c
print(h)
for v in ios:
    for l in ios:
        h=l-h
print(h)

y=[10,35,90,48,84,76,48,76,3]
if y[2]>y[3]:
    print(f"sum of y is {sum(y)}.".upper())
else:print(f"average of y is {sum(y)/9}.".upper())
if y[1]<y[2]:
    print(f"geometric mean of y is {y[2]*y[1]/y[3]+y[5]}.".upper())
else:
    print(f"division of y is {sum(y)//9}.".upper())

o="popcorn"
for t in o.split("o"):
    print(f"i need spacedish :{t:.>10}")
    # print(t)
for p in "popcorn".split("p"):
    print(f"i want spaces in popcorn:{p:.>10}")
    # print(p)

t=(1,2,3,4,5)
tuf=[1,2,3,4,5]
asus=5
# for h in t:
    # tuple(tuf(=tuf+h))
    # =tuf + h
    # print(tuf)
for r in tuf:
    asus+=r
print(asus)

# "tuple unpacking"
gone=[("a","b"),("a","c"),("b","d"),("c","e"),("d","e")]
for k,e in gone:
    print(f"the first letter of gone k:{k} \n       last letter of gone is e:{e}".upper())
d=[(20,30),(1,2),(10,20),(100,200),(1000,2000)]
# print(len(d))
# c=d
# for f,g in d:
#     c=f+g+c
#     print(c)
c=len(d)
f=c
for u,k in d:
    f=u+k+c
    print(f)
    # print(u)
    # print(k)
# shore=[(a,b),(c,d),(e,f),(g,h)]
# for java in shore:
#     print(str(java).upper())
# shore=[(a,b),(c,d),(e,f),(g,h)]
shore=[("a","b"),('c','d'),('e','f'),('g','h')]
# print(shore)
for k in shore:
    print(str(k).upper())

x=[(1,2),(3,4),(5,6),(7,8),(9,10)]
for u,b in x:
    if u or b2==0:
        print(f"the even number is.")
    else:print(f"the odd values is ")
x=[(1,2),(3,4),(5,6),(7,8),(9,10)]
for t,y in x:
    if t+y//5==11:
        print("right".upper())
    else:print("wrong".upper())

hi=[(1,2),(3,4),(5,6)]
for a,c in hi:
    print(c+a/3)
    # print(c,a)

for j,c,v in [("balls",23,5),("talls",25,10),("gains",10,5),("dells",4,3)]:
    print(j.upper(),c,v)
    # print(str(j),list(c),set(v))
    # print(str(j)+""+list(c)+""+set(v))

# car=[({"cars":{"t":"tesla","c":"chevorlet"},
#        "laptop":{"r":"razer","lg":"logitech"}})]
# for t,h in car:
#     print(t)



e=[10,20,30,40,50]
# for k in e:
#     if e==30:
#         print(f"average of k is:{e[2]//2}")
#         continue
#     else:print(f"sum of k:{sum(e)}")
for d in e:
    if d==30:
        print(f"average of k is:{e[2]//3}".upper())
        break
    else:print(f"sum of k is {sum(e)}")

h=[["apple",50,
    "samsung",20,
    "nothing",10]]
for k in h:
    if "a"in k[0] and k[1]>20:
        print(k)
# for j,m in h[0]:
#     print(j)
# c=[("apple",10)]
c=[["tesla",90],["cars",30],["rivian",9],["toyota",84]]
for u,o in c:
    print(u)
x=[["china",900,
    "india",124,
    "america",421]]
for t in x:
    if t[1]>t[5]:
        print(f"average of t[1[3[5]:{t[1]+t[3]+t[5]//3}")
    else:print(f"sqrt of t[1[3[5]:{t[1]+t[3]+t[5]**2}")


# print(r["fruits"])
# for y in r["fruits"]["bikes"]:
#     print(y)

d=[("donut",10,"louisana"),("chocolate",20,"toronto"),("strawberry",15,"california")]
for k in d:
    print(k[0])
for x in d:
    if d[0]==d[1]:
        print("yes".upper())
    else:print("no".upper())

if 24%2==0:
    print("yes".upper())
else:
    print("false".upper())
if 26%3==2:
    print("true".upper())
else:
    print("false")

world=[("toyota","subaru","suzuki"),("tesla","rivian","cadillac"),("hyundai","kia","mg")]
for w,o,r in world:
    print(f"i want [0] item from world:{w}.\n    i need [1] item from world:{o}.\n i acquire [2] item from world:{r}")
# for j,k,l in str(world).upper():
#     print(j)
#     print(k)
#     print(l)
for u,i,o in world:
    print(str(u).upper())
    print(str(i).title())
    print(str(o).swapcase())







# print("the life of pi is :{a:.10}".format(a=13))
# c=90
# print(f"the life of pie is {c:.>5}")

# j={"food":{"a":"apple"},
#    "pizza":{"m":"margherita"},
#    ""}

# q=[90,224]
# w=[99892,3324]
# q.append(w)
# print(q)



