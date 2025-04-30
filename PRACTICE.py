print("hello world","my name is computer",50)
print(20<30)
c=200
b=100
print(200<100)
u=90
w=20
print(u,w)
print(id(u),id(w))
print('u',w)
y="yuck"
print(y)
pratham=7
print('pratham')
a=1
b=2
c=3
print(a+b+c)
a=("apple")
b="ball"
print(a+b)
k="kolar"
g="gold"
f="fields"
print(k+" "+g+" "+f)
t=5
print(t+20)
r=40
q=23
print(r%q)
o=60
p=69
print(20%69)
"EXPONENTS"
print(2**2) #2*2
print(2**3) #2*2*2
print(2**4) #2*2*2*2
print(3**2) #3*3
a="apple"
p="phone"
print(a+" "+p)
i="iphone"
print(i)
["ASSINGMENT OPERATORS"]
c=45
print(c)
c=c+45
print(c)
c+=45
print(c)
c-=45
print(c)
d=20
print(d)
d=d+30
print(d)
d=d-10
print(d)
k=2**3
print(k)
e=35
r=50
print(e==r)
print(e<r)
print(r<e)
print(r>e)
g="giraffe"
m="monkey"
print(g+m)
x=-5,-4,-3,-2,-1
z=0,1,2,3,4,5
print(x+z)
u=5,6,7,8,9
a=1,2,3,4,5,6
print(u!=a)
aub=0,2,4,6,8,10
b=1,3,5,7,9,11
print(b+aub)
q=50500
w=100000
e=100
print(q%w/e)
t="turtle"
y=20
print(t,y)
print(id(y),id(t))
a=-5,-4,-3,-2,-1
b=0,1,2,3,4,5
print(a,b)
c=-10,-20,-30,-40
d=-50,-60,-70,-80,-90
print(c>d)
s=50
print(s+50)
a=50
b=60
print(id(a),id(b))
print(a+80)
U=-100,-99,-98,-97,-96,
A=95,94,93,92,91
print(U+A)
B= -10,-9,-8,-7,-6,5,6,7,8
C= 5,6,7,8,9,10
print(B,C)
print('B','C')
T="TOY"
B=5
print(T,5)
c=78
d=30
print(c!=d)
print(c<d)
print(c>d)
c='abc'
d='def'
print('c','d')
print(c+" "+d)
print(id(c),id(d))
a=24
b=2
print(a/b)
print(a**b)
print(b**a)
c=a+2
print(c)
print(c/b)
print(c*b)
d=c/a
print(d)
pv= 50500
r=10
t=5
print(pv/r)
print(pv/r*t)
print(pv*r/t)
u=0,1,2,3,4,5
v=-5,-4,-3,-2,-1,
print(u+v)
q=8/40
w=2*60
a=q-w
print(a)
s=a/w*q
print(s)
d=q+w-a*s
print(d)
d=96.27
e=q+w-a*s/d
print(e)
m="mcdonald"
b="Burger"
print(m,b)
print(id(m),id(b))
Name= "my name is pratham"
age=21
gender="male"
print(Name)
print(age)
print(gender)
"EXAMPLE" "NAME"
name=("pratham")
" FIND INDEX"
sentence="the boy plays the cricket"
print(sentence[4])
sen2="monkey climbs the tree"
print(sen2[0:12])
sen3="girls cannot play cricket"
print(sen3[0:25])
om,laksh,ram = 28,45,89
print(om*laksh*ram)
print('ram',45)
"NAMING"
u="umbrella"
r="%s is red color"
print(r % u)
c="%s is the president of country"
print(c %("kim jong un"))
d="%s barks Against the theif"
print(d%("dog"))
print(d[3:16])
o="%s is the optimistic player"
print(o %("pratham"))
print(o[7])
pratham,om,mann = 65,54,34
print(pratham+om-mann)

print('hello','stringint')

o=[("donald",78,"businessman"),("biden",89,"president"),("bush",90,"citizen of usa")]
for a,b,c in o:
    print(f"{a}:{b}:{c}".upper())
names,ages,roles=zip(*o)
print(names)
print(ages)
print(roles)

d=[1,0,23,9,48,89,45,89,56,89,35,32,42,34]
print(sorted(d))
print(d.count(89))
for j in d:
    if j==48:
        break
    print(j)

g=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for q in g:
    if q==7:
        break
    print(q)
# while q[3]<40:
#     q=q+2
#     print(q)

q={1,2,3,4}
w={3,4,5,6}
print(q^w)
print(q|w)
print(q&w)
q.remove(3)
print(q)
q.pop()
print(q)

a={1,2,3,4,5,6}
a.remove(5)
print(a)
a.update({7})
print(a)
a.add(8)
print(a)
print(len(a))
print(sum(a))
print(bin(sum(a)))
print(oct(max(a)))
print(hex(min(a)))
g=90.89
print(bin(int(g)))
print(int(g))

# n=int(input("numbers: "))
# m=float(input("numbrerss: "))
# o=n+m
# print("the bin of the sum is",bin(int(o)))


a=90
b=90.89244
c=a+b
print(bin(int(c)))

print("html")

def k(name="pratham",last_name='patel',cars="luxury"):
    print(f"{name}:{last_name}")
    print(f"i have a so much {cars} in my basement.")
k(name="tony",last_name="stark",cars="vintage cars")

# a=~4 ###############################################   how i get -1 ??? ##############################################
# b=a+4
# print(b)


def general():
    print("bangladesh")
    print(sep="//")
    print("army",end=" ")
    print("controls")
    print(sep=" ")
    print("the whole country.".split())
general()

def india():
    print("india","\n  will","\n  reach","\n  three","\n   dollar","\n   economy.")
india()

def create_sentences_with_n_word():
    print("israel")
    print("\nand")
    print("\npalestine")
    print("\nstill")
    print("\nfighting")
    print("\nfor",end=" ")
    print("\none")
    print("\npiece")
    print("\nof")
    print("\nland.")
create_sentences_with_n_word()


x=["donald lu","donald trump","new york","united","kingdom","hong","kong","china","tariff"]
c=[34,90,3578,45,78,35589,245,7882,34853,78822,48842,24,5,54,4,65,657]

for h in zip(x,c):
    print(list(str(h)))
    if "n" in list(str(h)):
     print("true")
else:print("false")
if "china" in x:
    print("yes")
else:print("no")


t=[("mortal",34,"gaming"),("dell",907585,"computer making"),("asus",889345,"asus wth dixon")]
company=pincode=production=t
print(f"{company}:{production}")


def i(k="k.k",a="antartica"):
    print(f"{a}")
    print(f" tv".upper())
    print("show")
    print("  is")
    print("famous")
    print("  in")
    print("netflix")
i(a="american")

def name_fun(first_name):
    print(first_name + " mustang")
name_fun("ford")
name_fun("tata")
name_fun("volsvaken")
name_fun("hyundai")


def parent_company(first_company,second_company):
    print(first_company+","+second_company)
parent_company("bajaj auto","bajaj housing finance")

def  company(second_company):
    print("tata --->  ".upper() + second_company)
company(second_company="tata motors")
company("tata power")
company("tata steel")
company("tata chemicals")
company("tata investments")
company("tata elxsi")

def firms(label_company,back_name):
    print(label_company+" <--- "+back_name)
    print(label_company+" <--- "+back_name)
    print(label_company+"<---"+back_name)
firms("adani","ports")
firms("tata","sons")
firms("l&t".upper(),"construction")

def naam(fname,surname):
    print(fname+" "+surname)
    print(fname+" "+surname)
naam("pratham","patel")
naam("om","patel")

def u(firm="leaders",enterprise="company"):
    print(f"{enterprise}={firm}".upper())
    print(f"{enterprise}={firm}".upper())
    print(f"{enterprise}={firm}".upper())
u(firm="jeff bezoz",enterprise="amazon")
u(firm="sundar pichai",enterprise="google")
u(firm="elon musk",enterprise="tesla")

def ceos(company,leaders):
    print(company+"..."+leaders)
    print(company+"..."+leaders)
ceos("reliance","mukesh ambani")
ceos("bajaj","rajeev bajaj")

def huge(c,cc):
    print(c+" "+cc)
huge("tata","salt")
huge("hindustan","unilever")

print(67%23)
print(229%14)

"financial management"

m=239995
r=8
print(1+8/m*5)
print(bin(int(1+8/m*5)))
print(oct(int(1+8/m)))
print(hex(int(1+8/m)))

def num(value,float):
    print(hex(int(value+float)))
    # print(oct(int(value+float)))
num(23,89.45)
num(344,90.23444)

def illustration():
    return "india is bigger than america in world"
print("china is a enemy of united states of america.")


d="donald trump"
for k in d:
    if "d"==d:
        print("yes")
    else:print("no")
if "d" in d:
    print("valid")
else:print("invalid")


h=["hong","kong","uunited","states","america","united","kingdom","china"]
if "o" in "hong":
    print("yes")
else:print("no")
if "h" in h:
    print("true")
else:print("false")


def bogo(dis,food):
    print(f"{dis} {food}")
bogo("buy 1 get 1 free","on the pizza")
def of(offers,items):
    print(f"{offers} are applied on the specilised  {items}")
of(offers="coupons",items="foods")


y=[3,2,4,5,1]
g=y.sort()

a=2
b=3
print(a**b**a)

print(12**2) # square
print(12**0.5) # square root
print(12**3) # cube
print(12)

# nu=int(input("enter number to find square : "))
# square=nu**2
# print("square of {} is {}".format(nu,square))

p="PythonHub"
result=p[::-1].lower()
print(result)

n='narendra modi'
a=n[::-1].upper()
print(a)


d="donald trump"
d.replace("joe","biden")
print(d)
print(d.strip())
print(d.replace("donald","biden"))
print(d.replace("donald","mcdonald"))
print(d.replace("trump","rum"))
print(d.replace("donald","do"))
print(d.split(","))
f=d.split(",")
print(f)
print(type((4+2)*6-1))
print(((4+5)//9-2))
print(hex((999+2334)-90+2542))



# pi=340/123
# radius=2.2
# area=pi*(radius**2)
# print(area)
# circumference=pi*(radius*2)
# print(circumference)


thesis="there is a man who sitting on the bench and drink water from his bottel."
print(thesis.split())
print(thesis.replace("man","women"),thesis.replace("his","her"))
print(thesis.replace("man""his","women""her"))


# file="txt,txt"
#
# f=open(file,r)
# print(data)
# f.close()
#
# with open(file,"r")as f:
#     data=f.read()
#     print(data)

def t(g,p):
    print(g+" "+p)
t(g="games",p="personal computer")

def cop(f="firms",l="location",person="leaders"):
    print(f"{f} ---> {l} === {person}".upper())
cop("tata","gandhinagar","ratan tata")
cop("reliance","jamnagar","mukesh ambani")
cop("tesla","texas","elon musk")
cop("facebook","california","mark zuckerberg")

def animes(j):
    print(j+".anime")
animes("japan")
animes("dragon ball z ")
animes("naruto")
animes("mayblade")


# countries_with_leaders=("russia","putin"),("america","joe biden"),("india","rahul gandhi"),("france","macron"),("austrialia","anthony albanese")
# for a,b in countries_with_leaders:
#     print(a.upper())

def default(d="dj",s="songs"):
    print(d+" plays his "+s+" song in france club.")
default("dj snake","magenta riddim")

def h(r="red",b="blue"):
    return "when bull see "+r+" color \n   he/she run so fast\n      but when he/she saw "+b+" color\n        they can get cool effect."
a=h('red',"blue")
print(a)

def ipo(*listing_gains):
    print(listing_gains[3]+" is a listing gain ipo for\n             investors.")
ipo("bajaj housing finance","tata technologies","namo e-waste","premier energies ")

def actors(*models):
    return models[2]," has good personality in film industry."
print("siddharath malhotra weds with kiara advani.")

asd=[89,90,234,444,{"names","ages"}]
aws=(90,23,324,2,42,["cities","villages"])
if asd[4]==aws[5]:
    print("true")
else:print("false")

if asd[1]==aws[0]:
    print("true")
else:print('false')

def k(*batteries):
    print(batteries[2]+" are connected with ",end=" ")
    print("laptops.")
k("phone chargers","car chargers","laptop chargers")

def dramas(*tv_shows):
    print(tv_shows[1]," was  famous in india.")
dramas("bigg boss","tmkoc")

def g(sports,leaders,brands):
    print(f"{leaders} is famous in {sports}\n        he is brand ambassador of {brands}.")
g(sports="cricket",leaders="virat kohli",brands="puma")

def g(names,values):
    print(names+" are matches with "+values)
g("companies","revenue")

def brands(laptops="dell",phones="apple"):
    print(f"{laptops}  brand does not compare with {phones}.")
brands(laptops="asus",phones="samsung")


def n(spell1,spell2,spell3,spell4,spell5):
    return spell1<spell4 or spell5>=spell2
d=n(90,34,24,23,4)
print(d)

def num(war,war1,war2,war3,war4,war5):
    return war-war5//war4+war3+war1|war2*4
ss=num(45,89,23,11,566,89)
print(ss)

rows=6
for i in range(rows):
    for j in range(i):
        print(i,end=" ")
    print(" ")

rows1=10              ##################################################################################################
for s in range(rows1):
    for k in range(s):
        print(s,end=" ")
    print(":")

r=4
for u in range(r):
    for j in range(u):
        print(u,end=" ")
    print(" ")

g=[1,2,[3,4],(22,399,34,4,4,2),{"pratham":"stand chart"}]
print(g[3][1])
print(g[0:4])
print(g[::-1])
print(type(g[4]))
print(g[::-1])
print(sorted(g[3]))
print(sum(g[2]*2))
g.reverse()
print(g)


for k in range(1,11):
    if k%2==0:
        continue
    print(k)

for a in range(10,30):
    if a==15:
        break
    print(a)

for r in range(10,30):
    if r==20:
        continue
    print(r)


post=[12,90,34,[556,89,345,89,24524],999,4533]
for demat in post[3]:
    print(list(str(demat)))
    print(post[3].count(89))
    print(sum(post[3]))
for h in post:
    print(sum(post[0:3]))

f=[1,2,3,4,5,6,7,8,9,10]
for k in f:
    print(k+3)
print(k+5)
print(sum(f))

for g in range(55,65):
    if g==58:
        break
    print(g)
for j in range(30,40):
    if j%3==0:
        print(j)

for pant in range(1,20):
    if pant==14:
        break
    print(pant)

for a_b_c in range(90,100):
    if a_b_c==94:
        continue
    if a_b_c==98:
        break
    print(a_b_c)

free_fire=[1,2,3,4,5,6,7,8,9,10,11,12,14,13,15,67,77,77,8,8,88,8,54654654654,6]
print(set(free_fire))

for pubg in free_fire:
    if pubg%2==0:
        break
    if pubg==15:
        continue
    print(pubg)
for cod in free_fire:
    if cod==10:
        break
    if cod==77:
        continue
    print(cod)
for jk in free_fire:
    if free_fire[5]<free_fire[9]:
        print("true")
    else:print('false')

if free_fire[15]>=10: ####################### i set this example for me #####################################
    print("2")
elif free_fire[2]>=8:
    print("8")
elif free_fire[4]>=6:
    print("6")
else:print("nothing")


for t in range(0,5):
    print("hello"[0:4].upper())



if (3>2):
    print("true")
else:
    print("false")

if {5>=3}:
    print("es")
else:
    print("no")

if [2,9,23,3,4]<=[1,90,234,4,42]:
    print("yes")
else:print("no")

axe=[1,0,34,24,4,24,53,(90,89,345,435,5,35),{"pewdiepie":"t-series"}]
print(axe[7].index(345))
print(axe[7].__contains__(24))
print(axe[::-1])

aaa=[1,2,3]
e=aaa.insert(1,4)
print(e)


def h(p="phones",c="charges"):
    print(f"{p} have so much\n       {c} people carry all the the time.")
h(p="phones",c="radiation")


g=1+9j
g+=g
print(g)

f=9+3j
f+=f
print(f)

a=56.90
a+=a
print(a)

d=1+2j
d+=d
print(d)

op=2+3j
op+=op
print(op)

h=-6
j=-2
print(h+j)

d={"a":1,"b":2}
result=d.pop("b")
print(result)

f=[23,90,455,895,66,45,4,{23,9,34,2,45},(12,99,54,55,5)]
g=f[7].remove(45)
print(f)
gg=f[7].update({100})
print(f)
h=f[7].update({11})
print(sorted(f[7]))

e=1
while e<5:
    e=e+1
    print("om")
d=1
while d<10:
    d=d+1
    print(d)

def principles(p="p",o="o",d="d"):
    print(f"principles of management has three features :- 1){p}  2){o}  3){d}")
principles("planning","organising","directing")

def mobile_games():
    return " most of the people play mobile games."
print("teenagers play mobile games & they  get negative effect.")

def movies(t):
    print(t+" cruise")
movies(t="tom")
movies(t="thomas")
movies("tollin")
movies("telco")
movies("tata")

def awards(national):
    return  national+" trophy"
awards(national="grammy")
awards(national="anthem")
awards(national="awards")
awards(national="president")
awards(national="citizen")
f=awards(national="national")
print(f)


def j (a,b,c,d):
    return a+b-c//d**2
k=j(20,1,4,58)
print(k)

def flow(lk,studio):
    return lk+studio
studio=flow(20.89,45.90)
print(studio)

def problems(complex,float):
    return complex+float
solve=problems(56+9j,45.23)
print(solve)

def add_num(num1,num2):
    return num1+num2
l=add_num(4,5)
print(l)

def result(q,w):
    return q+w
my=result(9,8)
print(my**2)
print(type(my))

def even_num(number):
    return number %2==0
f=even_num(20)
g=even_num(21)
print(f)
print(g)

def odd_num(num):
    return num%2==0
a=odd_num(10)
b=odd_num(12)
print(a)
print(b)


q=[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for k in q:
    if k%2==0:
        print(k)
# else:print("nothing")

def od(val):
    return val%2==0
v=od(100)
b=od(200)
print(v)
print(b)

def plus_minus(aa,bb):
    print(aa+bb)
    return aa+bb
cc=plus_minus(20,30)
plus_minus(40,50)

def h(a,b,c,d): #######################33 NEW START #####
    print(str(a-b//c+b))
    return str(a-b//c+b)
i=h(20,10,-10,-50)
h(10,30,90,50)


def mix(name,age):
    return name,age
d=mix("pratham",34)
print(set(d))

def bo(a,n,m,d):
    print(a==m or n==d)
    return n==m or d==m
qw=bo(45,90,23,89)
bo(12,90,233,45)


def a(*animals):
    print(animals[2]+" is a holy cow of india")
a("dog","cat","cow")

def square(numbers,values):
    print(f"{numbers} ---> {numbers}")
square(2,2)


def key(names):
    print("hyundai "+names)
key("creta")
key("verna")
key("alcazar")

def lights(l="l",r="r"):
    return f"{l} {r} shot is a difficult for the soldier."
c=lights("long","range")
print(c)

def creators(v="video creators"):
    print(f" graphic {v} are best for marketing.")
creators("creators")


def offers(m="com",c="mo"):
    print(f"{m} is free with {c}")
offers("mouse","computers")
offers("keyboard","laptop")
offers("graphic card","processor")

def services(s,w):
    print(f"{s} is free with {w}\n        because it gives",end=" ")
    print("compliment")
services("soda","whiskey")


rows1=10
for s in range(rows1):
    for k in range(s):
        print(s,end=" ")
    print(" ")

rows=5
for t in range(rows):
    for l in range(t):
        print(t,end=" ")
    print("")

def j(m,n):
    return bin(m+n)
f=j(34,90)
print(f)

def math(i,o,p):
    return  i+o*p
d=math(-5,-90,-500)
print(d)

def bowlers(b):
    print(f"{b} takes 400 wickets in his test career.".strip())
bowlers("bumrah")

print("ashwin made century in india vs bangladesh match".strip(" "))

def post(b,c):
    print(b+c)
post(10,20)

def fault(u=89,i=12,o=30):
    print(u+o+i)
fault(90,34,12)


def string(o=90,q=23):
    print(o+q)
string("23","45")

d=[90,4,22,12,{20,30,40,12,14,5}]
f=[90.90,892322,892324,8824,{25,35,40,5,10,12}]
print(d[4]^f[4])
print(d[4]|f[4])
print(d[4]&f[4])

print("narendra modi go to usa".split())

# q=[1,2,3,4,5,6,7,8,9,10]
# for l in q:
#     if l%2==0:
#         print(l)
#     if l[3]%2==0:
#        print(l)
    # for n in q:
    #     print(n+20)

f=[1,2,3,4,5,6,7,8,9,10]
for k in f:
    print(k+10)
print(k+100)
print(sum(f[0:4])/2)


def shanto(x,y):
    return (x+y)
kq=shanto(10,45)
print(complex(kq))
print()

def g(op,ios):
    return op//ios
df=g(23,90)
print(df)


rows=5
for r in range(rows):
    for k in range(r):
        print(r,end="")
    print("")
d=[1,2,3,4,5]
print(d[::-1])


f={"k1":[1,2,{"k2":["this is trichy",{"tough":[1,2,["hello"]]}]}]}
print(f["k1"][2]["k2"][1]["tough"][2][0].upper())


hi=-5,-4,-3,-2,-1
ho=0,1,2,3,4,5
print(hi+ho)

rows2=-5
for d in range(rows2):
    for i in range(d):
        print(d,end="")
    print("")

def sector(q,w,e,r,t,y):
    return q+r/e-t//w%y
f=sector(12,90,44,89,456,-90)
print(f)


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



def sentences123(lines):
    for k in lines:
        if k[0]=="p":
            return True
        else:return False
c=sentences123("pratham")
print(c)

def trees(banyan):
    wood=banyan.split()
    return wood[0]==wood[0]
mango=trees("apple")
orange=trees("neem")
print(mango)
print(orange)



# def r(list_values):
#     for v in list_values:
#         if v[4]==3:
#             return True
#         else: return False
# x=r([1,2,3,4,5])
# print(x)


# p="pratham patel"
# for n in p:
#     if n[6]=="m":
#         print("true")
#     else:print("nottingham")


# print(bool(21%2==0))
# print(bool(not 200%3==0))


# def g(numberq):
#     r=numberq%2==0
#     return r
# h=g(25)
# i=g(20)
# print(h)
# print(i)
#
# def f(numios):
#     q=numios%2==0
#     return q
# aws=f(90)
# awse=f(20)
# print(aws)
# print(awse)
#
# def kl(val):
#     return val%3==0
# d=kl(27)
# f=kl(295)
# print(d)
# print(f)
#
#
# def russia(num_list):
#  for k in num_list:
#      if k%2==0:
#          return True
#      else:return False
#      jk=russia([1,3,5])
#      abc=russia([2,4,6])
#      vbn=russia([2,1,1,1])
# print(jk)
# print(abc)
# print(vbn)





# def even(values):
#     for t in values:
#     if t%2==0:
#      return true
#            else:pass
#          return false


# def check_even(numbers):
#     for num in numbers:
#               if num%2==0:
#         return true
#     else:pass
#     k=check_even([1,2,3,4,5,6,7,8,9,10])
#     j=check_even([1,1,1,1,1,1,1,11,1])
#     print(k)
#     print(j)


# def sen(sent):
#     return "sentences"%2==0
# b=sen("sen")
# c=sen("sente")
# print(b)



# def print_result(a,b):
#     print(a+b)
#     return a+b
# print_result(10,5)
# return_result(10,5)










# def list(a=[1,2,34,4,5,99,34535,5,3,646,44,646,5,564,53,4,24,35,]):
#     for j in list(a):
#         print(j)
#         print(list())
#     list(a)


# for kl_rahul in range(20,35):
#     if kl_rahul+3:
#      print(kl_rahul)
# for l in g:
#  if g[3][5]==g[1]:
#     print("true")
# else:print("false")

# d="donald trump"
# print(d.replace("donald","don-key"))
#
# p=[1,2,3,4,5,6,7,8,9,10]
# p.reverse()
# print(p)






# for k in g[3]:
#     print(sorted(g[3]))
#     print(max(g[3]))
#     print(sum(g[3]))











