a=-45
b=7.9
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(65//b)
print('a',b)
print(a%65)
print(a/65)
print(a//65)
print(id(a),id(b))
print(a+100)
print(b//1.5)

q=30
w=98
print(q+w)
print(q-w)
print(q%w)
print(q**w)
print(w//q)
print(q<w)
print(q==w)
print(q!=w)

print(11/2)
print(11//0.2,0.5)

a=14
b=15
c=16
d=17
print(a<b and a==b)
print(c<d and c!=d)
print(a<b and b<c)
print(c<d and d<a)
print(id(a),id(b),id(c),id(d))
print(a!=b and b!=c)
print(c>=d or d<=a)
print('a',20,'b',30,'c',40,'d',50)
print(a&b)
print(b&c)
print(c&d)
print(d&a)
print(a|b,b|c,c|d,d|a)
print(a^b,b^c,c^d,d^a)
print(bin(a&b),bin(b&c),bin(c&d),bin(d&a))
print(bin(a|b),bin(b|c),bin(c|d),bin(d|a))
print(bin(a^b),bin(b^c),bin(c^d),bin(d^a))
print(a%c,b%d,a%d,c%a,b%a)
print(a^c,b^a,c^d,d^b)
print(a+c,b-d,d*a,c/b,b//c)
a=9/6
b=8*5
c=6+3
d=8-20
print(c+d)
print(b-a)
print(c//-5.3)
print(d//2)
print(a%b)
print(b-c,d*b,a/b,b**d)
print(a**c,b//a)
print(c+2.65774)
print(a/6784.9073)
print(b-34.567)
print(b+a-c/d*b)
print(b+a*c//d-b)
print(d//b%a+c-20%a)
print(d//-3,-2,-1)
print(c*-5-4-3-2-1)
print(b^-50-40-30-20-10)
h="%s help us"
print(h%("god will"))
a=20200
b=50500
c=100000
d=50000
print(d/b+c-a*d)
print(a+c-d*b//c)
print( 20200 is  b)
print(100000 is not a)
print(a<c,b>d,c<b,d>a)
print(b/d+c-a*d/b)

name="my name is pratham"
print(len("pratham"))
oh_boy="kane williamson"
print(oh_boy)
print(oh_boy[0:7])
print(oh_boy,40)
print(oh_boy[3])
print(oh_boy,type(oh_boy))

a=23
b=4.500
print(a%b)
print(a,type(a),b,type(b))
c=23+4j
print(c,type(c))

k='''
     kane williamson
      
      '''
print(k,type(k))

"Lists"

nz=[240,'rachin ravindra',130.45]
print(nz)
print(nz,type(nz))

"TUPLES"

rr=(250,'rr',2+1)
print(rr,type(rr))

"DICT"

sa={
    'south africa_player':'marco jansen',
}
print(sa)
print(sa,type(sa))
print(sa['south africa_player'])

"SET"
u={-3,-2,-1,0,3,-2,-1}
print(u)
print(u)
print(u,type(u))

"INPUT"

#a=input("Enter the value1:- ")
#b=input("Enter the value2:- ")
#print(a+b)

#q=int(input("Enter the value: "))
#w=int(input("Enter the value: "))
#percentage=q%w
#print("Percentage:",percentage)






"TYPECASTING"
#float_number=36.7890
#print(int(float_number))
#int_number=56
#print(float(int_number))
#complex_number=45+8j
#print(type(complex_number))
#string_num="34""67"
#print(type(int(string_num)))
#print(float(string_num))

"STRING FORMAT METHOD"

sen_1="{n} sugars & {a} sugars".format(n="natural".upper(),a="artifical".upper())
print(sen_1)

sen_2= "{g} boy & {b} boy".format(g="good".upper(),b="bad".upper())
print(sen_2)

"3"

text_1="welcome to {} {}".format("kunj".upper(),"plaza.".upper())
print(text_1)

text_2= "rushit {} to {}.".format("gone","canada").title()
print(text_2)

"2"

line_1="{1} plays outside the {0}.".format("rohan".upper(),"ground".title())
print(line_1)

line_2= "{1} in the {0}.".format("king charles","london")
print(line_2)

u=[8,9,4,5,664785,7685,765585,768855,7885]
a=[67,38,769449,767859,67685,67589586,67858]
u,a=a,u
print("the value of u is",u)
print("the value of a is",a)
km=90.89
miles=(0.621371)*km
print(km,"kms in miles will be",miles)

km=100
miles=(0.621371)*km
print("kms in miles will be",miles)

"AREA OF TRIANGLE"

h=78.34
b=23.90
area=(0.5)*h*b
print("the area of triangle is",area)

a=12
print(a**2)

#q="Adittion {a:>100} between {b:^50}".format(a=30,b=40)
#print(q)

#a="pratham {c:<10} and {d:<30}".format(c=10,d=20)
#print(a)

#p="pratham."
#print(f"hello, my name is {p.upper()}")

#a=10
#b=30
#print(f"the sum of {a+b}.")

#cat=20
#dog=50
#print(f"the sum of {cat-dog}.")

#cow=2
#bell=4
#print(f"the sum of {cow*bell}.")

#tiger=4
#lion=2
#print(f"the remainder of {lion/tiger}.")
#print(f"the remainder of {tiger/lion}.")


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



print(4*(6+5))
print(4*6+5)
print(4+6*5)
print(type(3+1.5+4))


h="hello"
print(h[1])
print(h[-1:])
print(h[::-1])
print(h[4])


list=[23,45,23,10,34,[0,3,4,"party","om","raid"]]
list_2=[45,78,9,34,24,24,33,"keyboard","mouse","wire"]
print(list[5][2])
print(list[5][4].upper())
list[5][5]="police".upper()
print(list)

print(list+list_2)
list_2[7]="monitor".upper()
print(list_2)



t=[89,56,445,23,1212,4,5,45,5,46,4,54,64,35,6457,7,576,76,76,7,6545,66,7,44,5,3,5]
print(sorted(t))
print(sorted(set(t)))
print(t[0:4])
print(t[4:9])
print(t[3:27:4])
print(t[::-1])
print(t[-2:])
print(t[:-2])
print(t[::-2])
print(t[2:])

state={
  "business":"man",
  "gujarati":"adani",
    "rajastani":"marwadi",
    "south indian":"murthy",
    "mumbai":"wadia"
}
print(state["business"])
print(state["rajastani"].upper())
print(sorted(state))
print(state.keys())
print(state["mumbai"].upper())
state["delhi"]="godrej"
print(state.keys())
print(state["delhi"].upper())
for k,v in state.items():
    print(v.upper())
# for k in reversed(state.items()):
#     print(reversed(k))
for v in reversed(state["rajastani"]):
     print(v.upper())

for item in state:
    print(state)

bet={'business': [24,43,{'gujarati': ['adani', {'patel': [44, ['amabani', "birla", {"simcard": ["harshad", {"mumbai": ["wadia"]}]}]]}]}]}
print(bet["business"][2]["gujarati"][0].upper())
print(bet["business"][2]["gujarati"][1]["patel"][0])
print(bet["business"][2]["gujarati"][1]["patel"][1][2]["simcard"][1])
print(bet["business"][2]["gujarati"][1]["patel"][1][2]["simcard"][0].upper())
print(bet["business"][2]["gujarati"][1]["patel"][1][2]["simcard"][1]["mumbai"][0].upper())



i=[8,6,2,4,1,0,10,12,14,16,20,24]
for x in i:
    print(sorted(i))
for r in i:
    print(r)


e=[12,14,16,18,20]
for d in e:
    print(d*d)
for t in e:
    print("hello".upper()[0:4]*2)



q=[1,2,3,4,5,6,7,8,9,10]
w=2
for num in q:
    d=w+num
    print(d)
print(d)



y=(90,34),(12,45),(56,78),(78,54) # tuple
for a,b in y:
    print(a*b)
for a,b in y:
    print(b**0.5)


z=({20,34},{12,32},{90,19},{45,32}) # set is unordered
for a,b in z:
    print(a)

u=[23,45,23,12,13,145,[65,77,8,765,[54,5,6,[77,[65,["om".upper()],4],46],7,89,87],6543,23,456789],876,543,4567,8]
print(u[6][4][3][1][1][0]*5)
print(u[6][4][6])

one = [1,2,[3,4]]
two = [1,2,{'k1':4}]

print(one[2][0] >= two[2]['k1'])



a=20   # swap variable integers
b=40
c=60
d=a,b,c=b,c,a
print(d)


ab="10"
bc='30'
cd='50'
ab,bc,cd=bc,ab,cd
print(ab,bc,cd)

x=21
y=42
x,y=y,x
print(y,x)




continents={
    "asia":"china",
    "asia 2":"india",
"asia 3":"russia",
"asia 4":"pakistan",
}
print(continents["asia"])
continents["asia 5"]="sri lanka"
print(continents.values())
print(continents.items())
for loop in continents:
    print(loop)
for i,l in enumerate(continents):
    print(i,l)
for k,v in continents.items():
    print(f"{k}:{v}")
for num in continents.values():
    print(num)
# for h in continents:
#     if h=="asia 2":
#         continue
#     print(h)
for r in reversed(continents):
    print(r)


u="united kingdom"
print(u[0:5]) #unite
print(u[2:]) #ited kingdom
print(u[::-2]) #mdnk dtn
print(u[-3:]) #dom
print(u[::3]) #utno


d={"key1-a":{"key2-a":{"key 1":8000,
                       "key 2":8001,}},
   "key1-b":{"key2-b":{"key 1":8010,
                      "key 2":8011}},
   "key1-c":{"key2-a":{"key 1":8100,
                       "key 2":8101,}},
   "key1-d":{"key2-c":{"key 1":8110,
                       "key 2":8111}}}
print(d["key1-b"]["key2-b"]["key 1"])
print(d["key1-b"]["key2-b"]["key 2"])
print(d["key1-c"]["key2-a"]["key 1"])
print(d["key1-c"]["key2-a"]["key 2"])
print(d["key1-d"]["key2-c"]["key 1"])
print(d["key1-d"]["key2-c"]["key 2"])



names=["pratham","om","vsihal","rinku"]
roll_no=[20,12,34,78]
for t in zip(names,roll_no):
    print(t)

subject=["maths","science","english"]
scores=[23,45,67]
for subject,scores in zip(subject,scores):
    print(f"{subject}:{scores}")

n=["pratham","om","parth"]
a=[23,45,89]
print(dict(zip(n,a)))


n=["om","shaurya","pratham"]
a=[23,89,45]
print(dict(zip(n,a)))

branch="Bank"
if branch=="garage":
    print("true")
elif branch=="bank":
    print("ture")
elif branch=="hotels":
    print("tyre")
else:print("nothing")

h=[1,2,3,4,5,6,7,8,9,10]
for g in h:
    print(g)

f="print only the words that start with s in this sentence"
for j in f.split():
    if len(j)%2==0:
        print(j,"<-- len of the each word")

w=[0,1,2,3,4,5,6,7,8,9,10]
for k in w:
    if k%2==0:
        print("even number",k)

for a in range(1,51):
    if a%3==0:
        print("divisible by 3",a)

d="create a list of the first letters of every word in this string"
for l in d.split():
    if l[0]=="s":
        print(l)

def elephant(j="jungle"):
    print(f"all the animals live in the {j}".split())
elephant()

def items(b):
    print(b+"business man")
items("adani is ")
items("ratan tata is ")
items("mukesh ambani is ")

g=[9,2,3,4,2,4.3,44,4,32,322,2]
f=[]
for k in g:
    f.append(k)
print(f)

d=(12,33,44,134,34,4144)
didi=[]
for g in d:
    didi.append(g)
    print(didi)

print("there is %s who is sitting under the tree\n                          and waiting for the apple"%"issac newtown".upper())
mouse=90
keyboard=100
cpu=keyboard/500
print(f"the result of cpu is {cpu:.2f}".format(cpu))
print(f"the outcome of cpu is ------> {b:50.5f}".format(b=cpu))
print(f" the binary number of cpu is {bin(int(cpu))}")
print(f"the hexadecimal of cpu is {hex(int(cpu))}")
print(f"the octal number of cpu is {oct(int(cpu))}")

# g=[1,2,3,4,5,6]
# for kaggel in range(6):
#     for google in range(kaggel):
#         print(google,end=" ")
# print()

# rows=int(input("rows: "))
# columns=int(input("columns: "))
# streaks=input("streaks: ")
# for r in range(rows):
#     for c in range(columns):
#         print(streaks,end=" ")
#     print()




a="arcade developers"
# for alpha in a:
#     if alpha.split("d"):
#         continue
#     print(alpha)
for akon in a:
    if akon=="l":
        break
    print(akon)


fox=[1,2,3,4,5]
cow=[6,7,8,9,10]
for an in fox:
    for herb in cow:
     print(an,"+",herb,"=",an+herb)
    print()
    print()
    print()
for j in fox:
    for n in cow:
        print(f"{j} - {n} ={j-n}")
u="one unit,second unit,third unit"
w=0
for werd in u:
    print(f"{w}:{werd}".upper())
    w+=1
for i in enumerate(u):
    if i=="u":
        break
    print(i)
for k in u.split("unit"):
    print(k)
for j in enumerate(u.split("unit")):
    print(f"{j}:{u.split("unit")}")

# for q in u.split("third"):
#     print(f"{q} ----> {u.split("second","third")}")

d="united kingdom"
print(d.split("g"))

u="one department,second department,third department"
print(u.split("department"))

p="pratham"
for n,r in enumerate(p):
    print(n)
    print(r.upper())
    print(sep=":")

r=[10,12,14]
h=[11,13,15]
for q in zip(r,h):
    print(q)
# for k,g,j in enumerate(zip(r,h)):
#     print(f"{k} --->{g}:{j}")

f="fool"
s="string"
for h in zip(f,s):
    print(f"{h}")


a="abcdefgh"
b="bazball"
count=0
for x,z in zip(a,b):
    print(f"{count}:{x}:{z}".upper())
    count+=1

def g():
    print("there is a elephant in europe".split("e"))
g()

def f(r):
    return "there is %s sitting in the room"%"man"
d=f(r)
print(d)

def g(a):
    return "%s is king of jungle"%"lion".title()
l=g(a)
print(l)

def s(divine):
    print("divine ".upper()+divine)
s("mirchi".upper())
s("kaam25".upper())
s("3:59".upper())
s("satya".upper())

print(id(True))

def h(abb,tata):
    return abb/tata
g=h(500,300)
print(f"the result of g is {g:20.34f}")

rows=5
for j in range(rows):
    for i in range(j):
        print(j,end=" ")
    print()

for a in range(5):
    for h in range(8):
        print(h,end=" ")
    print()
c="cadbury"
j=[]
for k in c:
    j.append(k)
print(j)

h="hello"
g=[]
for e in h:
    g.append(e)
    print(g)
y=[word for word in "imagica"]
print(y)

p=[v**2 for v in range(1,10)]
print(p)

r=[(1,2,3,4,5,)]
t=[(11,12,13,14,15)]
for l in r:
    for j in t:
     print(f"{l}:{j}")

d={1,2,3,4,5}
f={6,7,8,9,10}
for m in d:
    for c in f:
        print(f"{m}>{c}")

a=["string","uk","cod","mustang","nissan gtr"]
f=[1,290,223,242,13,]

name,age=a,f
print(f"name:{a}")
print(f"age:{f}")

for j in zip(a,f):
    print(j)

d={
    "caution":"drink and drive",
    "ms":"word",
    "charts":"excel",
    "blood group":"A+",
    "cars":"nissan gtr",
}
for j in d.keys():
    print(j)

rows=10
for japan in range(rows):
    for shangai in range(japan):
        print(shangai,end=" ")
    print()

d=[1,2,3,4,5]
f=[1,2,3]
for n in d:
    for m in range(n):
        print(m,end=" ")
    print()

# rowws=int(input("rowws: "))
# colummns=int(input("colummns: "))
# stands=input("stands: ")
# for j in range(rowws):
#     for op in range(colummns):
#         print(stands,end="/"*3)
#     print()
roows=5
colnums=6
simbol="!"
for h in range(roows):
    for n in range(colnums):
        print(simbol,end="*"*2)
    print()


s=range(1,10)
d=[]
sx="#"
for kk in s:
    d.append(sx)
    print(sx,end=" "*3)
print()

r=range(1,10)
x=range(0,5)
f=[]
a="@"
for jolly in r:
    for kgf in x:
        f.append(kgf)
        print(a,end=""*3)
    print()

def k3g(name="motor"):
    return name+" son"
f=k3g("tata".title())
print(f)

def n(c=12,v=15):
    return c/v
asd=n(10,20)
print("the result of asd is {xuv:.2f}".format(xuv=asd))

def a(area=90.23,perimeter=23.45):
    return area*perimeter/1/2
cvb=a(145.78,2390.443)
print(f"the total of a is {cvb}".format(cvb))
print(f"the result of a is {cvb:.3}".format(cvb))
print(f"the outcome of a is {cvb:.4f}".format(cvb))

# simson="!"
# for n in range(1,6):
#     for s in n:
#         print(s,end=" ")
#     print()


# oil_well=5
# for n in oil_well:
#     for m in n.


# g=60
# for ant in :
#     print("gala")

f=(1,2,3,4,5)
for g in f:
    pass
    print("faug")




s="sundar"
for j in s:
    print(j.upper()*2)



" 3/10/2024 "

def sum_values(c,v):
    return c+v
print(sum_values(20,10))

def kl(first_name,last_name):
    return first_name + last_name
print(kl("virat"," kohli"))
print(kl("ms"," dhoni"))
print(kl("rohit"," sharma"))

def banglore(numerical,python):
    return numerical/python
print(banglore(100,23))
print(banglore(12,90))
print(banglore(12,84))
print(banglore(15,32))
# print(f"the total of banglore is {b:.2f}".format(b=banglore(numerical=12,python=55)))

def mumbai(d,g):
    return d|g
f=mumbai(55,44)
print(f)
print(mumbai(34,19))
# print(mumbai("12","90"))

"check even number by use DEF FUNCTION"

def rome(values):
    dsa=values%2==0
    return dsa
print(rome(12))
print(rome(14))
print(rome(45))

def france(paris,belgium):
    fda=paris or belgium %3==0
    return fda
print(france(12,6))
print(france(10,3))
print(france(29,99))
print(france(15,18))

def suii(ronaldo):
    for crist in ronaldo:
        if crist%2==0:
            return True
        else:return False
print(suii([0,2,4]))
print(suii([1,3,5]))
print(suii([12,14,18]))

def mess(lion):
    for adidas in lion:
        if adidas%2==0:
            return "Yes"
        else:return "NO"
print(mess([10,11,15]))
print(mess([5,7,9]))

def gta(tfue=20,shroud=90):
    return tfue&shroud
print(gta(100,500))

def cod(io):
    return io//2
print(cod(45))

s=5
if s%2==0:
    print("true")
else:print("false")

def red(dragon):
    if dragon%2==0:
        return "rahul == true"
    else:return "kohli == false"
print(red(3))
print(red(6))

g=[(1,2,3),(9,3,2),(5,3,2)]
for ap,vb in enumerate(g):
    print(f"{ap}")

def ops(cod,fbi):
    return cod^fbi
print(ops(45,90))
print(ops(23,12))
print(ops(34,23))

def b(python):
    for cobra in python:
        if cobra%2==0:
            return "mission passed".upper()
        else:return "mission failed".upper()
print(b([2,4,6]))
print(b([3,5,7]))


# g="gta"
# if g=="gta vice city":
#     pri

def gif(small):
    return small[0]==small[0]
print(gif(small="mango"))
print(gif(small="apple"))

def figi(n):
    if n%2==0:
        return "dna".upper()
    else: return "blood".upper()
print(figi(24))
print(figi(39))

def paris(ux):
    for r in ux:
        if r%2==0:
            return "o+".upper()
        else: return "o-".upper()
print(paris([2,4,6]))
print(paris([1,22,33,44]))
print(paris({1,2,3,4,6}))
print(paris({10,20,30,40,50}))


def games(g):
    if g=="gta vice city":
        return "misson\n   failed".upper()
    elif g=="gta san andreas":
        return "misson\n   passed".upper()
    elif g=="gta 4":
        return "mission\n   failed".upper()
    elif g=="gta 5":
        return "mission\n   passed".upper()
    else: return "no pain"
print(games("gta 5"))

def rt(io):
    if io>=100:
        return "bingo".upper()
    elif io<=50:
        return "binge".upper()
    else: return "failed".upper()
print(rt(60))




def v(rog=20,tuf=50):
    return rog+tuf
print(v(10,20))

f=(1,2,3),(4,5,6)
for a in f[0]:
    print(a)
for aa,b,c in f:
    print(b)

def hell(ledger):
    for journal in ledger:
        if journal%2==0:
            return "PASS"
        else:return "FAIL"
print(hell([2,4,6]))
print(hell([1,3,5,7]))


fd=[1,2,3,4,5]
for m in fd:
    for v in range(m):
        print(v,end=" ")
    print()
kl=6
kohli=5
for mm in range(kl):
    for l in range(kohli):
        print(l,end=" ")
    print()

h=4
g=7
for a in range(h):
    for x in range(g):
        print(x,end=" ")
    print()

print("the grass is always\tgreener than otherside")
print("")

print("i once aught a fish %s"%"this \tbig.")

i="%s\tindia"
print(i%("%s is in third position in the economy race."))

# a="2.5"
# b=int(float(a))+int(a)
# print(b)

" 5/10/2024 "

def b(sand,water):
    print(f"{sand[0]}:{water[0]}")
b("watermelon","santoor")

def america(r,a):
    print(f"{r[0][0]}:{a[1][0]}".upper())
america("reddragon china","american eagle")

def jk(shimla):
    c=shimla.split()
    print(f"{c[0][0]}:{c[1]}")
print(jk("jammu kashmir"))
print(jk("janm sthami in august"))

def bat(f1,f2):
    return f1+f2==20
print(bat(2,1))
print(bat(10,10))

def o(j,k):
     if j+k==50:
        return "cid".upper()
     else:return "crime patrol".upper()
print(o(10,50))
print(o(10,40))

def watch(dogs,cats):
    if dogs%2==0 and cats%2==0:
        return min(dogs,cats)
    else: return max(dogs,cats)
print(watch(2,4))
print(watch(1,3,))

def b(bat,ball):
    for m in bat:
        for i in ball:
            if m%4==0 and i%5==0:
                return min(i,m)
            else:return max(m,i)
print(b([2,4,8,12,16,20],[3,5,10,15,20]))

def mushroom(veg,nonveg):
    for b in veg:
        for k in nonveg:
            print(f"{b%2==0} ====== {k%2==0}")
            # return max(b,k)
        # else:return min(b,k)
print(mushroom([2,3,4,5],[5,6,7,8]))

def xcu(red,blue):
    return red+blue==10
print(xcu(3,7))
print(xcu(2,9))

def cvb(o,p):
    if o+p==10:
        return "rocket".upper()
    else:return "crash".upper()
print(cvb(2,8))
print(cvb(2,5))

def eminem(bird):
    for k in bird:
        if k%2==0:
            return True
        else: return False
print(eminem([2,4,6]))
print(eminem([3,6,9]))

def n(a,b):
    if a%2==0 and b%2==0:
        print(f"{min(a,b)} | {max(a,b)} ")
        return min(a,b)
    else:return max(a,b)
print(n(2,4))
print(n(2,5))

def r(s,d):
    if s%2==0 and d%2==0:
        return min(s,d)
    else:return max(s,d)
print(r(10,24))
print(r(11,12))

def tea(chaas,paneer):
    print(f"{chaas[0]}:{paneer[0]}".upper())
    return chaas[0]==paneer[0]
print(tea("leopard","animal"))

def color(red,blue):
    print(f"{red[0]} == {blue[0]}")
print(color("united states of america","united soviet"))


def vb(m,n,mn):
    if m%2==0 and n%3==0 and mn%4==0:
        return "YOUTUBE"
    else:return "TWITCH"
print(vb(8,9,24))

def g():
    print('''
    pratham
        patel''')
g()
def trimmer(wwe,wwf):
    return wwe==wwf and wwe//wwf and wwe<wwf
    # return wwe+wwf and wwe/wwf and wwe*wwf
print(trimmer(23,90))

for k in range(1,6):
    for l in range(k):
        print(l,end=" ")
    print()

def c(jelly="strawberry",jam="mixed fruit"):
    print(f"{jelly[0]}=={jam[0]}")
print(c(jelly="watermelon",jam="pineapple"))

def vitamin(c,m):
    return bin(c**m)
print(vitamin(10,20))

def c(o,p):
    print(chr(o*p))
    print(chr(o//p))
c(10,20)

def cv(a,m):
    return a+m
print(cv(0.1,0.2))
print(cv(0.30,0.10))
print(cv(0.10,0.10))

def asd(m,n,c):
    if m+n==c:
        return "yes"
    else:return "no".upper()
print(asd(0.10,0.10,0.3))

def gif(jeth="tree",seth="three"):
    return chr(jeth+seth)
print(gif(jeth=90,seth=100))

print(0.8/3/4)










# for j in range(1,6):
#     for r in range(0,5):
#         print(r,end=" ")
#     print()

# def cod(d=input("vals: ")):
#     for h in d:
#         if h%2==0:
#             return "ACCESS"
#         else:
#             return "NOT ACCESS"
# print(cod())









# things=str(input("stores: "))
# if things=="bank":
#     print("bank".upper())
# elif things=="ice cream shop":
#     print("ice cream".upper())
# elif things=="grain shop":
#     print("grain shop".upper().split("A"))
# elif things=="garage":
#     print("garage".upper().split("G"))
# else:print("nothing")

# f={"male":23,"female":44,"man":12}
# print(f["male"])
#
#
#
#
# list_4=[89,45,67,34,[90,"pratham","om","rushit",90+8j]]
# print(list_4[4][4])
# print(type(list_4[4][4]))
#
