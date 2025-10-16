# def nu(n1,n2):
#     return n1+n2
# nu(10,20)
import random

from fontTools.misc.psOperators import ps_integer
from numpy.testing.print_coercion_tables import print_new_cast_table

i=[10,20,4,6,7857,65]
print(i[0:3])

def num(val,fla):
    print(hex(int(val+fla)))
    print(oct(int(val+fla)))
num(10,40)
num(100,200)
print()

# def rto(u,i):
#     return u+i
# rto(10,20)

def hello(c,v):
    print(c**v)
hello(5,30)

def rt(a,b,c):
    print(a+b/c)
rt(10,20,30)

def n(name):
    print(f"my name is {name}.")
n("pratham".upper())

def rt(m,n):
    return m**n/6
print(f"the mean of rt is {rt(5,6)}")
print(rt(5,6))
print()

def qwr(x,y,z):
    return 2*x+y*z
print(f"the total of qwr is {qwr(2,4,6)}.")

def add(q,w):
    return q+w
def div(q,w):
    return q/w
# print(f"the add and div are:-{add(5,10)},{div(50,110)}")
# print(add(5,10),div(50,100))
print(div(add(10,15),add(9,5)))
print()

# def mul(i,o,s):
#     return i*o*s
# def sub(i,o,s):
#     return s-i-o
# print(mul(sub(10,20,30),sub(70,90,80)))

def we(e):
    return f"my name is:{e}."
print(we("pratham".upper()))

def ui(u,i):
    return u**i//50
print(ui(50,80))

def ui(ux,iu):
    return ux**iu%50
print(ui(67,54))

def r(f):
    for i in f:
        return i
print(r([10,204,25]))

def cv(i=10,os=23):
    return i*os
print(cv())

def hi(name="python"):
    return f"hello {name}."
print(hi("java"))

def op(o,m):
    return o+m
print(op("10","50"))

def iti(yt):
    for u in yt:
        if u%2==0:
            return "True"
        else:"False"
print(iti([10,9,535,6,253]))
print()

g=[10,252,46,52,53]
for y in g:
    print(y)

def hu(*vc):
    for g in vc:
        return g+g
print(hu([10,425,55,25]))

def w(x):
    return x[0:4]==x[0:4]
# print(w("gaming keyboard"))
# print(w("warzone mouse"))
print(f"the {w("gaming mouse")}=={w("keyboard")}")

def ty(m):
    return m[1]==m[1]
print(ty([1,2,3]))
print(ty([4,5,6]))
print(

)
f={"name":"string",
   "d":"decimal",
   "l":"lists",
   "i":"int"}
for t in f.values():
    print(t[0:3].upper())

t=[0,1,2,3,4,5]
for g in t:
    print(g+0.5)

for h in range(0,20):
    if h%2==0:
        print(g)
print("New start".upper())
def ref(a):
    for t in a:
        if t%2==0 and t%4==0:
            print(t)
        else:print("zero")
print(ref([10,425,2,424,4,32,423,43,24,42,56,100,86,54564,5,7]))

t="string"
r=['rat','queen','king','house','game','fame','money']
for rat in r:
    if rat.startswith('k'):
        print(rat.join(t+''))
    else:print(rat.upper())


# x=[9.3,9.45,9,4.2,94.2,2.1]
# t=range(1,20)
# for y in t:
#     if y%2==0:
#         print(y+x)
#     else:print(x.append(y))

f='rotten'
vege=['fruits','tomato','potato','bhindi']
for cv in vege:
    if cv.startswith('f'):
        print(f.join(cv).upper())

t=[10,424,323,222425]
u=['Aa','Bb','Cc','Dd']
for ty in t:
    for amer in u:
        if str(ty).join(amer):
            print(str(ty))
        else:print('zero')

for u in range(0,30):
    if u%12==0:
        print(u)

di={'a':"apple",
    'b':"ball",
    "c":"catch",
    "d":"denmark",
    'e':"elephant"}
for g in di.values():
    print(g[0:3].upper()+" ".join('\nring'))

cars={'t':"tata",
      'r':"reliance",
      'm':'mahindra',
      "j":"jagaur"}
for w in cars.values():
    print(w[0:3].lower().join("\t[bond]".upper()))

r=[(10,42,244,2)]
print(type(r))
raw=([10,43,42,33])
print(type(raw))

g={13,242,43,4342,24}
t={1314,242,24,24,43}
print(f'The set operate use for same number:{g&t}')
print(f"The set and operator use for :{g|t}")
print(f"the set operator use in :{g^t}")

t='strif'
print(t.find('r'))
print(t.isalpha())

t=['cat','hat','sat','sit','coat']
g='lion'
for jk in t[0:2]:
    for w in g:
        print(w.join(jk).upper())
# for j in range(0,10):
#     for k in range(0,10):
#       if j%2==0:
#         print(f"The answer of:{j}")

t=[0,1,3,5,7]
g=[2,4,6,8,10]
for c in t:
    gt=t+g
    print(gt)
# h=[]
# op=12
# po=34
# for j in op:
#     h.append(op+po)
#     print(j)
f=[2,4,6,8]
v=24
for j in f:
    v=v+j
    print(v)

t=[0,1,3,5,7]
g=[2,4,6,8,10]
for c in t:
    for sd in g:
      v=sd+c
      print(f"{sd}\t+\t{c}=\t{v}")

tup=(1,2,4)
put=(0,3,5)
print(tup.__add__(put))
print(tup.__contains__(10))

## Tuple Unpacking
o=[('a','b'),(1,2),('A','B'),(3,4),('c','d'),('C','D')]
for t in o:
    print(str(t[0:1]).upper())
print()
o=[('a','b','c','d'),
   (1,2,3,4),('A','B','C','D'),
   (10,20,30,40),('rat','cat','hat','write'),
   (100,200,300,400)]
for ts in o:
    print(ts[0:3][0:2])
print()
for ax in o:
    print(ax[0:3][0:2])
print()
# for (a,x,e,s,q,d)in o:
#     print(x)

t=[0,1,3,5,7]
g=[2,4,6,8,10]
for c in sorted(t):
    for sd in reversed(g):
        print(c,end='-')
        print(sd)

go=[10,20,30,40,50]
print(go[0])
print(go[::-1])
print(go[0:5:2])
print()
tov=[[10,20,30,40,50],[100,200,300,400,500]]
print(tov[1][::-3])
print(tov[1][3]+tov[0][2])

r=[(1,2,3),
   (0.1,0.2,0.3),
   (10,20,30),
   (100,200,300)]
for k in r:
    print(k[0:2]+k[0:2])
print()
u=[0.1]
h=[1,2,3,4]
for j in h:
    u.append(h*3)
    print(u)

##'list'
rto=[1.11,1.12,1.13,1.14,1.15]
del rto[2] ## delete
rto[1]=0.30 ## replace
rto.append(50.3) ## add value
print(rto)
rto.insert(0,0.230) ## replace with insert
print(rto)
print(len(rto))
print(rto[-1]+rto[1])
print(f"add of {rto[-1]}+{rto[1]}={rto[-1]+rto[1]}.".title())
print(sum(rto))
print()

## 'tuples'
j=(1,2,3,4)
print(j[0:3])
print(j[0:3]*2)
print(j.__add__((0,13,4))) ## add
print(j.__contains__(3))
print(j.__contains__(5))
# print(j.__eq__(j))
h=(1.0,2.0,3.0,4.0)
n=(11,12,13,14)
print(h.__eq__(h))
print(h.__mul__(2)) ## multiple the whole tuple
print(h.__getitem__(3))
# print(h.__iter__())
print()

## "Dictionary"

fp={'g':"cricket",
    'v':'virat',
    "d":"dhoni",
    "s":"sachin",
    "p":"piyush"}
fp['d']='dhawan'
del fp['s']
print(fp.items())
print()

cl={"world":{"e":"elon",
             "m":"musk"},'us':{"d":"donald",
                               "t":"trump",
                               "j":"jd",
                               "v":"vance"},"brics":{"c":"china",
                                                      "r":"russia",
                                                     "i":"india",
                                                     "b":"brazil",
                                                     "s":"south africa"}}
print(cl['us'].values())
for g in cl['brics'].values():
    if g.startswith("i"):
        break
    else:print(g)

print(str(cl['brics'].values()).upper())
print(cl['brics'].values(),cl['world'].values())
for j in reversed(cl['brics'].values()):
    print(j[::-1].upper())

ele={'electronics':{"s":"samsung",
                    'l':[1,2,3]},"cars":{"t":"tigor",
                                        "a":'amaze',
                                        'h':"honda",
                                        "c":"city"},"stocks":{"amzn":1234,
                                                              "tsla":4552,
                                                              "msft":3002,
                                                              "infs":9012}}
for stoc in ele['stocks'].items() :
    print(str(stoc).join((ele['cars'].values())))
    print()
for j in ele['cars'].items():
    for k in ele['stocks'].values():
        print(str(k).join(j).upper())
    # print(reversed(str(j).upper())
    # print(str(ele['cars']))
    # print(str(str(j).startswith('a')).join(ele['stocks'].values())



# "For Loop"
for j in range(0,5):
    print(j)
l=[90,4,13,4,24]
v=[100,1,32,2]
for k in l:
    v.append(k)
    print(sorted(v))

for e in v:
    if e==32:
        break
    else:print(e)

cars={'f':'ferrai',
      'b':'bmw',
      'c':"chevrolet",
      't':'tigor'}
for c in cars.values():
    if c.startswith('c'):
        break
    else:print(c)

solar={"s":"sun",
      'm':"mercury",
      'v':"venus",
      "e":"earth",
      "ma":"mars",
      "j":"jupiter"}
for m in solar.values():
    if m.endswith('s'):
        break
    else:print(m)

solar={"s":"sun",
      'm':"mercury",
      'v':"venus",
      "e":"earth",
      "ma":"mars",
      "j":"jupiter"}
for m in str(solar.values()).upper():
    if m.endswith('r'):
        break
    else:print(m)

g=[103,22,4,233,4,4,42]
for u in g:
    if u>10:
     print(hex(u))
    else:print(oct(u))
t=[1,324,2,89,532,24]
for k in t:
    if k>50:
        print(float(k))
    else:print(hex(k))

for u in list(range(0,5)):
    print(u,"*",'2','=',2*u)
usa=[1,2,3,4,5]
j=[3]
for u in usa:
    for t in j:
        print(f"mul of {u}*{t}={u*t}")
a='america'
count=0
for k in a.upper():
    print(f"{k}:{count}")
    count+=1
g=[(10,20),(0.1,0.2),(1,2),(100,200)]
for j in g:
    print(f"the mul of {j[0]}*{j[1]}={j[0]*j[1]}")
print()

## 'ZIP FUNCTION'
us=[10,244,25,24,55,42]
ka=[1.1,1.2,1.3,1.4,1.5,1.6]
for t in zip(us,ka):
    print(t[0]+t[1])
    print(f"the add of {t[0]}+{t[1]}={t[0]+t[1]}")

quad={'a':"america",
      "i":"india",
      "j":'japan',
      "aus":"austraila"}
count=0
for q in quad['aus']:
    print(f'{q}:{count}')
    count+=2
print(

)
m='windows made by microsoft'
for l in m.split():
    if l.endswith('e'):
        print(l)
    else:print('ui')
print(

)
for k in m:
    print(k,end='-')
print(

)
t="tesla made by elon musk"
for g in t.split():
    if g[0]=='e':
        print(g)
l=[1,2,3,4,5]
for k in l:
    print(k*k)

elon='cow boy rings bell'
for lon in elon.split():
    if len(lon)%2==0:
        print(lon)
x='x made by elon musk'
for g in x.split():
    if len(g)%2==0:
        print(g)
# v='school boy across footpath'
# for l in v.split():
    # if len(l)==l[0:2]:
    #     print(l)
f='children plays games'
vowels='aeiouAEIOU'
count=0
for l in f:
    for char in l:
        if char in vowels:
            print(char)
# h='i lived in h tower'
# vowels=['a','e','i','o','u','A','E','I','O','U']
# result=('')
# for kat in h:
#     if not kat.lower in vowels:
#         result+=kat
# print(f"{result}",end=" ")

#### 'DEF FUNCTION'

def r(t,g):
    return t**g
# print(f"mul of {t} ** {g}={}")
print(r(9,3))
r(10,20)

def rog(o,p):
    print(o+p)
    print(o-p)
    print(hex(o+p))
    print(oct(o+p))
rog(40,10)

print('simple interset')

def ui(p,r,n):
    return p*r*n/100
print(ui(90000,8,10))

def sim(*p,r,n):
    print(int(p[0]*r*n/100))
    print(int(p[1]*r*n/100))
sim(10000,50000,r=8,n=10)


# def yt(p,r,n,t):
#     jk=p*r/n**t
#     return jk
# print(yt(50000,12.5,2,5))
#
# def cm(p,r,n,t):
#     gh=p(1+r/n)^(12,10)
#     print(gh)
#     ci=gh-p
#     print(ci)
# cm(500000,12.5,12,10)
# print(f'compound interest of cm is {ci}')

def r(g):
    return g**3
print(r(2))

def co(p,r,n,t):
    return p*r/n*t
print(co(10000,2,2,5))

# def co(p,r,n,t):
#     gh=p*r/n**t
#     print(gh)
#     ci=gh-p
#     print(ci)
# co(10000,2,2,5)


def io(f,m):
    v=f*m/100
    return v
print(io(1000,10))

import math as ma
def abc(pa,ri,tp):
    ci=pa*(ma.pow((1+ri/100),tp))
    print(int(ci))
    kl=ci-pa
    print(int(kl))
abc(50000,12.5,7)

# def xyz(paa,rii,tpp):
#     cii=paa*(3**1+rii/100)*tpp
#     print(cii)
#     asd=cii-paa
#     print(asd)
# xyz(50000,12.5,7)

def bo(jk):
    return jk.upper()
print(bo('country'))

def io(l,k):
    return l+" "+k
print(io('10','20'))
print()

b=[10]
c=[1,2,3,4,5]
for ck in c:
    b.append(ck)
    print(b)
print()
def axc(o,p):
    p=[]
    for op in o:
        p.append(op)
        print(p)
axc([1.1,1.24,13.44],p=[10,20])
print()

def rs(*m):
    return str(m[0][0:3]+" "+m[1][-3:-1]).upper()
print(rs('pratham','america'))
print()

# g={'c':"china",
#    'i':'india',
#    'b':'brazil',
#    's':'south africa'}
# def rt(*v):
#     return dict(v['c'])
# print(rt(*g))

v=[10,20]
for k in range(1,5):
    v.append(k)
    print(v)
print()

coun={'c':"china",
   'i':'india',
   'b':'brazil',
   's':'south africa'}
for l in coun.values():
    for k in coun.items():
        print(l,k)
for b in enumerate(coun.values()):
    print(b)
print()
j={1:'tata',
   2:'infosys',
   3:'mahindra',
   4:'gopal',
   5:'balaji'}
for k in enumerate(j.values()):
    print(k)

def hjk(o,p):
        for i in p:
            return i*o
print(hjk(o=[1,2,3,4,5],p=[2,4,6,8,10]))

o={9:"reta",
   3:"tacos",
   8:"jk",
   4:"io",
   2:"jio"}

for v in o.values():
    print(str(v[0:3]).upper())

i=[2,4,6,8,10,12,14,16,18,20]
for k,m in enumerate(i):
    print(f"{k} * {m} ={k*m}")

# g=['mann','rushit','harry','kaushal']
# for j in g[0]:
#     print(j[::-1],end=",")

o='Pratham'
print(o[::-1])
for s,d in enumerate(o[::-1]):
    print(s,d)
print()

g=['mann','rushit','harry','kaushal']
for k in g[1][::-1]:
    print(k)
print()

for b,d in enumerate(g[-1][::-2]):
    print(b,d)
for z in g[1]:
    if z=="s" and "i":
        print('loading....')
    else:print(z)
print()

ani=['lion','squirrel',
     'elephant','cheetah',
     'rhino','tiger']
for jun in ani[2]:
    if (jun=='e' ):
        print("waiting....")
    else:print(jun)
print()
# for h in ani:
#     print(h)
#     for k,l in enumerate(h[::-1]):
#         print(k,l)


for l in range(5):
    print(f"{l}+{5}={l+5}")
print()

t=[("a","apple"),("p",'pineapple'),
   ("c",'chiku'),('w','watermelon'),
   ('pu','pumpkin')]
for j in t:
    print(j[1][::-1])
print()
for w,b in t:
    print(b.upper()[::-1][0:4])
print()

# ani=['lion','squirrel',
#      'elephant','cheetah',
#      'rhino','tiger']
# for n in reversed(ani):
#     print(n)
# print()
# for l in ani[::-1]:
#     print(l)

# num=int(input('Any Number: '))
# fac=1
# for j in range(1,num+1):
#     fac=fac*j
# print('The factorial of %d = %d'%(num,fac))

# f=int(input(''))
# fas=1
# for k in range(1,fas-2):
#     fas=fas*k
# print('the fact of %d=%d'%(f,fas))

# b=int(input('num: '))
# fact=1
# for m in range(1,b+1):
#     fact=fact*m
#     print(b,fact)
# print(b,fact)


# b=int(input('factorial: '))
# fact=1
# for m in range(1,b+1):
#     fact=fact*m
#     print(f"{m}! = {fact}")
# print()
#
# g=int(input("sqr: "))
# print(g**2)
# print(g**3)
#
# sq=int(input("sqrt: "))
# print(sq**0.5)
#
# l=int(input("length: "))
# b=int(input("breath: "))
# g=0.5
# print(l*b*g)

a=2
b=3
c=4
a,b=b,a
b,c=c,b
a,c=c,a
c,b=b,c
print(a)
print(b)
print(c)
print()

s={1,2,3,4,5,6,8}
g={2,42,5,1,2,45,2}
print(s|g)
print(s&g)
print(s^g)
print()
g=[10,42]
for kg in range(3,7):
    g.append(kg)
    print(g)

o=['apple','america',
   'ball','brazil',
   'chiku','china']
v=0
for l in o[1]:
    print(v*l)
    # print(v,l)
    # print(f"{v} *={l}")
    v+=1

# s=int(input("num: "))
# for j in range(1,10):
#     print(f"{s} * {j} = {s*j}")

g='germany'
for j in g[-4:]:
    print(list(str(j).upper()))

# vac=int(input('num:'))
# cc=1
# for aa in range(1,vac+1):
#     va=vac*aa
#     print(f"{vac}*{aa}={va}")
#
# ab=int(input('op: '))
# cv=1
# for g in range(1,ab+1):
#     cv=cv*g
#     print(cv)
#
# fg=int(input("po: "))
# sd=1
# for y in range(1,fg+1):
#     sd=y*fg
#     print(f"{fg} *{y} ={sd}")
#
# a=int(input("as: "))
# b=1
# for c in range(1,a+1):
#     b=b*c
# print(f"{c}! = {b}")
# print()

# ab=int(input("float: "))
# cd=2
# for ba in range(1,ab-1):
#     dc=cd*ba
#     print(f"{cd} * {ba} = {dc}")

# abc=int(input("num: "))
# bca=1
# for ios in range(1,abc-1):
#     bca=bca*ios
#     print(f"{bca}:{ios}")

# x=int(input("nu: "))
# z=1
# for n in range(1,x+5):
#     zj=x*n
#     print(f"{x}*{n}={zj}")
# print()

# q=int(input("in: "))
# x=10
# for j in range(1,x+1):
#     b=b+j
#     print(f'{b}+{q}={b+q}')
# print()

# x=int(input("gh: "))
# z=10
# for i in range(1,x+1):
#     u=u*i
#     print(f'{u}*{i}={u}')

#### DOUBT #####
# xx=int(input("ni: "))
# xa=1
# for l in range(1,xx+1):
#     a=a+l
#     print(f"{a}+{l}={a}")

# k=int(input("mul: "))
# for l in range(11):
#     print(f"{k} * {l} = {k*l}")

s=random.randint(0,10)
if s>5:
    print(f"{s} it's great.")
elif s<5:
    print(f"{s} it's low.")
else:print("nothing")

print(12**2)
print(2**3)


# for sq in range(1,400):
#     if sq>=0:
#         print(sq**0.5)
#     else:print("no")

for b in range(1,6,1):
    for j in range(0,b):
        print("/",end=" ")
    print("")
print()
for k in range(5,0,-1):
    for a in range(0,k):
        print("-",end=" ")
    print("")

for y in range(1,6,1):
    for l in range(1,y):
        print("-","|",end=" ")
    print("*")

# for q in range(4,8):
#     for x in range(1,8,2):
#         print("",end=" ")
#     print("!")

t=[1342,533,24,242,3,24,23,345,324,2,11]
l=list(map(lambda h:round(h**0.5),t))
print(l)

d=[0,524,25,32,53,5235,3242,3532]
x=tuple(filter(lambda k:k/3,d))
print(x)

def rty(j):
    for d in j:
        if d/3==0:
            print(d)
        else:print('no')
rty([4244,35,33,54,2,532,43,42,52])
print()

z=100.00
f=0.08
c=5.0
print(z*(f+c))






















