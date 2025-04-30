# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 13:49:07) [MSC v.1938 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> print(" Hello World")
#  Hello World


# print("the complex numbers in decimal %5.34"%(23+8j))

f=[]
g=f.append(1)
print(g)

d=(90,242,5)
h=[1213,242]
h.append(d)
print(h)





gam=[1,2,44]
fgs=[1,23,4]
gam.append(fgs)
print(gam)
game=[0,4,21]
fame=[3,2,1]
# fame.insert(1,game)
# print(fame)
fame.extend(game)
print(fame)


print("first:{b},second:{c},third:{a}".format(a=1,b=2,c=3))
print("game:{0},fame:{1},politics:{2}".format("gta","kareena","bollywood"))
b=90
v=90
c=90
print(f"{b}:{c}:{v} are the same value")
print("{m} makes more {m}.".format(m="money"))
print("{0:7}& {1:9}".format("fruit","quantity").upper())
print("{0:10}& {1:6}".format("apple",23.))
print("{0:10}& {1:6}".format("pineapple",21))


colun=5
ro=4
f="#"
for b in range(colun):
    for l in range(b):
        print(f,end=" ")
    print()
c=5
r=5
o="!"
for v in range(c):
    for n in range(v):
        print(o,end=" ")
    print()
print()

for i in range(c):
    for m in range(r):
        print(o,end=" ")
    print()
print()



# def equal(a,b):
    # return a[0]==b[0]
# print(equal(a=[1,23,4,5]))
# print(equal(b=[1,2,5,6]))



# c="citadel has create more spy series all around the world"
# for b in c.split("a"):
#     if len(b)%2==0:
#      print(b)
u="united states of america set up the isreal to fight with arabs"
for r in u.split("t"):
    if len(r)%2==0:
        print(r.upper())
for l in u.split():
    if len(l)%2==0:
        print(l.upper().split("a"))

print("the intergers with:%6.1f"%(12.342))
print("the numbers with point:%5.4f"%(90.133))



def g(bb,cc):
    for k in bb:
        for v in cc:
            if k%2==0:
                return "YES"
            if v%3==0:
                return "ACC"
            else: return "KCC"
print(g([2,4,6],[1,3,5]))

def jk(mumbai):
    for pune in mumbai:
     if pune%2==0:
        return "NCC"
    else: return "ACC"
print(jk([1,2,3,4]))

f={19,24,12,12}
f.difference()
print(f)
for n in f:
    print(n)
for v in f:
    if 19 in f:
        print("y")
    else:print("n")

for t in range(1,9):
    print("hello"[0:4]*5)

for k in range(1,10):
    if k==5:
        continue
    if k==7:
        continue
    print(k)

# print("the %s of %s newspaper print in %s")
print("the %s of india in india"%"times")
print("the times of %s in %s"%("india","india"))

f=[10,20,30,40,50,60,70,80,]
for m in f:
    if m==30:
        continue
    if m==60:
        break
    print(m)

fgh=[[2,4,6],
     [8,10,12],
     [14,16,18]]
for c,v,b in fgh:
      print(f"{c} --> {v} --> {b}")
      pass
print("{a:.2f}".format(a=c))
print("{b:.2f}".format(b=c))

# for t in range(1,5):
#     for k in range(8,15):
#         for l in range(11,16):
#             combine=zip(t,k,l)
#         print(combine)
#

f=[range(1,5)]
d=[range(6,10)]
s=[range(11,15)]
fbi=list(zip(f,d,s))
print(fbi)

def pov(keyboard):
    return keyboard[0]==keyboard[0]
print(pov("google cloud"))
print(pov("amazon web services"))

def cpu(mouse):
    print(f"{mouse[0]} : {mouse[0]}")
print(cpu("google cloud"))
print(cpu("amazon web servies"))

def mouse(wired,inout):
    print(f"{wired[0]}:{inout[0]}")
print(mouse("tesla","facebook"))

def h(elephant):
    jungle=elephant%2==0
    return jungle
print(h(6))
print(h(7))

def b(ball):
    for c in ball:
        if c%2==0:
            return "YES please"
        else: return "NO please"
print(b([2,4,6]))
print(b([3,5,7]))

def v(c,v):
    return c[0]==v[0]
print(v([1,2,3],[4,5,6]))

def z(x,y):
    print(f"{x[0]} | {y[0]}")
z([1,2,3],[4,5,6])

def zoo(giraf,lion):
    if giraf[0]==lion[0]:
        return "OHH YEAH !"
    else: return "OOH NO !"
print(zoo([1,2,3],[4,5,6]))

def words(alpha,tiger):
    return alpha[0]==tiger[0]
print(words("jungle","tiger"))

# def ms(l,k):
#     for n in zip(l,k):
#         if n%12==0:
#             return "boom".upper()
#         else:return "fuss".upper()
# print(ms([2,4,6,8,10,12,24,36],[80,10,122,124,150]))

def again(u,i):
    for k in u:
        for l in i:
            if k%2==0 or l%3==0:
                return "ooh yeah !".upper()
            else: return "ooh no".upper()
print(again([2,4,6,8,10],[1,2,3,4,5,6,7,8,9]))


print("%s tralier will release today"%"sin\tgham\tagain")

def gh(o,p):
    if o and p%5==0:
        return min(o,p)
    else:return max(o,p)
print(gh(12,24))
print(gh(60,96))


def v(p):
    return chr(p+90)
print(v(10))

def v(op):
    return op+0.34
print(v(0.12))


def b():
    print({"name":"pratham",
           "age":23,"profession":"student",
           "height":180,"weight":"78"
           })
b()

def r(m,t):
    f=m.split() and t.split()
    return m[0]==t[0]
print(r("double","triple"))

def mi(o,p):
    fmcg=o.split() and p.split()
    print(f"{o}       {p}")
    print(f"{o[0]} == {p[0]}")

print(mi("undertaker","brock lesnar"))

print("decimal numbers:%1.5f"%(112.12))

print("decimal number :%1.1f"%(89.1234556))


def d(op):
    s=op.split()
    return op[:3].upper() and op[3:].title()
print(d(" kashmir"))

p="pratham"
for v in p:
    print(v.split())

def b(k,l):
    if k%2==0 and l%2==0:
        return min(k,l)
    else:return max(k,l)
print(b(10,11))
print(5,7)

def r(m,n):
    return m+n==20
print(r(9,10))
print(r(10,10))

def v(i,o,s):
    return i+o+s==33 or i==33 or o==33 or s==33
print(v(11,11,11))
print(v(12,13,12))
print(v(11,11,11))

def v(o):
    if len(o)>3:
        return o[:3] + o[3:].upper()
    else: return "failed".upper()
print(v("tacobell"))

def n(l):
        return l[3:].upper() + l[:3]
print(n("united"))

def m(o):
    return o[:4].upper()+ o[3:]
print(m("sovietunion"))

def x(u):
    if len(u)>3:
      return u[:3].upper().split()+u[4].split()+u[3:].upper().split()
print(x("tupperware"))

def v(m,k):
    return m[:3].upper().split()+k[3:].upper().split()
print(v("disney","wonderland"))

def b(o,p):
    return o[3:].upper().split("n")+p[:3].upper().split("n")
print(b("disney","wonderland"))

def h(p,a):
    return p[:4].upper()+"  "+a[3:].upper()
print(h("flipkart","amazone"))

def r(i,o):
    if len(i)>5 and len(o)>3:
        return i[:4].upper()+o[4:].upper()
print(r("wonderland","disney"))

def r(a):
    while a<10:
        a+=1
    return a
print(r(1))


def a(p,m):
    return p[0:4].upper().split()+m[:3].upper().split()
print(a("phanton","boyfriend"))

def c(i,b,m):
    return chr(i*b*m) and oct(i+b+m) and hex(i-b-m)
print(c(20,10,10))

def s(i,o,s):
    print(chr(i*o*s),oct(i+o+s),hex(i-o-s))
s(20,10,10)

def r(l):
    for v in l:
        if v%2==0:
           return v
print(r([1,2,3,45]))

def asd(g):
    for t in g.split():
        if len(t)%2==0:
            return t
print(asd("python programming language created by guidda van russo"))

h="hero financial corporation is a parent company of hero motor corporation"
for m in h.split():
    if len(m)%2==0:
        print(m)
v="russia brazil south africa india china have decided to fight against dollar"
for l in v.split("a"):
    print(l.upper())

def a(u):
    print(f"the a number of f string is {u:.2f}".format(u))
a(29.3453242)

def a(o):
    return o%12/10
print(a(12.000))

def q(v,l):
    if v%5==0 and l%2==0:
        return min(v,l)
    else:max(v,l)
print(q(10,10))
print(q(40,400))

f=1
while f<10:
    f+=1
    print("hello"[0:4].split()*3)
c="carlos cat stay stay in house"
for b in c.split():
    if len(b)%2==0:
        print(b)

def a(c,d):
    if c%10==0 and d%12==0:
        return min(c,d)
    else:return max(c,d)
print(a(9,8))
print(a(24,36))

def kj(o,l):
    if o%4==0 and l%5==0:
        return max(o,l)
    else:return min(o,l)
print(kj(16,20))
print(20,100)

def r(i,m):
    if i//2==0 and m//3==0:
        return max(i,m)
    else: return min(i,m)
print(r(10,9))
print(r(100,400))

def b(x):
    if x//2==0:
        return min(x)
print(b(4))
print(8)




def v(*u):
    for t in u:
        print(t)
print(v(10,20,30,40,50,40.213,3242,422,323))

def c(*i):
    for g in i:
        return g
print(c(100,200,300,400,500,600,32.34,234.434,45))

def a(*h,**pa):
    print(h)
    print(pa)
a(100,200,300,gender="male",bread="whitegrain")

def c(a):
    for l in a.split():
        if len(l)%2==0:
         return l.upper()
c("elon musk joins hand with donald trump")

def v(l):
    for a in l.split():
        if len(a)%3==0:
            print(a.upper())
v("elon musk join hands with donald trump in united states america of presidential election")

def back(m):
    return sum(m)
print(back([1,2,3,4,5]))

# def pov(a,l):
#     return sum(a,l)
# pov([1,2,3,4,5],(10,20,30,40,50))

def c(b,d):
    print(b,d)
c([1,2,3,4],[10,20,30,40])

def r(t,y):
    return t,type(y),y
print(r([10,20,30,40],{100,200,300,400,500}))

# def v(*abc):
#     return abc
# v("fruits","rahul","raw","mango","old","man","young","boy")

def j(*o):
    print(o[3]+o[5])
j(3,4,9,1,2,3,4,2,2,1,2,3,248,2532)

def n(*p):
    return (p[0][0:3].split()+p[1][0:4].split())
print(n("donald","united","trump"))

def m(*v):
    return v[0]+v[1]+v[2]
print(m(12,34,45))

def r(mit):
    if mit%2==0:
        return
print(r(2))

def asp(a,b,c):
    print(a,b,c==b,c,a)
asp(10,20,30)

def c(j,k,l):
    print(f"{j},{k},{l} == {k},{l},{j},{l},{j},{k}")
c(1,2,3)

# def b(m,o):
#     for k in m:
#         for t in o:
#             if k%2==0 and t%2==0:
#                 return min(k,t)
#             else: return max(t,k)
# print(b(1,2),(8,9))

def c(a,s): #########################################################################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    if a%2==0 and s%2==0:
        return min(a,s)
    else:return max(a,s)
print(c(10,12))
print(13,15)

def burger(a,q):
    return a[:3].upper().split()+ q[-4:].upper().split()
print(burger("imagicca","wonderland"))

def x(cv,nm):
    return cv[-2:].upper().split()+nm[0:3].upper().split()
print(x("chicago","texas"))

def c(m,n):
    return m+n==-1 or m==-1 or n==-1
print(c(10,1))
print(c(-1,2))

def a(z,f):
    return z+f==20 or z==20 or z==20
a(10,20)
a(3,2)

def o(l,v):
    c=l+v
    return c
print(o(10,20))

def a(m,d):
    if m%2==0 and d%2==0:
        print(max(m,d))
        print(min(m,d))
a(10,20)
a(30,55)

def c(l,a):
    return l+a
print(c(100,20))

def a(k,l):
    return k-l
print(a(1,2))

def j(i,o,p):
    return i[:2].upper().split()+o[:3].upper().split()+p[-2:].split()
print(j("united","states","america"))

def a(c,a):
    return c**a
print(a(12,2))

def m(o):
    if o%2==0:
        return o
print(m(12))
print(m(11))

for n in range(2,4):
    for l in range(1,3):
        print(l,end=" ")
    print()

d="donald trump"
for m ,n in enumerate(d):
    print(f"{m}:{n}")

# a=[1,2,3,4,5]
# b=[6,7,8,9,10]
# for x,n,m in enumerate(zip(a,b)):
#     print(f"{x} --> {n}")

def j(a):
    for l in range(1,5):
        print(a)
j("hello")

def a():
    n=3
    for g in range(n):
        print("hello"[0:4].upper())
a()

###### ADVANCED DEF ########
def short_long_words(word_lists):
    shortword=min(word_lists,key=len)
    longword=max(word_lists,key=len)
    return shortword , longword
asap=["apple","dictionary","united states america","cuba","fiji"]
result=short_long_words(asap)
print(result)

def num(valuelists):
    short_num=min(valuelists)
    long_num=max(valuelists)
    return short_num and long_num
fbi=[1,2,100,30000,13,23,242,32,42,3]
m=num(fbi)
print(m)

def g(jk):
     erd=min(jk,key=len)
     erf=max(jk,key=len)
     return erd.upper() and erf.upper()
jkl=["apple","samsung","triple","double","china"]
l=g(jkl)
print(l)

def v(o=3):
    for l in range(o):
        print("python")
v()

def fruits(virat):
    short_veg=min(virat,key=len)
    long_veg=max(virat,key=len)
    return short_veg , long_veg
vegetables=["tomatoes","potatoes","cauliflower","lady finger","onion"]
t=fruits(vegetables)
print(t)

def g(forest):
    jungle=len(forest)
    return jungle
f=["apple","pineapple","watermelon","papaya","kiwi"]
d=g(f)
print(len(f[1]))

# s=["apollo","forest","elephant"]
# print(len(s[0]))

b=["blue label","red label","scotch whisky"]
for a in b[0:8]:
    print(a[2].upper()*4)

# f="blood bank","blood group","banking sector"
# for l in f[-4:]:
#     print(l[0][-4:].upper()*3)

for g in "string"[0:4]:
    print(g.upper()*3)
    print(sep="/")

s="string"
d=[]
for j in s:
    d.count(s)
    print(s)

a="america"
f=[]
v=[1,2,34]
for k in a:
    f.extend(v)
    print(f)


count=0
q=[1,2,3,4]
w=[5,6,7,8]
for j,k in zip(q,w):
    print(f"( {count} ) {j} * {k} = {j*k}")
    count+=1

def c(p):
    a=len(p)
    return a
l="sport","cricket","football"
qwert=c(p)
print(qwert)

i={"a":"asia",
   "c":"china",
   "i":"india",
   "p":"pakistan"}
for b in i.keys():
    print(b.upper())
for t in i.values():
    print(t.split("a"))
for c in i.values():
    print(c.title())

def v(*o):
    print(o[0]+10)
v(10,20,10)

def r(*n):
    print (n[1]+3)
r(10,-20,1,-2)

def m(**k):
    print(k["d"]+" are sitting on the roads")
m(d="dogs",c="cats",co="cows")

def v(x,o,p):
    return x[0:3].upper().split()+o[3:5].upper().split()+p[-2:].upper().split()
print(v('chicago',"chicago","chicago"))

def v(m,c,b):
    return m[0:3].split()+c[0:4].split()+b[-4:].split()
print(v("california","new york","korea"))

def x(n,m):
    return n[0:3].upper().split(),m[0:5].upper().split()
print(x("president","prime minister"))


a=[1,22]
a.extend(g)
g=["lkj,dd"]
print(a)

p=["oops","plkis"]
s=[1,2,3]
p.extend(s)
print(p)

q={1,2,3,4}
s={0,9,1,3,2}
print(q|s)
print(q&s)
print(q^s)

# a=open("C:\Users\hp\OneDrive\Desktop","r")
# print(a.read())

d=("sport","cricket","baseball","basketball")
s1,s2,s3,s4=d
print(f"s1:{s1}")


def shortnumber(a):
    shortest_values=min(a)
    longest_values=max(a)
    return shortest_values,longest_values
q=[100,200,3000,402,23,33,42,43,53,4,892,24]
s=shortnumber(q)
print(s)

for j in range(1,6):
    for l in range(j):
        print(l,end=" ")
    print()


for n in "titanic"[0:5]:
    print(n.upper()*5)

a=1
while a<20:
    a+=1
    if a==15:
        break
    print(a)

q=[1,2,3,4,5]
for u in q:
    if u==3:
        break
    print(u)

print("there is {1} who have the {0}".format("man","money"))
print("there are so many {b} man in india one of them is {g} for people and others are {m}  for their needs".format(b="business",g="good",m="mean"))

q=[1,2,3,4,5,6,7,8,9,10]
for n in q:
    if n==6:
        break
    print(n)
    print(sep="/")
# for j in q:
#     if j//2==0:
#      print(j)

d=[10,20,30,40,50,60,70,80,90]
for m in d:
    if m/2==0:
        print(m)

for i in range(1,4):
    for k in range(1,2):
        print(i,k)

h=0
g=["pension","gratuity","dearness","allownace","provident"]
for j in g:
    print(f"{h}:{j}")
    h+=1

# for n in range(10,15):
#     for g in range(16,20):
#         for b,m in enumerate(zip(n,g)):
#             print(f"{b} ==|== {m}")

a=["verb","adjectives","adverb","noun","object"]
s=[1,90,32,32,42]
for u in enumerate(zip(a,s)):
    print(u)
for f,g in enumerate(zip(a,s)):
      print(f"{f} | {g}")
for p,o in zip(a,s):
    print(f"{p} > {o}")

t=[1,9,30,24,248,48,924,89,24,90,-24,24]
print(t[-2])
print(chr(t[2]))
print(hex(t[-4]))
print(oct(t[-6]))

j=90.245
print(f"the variable j is in {j:.1f}".format(j))

def r(o,p):
    x=o+p
    c=o-p
    v=o*p
    b=o/p
    return x,c,v,b
# print(r(12,90))
# r(12,35)
print(r(89,24))

q={1,2,3,4,5}
f={9,8,4,5,2}
print(f"the intersect of q and f = {q&f}.")
print(f"the union of q or f = {q|f}")
print(f"the third result come from q^f = {q^f}")


pov=[1,90,349,355,23]
pov.insert(1,200)
print(pov)
s=[500,400,100]
pov.extend(s)
print(pov)
pov.sort()
print(pov)

def x(k,l,o,p):
    return k+l-o*p
print(x(12,9,35,5))

s=(1,2,4,6,5,32,43)
a=(10,20,30,40,50,60)
for n in zip(s,a):
    print(n)
for g,m in zip(s,a):
    print(f"{g} ::: {m}")

def deer(black="star"):
    print(f"salman khan kill {black}.")
deer(black="blackbuck")

def a(b,c):
    return b + c
result=a("traffic","jam")
print(result)

def c(z,x):
    if z%2==0 and x%3==0:
        return min(z,x)
    else:
        return max(z,x)
print(c(10,20))
print(c(12,24))

def turtle(snake):
    return snake[0]==snake[0]
print(turtle("anaconda"))

def tiger(lion):
    print(f"{lion[-6:].upper()} === {lion[-6:].upper()}")
tiger("houston texans")

def bank(money):
    trans=money.split()
    print(f"{trans[0]} > {trans[0]}")
bank("credit card")

def r(q):
    if q/2==1:
        return min(q)
    else:
        return q
print(r(10))
print(r(6))

def vb(w=10,e=20):
    f=w-e
    r=chr(w*e)
    t=bin(w+e)
    return f,r,t
print(vb(10,100000))
print(vb(10,10))
print(vb(w=10,e=20000))

q=[10,20,30,40,50]
g=[]
for d in q:
    g.append(d)
    print(g)
def v(op):
    for k in op:
        print(k)
v([1,2,3,4,55])

def r(tire):
    for k in tire:
        if tire==5:
            break
        print(tire)
r(range(1,10))

q=[1,2,3,4,5,6,7,8,9,10]
for n in q:
    if n==4:
        break
    print(n)

# a=10
# while a>20:
#     a=a+2
# print(a)

print("russia\n    brazil\n     south africa\n      india\n        china\n           are all together.".upper())

b=5
while b<10:
    b=b+2
    print(b)

w=[10,20,[10,30]]
a=[100,200,{"p":"parrot"}]
print(f"{w[2][0]} == {a[2]}")
print(w[2][0]==a[2])


def carrot(vegetables,fruits):
    juice=vegetables+fruits
    # films=vegetables|fruits
    return juice
print(carrot([1,2,3,4,5],[10,20,30,40,50]))
# print(carrot({},{10,20,304,12,3,4}))


def games(pubg,fortnite):
    cod=pubg&fortnite
    return cod
print(games({1,2,3,4},{10,2,3,4,50}))

def cats(dogs,bulls):
    for cows in dogs:
        for deers in bulls:
            print(type(cows))
print(cats((100,200,300,400,500),(1000,2000,3000,4000,5000)))

def bob(banks,logo):
    for a in banks:
        for b in logo:
            print(type(banks),type(logo))
            # return type(logo)
# print(bob(tuple(1),{1,2,3}))
bob([1,2,3],{"banks":"hdfc".upper()})

def c(vb):
    d=len(vb)
    f=len(vb)
    return d,f
a=["string","tuple","sets","forest"]
x=c(a)
print(x[0])

# def balls(tennis,football):
    # for t in tennis:
    #     for f in football:
    #         if t%2==0 and f%2==0:
    #             return max(t,f)
    #         else:return min(t,f)
# print(balls(tennis=10,football=60))

# def foods(mcd,kfc): $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ i have problem in this code $$$$$$$$$$$$$$$$$$$$$$$$$$
#     if mcd%2==0 and kfc%2==0:
#         return max(mcd,kfc)
#     else:
#         return min(mcd,kfc)
# print(foods(70,82))
# print(foods(90,95))

def colors(red):
    for r in red:
        return r
print(colors([1,2,3,4,5]))

def trimmer(*clips):
    print(clips[0]+clips[2])
    print(bin(clips[0]+clips[2]))
trimmer(100,200,509)

tuples=(-5,-4,-3,-2,-1)
for l in tuples:
    # print(l)
    print(tuples)

telephone={"fafda":"jalebi",
           "tomato":"onion",
           "burger":"king",
           "h":"p",
           "chocolate":"kitkat"}
for j in telephone.items():
    print(j)
for l in telephone:
    print(l.upper())
for ket in telephone.keys():
     print(len(ket))
# for c in telephone.keys():
#     print(len(c))

def america(ironman):
    i=min(ironman,key=len)
    r=max(ironman,key=len)
    return i,r
captain=["marvels","xmen","crime patrol"]
outcome=america(captain)
print(outcome)

def bike(cycle):
    c=min(cycle)
    y=max(cycle)
    return c,y
tube=["pipes","tubes","rods","tyres"]
f=bike(tube)
print(f)

def china(thailand):
    for t in enumerate(thailand):
        print(t)
china(["america","china","russia","iran","sri lanka"])

# def japan(atom): $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  enumerate use in def function $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#     a=min(atom)
#     t=max(atom)
#     return enumerate(a,t)
# asd=["books","pencil","rubber","sharpner"]
# k=japan(asd)
# print(k[0])

# def tower(a):
#     b=min(a)
#     c=max(a)
#     return b,c
# d=["apple","sting","monster","energy","redbull"]
# e=tower(d)
# print(e[0])

o=["red bull","monster","energy","biscuit"]
print(len(o[0]))

def bulls(basket):
    return len(basket[3])
print(bulls(["string","dictionary","tuple","telephone directory"]))

def v(words):
    w=len(words[0][0:4])
    o=len(words[4][7:11])
    return w,o
pd=["united states of america","united kingdom","thailand","japan","new zealand"]
df=v(pd)
print(df)

# dj=["united states of america"]
# print(len(dj[0][0:4]))

def bowl(nfl): #####################################            different answer           #############################
    n=nfl[0][0:4] + nfl[1][-4:]
    # f=nfl[1][-4:]
    return n,f
cv=["telephone","wonderland","switzerland","nicargua"]
jk=bowl(cv)
print(jk)


r="redlight"
red=list(r)
print(red)

def u(sentence):
    return list(sentence)
sentence="good morning".upper()
print(u(sentence))

d="donald-trump-serves-mcdonald-french-fries-to-customers."
print(d.split("-"))
print(list(d.upper()))

def modi(barack,obama):
    print(barack + obama)
    print(bin(barack+obama))
    print(chr(barack+obama))
    print(hex(barack-obama))
    print(barack+obama)
modi(10,90)

def momo(bill):
    if bill%2==0:
        return "true".upper()
    else:
        return "false".upper()
print(momo(10))
print(momo(15))
print(momo(30))

def vc(o,p):
    print(o+p)
    print(o-p)
    print(o/p)
    print(o%p)
    print(chr(o*p))
print(vc(10,20))

def gogo(pop):
    return pop+" is shutdown after 20 years."
print(gogo(pop="cartoon network".upper()))

def cid(cid_officer):
    print(f"{cid_officer} breaks the door of every house of the show.")
cid("daya".title())

def comedy(show,shows):
    print(f"{show} and {shows} are comedy couples in the show.".format("daya","jethalal"))
print(comedy("daya","jethalal"))

def go(pro,hedge):
   return len(pro),len(hedge)
print(go("united","kingdom"))

def coconut(choco,bar):
    return choco + bar
print(coconut(10,20))
print(coconut("protein"," bar"))

def stick(*era):
    print(era[1]+era[2])
stick(100,200,300)
stick("bamboo","stick"," acre land")

def play(games,sports,matches):
    print(f"{games} : {sports} : {matches}")
play(games="pubg",sports="cricket",matches="football match")

def ios(apple):
    for i in apple:
        print(i)
android=["samsung","nothing","java","nokia"]
ios(android)

def tower(x):
    return 8*x
print(tower(2))
print(tower(3))
print(tower(4))


t=[1,20,39,99,34,89,13,"rabbit","java","lion"]
cv.append(t)
print(t)
t.insert(0,200)
print(t)
s=[1,2,3,4,5,5,6,7]
s.append(t)
print(s)
print(t[-4:])
print(t[2:12:3])
print(t[0]+t[3])
print(bin(t[0]*t[2]))
print(bin(t[1]|t[3]))
t[-1]="cheese"
print(t)
t.insert(-1,"potato")
print(t)
t.insert(1,"hard disk")
print(t)
t.insert(0,"macdonald")
print(t)
print(t+s)
print(list(t))
one_two=["diu","goa","surat","passport","daman"]
print(one_two)
print(len(one_two[0]))
one_two[-2]="rajkot"
print(one_two)
print(t[0]+"  "+one_two[0])
print(t[-1::]+one_two[-1::])
print(t)
print(one_two)
print(t[::-1]+one_two[::-1])

print(t[0][0:5].upper())
print(t[-3][0:2]+one_two[-2][0:3])
print(t[0][0:3]+" "+"n "+ t[-1])
print(one_two*2)
print(max(one_two))
print(min(one_two))
# print(len(t[0],len(one_two[1])))
b=[1,2,3,4,5,[10,20,30,40,50,[100,200,300,400,500]]]
print(b[5][0])
print(b[5][5][0])
b[5][5][0]=5000
print(b[5][5][0])
print(len(b))
print(b[5][2]+b[5][5][2])
print(chr(b[5][2]+b[5][5][2]))
print(t)
del t[0]
print(t)

"DICTIONARIES"

country={"asia":"india",
         "europe":"spain",
         "west":"america",
         "north pole":"artic",
         "south pole":"antartica"
         }
print(country["west"])
print(len(country))
print(len(country["south pole"]))
country["europe"]="italy"
print(country["europe"])
print(country["west"])
print(country["asia"].upper()+" "+country["north pole"].upper())
country["east"]="japan"
print(country)
# print(country.keys()+country.values())
# print(country.keys().upper(),country.values().upper())
print(len(country.keys()))

companies={"it".upper():"tcs".upper(),
           "vehicles":"bajaj",
           "truck":"force",
           "cars":"tata"
           }
print(len(companies))
print(companies)
# print(country+companies)
print(country["west"],companies["cars"])
# print(country["north pole"[0:3],companies["vehicles"[0:3]]])
print(country["north pole"][0:3].upper())
print(country)
print(companies)
print(country["south pole"][-4:],companies["cars"])
print(country["east"][0:2],country["asia"][2:])
print(country["west"]*3)
# print(country.keys()*2)
companies["steel"]="tata","jsw"
print(companies["steel"])
print(companies["steel"][1])
print(list(companies["vehicles"]))
print(tuple(companies))
# print(type(companies))
print(set(companies))
print(companies)




coffee={"chai":("tata","red label"),
"coffee":("nestle","bru"),
"daru":["black lable","blue lable"],
        "shoes":"nike",
        "height of person":["pratham",180],
"number of person":[1,2,3,4,5]
        }
print(coffee)
market=[100,23,3,2,3,21,32]
market.append(coffee)
print(market)
print(coffee["chai"][1].upper())
coffee["brand"]=["shoes","black and white"]
print(coffee["brand"])
print(coffee["shoes"]+" "+coffee["brand"][1]+" "+coffee["brand"][0])
print(f"the color of {coffee["shoes"].upper()} sneakers is {coffee["brand"][1].title()}.")
print(coffee)
# print(f"{coffee["daru"][0]} and {coffee["daru"[1][0:4]]} are not good combination in color variant.")
# print(coffee["daru"][0])
print(f"the {coffee["daru"][0][0:5]} and {coffee["daru"][1][0:4]} color are not a good combination.")
print(list(coffee["shoes"]))
print(coffee)
del coffee["chai"]
print(coffee)

"TUPLES"

d=(1,2,3,4,5)
ase=[]
ase.append(d)
print(ase)
print(type(ase))

youtube=("series","pandas","numpy","matplotlib","sequel")
print(len(youtube))
print(len(youtube[0]),youtube[-2])
print(f"{youtube[1]} {youtube[0]}")
# print(youtube.count(1
# print(youtube.__add__(k))
# print(youtube)
k=("dataframe","array","list","strings","numpy")
print(youtube.__add__(k))
print(youtube.count("numpy"))
g=youtube+k
print(g)
print(g.count("numpy"))
print(ord(k[2][0]))
print(ord(k[0][3]))








giraffe=(20,10,9,23,45,2,42,2,3,11,21,42,4)
tiger=(10,20,30,40,50,60,70)
print(giraffe[2]+tiger[1])
# print(zip(giraffe,tiger))
print(chr(giraffe[4]+tiger[4]))
print(chr(tiger[1]*giraffe[2]))
print(giraffe.count(2))
a=giraffe+tiger
print(a.count(20))





r=(10,20,30,40,(100,200,300,400,500))
print(r[4][0]+r[4][-1])

mix=[1,2,3,(90,32,44,24,23,32),{"usa":"president",
                                "uk":"prime minister",
                                "mobile":"samsung",
                                "tv":"onida"}]
print(mix[4]["usa"])
print(mix[3][0]==mix[4]["mobile"])
print(type(mix))
print(type(mix[3]))
print(type(mix[4]))

mike=(1,2,3.34,(10.34,(2,4.24,100,2),00))
print(mike[3][1][0])
print(mike[1]==mike[3][1][0])
print(mike[0]==mike[3][0])
print(f"{mike[0]}===={mike[3][2]}")

print(mike[3][1][1])
print(f"the measurement of {mike[2]:.10f}")

print(mike[2]*mike[3][0])
print(f"the decimal number of {mike[2]*mike[3][0]:.2f}.")

g=["string","pot","cows","doggy","elephant","gopro","finland","alaska"]
print(sorted(g))
# print(dict(g))

belgium={"europe":"finland",
         "asia":"china",
         "crude oil":"russia",
         "arabs":"middleeast",
         }
print(sorted(belgium.keys()))
print(sorted(belgium.values()))

d={"a":1,"b":2}
result=d.copy()
result["c"]=3
print(d)
print(result)

korea={"america":20,"russia":12}
out=korea.copy()
out["china"]=130
print(korea)
print(out)

japan={"abc":123,"def":456,"hij":789}
new=japan.copy()
new["xyz"]=101112
print(japan)
print(new)

f=(9,23,42,90,40,89)
g=(42,4,"op",4,24.24,24)
f.__add__(g)
print(f)
print(f.index(89))


un="united states of america"
print(un.find("s",8))
# print(un.index("s",9))
print(un.index("a"))

"SETS"
setting={1,90,24,24,90,89,78,43,43}
getting=[1,90,34,24,9,90,78,43,22]
print(setting==getting)
# print(setting[1]==getting[1])
print(type(setting))

rigi={"sports","ball","bats","ball","sports","caught"}
print(set(rigi))
print(rigi)
print(sorted(rigi))

g=(90,13,90,13,14,90,9,98,94,24,8)
fiji=[]
fiji.append(g)
print(g)

rico=[1,2,3,4,5,6,7,8,9,10]
figo=[10,20,30,40,50]
figo.append(rico)
print(figo)

x=[1,2,3,4,5,1,90,9,242,224]
y=[90,12,13,13,11,31,14,1]
z=[90,31,34,32,90,42,4,13,1,32]
x.append(y)
y.append(z)
z.append(x)
print(x),print(y),print(z)

sd=[1,2,3,4,5]
ds=[100,200,300,400,500]
sd.extend(ds)
ds.extend(sd)
print(sd)
print(ds)
print(sd.index(200),print(ds.index(200))),print(ds.index(200))

double={"sports players":{
    "cricket":"virat kohli",
    "football":"lionel messi",
    "rubgy":"tom bradd",
    "basketball":"lebron james"
}}
print(double["sports players"])
print(double["sports players"].keys())
print(double["sports players"].values())
print(double["sports players"].items())
double["sports players"]["hockey"]="shah rukh khan"
print(double["sports players"].keys())

# finland=double["sports players"]
# first=finland.copy()
# first=hurdle["ruby"]="kansas cheifs"
# print(finland)
# print(first)
# print(double["sports players"])
# print(first["hurdle"])

simple={"abc":123,"def":456,"hij":789} ############################################### $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
computation=simple.copy()
computation["intership"]="intern"
print(simple),print(type(simple))
print(computation),print(type(computation))

opencv={"components":{"mobile":"battery",
                      "computer":"motherboard","machine":"power","cars":"engine"}}
django=opencv.copy()
django["solar"]="panels"
print(opencv)
print(django)

# g=[]
# g.append(mike[3])
# print(g)

for t in range(1,5):
    for r in range(6,10):
     # print(t,r)
        print(r)
        print(t,sep="/"),print(t)
        print(r,end=" ")
        print("|")

for i in range(1,5):
    for l in range(i):
        # print(l)
       print(i)

g=[1,3,22,2,24,29,42,29,24,92]
for l in g:
    print(l)
for k in g:
    print(k+10)

going=[1,2,3,4,5]
# for l in going:
#     print(l+10)
# print(l-10)
print(going[1]+1,print(going[2]-2,print(going[3]*3,print(going[4]/4))))
print(going[2]-2)
print(going[3]*3)
print(going[4]/4)
print(going[1]+1)

# m="modi" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# d="donald trump said %s is total killer." $$$$$$$$$$$$$$$$$$$$$$$$$$$$4$
# print() $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

d=["dango","duck","go","baby","shark"]
a={"apple","ball","car","dog","elephant"}
for t in d:
        print(t)

location=["states","g","m","j","r","t"]
places=["5","gujarat","maharashtra","jharkand","rajastan","tamil nadu"]
location_places=dict(zip(location,places))
print(location_places)

opd=("europe","f","p","s")
ops=("3","france","poland","spain")
opd_ops=list(zip(opd,ops))
print(opd_ops)
print(f"{opd[1]}:{ops[1]}")

mixed=[("air","oxygen"),("hydrogen","gas"),("helium","ballon gas"),("nitro","oxide")]
chemicals,variants=zip(*mixed)
print(chemicals,print(variants)),print(variants)

f=["america","cuba","china","russia","india","france"]
g=[7,4,3,6,5,8]
print(dict(zip(f,g))
)

hd=[1,23,90,3,2,0,48,9,4,35,3,2]
simp=[2,42,48,9,4,2,2,14,2]
print(set(zip(hd,simp)))
print(set(hd+simp))
print(f"the union of whole set numbers {set(hd+simp)}")
# for k,l in set(zip(enumerate(hd,simp))):
#     print(k,l)

# def v(o,p):
#     return o+p
# print(v(9+24))
#
# p=["prqtham","om",90.245,90,231,1124,"sting","monster","red bull"]
# d=["89","424","424","24324","9024","452","india"]
# print(dict(zip(p,d)))

def ui(m,n):
    return m+n
print(ui(10,20))

def bn(c,v):
    print(v-c)
    print(c+v)
    print(bin(c-v))
    print(v|c)
    print()
bn(10,200)

def square(i,o):
    return i[0]
print(o[0])
print(square("orange","apple"))

def ios(apple):
    for l in apple[0:4]*3:
        print(l.upper())
print(ios("united"))

def android(samsung):
    for k in samsung[0:2] and samsung[2:5]:
        print(k.upper())
print(android("japan"))

s={"states":{"g":"gujarat",
             "m":"mahashratra",
             "j":"jharkand",
             "u":"uttar pradesh",
             "t":"tamil nadu",
             "b":"bihar",
             "r":"rajastan"}}
print(s["states"]["b"])
s["states"].update()
print(s["states"])
for g in s["states"].keys():
    print(g.upper())
for n in s["states"].values():
    print(len(n))
for m in s["states"]["t"]:
    print(len(s["states"]["t"]))
for k in s["states"]["g"]:
    print(len(k))

def hajj(dubai):
    for g in dubai:
        if g[0]==g[0]:
            return "yes"
        else:return "no"
print(hajj("new zealand"))

def east(china,india):
    if china.split() and india.split():
        return china[0]==india[0]
print(east("canada","america"))

def n(num,hum):
    if num==hum:
        return "yesss".upper()
    else:return "ohh no".upper()
print(n(10,20))

# def gif(q): $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$      PROBLEM       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#     for w in q:
#         if w%2==0:
#          return w
# print(gif([10,20,30,40,50.60,90,12,3]))

print(20000/5*2)
print(50000%3**2)
print(40000*3/2)
print(10000/4**3)

w="web development"
for u in w.split():
    if len(u)%2==0:
     print(u)
for g in w:
    print(len(w))
for v in w[0:8]*3:
    print(v[0:7]*4)

u="united nations"
for k in u[0:4]:
    print(k.upper()*3,sep="/")

"rectangle"
# l=float(input("length: "))
# b=float(input("breadth: "))
# measurement_of_rectangle=l*b
# print(f"the measurement of rectangle :- {measurement_of_rectangle}")

"square"
# square_of_rectangle=l*b**2
# print(f"the square of rectangle:-{square_of_rectangle}")

v="vba macros"
for r in v[0:2].upper()*2:
    print(r*3)
    print(sep="./.")
    # print(r*4)
    # print(r)
    # print(r[0:2].upper()*3)


ey=(90,242,1,"engine","free fire")
f=[]
d={89,342,990,'pwc',"pvc","pipes"}
for l in ey:
    f.append(l)
    print(f)
for n,m in enumerate(zip(ey,d)):
    print(f"{n}:{m}")
for d,s in enumerate(zip(ey,d)):
    print(f"|-|-| {s} :/:/:/ {d} ")


print()


print("/"*5)
print("/"*4)
print("/"*3)
print("/"*2)
print("/"*1)

r=["cars","bikes","sports","belgium","japan","sneakers"]
for cid in r:
    print(len(cid[-1]))
for l in r[-1]:
    print(len(l))

f=["sneakers","bikes","toyota","suzuki","honda","toyota"]
print(len(f[0]))
for t in f[1]:
    print(len(f))
for v in f[2]:
    print(f[2])
for i in f:
    print(len(i[2]))
for u in f[2]:
    print(u[0:3].upper()*3)
for k in f[2][0:3]:
    print(k.upper()*3)
# for d in f["toyota"]:
#     print(d)
for free in "toyota":
    print(len(free))

pogo=["tv","mobile","pencile","smartwatch","rubber"]
for k in pogo+f:
    print(len(k))
for n in pogo:
    print(len(n))

# cn=[10,29,94,24,2,99,42]
zx=["lap","maverick","card","com","ware","mou"]
# print(len(cn))
for parrot in zx:
    print(len(parrot))
for joker in zx:
 print(len(zx[2]))

def spain(japan,cuba):
    return japan[0]==cuba[0]
g=spain("netherland","union territory")
print(g)

def poland(h,o):
    return h[0]+o[2]
print(f"the total is {h} + {o}")
xyz=poland(h=[10,20,38,94,24],o=[10,20,30,40,50])
print(xyz)

i="india has more population than china."
for k in i.split():
    if len(k)%2==0:
        print(k)
h=[1,99,32,49,89,89,9,24,24,79,42]
print(h.count(24))
print(sum(h[0:4],sum(h[-4:-1])))
for goa in h:
    if goa==49:
        break
    print(goa)

k=[1,2,3,4,5,6,7,8,9,10]
print(k[-5:-1])
print(sum(k[0:4],sum(k[-5:-1])))
print(k[-1:])
print(chr(k[3]))
print(k[::-1])

for lamb in reversed(k):
    if lamb==4:
        break
    print(lamb)
for lion in k[-5:-1]:
    break
print(lion)

print("i\nhate\ncost\accounting subject because i don't know about accounting.",sep="$")
print()

d="donald trump"
count+=0
for v in d:
    print(f"{count} ----> {v}")
count=+1

def b(*colonial):
    print(f"{colonial[1].title()} and {colonial[2].title()} were come to india before 200 years ago.")
b("americans","britishers","europian")

def shops(banks):
    print(f"{banks[0:3]} == {banks[-5:]}")
    # return max(receipt) and min(cash_counter)
receipt=shops("money back")
cash_counter=shops("fixed installments")
# print(receipt,cash_counter)
print(receipt==cash_counter)

def doremon(*bheem):
    return chr(bheem[0]+bheem[2])
print(doremon(100,200,300))

if 0.1+0.2==0.3:
    print("true")
else:print("false")

d="donlad india"
print(d[0:3].capitalize(),d[7:9].upper(),d[-5:].capitalize())

def color(red):
    return red[0:3].capitalize(),red[-3:].capitalize()
print(color("japan"))

def app(apply):
    print(apply|apply)
black=app({1,2,3,4,5})
white=app({1,2,3,10,20})
print(black,white)

def listing(tyre):
    print(tyre[0:3])
listing(tyre=["10","20","30","40"])
listing([10,20,30,40])

def pump(steel,iron):
    print(steel&iron)
    print(f"the intersection of two arguments :- {steel&iron}")
    print(steel|iron)
    print(f"the union of two arguments :- {steel|iron}")
    print(f"the steel.difference(iron) :- {steel.difference(iron)}")
    print(steel.difference(iron))
    print(steel^iron)
    # print(steel.intersection(iron))
    # print(f"the steel.intersection(iron) :- {steel.intersection(iron)}")
pump(steel={1,2,3,4,5},iron={10,2,3,40,5,12,2,3,40})

def dhoni(virat):
    return virat[0:3].capitalize() +" " +virat[2:6].capitalize()
print(dhoni("barack obama"))

def dhawan(siraj,shammi):
    return siraj[0:].capitalize() + shammi[4:8].capitalize()
print(dhawan("cow","tacobell"))

def marry(holi,diwali):
    return len(holi[0:3]),len(diwali[2:5])
    # return len(holi[0:3].capitalize()),len(diwali[2:5].capitalize())
# marry("russia","india")
print(marry("russia","diwali"))

def ss(dodge,bugati):
    print(len(dodge[-5:].capitalize())),print(len(bugati[-3:].capitalize()))
ss("lamborghini","chiron")

def macros(v,r,t):
    print(v*r**t)
    print(v%r**t)
    print("put decimal on {w:.2f}".format(w=v%r**t))
# cuban=59.3241214141
# print("there is two decimal on {w:.2f}".format(w=cuban))
macros(20000,10,0.8)
macros(40000,13,0.11)

def iodine(a,*b,c):
    print(a+b[2]*c)
# iodine(10,11,23,4,13) ########################################## problem ########################################
iodine(10,20,23,12,c=32)


def vicky(bmw,chase):
    print(bmw&chase)
    print(bmw|chase)
    print(bmw^chase)
print(vicky({1,2,3,4,5},{1,5,4,2,9,0,4834}))

f=[1,2,3,4,5]
g=[6,7,8,9,10]
for k in f:
    for l in g:
        print(f"the addition of f+g is {k} + {l} = {k+l}")

for m in range(1,5):
    for o in range(4,8):
        print(m)
    print(o)

s=1
while s<20:
    s=s+2
    print("hello"[0:4].upper())
    print(s)

# a=(10,290,34,42,99,"name","age","place","population","gender")
# numbers,names=a
# print(numbers,names)

py={"electricity":{"spark":"earthing",
                   "green":"wire",
                   "red wire":"danger wire",
                   "blue wire":"cool wire",
                   "GEB":"transformer"}}
print(py["electricity"]["spark"])
for l in py["electricity"].keys():
    print(l.upper())
py["electricity"]["electric"]="battery"
print(py["electricity"].keys())

if "wire" in py:
    print("true")
elif "wire" in "components" in py:
    print("false")
elif "wire" in "red" in py:
    print("valid")
elif "wire" in "blue" in py:
    print("invalid")
else:print("inaccess")

for i in range(6):
    print(f"the squares of range  {i*i}")
s={x:x*x for x in range(6)}
print(s)

g=[1,2,29,39,22,2,42,40,44]
p=[90,24,22,3,32,24,2,23.9,23]
for h,i in zip(g,p):
    print(f"the subtraction of g,p is {h-i}")


print(10/5)
print(10//5)
print((((sum([1,2,3,4])))))
print((((type(sum([1,2,3,4]))))))

g=(90,23,29,0,32,24,22,12)
print(g[0:3])
print(g.count(90))

def v(a):
    """print kgo"""
print()

a="anthony"
print(f"i put space in this string:-{a:_>20}")
print(f"{a:_<50}")
print(f"{a:|<15}")
print(f"{ord(a[5]):.10f}")
print(ord(a[5]))
print()

p="hell"
print(f"{p:|<20}")
print(f"{p:~>20}")
print(f"the alphabet l in word [hell] in which postion:-{ord(p[2])}")

c=["calicut",90]
print(f"the alphabet of word calicut: {ord(c[0][6])}".title(),f"the number 90 is convert into: {chr(c[1])} ".upper())
print(c[0][4],print(c[1])),print(c[1])
print(chr(c[1]))

print("the {} is elected as 47th president of the {}.".format("donald trump","usa"))

un="united states of america"
print(un[0:4].capitalize(),un[-4:].capitalize())
print()

print(f"the spaces in numbers in :{10::<10} and {5:->10}")
print()
print(f"{'qwerty':_>10}\n        {'key-bo':_<10}")
print()
print(f"{'soft':_>10}\n{'ware':_<10}")
print()
print(f"{'hexi:_<10'}\n{'decimal:_>10'}")
print()
print(f"{'north':_<10}\n          {'korea':_>10}")
print()
print(f"{'timber':_>10} ----- {'wood':_<10}")
print()
print(f"{'world':_<10}_____{'war':_>10}")
print()
print("narendra modi will go to nigeria,and then he will go to brazil for g20 summit",sep="*")
print()
print("donald", "trump", "calls", "three", "world", "leaders",sep=" / ")
print()


print(56.9032*32.113+2)

# l=float(input("l: "))
# b=float(input("b: "))
# t=int(input("t: "))
# print(f"the perimeter of rectangle is:- {l*b+t}")

print(10%5)
print(20%42)
print(9042%532)
print(id(344.923%2321.242))
print(ord("g")),print(ord("G"))
print()
print(chr(190),ord("U"))
print(chr(188))
print()
print(chr(188),chr(189),chr(190))

print(chr(190))











# def joint(s,ss):
#     print(s+ss)
# joint("hard","ware")
#
# d='russia'
# i="india"
# print(len(d[0:3]))
# print(len(i[2:5]))


# print("donald trump said %s is total killer"%s"modi")

# bkt=(1,2,2,00000,(42,424,12,131),90,12,31,34,1)
# print(bkt[3])
# print(bkt[7])






# print(float(-5))
# print(complex(-10))


# color=[1,2,3,4,5]
# for l in color:
#     print(l)


# numbers=int(input("numb: "))
# if numbers%2==0:
#     print("even numbers")
# else:
#     print("odd numbers")


# j=[1,2,3,4,5]
# for i in j:
#     print(type(i))




# def g(h,i):
#     for v in h:
#         for b in i:
#             if v%2==0 and b%2==0:
#                 return min(v,b)
#             else:return max(v,b)
# print(g([2,4,6],[1,3,5,7,9,11,13,15]))
# print(g([10,20,30],[100,200,300,400]))


# def c(l,m):
#     return oct(l+m)
# print(c(0.10,0.20))



# def v(*b,k):
#     for n in zip(b,k):
#         return n
# print(v("string","dictionary","tuple","space","keyboard",k="one two three"))


# def r(g,t):
#     return g+t
# print(r[1,2,3,4],[5,6,7,8])
#
# def c(v,b):
#     for k,l in v,b:
#         return k+l
# print(c[1,2,3,4],[5,6,7,8])



# def g(games):
#     for n in games:
#         if n%2==0:
#             return min(n)
# print(g([2,4,6,8,10]))



# def faltu(vicky):
#     for m in vicky:
#         if m%2==0:
#             return max(m)
# print(faltu([2,4,6,8,10]))





# def v(o,p):
#     for l in o:
#         if l%2==0:
#             break
#         return l
#     for k in p:
#         if k%2==0:
#             continue
#         return k
# print(v[1,2,34],[2,3,4,13,42,424])


# a=1
# b=2
# c=3
# a,b,c=b,c,a
# print(a,b,c)
# print(b,c,a)







