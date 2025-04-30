
#################### FOR LOOP (BREAK,PASS,CONTINUE) USE IN LIST########################################################
o=[90,45,34,23]
for item in o:
     pass
print("om is bad boy.".upper())

i=[2,4,6,8,10]
for j in i:
    pass
print(23)

p=[2,4,6,8,10,12,14,16,18,20]
for g in p:
    pass
print(g,"is even")
print(p,"is even")
for t in p:
    pass
print("joe biden withdraw his name from US elections.")

c="counter strike"
for r in c:
    pass
print("global offensive")


r=[2,4,6,8]
for w in r:
    if w==6:
        continue
    print(w)

a=[1,3,5,7]
for k in a:
    pass
    print("gamers")


e=[90,45,66,333,4,4,5,5]
for loop in e:
    if loop==66:
        break
    print(loop)
r="rajastan"
for t in r:
    if t=="a":
        break
    print(t)
for loop in r:
    if loop=="a":
        continue
    print(loop.upper())

t=[(11,10),(12,45),(22,14),(23,56)]
for w in t:
    if w==(11,10):
        continue
    print(w)

f="france"
for loop in f:
    if loop=="r":
        continue
    print(loop)
for g in f:
    if g=="n":
        break
    print(g.upper())


############################################## FOR LOOP (CONTINUE,BREAK,PASS) IN STRINGS ###############################

c="china"
for letter in c:
    if letter=="n":
        continue
    print(letter)

i='india'
for t in i:
    if t=="d":
        continue
    print(t.upper())

s=({23,45,89,45,6,7,54,34,5,3})  ########################### SET ####################################
print(type(s))
# for o in s:
#     if o==89:
#         continue
#     print(o)
for loop in s:
    if loop==45:
        break
    print(loop)

b="barack obama"
count=0
for character in b:
    if character=="b":
        print(f"{character}:{count}")
    count+=1
count=0
for u in b:
    print(f"{b}:{u}")
    count+=1
for j in b:
    if j=="a":
        continue
    print(j.upper()*5)
for i in b:
    if i=="a":
        break
    print(i)
print(b.find("a",2))

c="the box of full of chocolates"
for f in c.split():
    if len(f)%2==0:
     print(f)
for g in c.split():
    if g[0]=="o":
        print(g.upper())
count=0
for character in c:
    print(f"{character.upper()}:{count}")
    count+=1

t="the box of full of chocolates"
for letter in t:
    if letter=="f":
        continue
    print(letter)
for loop in t.split():
    if loop[0]=="b":
        print(loop)

f="france"
for i in f:
    if i=="r":
        continue
    print(i)
for t in f:
    if t=="n":
        break
    print(t.upper())

d={"dict":"telephone",
   "business":"india",
   "adani":"cemet",
   "amabani":"jio simcard"}
for f in d.items():
    if f=="business":
          break
    print(f)



a=("america is best than tokyo")
print(list(str(a)))

w={"south africa":"shamsi",
   "america":"texas",
   "india":23,
   "keyboard":45}
print(list(str(w)))



r="republic of china"
count=0
for character in r:
    print(f"{count}:{r}")
    count+=1
for i,e in enumerate(r):
    print(f'{e}:{i}')
for word in r.split():
    if word[0]=="r":
        print(word)
for x in r.split():
    if len(x)%2==0:
        print(x)
q=[12,23,34]
for u in zip(r,q):
    print(u)


r="republic of china"
c="coronavirus"
print(f"{c} spreads by {r}.")


print(45+90-90+2/34**2)
print(not 89<90 and 34<90)
print(not 23>90 or 200<100)
print(56==90 and 34!=90)
print(34==90 or 56<45)
print(89&77 and 90|23 or 45^75)

s="s"
q="s"
print(s==q)

c="china"
r="republic of china"
print(c==r)

b="bill cliton was a president of united states of america."
for loop in b.split():
    if loop[0]=="o":
      print(loop)
for word in b.split():
    if len(word)%3==0:
        print(word)
for w in b.split():
    if len(w)%2==0:
        print(w.upper())
print(list(b.split()))
print(list(b))

q={12,34,56,78,90}
print(list(q))


a=10
a-=89
print(a)

r=45
r*=89
print(r**0.5)

o=90
d=90
print(bool(not(89<100)))



print("{1} and {0} are rivals in the united states of america.".format("donald trump","joe biden"))



f={"dictionary":"telephone",
   "directory":"names",
   "age":2345212123344,
"phone number":"89457672663",
   "government":"indian",
   "job role":"prime minister",
   "states":"gujarat"
   }
for k,v in f.items():
    print(k.upper())
for word in f.items():
    if len(word)%2==0:
        print(word)
for loop in enumerate(f):
    print(loop)
count=0
for character in f.values():
    print(f"{character}:{count}")
    count+=1
# s=[]
# for d in f:
#     d.join(f)
#     print(d)


o="%s in the box"
print(o%("chocolates in the"))



w=90
print(id(w))
w=w-34
print(id(w))
w=w-w
print(id(w))



# e=["list",89,234,{23,78,445}]
# w=[89,4,839,4539890,(55445,94,10,89,484)]
#
# print(e[3]<w[4])

y={1,2,4,589,989,445,5.6} ################################### UNION AND INTERSECTION USE IN SET #####################
z={2,89,45,89.89,46,"abc","xyz"}
print(type(y))
print(y|z)
print("set a U b = ",y.union(z))
print(y&z) # common number find in set  ####
print("set y intersection z = ",y.intersection(z))

print("tictac has less followed by public comparison to ",end=" ")
print("gems".upper())
print("amit","shah","took","3.4 lacs","shares","of","larsen","and",sep="<",end="")
print("turbo")



print("/"*1)
print("/"*2)
print("/"*4)
print("/"*8)
print("/"*12)
print("/"*16)
print("/"*20)

d="donald trump is a business of america." ################################### NEW PRACTICE ############################
f=[]
for t in d:
    f.append(t)
    print(f)

w=[23,89,78,445,8900]
q=[12,89,78,344,87823]
for u in zip(w,q):
    print(u)


q=[2,4,6,8,10]
e=[1,3,5,7,9]
for t in q:
    for u in e:
        print(t*u)
# for y in q:
#     print("2*",y,"=",2*y)

for t in q:
    for g in e:
        print(t,"*",g,"=",t*g)
for g in zip(q,e):
    print(g)
for t in q:
 for y in e:
     print(t,":",y)
for u in zip(q,e):
    print(list(str(u)))
# print(set(u))


d=(23,89),(12,3),(67,89),(89,9)
p=[]
for a,b in d:
    # print(a)
    # print(b)
    print(a,"*",b,"=",a*b)
    # print(a*b**0.5)

f=[2,3,4,5,6]
t=[1,3,4,5,6]
for g in zip(f,t):
    print(g)
for z in f:
    for x in t:
         print(z,"*",x,"=",z*x)
#         print("2*",z,x,"=",2*z,x) ####
for s in f:
    for i in t:
        print(s)
        print(i)
        print(sep="/")
for q in f:
    for y in t:
        print(f)
        print(t)
        print(sep="/")
        print(f,t,sep="^")



for g in f:
    for h in t:
        print(g,"/",h)
        print(g,"*",h,"=",g*h)
        print(f,"+",t,"=",f+t)
        print(g,"+",h,"=",g+h)


a=[2,39,0,889,34]
b=[89,34,89,89]

for t in a:
    for y in b:
        print(t,"*",y,"=",t*y)

w=(2,3),(4,5),(6,7),(8,9)
e=(1,3),(3,5),(7,9),(10,12)

for t in zip(w,e):
    print(t)
for r in w:
    for u in e:
        print(r+u)
for u in w:
    if u==(4,5):
        break
    print(u)
for i in w:
    if  i==(6,7):
        continue
    print(i)
# for g in w: #####
#     for o in e:
#      if g==(4,5):
#          continue
#      print(g)
#      if o==(7,9):
#          break
#      print(o)


p={1,2,3,4,5,6,7,8,9,10,22,10,12201,22,}
l={0,2,3,4,589,77,46,7678,454,677,4354}
print(p|l)
print(set(p))
print(set(l))


q=(12,23),(34,89),(78,90),(70,90)
i=[]
for u in q:
    i.append(u)
    print(list(u))
for a,b in q:
    print(a*b-a+b//a**0.5)
for x,y in q:
    print(x+y-109)
for d in q:
    if d==(78,90):
        break
    print(sum(d))

o="om"
d=[]
for t in o:
    d.append(t)
    print(d)


w=[1,2,3,4,5,6,7,8,9,10]
for u in w:
    if u==5:
        break
    print(u)
for t in w:
    if t==9:
        continue
    print(t)
for i in w:
    print("2*",i,"=",2*i)
for q in w:
    if q%3==0:
        print(q)
for r in w:
    print(r*r)


d=(0,2),(1,3),(2,4),(3,5),(4,6)
f=[]
for a in d:
    f.append(a)
    print(f)
for b in d:
    print("2*",b,"=",2*b)
for x,y in d:
    print(x*y**2)


ww2="united states of america dropped the atom bomb on the japan."
for y in ww2.split():
    if len(y)%2==0:
        print(y)
for e in ww2.split():
    if e[0]=="t":
     print(e)
print(set(ww2))





def sum_sub_mul(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e


result=sum_sub_mul(10,5)
print(result)
print("type of result is ",type(result))


def cs():
    print("counter")
    print("strike")
cs()

r={1,39,40,578,3789,90,35,78,345,3667}
print(type(r))
print(sorted(r))
u=[]
for y in r:
    u.append(y)
    print(u)
for u in r:
    print(u**0.5)
for y in r:
    print(y,"-",100,"=",y-100)
if 578 in r:
    print("yes")
else:print("no")

if 578<3667 in r:
    print("valid")
else: print("in valid")


p=[2,4,6,8,10,12,14,16,18,20]
for o in p:
    print(o**2)
for w in p:
    print(w+10)
print(w+10)


person=("hopkins",89,"profession")
name=age=role=person
print(f"{name}:")
print(f"{age}")
print(f"{role}")

print(f"name:{name}")
print(f"age:{age}")
print(f"role:{role}")


def func():
    return 5,-7.15,[4,5]
x,y,z=func()
print(x,y,z)

r=[1,2,3,4,5]
g=[]
for k in r:
    g.append(5)
    print(g)

f=(1,2,3),(9,3,34),(9,8,90)
for a,b,c in set(f):
    print(a,b,c)

op=[1,99,233,0,9,343,453]
print(set(op))

d1=[1,2,3,4,5]
d2=["a","b","c","d","e"]
for j in dict(zip(d1,d2)):
    print(j)
for m in zip(d1,d2):
    print(m)

for a,v in zip(d1,d2):
    print(f"for first item {a} and second item is {v}".format(a,v))

t="tree"
print(f"there is a {t}.")

g=[1,2,3]
if "c" in g:
    print("true")
else:
    print("false")

# def inpu(n):
#     print("hello "+n)
# inpu(str(input("words: ")))

def sen(k):
    for i in k:
        if i[0]=="L"and i[0]=="L":
            return True
        else: return False
g=sen("Levelheaded Llama")
f=sen("Crazy kngaroo")
print(g)
print(f)

def dolar(c,r):
    if c+r==20:
        return 'yes'
    else: return "no"
rupee=dolar(10,20)
yuan=dolar(12,8)
ruble=dolar(13,0)
print(rupee)
print(yuan)
print(ruble)

# def food(naam):
#     for l in str(naam).capitalize():
#         if l[0].capitalize() and l[4].capitalize():
#             return "valid"
#         else: return "Not valid"
# salad=food("macdoanld")
# print(salad)

# d=[12,9,3,4,4,343,43,43,4,432,432,23]
# for l in d:
#     if l%2==0:
#         print(min(l)

g=range(15,30)
for l in g:
    if l%2==0:
        print(l)
w=20
d=30
print(w+d,w-d,w*d,w/d)

name="pratham"
print(name)

h="hello"
print(h*10)

p="pratham"
last_name="patel"
print(p+" "+last_name)

b="barack obama"
print(b[0:5])

u="united kingdom"
print(u[1:])

name,age="pratham",23
print(f"{name}|{age}")

a,b,c="pizza","apple pie","watermelon"
print(f"there are three different food items {a}:{b}:{c}")

spo=['cricket',"football","soccer","rugby","volleyball"]
print(spo[2])
spo[2]="golf"
print(spo)

n=[20,90,24,51,100,24,24211,43,85,9241]
del n[5]
print(n)

for k,n in zip(spo,n):
    print(f"{k}:{n}".upper())

rafale=[12,12902,13,3,24,242,2,410,30]
golf=[5,13,90,89,343,43,5,235,32525]
d=rafale+golf
print(d)
print(set(d))

hop={"rud":23,"bhavya":90,"smith":23,"rafale":11,"thomas":233}
print(hop["rud"])
del hop["smith"]
print(hop)
print(list(str(hop.keys())))
print(hop.values())
print(hop.items())

pictures=("singham","singham returns","singham again","simmba","sooryavanshi")
print(pictures.index("simmba"))

h=(1,2,9,4,2,2,4,24,3,4,44)
print(h[0:4])

print(chr(100))
print(ord("Z"))

#### LAMBDA ####

# map(lambda x:x*2,numbers)
double=lambda   x:x*2
print(double(2))
print(double(3))

a=lambda c:c*2
print(a(5))
print()
b=lambda c,d:c+d
print(b(2,3))

prat=lambda g:g+4
print(prat(g=5))
parth=lambda p:p+2-3*4/5
print(parth(p=10))
print()

cat=lambda bat:True if bat%2==0 else False
print(cat(10))
print(cat(11))
print(cat(14))

ball=lambda foot:foot+10
print(ball(foot=-10))
print()
print(ball(foot=-20))
print()

hippo=[1,2,3,4,5,6]
forest=lambda hippo:hippo*2
print(forest(hippo))
print()

cricket=[1,2,3,4,5]
pad=lambda cricket:cricket*2
print(pad(cricket))

f=lambda c:c*2
print(f(c=2))

d=lambda dog:dog*2
c=lambda dog,coat:coat*dog*3
print(c(dog=10,coat=20))
# e=lambda dog,cat:dog,cat
print()

# photo=[1,2,3,4,5]
# frame=lambda photo:photo*2+3-4//5
# print(frame(photo[0:3]))

print((lambda c,v:c+v)(10,3))
print((lambda a,b,c,d:a+b-c*d//a)(10,20,30,40))
print()

# g=["ten","nine","thirteen","twelve","eleven"]
# print(lambda g:len(g)

gm=lambda a,b,c,:a*b//c
print(gm(a=20,b=10,c=5))
print()
# b=lambda a:a*a
# c=b(10,4)
# print(c)

z=lambda s:s*2
print(z(s=2))
print()

figi=lambda cube:cube*4
print(figi(cube=5))
print((lambda g:g+2-4*7+10)(g=90))
print((lambda v:bin(v))(v=2))
print((lambda c:chr(c))(c=100))
print((lambda o:ord(o))(o="p"))
# print((lambda e:bin(e+r))(e=10,r=
print((lambda f:f*f)(f=9))
print((lambda a,s:a+s)(a=10,s=-0.9))
print((lambda first,last:first+" "+last)(first="sunriser",last="hydrebad".title()))
print()
print((lambda n:"ACCESS" if n<10 else False)(n=4))
print()
a_b_c=lambda xyz:xyz*2
print(a_b_c(xyz=2))

cat=lambda c,a:c+a
cat_result=cat(c=10,a=-0.3)
print(cat_result)
print((lambda f,l:f+l)(f="first",l="one"))
f=lambda filipino:filipino
k=lambda phillips,filipino:phillips+" "+filipino
print(k(filipino="as we".upper(),phillips="get".upper()))

america=lambda biden:biden
usa=lambda biden,us:biden+" released long range missile on "+us
print(usa(biden="ukraine".title(),us="russia.".capitalize()))
print()
cuban=lambda c,u,b,a,n,:c+u//b-a**n
print(cuban(-0.1,-0.2,-0.3,-0.4,-0.5))
print(cuban(c=-0.10,u=-0.15,b=-0.20,a=-0.25,n=-0.30))
print(cuban(10,20,30,40,50))
print(

)
delhi=lambda d,e,l,h,i:oct(d+e-l**h//i)
print(delhi(10,20,30,40,50))
print(delhi(100,200,300,400,500))
print(

)
kota=lambda k,o,t,a:hex(k//o-t+a)
print(kota(50,40,30,20))
print(

)
print((lambda h,d,a:a-d+h)(h=10,d=10,a=5))
print((lambda b,i,l:b+i-j*l//i)(b=10,i=20,l=21))
print()
print((lambda s,h,i,t:s+h-i*t)(s=10,h=-1.15,i=2.5,t=-3.5))
b=lambda v:v*2.5
print(b(v=-0.5))
print(

)
r=lambda f:f*0.5
print(r(f=0.5))
print((lambda d:d**3)(d=2))
print((lambda q:q**3)(q=0.5))
print((lambda r:r%2)(r=6))
print()
print(6%2,6//2)
print(200%3)
print(100%50,50%100,3%6)
print()
print((lambda ios:ios//5)(ios=100))
print((lambda app:app/5)(app=10))
# print((lambda apps:apps[::-2])(list(apps=[1,2,3,4,5,6,7,8,9,10])))
print()
mao=[1,2,3,4,5,6,7,8,9,10]
print(mao[::-2],mao[::-3],mao[::-4],mao[::-5])
# print(sum(mao[::-2],mao[::-3],mao[::-4],mao[::-5]))
# print(sum(mao[::-2],mao[::-3]))
print(sum(mao[::-2]),sum(mao[::-3]))
print(mao[2::2])
print(mao[:5:2])
print((lambda mao:sum(mao)))
print()
print((lambda l:chr(l+2))(l=90))
print()
def abc(o):
    return lambda d:d*o
p=abc(2)
print(p(10))
def g(p):
    return lambda k:k**p
t=g(2)
print(t(12))

def v(l):
    for i in l[0:4]:
      # return i
     print(i)
types=[1,2,3,4,5,6]
v(types)
print()

h=lambda kangaroo:kangaroo*2
print(h(5))

i=lambda flash,light,electricity:electricity+flash+light
print(hex(i(10,20,30)))
print(chr(i(100,200,300)))
print(id(i(500,2001,29.32)))
print(i(-0.1,-0.10,-0.4))
print()

def g(k,h):
    return lambda o,p:o*p
j=g(10,20)
print(j(2,3))
print()

def america(usa):
    return lambda biden:biden*usa
joe=america(2)
trump=america(3)
print(joe(4))
print(trump(5))
print()
def rigi(dhoni):
    return lambda ms:ms+dhoni
# print(f"the addition of {ms}+{dhoni}=={ms+dhoni}")
singh=rigi(10)
paan=rigi(20)
print(singh(5))
print(paan(10))
print()
def face(recon):
    return lambda b:b+b
create=face(100)
web=face(100)
print(create(20))
print(web(10))
print()

def game(match):
    return lambda fees:fees+match
penalty=game(100)
due=game(100)
print(penalty(10))
print(due(20))
print()

def cricket(bat,ball):
    return lambda b,c:bat+ball
pad=cricket(10,20)
pads=cricket(5,15)
print(pad(2,4))
print(pads(1,3))
print()

def t(i,o,s):
    return lambda c,p,l:c*i and o*p and s*l
g=t(1,2,3)
e=t(4,5,6)
l=t(7,8,9)
print(g(10,20,30))
print(e(40,50,60))
print(l(70,80,90))
print()

def captain(america,kingdom):
    return lambda chris,evans:america+kingdom and chris*america
cap=captain(10,20)
tail=captain(100,200)
print(cap(30,40))
print(tail(5,15))
print()


def foot(ball,kick):
    return lambda b,k:kick+ball or b*ball or ball-kick
clear=foot(10,200)
bowling=foot(30,10)
print(clear(1,2))
print(bowling(3,4))
print()
def goat(cr,messi):
    return lambda c,m:c*m or m+messi
r=goat(5,6)
s=goat(7,8)
# print(r)
# print(s)
print(r(1,2))
print(s(3,4))
print()

def bread(layer,slices):
    return lambda n,m:layer*slices/layer+slices-layer
b=bread(10,20)
l=bread(-10,-20)
print(b(2,3),l(-2,-3))
print()
def ring(marriage):
    return lambda reception:reception*marriage
flowers=ring(4)
flows=ring(5)
print(flowers(10))
print(flows(10))
print()

##########    MAP   #######

# def kashmir(jammu):
#     return len(jammu)
# c=map(kashmir,("one","two","three","four"))

valu=[1,2,3,4,5]
def square(x):
    return x**2
square_numbers=list(map(square,valu))
print(square_numbers)

k=[1,2,3,4,5]
def c(v):
    return v**3
sq_3=list(map(c,k))
print(sq_3)

words=["one","two","three","four","five"]
def b(o):
    for v in o[0:3][0]:
        print(v.upper())
b(words)

# atamcs=[1,2,3,4,5,[10,20,[100,200,300,[1000,2000,3000,[0.1,0.2,[0.0,0.1]]]]]]
# def fogg(f):
#     for l in f[5][][]:
#         return l
# print(fogg(atamcs))

print((lambda c,v,b:c+v-b)(10,20,30))
print((lambda cat,dog,cow:bin(cow-cat+dog))(dog=100,cat=200,cow=100))
print((lambda lion,tiger,zebra:oct(tiger+zebra-lion))(20,20,30))
print()

w=lambda d:d*d
print(w(2))
print()

crack=lambda c,a:c+a
print(crack(10,20))
print()
energy=lambda d,a:d==a
print(energy(10,20))
print()

# def bio(graphy):
#     print((lambda kgf:k+g+f*graphy))
# deisel=bio(10)

def r(rigi):
    return lambda rog:chr(rog*rigi)
dhani=r(10)
print(dhani(100))
print()

def bogo(offer,free):
    return lambda left,right:offer+left and free+right
pizza=bogo(2,3)
print(pizza(10,20))
print()
def business(devops,web):
    return lambda opera,mini:devops+opera or web+mini
it=business(2,3)
consultant=business(10,20)
print(it(100,200))
print(consultant(5,4))
print()

def mario(game,resume):
    return lambda g,r:g+game and r+resume
pause=mario(2,3)
setting=mario(10,20)
print(pause(1000,2000))
print(setting(100,200))
print()

# def bharat(forge):
#     for t in forge:
#         return lambda g:t
# sona=bharat(list[1,2,3,4,5,6,7,8,9,10])
# print(sona[1,2,3,4,5,6,7,8,9,10])

# def planet(dwarf):
#     return lambda t:dwarf
# for k in t:
#     print(k)
# g=planet([1,2,3,4,5])
# print(g)






# i={1:"one",2:"two"}
# d={1:"one",2:"two"}
# print(id(i)==id(d))
# print(bin(i)==bin(d))
# print(type(i)==type(d))


# def trump(donald):
#     return lambda r:t==donald
# tower=trump(10)
# manger=trump(20)
# print(tower(100))
# print(manger(200))

# def b(c,d):
#     print(lambda c,d:c+d)
# e=b(100,200)
# g=(30,40)
# print(e(10,20))
# print(g(30,40)

# def old(spice,new):
#     print((lambda s,n:s+spice,(lambda s,n:n+new)))
# o=old(2,3)
# print(old(10,20))

# def cements(bricks,stones):
#     print(lambda b,s:b+bricks(lambda b,s:s+stones))
# cost=cements(2,3)
# print(cost)

def kgf(jk,cements):
    return lambda j,k:j+jk or k+cements
r=kgf(100,3)
rr=kgf(5,10)
print(r(10,20))
print(rr(1,2))

trap=lambda zoo:input("zoo:")
if trap==10:
    print("true")
elif trap!=5:
    print("yes")
else:
    print("nothing")
print()

canada=lambda camel:camel+2
america=lambda joe,biden:joe+biden
print(canada(2))
print(america(2,4))
print()

high=lambda c,v:c if c<v else v
print(high(10,15))
print()

va=lambda v:v%2==0
print(va(10))
print(va(15))
print()

print(p(10),p(20),p(40))
print()

print((lambda tiger:"valid"if tiger<=100 else "invalid")(tiger=101))
print()
# v=input((lambda f:"access".upper() if f<=100 else "reject")(101))
# print(v)

# pratham=int(input("pratham:-"))
# p=lambda pratham:"true".upper() if pratham>=100 else "false".upper()
# print(p)

# p=((lambda pratham:"true".upper() if pratham>=100 else "false".upper())(pratham=int(input("pratham:- ")))) $$$$$$$$$$$$$$$$$$$$$$$
# print(p)

# condition=((lambda ops:"yes".upper()if ops<=100 elif ops<=50 else "no".upper())(ops=int(input("ops:-"))))
# print(condition)

# state=((lambda write:"fireworks".upper().split() if write<=50
#         else "lose\nthe\nair\nballon".upper().split())(write=int(input("word:- ")))) $$$$$$$$$$$$$$$$$$$$
# print(state)



# print("the name of the president.".split(":"))
text="the,name/of/president."
g=text.split("/",3)
print(g)

pra="pratham/is/good/boy"
patel=pra.split("/",5000)
print(patel)

i="india,is,great,country"
t=i.split(",",2)
print(t)

# h=((lambda horse:"true".upper()if horse>=-50 else "false".upper())(horse=float(input("horse: "))))
# print(h)
# d=((lambda donkey:"passed".upper()if donkey>=50 else "failed".upper())(donkey=int(input("donkey: "))))
# print(d)

def nirma(college,unicorn):
    return lambda c,u:c+college and u+unicorn
student=nirma(0.2,0.3)
teacher=nirma(0.10,0.20)
print(student(10,20),print(teacher(0.02,0.03)))

def sqr(v):
    return v**2
k=[1,2,3,4,5]
print(list(map(sqr,k)))

def b(o):
    return o*3
g=[1,2,3,4,5]
print(list(map(b,g)))

def miraj(carrier):
    return carrier+2
aircraft=[1,2,3,4,5]
print(f"{aircraft}+{2}=={tuple(map(miraj,aircraft))}")
print(tuple(map(miraj,aircraft)))

# def mart(v):
#     return lambda b:"true"if b%2==0 else "false"
# f=mart([1,2,3,4,5,6,7,8,9,10])
# print(f([1,2,3,4,5,6,7,8,9,10]))

def soap(life):
    return lambda l:l**life
boy=soap(2)
print(boy(20))

def beauty(brain):
    return lambda b:b+brain[3]
key=beauty([10,20,30,300])
print(key(20))

def sector(pfc,vmart):
    return lambda m,n:m+pfc and n+vmart
report=sector(5,10)
print(report(2,4))

def cube(i):
    return i*i*i
gig=lambda i:i*i*i
print(cube(5))
print(cube(6))

def ios(s):
    return s+s*s
u=lambda s:s+s*s
print(f"defined function with ios(s):",{ios(2)})
print(ios(2))
print(f"using lambda function,ios(s):",{ios(4)})
print(ios(4))
print()

def retail(store):
    for t in store[0:4]:
        print(t)
f=retail([10,2.3,3.45,4.12,5.231,6.90,7.1314])
print()

def canada(visa,pr):
    return visa+pr*visa/pr
v=lambda visa,pr:visa+pr*visa/pr
print(canada(5,10))
print(canada(2,5))
print()

def dance(zumba):
    print("2"+zumba)
dance("4")
dance("5")
dance("6")

def firm(comp):
    print("tata\n     ".upper()+comp)
firm("tea".upper())
firm("motors".upper())
firm("technology".upper())
firm("power".upper())
print()

def green(energy):
    return energy+energy//energy
i=lambda energy:energy-energy+energy
print(green(200))

# def b(o):
#     return o*3
# g=[1,2,3,4,5]
# print(list(map(b,g)))

def addition(edison):
    return edison//3
p=[1,2,3,4,5]
print(list(map(addition,p)))

def borison(boggy,doggy):
    return boggy+doggy-boggy/doggy
u=lambda boggy,doggy:boggy+doggy-boggy/doggy
print(borison(10,15))

n=[4,3,2,1]
print(list(map(lambda x:x**2,n)))

def l(p):
    for c in p:
     if c//3==0:
        print("true")
     else:
         print("fail")
v=l([3,9,12,15])

def value(num):
    return num**2
j=[1,2,3,4,5]
print(set(map(value,j)))
for i in map(value,j):
    print(i)

def line(sting):
    if len(sting)%2==0:
        return "EVEN"
    else:return sting[0]
m=["dictionary","pratham","set","laptop","monitor"]
print(list(map(line,m)))

def bowl(spicy):
    if len(spicy)%2==0:
        return "yes".upper()
    else:return spicy[0]
k=("pratham","america","new","kiwis","zealand")
print(set(map(bowl,k)))
print(type(map(bowl,k)))

def spicy(meal):
    return lambda meal:sorted(meal)
o=["paneer bowl","maggi","salad","milkshake","pizza","burger","apple","falooda"]
print(tuple(sorted(o)))

def food(fruits):
    print((lambda fruits:sorted(fruits)))
t=["apple","pineapple","watermelon","kiwi","cherry"]
print(tuple(sorted(t)))
print(len(t))
print()

# def brands(shoes,cars):
#     return lambda shoes,cars:map(shoes,cars)
# shoes=["nike","puma","bata","adidas","new balance","campus"]
# cars=["tata","mahindra","roblox","tesla","raven","cadilla"]
# print(set(map(shoes,cars)))

# def brands(shoes):
#     return lambda shoes:map (shoes)
# sole=["nike","puma","adidas","new balance","campus"]
# print(set(map(brands,sole)))

# def store(retails):
#     return lambda retails:map
# o=["pantaloons","zudio","bata","beardo"]
# tuple(map(store,o))

s=["1","2","3","4"]
j=map(float,s)
print(tuple(j))

# def shoes(s):
#     return list(map(shoes,d))
# d=["nike",'adidas',"puma","campus","skechers"]
# print(tuple(map(shoes,d)))

shoes=["nike","adidas","campus","skechers","puma"]
# print(map(lambda s:s.upper(),shoes))
h=map(lambda s:s.upper(),shoes)
print(tuple(h))
print()

def brands(boots):
    return lambda boots:boots.capitalize()
o=["converse","bata","campus","centrino"]
j=map(lambda f:f[0:3].upper(),o)
print(tuple(j))

def integers(vals):
    return lambda vals:vals
k=["1","2","3","4","5"]
va=map(lambda h:int(h),k)
print(set(va))

def c(n):
    return lambda c:int(c)
d=["1","2","3","4"]
# b=map(bin(lambda s:float(s),d))
b=map(lambda s:int(s),d)
print(tuple(b))

def mini(browser):
    if len(browser)%2==0:
        return "browse"
    else:return browser[0]
l=["yandex","google browser","duck","duck","go","opera"]
print(tuple(map(mini,l)))

# g=["0.1","0.2","0.3","0.4"]
# print((lambda h:set(map(h,p)))([1,2,3,4,5]))

print(4** 2)

def c(v):
    return v**3
l=[1,2,3,4,5]
print(tuple(map(c,l)))
print()

# def walker(jhonny):
#       p=["walker","scotch","red","label"]
# print(list(map(walker,p[0:3])))

def klm(k,l,m):
    return lambda c,v,b:k+c*v//b
# print(f"i put a more spaces before the value:{klm:10}")
f=klm(0.1,0.2,0.3)
print(f(10,20,30))

def o(p):
    return p*2
h=[1,2,3,4]
print(tuple(map(o,h)))

def golmaal(again):
    return again+2
d=lambda again:again*2
print(d(12))

def rice(paneer):
    return lambda paneer:paneer*paneer
f=rice(10)
print(f(12))

def kiwi(street):
    return street[0:5].uppper()
o=lambda street:street[0:3].upper()*3
print(o("golmaal again"))

# d="japan street"
# print((lambda d:d.upper()*3))

print((lambda g:g[0:5].upper()*3 and g[-6:].upper()*3)("japan street"))
print((lambda b,n,m:b+n+m/3)(10,20,30))
print((lambda c,v,b:c[0:3] and v[0:5] and b[0:4])("america","england","india"))

# def m(k): return k**3
# print(square(5))

def t(a):
    return a
d=lambda a:a**5
print(d(2))

s=lambda s:s[0:4].upper()
print(s("united kingdom"))
print()

n="new zealand"
for k in reversed(n[0:5].upper()):
    print(k*4)

# n=lambda o:reversed(o[0:5].upper())
# print(n("gerald goetzee"))

g=lambda f:f*f*f
print(g(10))
print()
# s=lambda c:reversed(c) $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
# print(s("titanic"))

# s=[10,20,30,40]
# print(lambda x:x*2,(tuple(map(x,s)))) $$$$$$$$$$$$$$$$$$$$$$$$$$$
# print(list(map(lambda n:n*2,[1,2,3,4,5])))


k=lambda g:g.upper()
print(k("titanic"))
n=lambda h:len(h)
print(n("united"))
g=lambda s:s[0:5]
print(g("america"))
p=lambda f:sorted(f)
print(p(["ten","four","three","one"]))




# n=10
# if n<5:
#     print("true")
# elif n<=2:
#     print("true")
# else:
#     print("nothing")


# f=int(input("x:"))
# if f<10:
#     print("true".title())
# else:
#     print("false".title())