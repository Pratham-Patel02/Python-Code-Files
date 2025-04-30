print(0.1+0.2)

if 0.1+0.2==0.3:
    print("true")
else:print("false")

print(chr(100+200))

if chr(67)=="C":
    print("true")
else:print("false")

n=[100,200,22,90,23,32,23124,2,19,4538,553,900,45]
s=["lsit","strimg","dictonary","tuple"]
q=n+s
print(q)
print(sorted(n))
print(str(n).isalnum())
print(str(n).isdigit())
print(str(n).isalpha())
print(type(s))
print(tuple(n))
print(chr(sum(n)))
print(ord(s[0][0]))
print(bin(sum(n)))
n.remove(200)
n.insert(1,10)
print(n)
print(n)
print(n[0-5])
print(q.clear())

w=["words","sentences","alphabets","dictionary","sets","tuple"]
print(w[2][0:5].upper())
print(w[3].split())
w.pop(1)
print(w)
print(w.pop())
print(len(w))
w.reverse()
print(w)
w.sort()
print(w)

g=["sring",8.233,9834,(12,90)]
if g[1]==g[3][0]:
    print("true")
else:print("false")
g[0]=12
print(g)
if g[0]==g[3][0]:
    print("yes")
else:print("no")
g[3]=24,23
print(g)
# print(sum(chr(g[3])))
print(chr(sum(g[3])))

key=[1,2,3,4,5,[10,20,30,40,[100,200,300,400]]]
print(key[0:4])
print(key[5][4][2])
print(sum(key[5][4][0:4]))
print(chr(sum(key[5][4][0:4])))
print(bin(sum(key[5][0:4]))),print(chr(sum(key[5][0:4])))
print(chr(sum(key[5][4][0:3])))
print(bin(sum(key[5][4][0:3])))

t=[1,2,3,4,5,[2,3,4,[8,9,[10]]]]
print(t[5][3][2][0])
print(bin(t[5][3][2][0]))

d=["sorted","apple","ballet","cat","tree","zebra","long"]
d.sort()
print(d)

u={"apple":23,
   "pineapple":200,
   "cat":4,
   "nimbu":20,
   "car":10.40500,
   "grass":200
   }
print(u["car"])
u["pineapple"]=10
print(u.values())
u.pop("apple")
print(u)
u["trucks"]=30
print(u.keys())
#
f={"bikes":20.999,"numbers":[100,200,300],"fruits":{"apple":20}}
print(f["numbers"][1])
print(f["fruits"]["apple"])
f["fruits"]["apple"]="watermelon"
print(f.items())
f["fruits"]["apple"]="mango"
print(f)
f["numbers"]=10,20,30
print(f.values())
f["fruits"]
print(f)
print(f["fruits"])
print(str(f["fruits"]))

a=10
b=40
c=10
d=56
print(a/b)
print(c*d)
print(a+c%d//b)
print(a//d,b+c,c**2,d+10)
print(chr(a+b-c+d))
print(chr(a//d))
print(chr(a-c))
print(chr(c+b))
print(chr(a+b+c+d))
print(ord("A"))
print(ord("z"))
print(a==b or b!=c)
print(a==c and b!=d)

s='string'
print("s" in 'string')
print("s" not in "string")

print(id(90+12-89))
print(bin(89-45*23))
print(oct(12390+2423))
print(hex(12**2))
print(oct((90)))
print(id(2*10+10*3))
print(chr(2*3*4*5*6*7*8*9))
print(bin(10*9*8*7*6*5*4*3*2*1))
print(chr(34))
print(bin(100-90-80-7-1))
print(chr(500))

print(45.89+13.922)
print(id(12.90+89.24))
print(oct(12))
print(id(1))
print(bin(12|34))
print(bin(34&90))
print(id(90^654))
print(oct(56&78))

apple=-5
ball=-10

print(apple|ball)
print(apple+ball)
print(-100+5)
print(-100-10)
print(+100+15)
print(+100-20)
print(apple//1.5)
print(ball^apple)
print(ball%apple)
print(apple==ball)

ios=[1,2,4,[90,24]]
syrup=[12,9023,{"chocolate":20}]
print(syrup[2]["chocolate"])
print(ios[3][0]+syrup[2]["chocolate"])
print(bin(ios[3][1]-syrup[2]["chocolate"]))

r={"title":
{"movies":"go goa gone",
 "m1":"shivaay",
 "m2":"main hoon na",
 "web series":"taaza khabar",
 "shows":"wagle ki duniya",
 "fight shows":"bigg boss",
 "comedy movie":"hera pheri"
 }}
print(r["title"])
print(r["title"]["movies"].upper())
r["title"]["movies"]="phir hera pheri"
print(r["title"].values())
print(len("title"))
del r["title"]["movies"]
print(r["title"].values())
print(r["title"].get("fight shows"))
r["title"].pop("m2")
print(r["title"].values())
print(list(r["title"]))
del r["title"]["shows"]
print(r["title"].items())
print(r["title"]["web series"]==r["title"]["comedy movie"])

mouse=[1,2,3,
       [4,5,6],
       [7,8,9]]
print(mouse[3])
print(mouse[4])
print(sum(mouse[3])/2)
print(sum(mouse[4])*2)
print(mouse[4])
print(mouse[0:4])

fr=["apple","pineapple","watermelon","strawberry","chocolate","litchi","mango"]
print(fr[0:3])
print(fr[2:])
print(fr[:5])
print(fr[-3:])
print(fr[:-3])
print(fr[::-1])
# fr.sort()
# print(fr)
print(fr[1:7:2])
# fr[2:7:1].append('orange')
f=fr.append("orange")
print(fr)
d=fr
d.append("chiki")
print(d)
print(d[2:-2])
print(d[::-2])

v=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(v[::-2])
print(v[::-4])
print(v[-4:])
print(v[::2])
print(v[::5])
print(id(v[5]))
print(bin(v[3]))
v.insert(3,34)
print(v)
print(v.index(34))
del v[4:10]
del v[3:10]
print(v)
g=[90,23,32]
v.append(g)
print(v)
f=["fly","ccoco","birds"]
g.append(f)
print(g)
del g[3][1]
print(g)

p=[1,2,3,4,5]
pg=[10,20,30,10]
p.extend(pg)
print(p)
p.extend(f)
print(p)
# mop=list(input("l: "))
# print(p+mop)

punk=["dictionary",34.8922,1223,True,{"data":"consumers"},(20,34,21)]
print(type(punk[0]))
cyber=["usa","grand","sting"]
punk.extend(cyber)
print(punk)
print(type(punk[4]))
print(type(punk[5]))
print(type(punk)[4])

one=[1,2,3]
two=[4,5,6]
three=[7,8,9]
four=[one,two,three]
print(four)
print(four[0][1])
print(four[0].index(3))
print(four[1].index(5))

c={"list":123.4,
   "loops":"fruit loops",
   "dictionary":{"south":"chennai"}}
print(c["dictionary"]["south"])
c["loops"]="for","while"
print(c)
print(c["loops"][0].upper())
c["floats"]=89.342
print(c.keys())
c["list"]=1,2,3,4,5
print(c['list'])

fgh={"books":[1,2,3,{"movies":["kuch kuch hota hai",{"shows":["cid",{"country":"america"}]}]}]}
print(fgh["books"][3]["movies"][0])
print(fgh["books"][3]["movies"][1]["shows"][1]["country"].upper())


p={"fruits":"apple",
   "pvr":"movies",
   "washroom":"gents",
   "sports":"cricket",
   "equipment":"ball",
   }
print(p.clear())
print(p)

f=[[1,3,5],
   [7,9,11],
   [13,15,17],
   ]
print(f[0])
print(f[0].index(5))
print(f[1])
print(f[1].index(9))
print(tuple(f))
print(type(tuple(f)))
print(type(f))
if f[0].index(3)==f[2].index(15):
    print("yes")
else:print("no")
print(sum(f[0])/3)
print(f[2][1]/3)
g=[19,21,23]
f.extend(g) ############################################## IN EXTEND THERE IS NO OPEN SQUARE BRACKET REQUIRED ##########
print(f)
f.append(g) ########################################### IN APPEND THERE IS A SQUARE BRACKET IN NESTED LIST #############
print(f)
print(bin(f[2][1]))

u=90.344
print(int(u))
print(complex(u))
# k=[1,2,3]
# print(float(k))
g="100"
print(float(g))

s={1,2,34,90}
print(type(s))

f=[0,234,343,4353,432.53,52]
f.pop(1)
print(f)
f.reverse()
print(f)
print(f[-4::])

print("pratham\tpatel")

e=40
if e<=10 or e<=50 or e<=20:
    print("50")
else:print("10")

q=10
if q<=5 and a<=15:
    print("true")
else:print("false")

p="pratham"
print(p+" is a good boy !"*3)

print("i am earth".capitalize())
i="i am earth"
print(i[5:10].capitalize())
print("there are two who led the team of bjp party {} and {}".format("narendra modi","amit shah"))
print("{1} and {0} are rivals in US elections".format("joe biden","donald trump"))

d=100/456
print(d)
print("the exact outcome of {s:1.3f}".format(s=d))
print("the result outcome is {r:4f}".format(r=d))

f=12
g=10
gp=f/g
print("result of {a:5f}".format(a=gp))

q=12
e=34
sa=q+e
print("final of {ds:10.23f}".format(ds=sa))

r=[1,23,400,435,332,53,325,89,429,3259,88,89,4329]
r.sort()
print(r)
r.insert(2,100)
print(r)
r[2]=1400
print(r)
print(r.count(89))
r.remove(325)
print(r)
a=["string","tuple","dictionary","set"]
# r.extend(a)
# print(r)
a.sort()
print(a)
d=[0,2,4,6,8]
d.append(r)
print(r)
print(r[::-2])
del r[0:6]
print(r)
print(r[2:-3])
print(r[2:])

mouse=[3.45,1.23,9.89,0.34,8,12.34,89.345,"keyboard","desktop","graphic card"]
print(mouse[-2:])
print(mouse[-1][8:10].capitalize())
print(mouse[-3][0:3].find("e"))
print(mouse[-3][0:3].find("a"))
print(mouse[-1].find("a",4))
print(mouse[-1].partition("r"))

u="united states of america"
print(u.capitalize())
print(u.find("s",8))
print(u.partition("a"))
print(u.split("t"))
print(u[0:4].upper()*5+"/"*5) # how to separate unite from *5 #####

gta={
    "collections":{
        "games":"grand theft auto",
        "sports":"cricket",
        "movies":"main hoon na",
        "companies":"wipro",
        "gender":"male","female":"lady",
    "cars":"bmw",
    }
}
print(gta)
print(gta["collections"]["sports"])
print(gta["collections"]["games"])
gta["collections"]["sports"]="football"
print(gta["collections"]["sports"])
# print(list(str(gta["collections"])))
del gta ["collections"]["female"]
print(gta["collections"].keys())

s=(1,2,3,4,5,6,78)
print(s.__mul__(3))
print(s.__add__((90,100)))
d=[1,2,3,4,5]
print(tuple(d))
print(type(d))
print(f"{30:10.30f}".format(30))
j={100,100.23,10.34,200}
print(type(j))
j.update({500})
print(j)
j.add(19000)
print(j)
k={90,100,200,500,30,10,2,5,32}
print(k)
print(k.intersection(j)) # INTERSECTION MEANS FIND SAME NUMBER IN BOTH THE SET ###########################
print(k.union(j))
print(k^j)
print(k)


sd={10,20,30,40,50,60}
memo={10,100,200,300,40,50,60}
print(sd|memo)
print(sd^memo)
print(sd&memo)
# print(f"result of {e:6.10f}".format(e=memo[1]))
print(sum(memo))
# print(f"pratham{p:1.3f}".format(p=sum(memo)))
print(bin(sum(memo)))
print(chr(sum(memo)))
print(hex(sum(memo)))
print(oct(sum(memo)))

print("%s is the prime minister of india"%'narendra modi')
print("%s will release in diwali 2024"%"singham again")
print("%s is better than american chocolate"%"british chocolate".capitalize())
s,m="putin","modi"
print("%s come to india\nand meet prime minister %s"%(s,m))
t,tw="30","20"
print("%s is greater than %s"%(tw,t))
print("now a days\n      there is no movies will %s"%"release")
b,bo,c="bat","bowl","cricket"
print("%s and %s are most important things in %s"%(b,bo,c))
v,g,i="india","gujarat","vadodara"
print("i live in %s\n             %s\n                 %s"%(i,g,v))
sp=12,555
print(f"bajaj auto share price is {sp}")
print("vadanta shares jump from 400 to %s in just one week"%"512")
print("{} and {} and {} performed a dance in anant ambani wedding".format("salman khan","shah rukh khan","aamir khan"))
# print("%s and %s meeet in usa during quad summit 2024" %"google tech ceo" %"narendra modi")

o=90.1423
g=34.7845
p=o/g
print("the total result of float is {m:50.10f}".format(m=p))

i=90
w=34
z=i/w
print("the result of int is {f:100.5f}".format(f=z))

faug=90+8j
pubg=23+9j
fort=faug*pubg
print("the total result is {cod:500.50f}".format(cod=fort))

o=[20,4,91,103,23,24,4,213,6,4,8,102,120,1500]
for j in o:
    if j%2==0:
        print(j)
# print(j.bit_count())
# else:print("%s odd one out:"%())
    else:print(f"odd number:{j}")

l=0
for g in o:
    l=l+g
print(g)

s=[1,2,3,(90,34454),{90,34252},{"90":"ninghty"}]
a=[(90,89.24),{1,2,3},["sting","str"],{"game":"pubg"}]
print(a[0][0]|s[3][1])
if s[4]==a[1]:
    print("oh yes"+"!")
else:print("oh no")


movies=[("movies","bhool bhuliyaa"),("singham again","snub"),("dangal","force"),("clean","dirty")]
for t,b in movies:
    print(t.split("a"))
for k in enumerate(movies):
    print(k)

print("there is a %s near the canal"%"crocodile")
print("there is %s in the box"%"bunch of chocolates")
k,d="kim jong un","donald trump"
print("%s and %s both have the nuclear power"%(d,k))
print(f"the final result (outcome) of {f:1.30f}".format(f=89.23+12.98))

print("there are so many villages in india as compare to america".split("i"))
print(f"there is so many population in india {23.932234342:.2f}")
f=9.3242
g=32.424
h=f/g
print(f"{h:.2f}")

shyam=80
taam=40
shaan=12
jaam=shyam/shaan+taam
print(f"result of three students is {jaam:.2f}".format(jaam))
print(f"outcome of students is {jaam:90.45f}".format(jaam))
print("there is a scientific research that human wants\t8 hour sleep.")

r=[[10,20,30],
   [30,40,50],
   [60,70,80]
   ]
for a,b,c in r:
    print(a)

g="monster"
for k in enumerate(g):
    print(f"{k}")

city=[1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,22,24,26,28,30]
for downtown in city:
    if downtown==12:
        break
    print(downtown)

u="united kingdom"
for g in u[0:4]:
    print(g.upper())
for usa in u[-7:-3]:
    print(usa.split("i"))
for n in u:
    print(n.upper(),end=" "*3)

i="india"
for k in range(5):
    for l in i:
        print(l.upper(),end=" ")



f=[[1,2,3],[4,5,6]]
print(f[0])
for y in range(2):
    for a in f[0]:
        print(a)
h=(1,3,5),(5,7,9)
for s in range(3):
    for n in h[1]:
        print(n,end="-"*3)
print()
khajur=[10,20,290,242,2,42,4,3]
khajur.sort()
print(khajur)
for j in range(4):
    for k in khajur[0:3]:
        print(k,end=":"*3)
print()
if khajur[5]=="42":
    print("equal")
else:print("not equal")

boat=[1,2,3,4,5]
aeroplane=[6,7,8,9,10]
for l in zip(boat,aeroplane):
    print(l)
for a in enumerate(zip(boat,aeroplane)):
    print(a)
print()
count=0
for paisa in zip(boat,aeroplane):
    print(f"{count}:{list(paisa)}")
    count+=1
print()
v_mart=0
for kaala,khatta in zip(boat,aeroplane):
    print(f"{v_mart}:{kaala}:{khatta}")
    v_mart+=1

print("the precision of formating is {g:<f}".format(g=20.233904353533))

a=10
b=20
c=30
a,b,c=b,c,a
print(b,c,a)
print(a,b,c)
print(c,b,a)
print(a,c,b)

p='Print only the words that start with s in this sentence'
for l in p.split():
    if l[0]=="s":
        print(l)

for j in range(0,10):
    if j%2==0:
        print(j)

# o=[range(1,50)]
# print(type(o))
# for k in o:
#     if k%3==0:
#         print(k)

f='Print every word in this sentence that has an even number of letters'
for s in f.split():
    if len(s)%2==0:
        print(s.upper())

k='Create a list of the first letters of every word in this string'
for i in k.split():
    print(list[i[0].upper()])
# for g in k.split():
#     print(i[0:25][15].upper())

print([x for x in range(1,51)if x%3==0])

d=range(0,51)
for h in d:
    if h%3==0:
        print(h)



# dashes_means_rows=int(input("dashes_means_rows: "))
# stand_lines_means_columns=int(input("stand_lines_means_columns: "))
# asterisk=input("asterisk: ")
# for v in range(dashes_means_rows):
#     for h in range(stand_lines_means_columns):
#         print(asterisk,end=" ")
#     print()


# e=90
# print(type(e))
# print(str(e))
# print(float(e))
# print(complex(e))





# print(float((1,2,3)))

# for a,b,c in four:
#     print(f"{a} & {b} & {c}")

# asd=["string","gogo","ball","america","canada","belgium"]
# asd.sort()
# print(asd)

# i=int(input("v: "))
# print(chr(i))

# print(2+10*(10+3))
# print(chr(67))
