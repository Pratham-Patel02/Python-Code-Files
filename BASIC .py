
fruits= "apple","mango","watermelon","pineapple"
vegetables= "cabbage","onion","tomato","carrot"
print(fruits+vegetables)
print(fruits[0:2])

c="call of the Duty"
print('a'in c)
x=('1:a and 2:b')
print('2'in x)

["LOGICAL OPERATOR"]
a=10
b=20
print(a<b)
print(b>a)
print(a==b)
print(b!=a)
print(a>b and b<a)
print(a!=b or b<a)

["MEMBERSHIP OPERATOR"]
j="joe Biden"
print('b' in j)
u=-3,-2,-1,0
print(-3 in u)
print(0 not in u)

["IDENTIFY OPERATOR"]
u= -2,-1,0
a= -1,-2,3,
print(u is a)
print(u is not a)

["LOGI"]
a=20
b=80
print(a<b and a!=b)
print(b>a or b==a)      
                        
u="man TAKES umbrella for himself"              
print('takes'in u)
s="%s sat on the bench"           
print(s%("a man"))
print(s[0:10])
a=20
b=50
print(a*b)
print(a+b)
print(a%b)
print(a/b)
print(a**3)
print(a<b and b>a)
print(a>b or a!=b)

["BITWISE OPERATOR"]
a=10
b=50
print(bin(a&b))
print(bin(a|b))
print(a^b,bin(a^b))
c=45
d=50
print(bin(c&d),c&d)                 
print(c|d, bin(c|d))                   
print(bin(c^d))

a=20
b=50
print(a&b,bin(a&b))
print(a|b,bin(a|b))
print(a^b,bin(a^b))
q=0
w=1
print(q&w,bin(q&w))
print(q|w,bin(q|w))
print(q^w,bin(q^w))

print(19&7)
print(12|9)

a={'0,2,4,6,8,10,12,14,16,18,20'}
print('8'in a)

a=10
b=-10
c=0
print(a-10)
print(10-5)
print(10+5)
print(-10-5)
print(-10+5)
print(+10+5)

a=24
b=50
print(a&b)
print(a|b)
print(a^b)
print(a&b,bin(a&b))
print(a|b,bin(a|b))

c=40
d=-10
print(c<d or c>d)
print(c==d and c!=d)
print(d<c and c>d)
print(d*50)
print(c/100)
print(d-100)
print(-10+23)
print(d+60)
print(d+60*40/80)
print(c**50)

j="%s 50"
print(j %("100+"))
print("%s" in j)
print('60'not in j)
print('50' in j)
print(id(j),id(50))

q='12'
w='34'
print(q==w and q!=w)
print(w>q or w==q)
print('12' in w)
print('12' in q)

a=40
b=67
print(a&b,bin(a&b))
print(a|b,bin(a|b))
print(a^b,bin(a^b))
print(bin(a&b),a&b)
print(bin(a|b),a|b)
print(bin(a^b),a^b)

print(11/2)
print(11//2.0)


x={'a','b'}
print('a'in x)
o=3456
u=5213
print(u-o)
print(o/u)
print(o&u)
print(u|o)
print(u|o,bin(u|o))
print(o==u or o<u)
print(id(o),id(u))
print(u!=o and u==o)

print("the","taj","mahal","situated","in","the","agra.", sep="-")
print("America is near the",end=" ")
print("Cuba.",end=" ")
print()
print("shroud is best player in",end=" ")
print("Esports.")

print("shroud is the best player in the",end=" ")
print("csgo".upper())
print("pratham")


#o=input("Enter the values: ").split()
#print(o)


j=[8,9,6,5,7,4,1,0,3]
print(j)
del j[0:4]
print(j)
j.pop(2)
print(j)

k=[2,4,6,8,10]
print(k[2]&45)
print(k[3]//8)

a=2
b=4
c=6
d=8
gmean=(a*b)/(a+b)
gmeans=(c*d)/(c+d)
print(gmean)
print(gmeans)

#d={'name: pratham'
 #  'salary':50000}
#print(d{'name'})

s={
'name':'pratham',
'age':23,
'salary': 50000
}
print(s['salary'])
print(s['name'][0:3])


a={
'laptop':'Asus',
'category':'F15',
'price': 75800,
'name':'asus rog',
'battery':'90watthour'
}
print(a['laptop'])
print(a['name'].upper())
print(a['laptop'],a['category'])
print(a['battery'].split())


k=["keyboardmousemotherboardprocessor"]
print(sorted(k))
print(k.count('k'))

n={
'number':9033868708,
'name':'pratham',
'age': 23,
'gender':'male'
}
print(n['name'])
print(n['age'])
print(n['number'])
print(n['gender'])

h={"name": "pratham",
   "name1": "om",
   "name2": "shaurya",
   "name3": "manan",
   "name4": "smith",
   "name5": "raj"
   }
print(h["name1"])
print(h["name2"].upper())
print(h["name4"].upper().split())


"PARTICULAR DATA"

d={"name7":"pratham",
   "phone": 9409166254,
   "age":21,
   "height": 180,
   "last name": "patel",
   "studied":"BITS",
   }
print(9409166254 in d)
print("9409166254" in "phone")
print(d["name7"],d["last name"].upper())
print(d["height"])
print(d["name7"])
print(d["age"])


q={(2,1):"A",
   (3,4):"B",
   (5,6):"c",
   }
print(q.values())
print(q.keys())
print(list(q.keys()))
print(list(q.values()))
print(list(q.items()))
print(q.keys(),q.values())



w={"tower":"H",
   "flat":"I",
   "duplex":"second",
   }
print(w.get("tower"))

a={"name":"pratham",
   "std":"fifth",
   "age":21,
   "gender":"male",
   "phone":9409166254,
   }
print(a.get("name").upper())
print(a.get("phone"))
print(a.keys())
print(a.values())
print(list(a.items()))
print(bin(a["phone"]))
#del a["phone"]
#print(a)
print(a.pop("phone"))
print(a)
print(a["std"][0:3].find("i"))


"COLLEGE TEACHERS"
n={"name":"amal",
   "k1":"jitin",
   "k2":"adit",
   "k3":"devang",
   "k4":"amit",
   }
print(n.keys())
print(n.values())
print(n.items())
print(list(n.items()))
print(n.get("k2").upper())
print(n.pop("k1"))
print(n)
print(n.setdefault("k3","????").upper())
print(n.setdefault("k4","???").upper())
print(n.setdefault("k5","nitin".upper()))
print(n)
print(n.update({"k6":"shivangi","k7":"keval","k8":"jangiya"}))
print(n)
print(len(n))



"uniques names"

c={"c1":"red",
   "c2":"blue",
   "c3":"purple",
   "c4":"green",
   "c5":"yellow",
   }
print(c["c5"])
print(c["c3"].isalpha())
print(c.keys())
print(c.values())
print(list(c.items()))


a={(0,8):"pratham",
   (1,2):"aayush",
   (3,4):"rabada",
   (4,5):"nokia",
   (3,6):"samsung",
   }
print(a.get((3,4)).upper())
print(a.keys())
print(a.values())


tower={
   'op':{"name":"pratham","age":34,"height": 183},
   'kp':{"name1":"parth","age":23,"height":150},
   'rp':{"name2":"shaurya","age":20,"height":140},
   'ty':{"name3":"rishi","age":19,"height":156}
}
print(tower['op']["age"])
print(tower['rp']['name2'])
tower['kp']['name1']='rushit'
print(tower['kp']['name1'])
del tower['op']
print(tower)





a=34
b=67
c=89
d=10

print(a==b and b<c and c>d and d<a)
print(a==b or b<c or c>d or d<a)
print(a==b)
print(b!=a)
print(c<d and d>c)
print(d<c and d<c)
print(c>b or a<c)
print(a|b,c&d,b^a)
print(oct(a))
print(hex(b))
print(chr(c))


e={'py':{"creator":"facebook"},
   "ty":{"creat1":"instagram"},
   "uy":{"creat2":"snapchat"},
   }
print(e['ty'].keys())
print(e['ty'].values())


q={"ip":"pratham","uo":"om","lo":"ui","ux":"indigo","er":"qwerty","rt":"iop"}
print(q.pop("ip"))
print(q.items())
print(q["lo"].upper(),78)


games={"cod":"codmw1",
       "cod1":"codmw2",
       "cod2":"codmw3",
       "cod3":"codbo",
       "cod4":"codbo2",
       }
print(games["cod2"].upper())
print(list(games["cod4"]))
print(list(games))
print(list(games.values()))
print(list(games.get("cod2")))
games["cod2"]="codbo3"
print(list(games["cod2"]))
del games["cod4"]
print(list(games.items()))


accessories={"pc":"personal",
             "computer":"wire",
             "screen":"black",
             "pairs":["keboard","mouse"],
 }
print(accessories["pairs"])
print(list(accessories["pairs"]))
print(list(accessories["pc"].upper()))




# a=45
# b=30

# a = b

# print("the value of a is ",b)


s=56
d=23

temp=s
print("the value of temp variable is",temp)

s=d
print("the value of s is ",s)

d=temp
print("the value of d is",d)

q=45
e=67

q,e=e,q
print("the value of q is",q)
print("the value of e is",e)


"PROM DANCE DICT"

prom={"pair":"karan",
      "p1":"swati",
      "p2":"manan",
      "p3":["yug","yogini"]}

print(list(prom["p2"]))
print(list(prom.items()))
print(list(prom["pair"].upper()))
print(prom.keys())
print(prom.values())
print(prom.items())
# print(prom["p3"].count("y"[2]))
# print(prom["p3"].index("i",2))

print(list(prom["p3"][1].upper()))
print(prom['p3'][1].index('i',4))
print(prom.get("pair"))


u=[40,60,80,8,84,830,32,3892]
i=[9,4932,82,383,87902]
u,i=i,u
print("the value of u is",u)
print("the value of i is",i)


"TUPLES"

tup=("apple",234,45+7j)
uio=(45,90)

tup3=tup+uio
print(tup3)
print(tup3.__len__())
print(type(tup))
print(tup3.index(234))
print(tup3)

t=({"name":"pratham","age":23,"height":123
    },[2,5,8,1,90,45,78,90,38,74,2719])
t1=(34+8j,90,70+8)
t2=t+t1
print(t2)
print(t2[0])
print(t2[1].index(90))
print(t2[1],t2[3])
print(t2[0],t2[1],t2[2],t2[3],t2[4])
print(list(str(t2[2])))
print(type(t2[2]))



# x=int(input("enter the value: "))
# print(x*"5")

u=[1,8,9,5,3,58,30,5873,3853,4858]
print(u[2::])
print(u[1::2])
print(u[::-4])
print(u[:2:-2])
print(u[2:7])
print(u[::-3])
print(u[2:-3])
#print(u[1::-3])


a=56
b=90                     
a,b=b,a
print("the value of a is",a)
print("the value of b is",b)

u=(20,50,90,45,78,88,93,820)
print(max(u))
print(min(u))
print(sorted(u))
print(bin(u[1]))
print(chr(u[4]))
print(chr(u[-1]))
print(chr(u[7]))
print(u[2]+20)
print(u[3]/5)
print(u[0]**2)
print(u[1]-u[-2])
print(u[2]//9)
print(u[2]/1.5)
print(list(u))
print(list(str(u)))



e="string","sring1","string2"
print(list(str(e[1])))
print(type(e))


s="horseharsh"

print(s.count("h"))
print(list(str(s[0]).upper()))
print(max(s[0]))
print(s.index("r",4))
print(s[0:3].upper(),s[3:6].count("e"))
print(type(s))
print(s.count("e"))
print(ord(s[2]))

p="pratham"
print(f"{p} is a good boy.")

s="{1} is a bad {0}.".format("om","boy")
print(s)


d="stringstringstrig"
print(d.index("r",3))

print(ord("r".upper()))
print(chr(82))

r=(2,4)
print(sum(r,10))


f=(20.90,30.56)
print(sum(f,100))



r=["neeta","pratham","om","birla","tata","adani","ambani"]
print(r[1].count("a"))
print(r[1].index("a",3))
print(len(r))
print(r[0][0:3],[1][3:6],[2][0],[3][0:3],[4][0:3],[5][0:2],[6][3:6])
print(r[0][0:3],r[1][3:6].upper(),r[2][0],r[3][0:3].upper(),r[4][0:3],r[5][0:2].upper(),r[6][3:6])
print(type(r))

p=(90,45,45,889,12,56,80,90,90,90)
print(sum(p))
print(sum(p,2))
print(p[0])
print(p[3:])
print(sum(p[0:4],1))
print(sum(p[1:3]))
print(type(p))

# y=1.,5.,6.,7.,90.,
# print(type(y))
# print(y)
# q=(1,)
# e=1.,
# print(q)
# print(e)


j=(3,3.,20.,10000,3.4)
print(j[1:])
print(type(j))
print(j*2)


my_tuple = (50, 60, 100)
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3
print(len(my_tuple))
print(len(t2))
print(t1)


w=(10,20,50,70,100)
r=w+(120,150)
t=w*2
print(len(t))
print(t[0:3]*5)
print(len(t[0:3]*5))
print(120 in r)
print(150 not in r)
print(r)
print(w[0:2])
print(w[0:2]*9)
print(t[1:3*4]) #problem t[1:3*4]
# print(sum(w[0:3])) #problem w[0:3+2]
print(sum(w[0:3],5))





var=456
t1=(1,)
t2=(2,)
t3=(3,var)
t1,t2,t3=t2,t3,t1
print(t1,t2,t3)


d=(20,30,100)
print(sum(d))
print(sum(d,10))
print(d[1]*30)
print(d[1:3]*2)




# sd=["string","pratham","om","kapoor"]
# print(sd*10)
# print(sd[1:3]*5)

# de="string","string1","string2"
# print(de*3)
# print(de[1:3]*5)



t=("apple","pineapple","oranges")
r=(12,67,89,23.45)
e=t*2
print(e)
print(type(t))

w=(12,45,56,78)
p=("pratham","om","adani")
print(w+p)
print(w*2)
print(type(p))


q={"pratham":34,"om":12,"prapti":30,"mann":45}
print(q.items())
print(q.clear())




"SETS"
d={10,45,90,890}
print(type(d))
d.add(89)
d.add(1)
print(d)
d.pop()
print(d)
d.pop()
print(d)
d.remove(90)
print(d)
# d.clear()
# print(d)
d.discard(45)
print(d)
d.update({45,667,780,1000,46})
print(d)
print(d.clear())

w={89,56,34,23,14}
print(sorted(w))
print(min(w))
print(max(w))
print(sum(w,20))
print(type(w))

# a=int(input("enter the values:"))
# b=int(input("enter the values: "))
# print(a+b)
# print(a*b)
# print(a/b)
# print(a-b)





"TUPLE"
a=("orages","apple","pratham")
print(a[2][0:4].upper()*3)

g=(23,45,67,89)
h=(20,40,60,80)
d=("pratham","om","family members")
print(g+h+d)
print(sorted(g),(h),(d))
print(g+h)
print(sum(g,6))
print(sum(g*2))
print(g*2)
print(bool(20 in g))
print(40 in g)
print(list(str(d).upper()))
print(str(d[2]).find("m",8))
print(h+d)



o=(90,89,45,2728,1,2,4,3,0,7,56,1,6,)
i=o+(100,45)
print(sum(o*2))
print(o*2)
print(o.count(1))
print(bin(sum(o)))
print(chr(sum(o*5)))
print(chr(sum(o)))
print(o.index(1,5))
print(i)

u=(23,45,78,1000)
o=u+(89,67)
print(o)
print(sum(o))
print(u*2)
print(sum(u)*2)
print(u[0:2])
print(sum(u[0:2]))
print(sum(u[0:2],2))
print(type(u))


"sets"
t={12,34,56,78}
print(type(t))
print(t.pop())
# print(t.discard(0))
print(t.remove(12))
print(t)
print(t.add(100))
print(t)

"dictionary"

pro1={"gr1":"pratham""om",
"gr2":"om"  "nand",
      "gr3":"bhavya" "meet",
      "gr4":"kelvin"  "chand",
      "gr5":"dharmik" "dharmik",}

print(pro1.keys())
print(pro1.values())
print(pro1.get("gr2"))
print(list(str(pro1.get("gr3").upper().count("e"))))
print(bool("kelvin" in "gr3"))
print("gr5".count("dharmik"))


"LIST"
a=[34,12,34,56,789,0,80,90,1,3,5,6,9,2,4,9,10]
print(sorted(a))
print(a[-4])
print(a[-4:-1])
print(sum(a[-4:-1]))
print(a.count(9))
print(a.pop(1))
print(a[-2:])
print(a[4:])
print(a[2::-2])
print(a[2::4])
print(sum(a[2::4],4))

"CONDITIONAL STATEMEnet"
q=56
if q<=78:
    print("pass")
else:
    print("fail")



e=90
if e<200:
    print("access")
else:
    print("not access")

g=89
if g<90:
    print("fail")
else:
    print("pass")

if  89<90:
    print("yes")
else:
    print("no")
if  200<100:
    print("no")
else:
    print("access")

if  65==a:
    print("yes")
else:
    print("no")
if  "5" in "65":
    print("true")
else:
    print("false")
    if  "78" is "string":
        print("allowed")
    else:
        print("not allowed")
if  45<89:
    print("u")
else:
    print("k")



u=[90,89,2,5,7,8,90,1,2,0]
if  90 in u:
    print("y".upper())
else:
    print("n".upper())
if  56 in u:
    print("a".upper())
else:
    print("n a".upper())



"DICTIONARY + IF ELSE"

q={"name1":"om",
   "name2":"pratham",
   "name3":"akash",
   "name4":"boy",
   }
if  "boy" in "name4":
    print("acc".upper())
else:
    print("denied".upper())

if  "yash"in q:
    print("include")
else:
    print("not include")

if  "pratham" in "name2":
    print("involve")
else:
    print("not involve")

    if  "pratham" in q:
        print("access".upper())
    else:
        print("not access".upper())
        if  "pratham" in "name2":
            print("approve".upper())
        else:
            print("not approve".upper())

if  23<89 and 34<56:
    print("approved".upper())
else:
    print("denied".upper())

if  34<89 or 90>89:
    print("accessed".upper())
else:
    print("not access".upper())



if "l" in "london":
    print("true".upper())
else:
    print("false".upper())

if  "c"=="C":
    print("true")
else:
    print("false")


# u=["apple","pineapple","basket","shooppes","dmart","more smart store","croma"]
# if 0=="apple" not in u:
#     print("yes".upper())
# else:
#     print("no")


# u=["apple","pratham","rohan","vishal","rinku"]
# print(u[0][0:3])
# if [1][0:3] is "pra" in u:
#     print("true".upper())
# else:
#     print("false".upper())


if  3**2 is 9:
    print("yes".upper())
else:
    print("no".upper())


if  89<90 and 23<90:
    print("y".upper())
else:
    print("n".upper())
if  20000<500000 or 89<67:
    print("accepted")
else:
    print("not accepted")

if 89<200:
    print("access".upper())
else:
    print("not".upper())


w=34
if  w<40:
    print("a".upper())
elif w<50:
    print("b".upper())
elif w>56:
    print("c".upper())
else:
    print("d".upper())

e=90
if  e>100:
    print("yes")
elif e>300:
    print("yes1")
elif e<200:
    print("yes2")
else:
    print("no1")

r=200
if  r<100:
    print("acc")
elif r>899:
    print("ess")
elif r<300:
    print("valid".upper())
elif r>500:
    print("not valid")
else:
    print("not accessed")

print("the word is ",end=" ")
print("{best}.".upper())
print("the","world","is","best",sep="/")

v=("america is best")
print(list(str(v)))
print(type(v))



y=(2,5,7,2,89,90,134,87,7848,7499,2,4,90,13,89,234,578449)
a=y+(10,20)
q=a+y
print(sorted(q))
print(q.count(2))
print(y)
print(a)
print(sum(y[0:4]))





s={78,89,78,67,1,23,4,5,6,7,0,20}
print(type(s))
d={23,2,1,3,5,690,89,78,56,2723923,784,5758394}
print(type(d))

print("the {} is best".format("world"))


s={.2,0.,3.5,1.}
print(sorted(s))


# d={"gem": "pratham",
# "gem2":"om",
#    "gem3":"sparsh",
#    "gem4":"youtube"
#    }
# if  "pratham" in o:
#     print("true".upper())
# elif "pratham" in f:
#     print("access".upper())
# elif "pratham" in q:
#     print("not access".upper())
# elif "pratham" in d:
#     print("valid".title())
# else:
#     print("false".upper())


# marks=int(input("values of student(0 to 100)\n"))
#
# if marks>=90:
#     grade="outstanding"
# elif marks>=80:
#     grade="excellent"
# elif marks>=70:
#     grades="very good"
# else:
#     grade="fail"
#     print("your grade is:"+ grade)

# marks1=int(input("marks of student: "))
# if marks1>90:
#     print("outstanding")
# elif marks1<80:
#     print("excellent")
# elif marks1<70:
#     print("very good")
# elif marks1<60:
#     print("good")
# else:
#     print("fail")
#
# t=-8
# if  t==5:
#     print("true")
# elif t<=6:
#     print("yes")
# elif t>0:
#     print("access")
# else:
#     print("none")



u={"name":"pratham",
    "roll no": "23",
    "subject":"python",
    "profession":"student"
    }

u["name"]="parth"
u["roll no"]="67"
u["subject"]="java"
print(u)
print(u.keys())
print(u.values())
print(list(u.get("name")))
print(list(u.items()))


if "java"in d:
    print("yes")
# elif "java" in u:
    print("access")
else:
    print("no")

print("hi my name is \"pratham\"")
print('my\'name is robot.')

u=(90,89.90,45,89,"pratham")
print(type(u))
print(str(u))
print(set(u))
print(list(u))


# if "90 is greater than 9":
#     print("true")
# else:
#     print("false")
#
# if  "youtube has more videos rather than google":
#     print("yes")
# else:
#     print("no")
#
# if "mark zuckerberg is ceo of google":
#     print("valid")
# else:
#     print("invalid")
#
# if "sundar pichai is born in america?":
#     print("yes".upper())
# else:
#     print("no".title())

if "90<9":
    print("access")
else:
    print("not access")

if 90<9:
    print("true".upper())
else:
    print("false".upper())

s={34,67,89,9.89,67,245,789,76384934,90,234,678,452731,415621}
print(type(s))
print(s.pop())
print(sorted(s))
print(s.discard(789))
print(s)
print(s.remove(90))
print(s)


if -4 is  "positve number":
    print("true".upper())
else:
    print("false")

# q=int(input("value: "))
# if q%2==0:
#     print(q,"even number")
# else:
#     print(q,"odd number")

# m=7000
# cr=8
# c=m*cr/100
# print(c)
#
# pvaf=9.567
# pvif=0.589
#
# pvb=[c*pvaf]+[m*pvif]


if 60<30:
    print("false")
else:
    print("true")


if 20<89:
    print("true")
else:
    print("false")

if  30>89:
    print("false")
else:
    print("true")

if  50<100:
    print("true")
else:
    print("false")


if  67<20:
    print("true")
else:
    print("false".upper())


 
y=[90,56,45,24,22,89,80,8,89,23,55,78]
print(max(y))
print(min(y))
# print(float(y))
print(str(y))
print(sum(y))
y.append(659)
print(y)
print(y.count(2))



my_list=[(1,2,3),(4,5,6),(7,8,9)]
for item in my_list:
    print(item)
for a,b,c in my_list:
    print(c)



if 56+90:
    print("true")
else:
    print("false")

if 89==90:
    print("true")
else:
    print("false")

t={"country":"china","c1":"america","c2":"cuba","c3":"india"}
print(t.keys())
print(t.values())
print(t.items())
t["c4"]="russia"
print(t)
t["c1"]="canada"
print(t)
print(t.get("country").upper())
print(len(t))

a=7
b=4
print(a/b)
print(a//b)


r={"a":(1,2),"b":(3,4),"c":(5,6)}
print(r.keys())
r["d"]=(7,8)
print(r)
print(r.items())
r["e"]="standard"
print(r)
print(len(r.values()))


d="duck"
print(d.isalpha())
print(d.isalnum())
print(d.isdigit())
l={"u","standard","double pump"}
print(l)
print(type(l))

a=3
b=4
print(b+a)
print(a+56)
print(b/2)
print(b//2)

aa=20
bb=10
print(aa%bb)
cc=66
dd=3
print(cc%dd)
q=20
e=45
print(q%e)
r=89
w=45
print(r%w)

pra=3+5-7/8*3
print(pra**2)
ert=(50+100)*(10+20)
print(ert)

a=2
b=4
c=6
d=8
print(a+b-c+d)
print(b-c+d/a)
print(c+a/b-d)
print(d+b/c-a)
print(b-c+d/a*2)
print(0.1+0.2-0.3==0.0)



pra=90
print(pra)
print(pra+pra)
print(pra-12)
print(pra/10)
pra=pra+pra-34.90
print(type(pra))

length=30
breadth=20
square_meter=length*breadth/20
print(square_meter)
print(type(square_meter))

cube=20**2
print(cube)

print(12**2)
print(12*2)


d=(23,56,7,8,23,24,13,56,"pratham","om","parth")
print(type(d))

print("the","Taj Mahal","is","located","in",sep="/",end=" ")
print("india.".title())
print("zero","is","more","than",sep="****",end="////")
print("one")

a=["pratham",23]
b=["om",24]
print(a[1]+b[1])
print(a[1],b[1])
print(a[1]*b[1])
print(a[1]/b[1])
print(a[1]-b[1])
print(a[1]*2,b[1]*2)
# print(a[0[0:3]])
print("america","is","a","bad",sep="8",end=" ")
print("country".title())
print("russia","is","fight","with","usa",sep="</>")
print("iron man fights with \n hulk".upper())
print("pratham is ranker in class\nbut,om is smart boy.")
print("a man buys shares at rupees 3456\nbut he sold shares at 4590 rupees")
print("in world 204 countries\nhowever russia and usa still fighting.".upper())
print("in","my","body","there","are","204","bones",sep="\n".upper())
print("there are 204 fighters\nbut there 10 actors in movie.")
u="pratham"
print(f"{u}" "is" "a" "good")


i="67"
y="89"
print(i+y)
# p=int(i+y)


print(23<=90)
print(23>=9)
print(23==34)

p="pratham"
print(bool("p" in "pratham"))
print("r"in "pratham")
# print(m in pratham)
# print(r in pratham)

a=90
b=20
c=45
d=89
print(a>=b and b<=a)
print(a<=c or d>=a)
print(a<=c and d>=a)



a=6
a=a+a
print(a)
print(float(a))
print(str(a))


item_a=300
item_b=400
item_c=500
tax_rate=8

item_d=item_a+item_b+item_c
print(item_d)
item_e=item_d*tax_rate
print(item_e)

fruits="pineapple"
print(fruits[::4])
print(fruits[::2])
print(fruits[0:4])
print(fruits[-4:-1])
print(fruits[-4:0])
print(fruits[::-1])
print(fruits[2:8:2].upper())
print(fruits[::-3].upper())
print(fruits[::2].upper())
print(fruits[::3].title())
print(fruits[2:6:2])
print(fruits[3:8:1])
print(fruits[2:8:2].upper())
print(fruits[1:8:2]) #iepl




c="chandigarh"
print(c[0:5].upper())
print(c[4::])
print(c[3:9:2]) #nia
print(c[::-4])
print(c[:-4].upper())
print(c[-4:].upper())
print(c[5:])
print(c[::-2])


d=" dubai usa"
print(d.split())
print(list(d))

m="my name is pratham"
print(m.split())



u="united states of america"  # 22 # araoetdi
print(u[::3].upper())
print(u[4::].upper())
print(u[2:15:3])
print(u[3:22:2].upper())
print(u[2:24:4])  #i tomc
print(u[5:25:5]) #dtfr
print(u[-2:].upper())
print(u[-4:].upper())
print(u[-5:].upper())
print(u[:-2].upper())
print(u[:-4])
print(u[:-10])
print(u[4::])
print(u[::5])
print(u[::3]) #utasfmi
print(u[::-2])
print(u[::-3])



c="republic of china"
print(c[-3:-1].upper())
print(c[-5:-2])
print(c[::-3].upper())



print(45%7)
print(45%5)
print(100%20)
print("45+ioc")
print(45,"unganda")
print(34<90 and 89<100) # true
print(34>78 or 90<67) # true
print(50<89 or 78<100) # false
print(34<90 or 89>100) # true
print(89<100 and 45>89) #false
print(20>190 or 45<89) # true

print(78/90+34-90/6**2/16)

e="europe"
print(e[0:4].upper()*5)
print(e[-4:].upper()*5)
print(e[-3:].upper()*4)
print(e[-2:].upper()*3)
print(e[-2:].upper()*2)
print(e[-1:].upper()*1)

print(";;;;;;;;;;")
print(";;;;;;;;")
print(";;;;;;")
print(";;;;")
print(";;")
print(";")
print(";;")
print(";;;;")
print(";;;;;;")
print(';;;;;;;;')
print(";;;;;;;;;;")



print(";"*2)
print(";"*4)
print(";"*6)
print(";"*8)
print(";"*10)

i=[0,8,3,4,1,0,18,78,78,10,19,97,784,6784,562]
print(max(i))
print(sum(i))
print(min(i))
print(i.count(0))
# for items in i:
#      print(sorted(i))
#      for x in i:
#          print(i)

r={"o":"",
   "p":"",
   "e":"","r":"","a":""}
print(r)
# for x in r:
#     print(r)
#     for items in r:
#         print(r)


# print(12*2)
# print(13*2)
# print(14*2)
# print(15*2)
# print(16*2)
# print(17*2)
# print(18*2)
# print(19*2)
# print(20*2)

q=(12*2,13*2,14*2,15*2,16*2,17*2,18*2,19*2,20*2)
print(q)
# for x in q:print(q)
for canada in q:print(q)

if 42 in q:
    print("yes".upper())
else:
    print("no".upper())

if 24<32 in q:
    print("access")
else:
    print("not access")


print("{},{},{}, are the even numbers.".format("2","4","6"))



a=90
b=89
c=a+b+1
print(c)
print("the outcome of the sum is {}".format(c))

u= "%susa"
print(u"%s""is a bad country.")



p="pratham patel"
print(p[0:4])
print(p[::-3])
print(p[3::])
print(p[4:13:2]) #hmptl
print(p[3:])

e="europian union"
print(e[0:5].upper())
print(e[::-4].upper())
print(e[5:].upper())
print(e[-4:-1].upper())
print(e[0:4].upper()*10)
print(e[-4:])
print(e[:-4])
print(e[::-2])



print("sidhu {} and his {} are {}".format("mossewala","songs","nice"))
print("{3} roshan {0} are good for {1} movies and {2} movies.".format("hritik".upper(),"looks","action".title(),"romantic".title()))
print("pushpa {} will {} in {} ".format("2","release".title(),"december".title()))



print("/"*1)
print("/"*2)
print('/'*4)
print('/'*6)
print('/'*8)
print('/'*10)
print('/'*12)
print('/'*10)
print('/'*8)
print('/'*6)
print('/'*4)
print('/'*2)
print('/'*1)



print("|"*20)
print("|"*18)
print("|"*16)
print('|'*14)
print("|"*12)
print("|"*10)
print("|"*8)
print('|'*6)
print('|'*4)
print("|"*2)
print('|'*1)



print("||||||||||||||||||||||||")
print("  |||||||||||||||||||  ")
print("     |||||||||||||   ")
print("       |||||||||  ")
print("         ||||")
print("          |||   ")
print("          ||      ")
print("           |   ")






m="mission impossible ghost protocol"
print(m[0:4])
print(m[4:35:3])
print(m[-3:])
print(m[::-2])
print(m[:-3])
print(m.index("s"))
print(m.find("s",8))
print(m.split())




list_num=[0,3,45,6,7,2,0,89,84,56584,78,345,6724]
list_num[0:4]=34,66,12,12
print(list_num)
print(list_num.count(12))
print(sum(list_num[2:4]))

# problems in strings and sets update.


u={"battery":"v_gaurd",
   "b1":"exide","b2":"amara","b3":"tesla",
   "b4":"lithium","b5":"motorola"}
u["b4"]="radbrad"
print(u)
print(u.items())


k="united kingdom"
print(k[0:4].upper())
print(k[:-4].upper())
print(k[::-2].upper())
print(k[-3:].upper())
print(k[4:-3].upper())
print(k[2:-4].upper())


n="new zealand"
print(n[0:3])
print(n[1:-3])
print(n[::-1])
print(n[:-2])
print(n[2::])



print(90+89-34/2**23/56)
print(90*(5+1.0))


list=[2,3,4,5,6,"pratham","om"]
print(len(list))
print(list[5])
list[0]=1
print(list)
list.append("parth")
print(list)
print(list.pop(1))



# q=[89[56,89]]
# print(q.index(89,1))



"CONTROL FLOW"

if True:
    print("its false")
else:print("its true")

hungry=False
if hungry:
    print("please feed me")
else:print("don't")


my_name="pratham"
if my_name=="om":
    print("correct".upper())
elif my_name=="pratham":
    print("true".upper())
else:print("not correct")


n=89
if n==90:
    print("it's correct!")
elif n==23:
    print("it is also true")
elif n==89:
    print("access".upper())
else:print("false".upper())




# w="water"
# if om_drinks_coco_cola:
#     print("access")
# elif om_drinks_w :print("true".upper())
# else:print("he does not drink")





# q=45
# if q % 2==0:
#     print("q is even number")
# else:print("q is odd number")



b=90
if b>180:
    print("b is greather than 180.")
elif b==90:
    print("level is same")
else:
    print("level is not same.")

# kittens=int(input("how many cats are born: "))
# if kittens<10:
#     print("cats are nice")
# elif kittens==kittens:
#     print("average")
# else:
#     print("jolly mode.")


marks=int(input("marks: "))
if marks<50:
    print("fail")
elif marks==50:
    print("p")
elif marks<=70:
    print("c")
elif marks<=80:
    print("B")
elif marks<=95:
    print("very good")
elif marks<100:
    print("excellent".upper())
else:
    print("low grade")


v=int(input("number: "))
if v<=100:
    print("more less than")
elif v<=500:
    print("average less than")
elif v<=700:
    print("medium less than")
elif v>=1000:
    print(" high score")
else:print("no option")



a=int(input("number:"))
b=600
c=800


if a<c:
    print("very high")
elif a<=b:
    print("high")
else:print("none of the above")


# q=78
# if q==isalpha(): # problem("Doubt")
#     print("wrong")
# elif q==isnum():
#     print("right")
# elif q== isdigi:
#     print("more right")
# else:print("none of the above")




s=input("enter the word: ")
if s=="winter":
    print("then, i go for running.")
elif s=="rainy":
    print("then, i go for hot lunch.")
elif s=="spring":
    print("i go for exercise")
elif s=="summer":
    print("i go for vacation.")
else:print("nothing")


p=input("bird: ")

if p=="lion":
    print("she fights")
elif p=="sparrow":
    print("flies")
elif p=="parrot":
    print("fly")
elif p=="pigeon":
    print("she is flying")
else:
    print("other types of birds.")



# dict={(0,1):"pratham",(1,2):"om",(2,3):"parth",(3,4):"prathamesh",(4,5):"rushit"}
# print(dict.keys())
# print(dict.values())
# print(dict.items())

a={"key2":["x","y","z"]}
print(a)
print(a["key2"])
# print(a["key2"[2]])
print("key2"[2].upper())


y=[78,89,56,"pratham"]
t=(0,89,"uiop")
m="mission impossible"
print(y.index(56))
print(t.index(89))
print(m.index("s"))
print(89+90-87*7/78//2)

a=90
print(a+(a-45))


a=10
b=-10
c=0
if a>0 or b>0:
    print("either of the number is greater than 0")
else:
    print("no number is greater than 0")
if b>0 or c>0:
    print("either of the number is greater than 0")
else:
    print("no number is greater than 0")


abc=90
edf= 45
if abc>100 and edf<90:
    print("no value is saving")
else:
    print("it saves")
if edf>90 or abc<100:
    print("it  is right")
else:
    print("it is wrong")


age=int(input("age: "))
if age<10:
    print("child")
elif age<15:
    print("school child")
elif age< 20:
    print("teenager")
elif age>=18 and age<65:
    print("you are adult.")
else:
    print("you are a nothing.")

q=5
w=10
q+=w
print(w)








if 5==6:
    print("1")
elif 5>=9:
    print("more")
elif 5<=8:
    print("less")
elif 5<=6:
    print("same")
else:print("nothing")







































# i=[3,3.,20.,10000,3.4]
# print(i[-3:-1]) # problem -3::-1




# g="gate smashers"
# print(g[-1::-13])

# o="pratham"    
# print(o.split(maxsplit=3))
        