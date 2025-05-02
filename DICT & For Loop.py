fdi={'fbi':[3,4,{"police":["chor",{"911":[4,5,["cid"]]}]}]}
print(fdi["fbi"][2]["police"][0])
print(fdi["fbi"][0])
# fdi["fbi"][2]["police"][1][2]="911"
# print(fdi)
print(fdi["fbi"][2]["police"][1]["911"][0])
print(fdi["fbi"][2]["police"][1]["911"][1])
print(fdi["fbi"][0])
print(fdi["fbi"][1])
print(fdi["fbi"][2]["police"][1])
print(fdi["fbi"][0])
print(fdi["fbi"][1])
print(fdi["fbi"][2]["police"])
print(fdi["fbi"][2]["police"][0])
print(fdi["fbi"][2]["police"][1])
print(fdi["fbi"][2]["police"][1]["911"][2])


spd={'power':[{'rangers':['spiderman',['thor'],{"cid":["swiss",["police"]]}]}]}
print(spd["power"])
print(spd["power"][0])
print(spd["power"][0]["rangers"])
print(spd["power"][0]["rangers"][0])
print(spd["power"][0]["rangers"][1])
print(spd["power"][0]["rangers"][2])
print(spd["power"][0]["rangers"][2]["cid"])
print(spd["power"][0]["rangers"][2]["cid"][0].upper())
print(spd["power"][0]["rangers"][2]["cid"][1][0].upper())

kl={'name': [1, 2, {'aayush': ['surname', {'patel': [23,['profession',"data engineer",{"gender":["male"]}]]}]}]}
print(kl["name"])
print(kl["name"][0])
print(kl["name"][2]["aayush"])
print(kl["name"][2]["aayush"][0])
print(kl["name"][2]["aayush"][1])
print(kl["name"][2]["aayush"][1]["patel"][0])
print(kl["name"][2]["aayush"][1]["patel"][1])
print(kl["name"][2]["aayush"][1]["patel"][1][0])
print(kl["name"][2]["aayush"][1]["patel"][1][1])
print(kl["name"][2]["aayush"][1]["patel"][1][2]["gender"][0])


klr={'name': [1, 2, {'pratham': ['surname', {'patel': [44,['job role',"pc engineer",{"gender":["male",{"family man":["srikant"]}]}]]}]}]}
print(klr["name"])
print(klr["name"][0])
print(klr["name"][2]["pratham"][1]["patel"][1][2]["gender"][1]["family man"][0].upper()) #SRIKANT
print(klr["name"][2]["pratham"][1]["patel"][1][1].upper())
print(klr["name"][2]["pratham"][1]["patel"][1][2])
print(klr["name"][2]["pratham"][1]["patel"][1][2]["gender"][1])
print(klr["name"][2]["pratham"][1]["patel"][1][2]["gender"][0])
print(klr["name"][2]["pratham"][1]["patel"][1][2]["gender"][1].keys())
print(klr["name"][2].values())
print(klr["name"][2]["pratham"][1].values())
print(klr["name"][2]["pratham"][1]["patel"][1][2]["gender"][1].values())
print(klr["name"][2]["pratham"][1]["patel"][1][0].upper())
print(klr["name"][2]["pratham"][1]["patel"][0])
print(klr["name"][2]['pratham'][1]["patel"][1][1])
print(klr["name"][2]["pratham"][1]["patel"][1][2]["gender"])

hb={'cut':[{'asian':["korean",['chinese'],{"asia":["indian",[{"army cut":"medium"}]]}]}]}
print(hb["cut"])
print(hb["cut"][0]["asian"])
print(hb["cut"][0]["asian"][2]["asia"])
print(hb["cut"][0]["asian"][2]["asia"][0])
print(hb["cut"][0]["asian"][2]["asia"][1])
print(hb["cut"][0]["asian"][2]["asia"][1][0])
print(hb["cut"][0]["asian"][2]["asia"][1][0]["army cut"].upper())

hd={'name':[1, 2, {'food': ['apple', {'quantity': [4,['country',"continent",{"asia":["india",{"russia":["putin",{"dubai":"camel"}]}]}]]}]}]}
print(hd)
print(hd["name"][2]["food"])
print(hd["name"][2]["food"][1])
print(hd["name"][2]["food"][1]["quantity"])
print(hd["name"][2]["food"][1]["quantity"][0])
print(hd["name"][2]["food"][1]["quantity"][1][0])
print(hd["name"][2]["food"][1]["quantity"][1][1])
print(hd["name"][2]["food"][1]["quantity"][1][2])
print(hd["name"][2]["food"][1]["quantity"][1][2]["asia"])
print(hd["name"][2]['food'][1]["quantity"][1][2]["asia"][0])
print(hd["name"][2]["food"][1]["quantity"][1][2]["asia"][1])
print(hd["name"][2]["food"][1]["quantity"][1][2]['asia'][1]["russia"])
print(hd["name"][2]["food"][1]["quantity"][1][2]['asia'][1]["russia"][0].upper())
print(hd["name"][2]["food"][1]["quantity"][1][2]['asia'][1])
print(hd["name"][2]["food"][1]["quantity"][1][2]['asia'][1]["russia"][1])
print(hd["name"][2]["food"][1]["quantity"][1][2]["asia"][1]["russia"][1]["dubai"].upper())


d={"key1":"apple","key2":"pineapple","calendar":{"janurary":1,"feburary":2,"march":3},"year":[2020,2021,2022]}
print(d["year"][1])
print(d["calendar"]["janurary"])
d["calendar"]["march"]=4
print(d["calendar"])

dic={"2020":{"vedang":31,"om":29,"mar":31},"2021":{"april":30,"may":31},"2022":"june","2023":"july"} # never make a pair str and int in list include dict.
print(dic["2020"]["om"])
print(dic["2021"]["april"])
d["2022"]="december"
print(d["2022"])
print(d)



dt = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(dt["k1"])
print(dt["k1"][0])
print(dt["k1"][0])
print(dt["k1"][1])
print(dt["k1"][0])

print(dt['k1'][0])
print(dt['k1'][0]["nest_key"][0])
print(dt['k1'][0]["nest_key"][1])
print(dt["k1"][0]["nest_key"][1][0])


dc = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(dc["k1"][2])
print(dc["k1"][2]["k2"][1])
print(dc["k1"][2]["k2"][1]["tough"][2])
print(dc["k1"][2]['k2'][1]["tough"][2][0])
print(dc["k1"][2]["k2"][1]["tough"][2][0])


fd={"op":[{"om":["taj mahal",["japan"]]}]}
print(fd["op"][0]["om"][1][0])
print(fd["op"][0]["om"][0])



list_2=[10,90,56,78,893,4576776,67,[89,34,244,22,[45,5,6,[6,[3,4],49],6,789],338824],4488239,85,56,32]
print(list_2[7][4][0])
print(list_2[7][4][1])
print(list_2[7][4][3][0])
print(list_2[7][4][3][1][1])
print(list_2[7][5])
print(list_2[7][4][4])
print(list_2[7][4][5])
print(list_2[7][4][3][2])




if 5<90 or 40>100:
    print("true")
else:print("false")

if 5<90 and 40>100:
    print("true".upper())
else:print("false".upper())




#########################################################################################################################################################

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

print(l_one[2][0] >= l_two[2]['k1'])

j=[34,89,["k2",90]]
f=[90,34,{56,87}]
print(j[2][1]>f[1])


a= 12

b = a-10

print(not(a>b))


# FOR LOOP
s="sun"
for x in s:
    print(s)

my_list=[2,4,3]
for item_name in my_list:
    print(item_name)


df={"t-shirt": 23,"pants":30,"trousers":21,"boxers":10}
for item_name in df.keys():
    print(item_name)
for item_name in df.values():
    print(item_name)
for x in df:
    print(df)

p="pratham"
for item_name in p:
    print(item_name)

r=["string","pratham","loop","rishi","ratang"]
for num in r:
    print(num)
for items in r:
    print(r)
for item_name in r:
    print(item_name)
for pratham in r:
    print(pratham)
for x in r: # print("any string")
    print("pratham")



num_list=19
if num_list%2==0:
    print(num_list,"even number")
else:print(num_list,"odd number")



a="america"
for x in a:
    print(a)
for jelly in a: #ubho alphabets of america:
    print(jelly)
for item_name in a:
    print(item_name)



y=[20,40,60,80]
for item_name in y:
    print("pratham")



yq=["pratham",9,"om","rushit",32]
for item_name in yq[0]:
    print(item_name)
for num in yq:
    print("aayush")


d={"name":"pratham","age":21,"subject":"python","weight":78,"height":180} # for loop in "dictionary"
for dictionary in d.keys():
    print(dictionary)

for x in d["name"]:
    print(d["name"])

for item_name in d['subject']:
    print(item_name.upper())

for num in d.values():
    print(num)

for shampoo in d["name"]:
    print(shampoo.title())


r="republic of china"
for letters in r:
    print(letters.title())


n="north korea" # for loop "string"
for x in n:
    print(n)
for kitchen in n:
    print(kitchen)
for items_name in n:
    print("china".upper())
for num in n:
    print(num.upper()*5)
for item_name in n:
    print(item_name)
for letters in n:
    print("om"*10)



q=[1,2,3,4,5,6,7,8,9,10] # for loop "list"
# for x in q:
#     print(q.count(46))
for num in q:
    print(num)
for calnedar in q:
    print("india")
for num in q:
    if(num%2)==0:
        print(num)
    else:print(f"odd number: {num}")

qw=[1,2,3,4,5,6,7,8,9,10]
k=2
for num in qw:
    w=k+num
print(w)


s={"apple":20,"clothes":400,"fridge":"modern","rent":"installment","shoes":"nike"} # for loop in "dictionary"
for oven in s.keys():
    print(oven.upper())
    for key in s.values():
        print(key)
    for lock in s.values():
        print(lock)
for x in s["shoes"]:
    print(s["shoes"].upper())

op= {'country':[{'indian':['cricketers',['dhoni'],{"virat":["kohli",["rohit"]]}]}]}
print(op["country"][0])
print(op["country"][0]["indian"])
print(op["country"][0]["indian"][0].upper())
print(op["country"][0]["indian"][1])
print(op["country"][0]["indian"][2])
print(op["country"][0]["indian"][2]["virat"])
print(op["country"][0]["indian"][2]["virat"][0].upper())
print(op['country'][0]["indian"][1][0].upper())


sa={'sports': [1, 2, {'cricket': ['football', {'bat': ["virat",[18,"kohli",{"rohit":["sharma"]}]]}]}]}
print(sa["sports"][1])
print(sa["sports"][2]["cricket"])
print(sa["sports"][2]["cricket"][0].upper())
print(sa["sports"][2]["cricket"][1]["bat"])
print(sa["sports"][2]["cricket"][1]["bat"][0].upper())
print(sa["sports"][2]["cricket"][1]["bat"][1][0])
print(sa["sports"][2].keys())
print(sa["sports"][2]["cricket"][1].keys())
print(sa["sports"][2]["cricket"][1]["bat"])


ds={'continent': [40,60,34,12,{'asia': [34,56, {'india': ["virat",["china",23,45,{"bhutan":["nepal",{"pakistan":"babar"}]}]]}]}]}
print(ds["continent"][4].keys())
print(ds["continent"][4]["asia"])
print(ds["continent"][4]["asia"][2]["india"][0])
print(ds["continent"][4]["asia"][2]["india"][1][3]["bhutan"])
print(ds["continent"][4]["asia"][2]["india"][1][3]["bhutan"][1].values())
print(ds["continent"][4]["asia"][2]["india"][1][1])

for x in ds["continent"][4].values():
    print(ds["continent"][4].values())



for x in range(20,40):
    print(x)

q=[90,67,45,23,12,100,250,450,500]
for coconut in sorted(q):
    print(coconut)
for mouse in reversed(q):
    print(mouse)
for x in q:
    print(q)
for x in (q)[2:6]:
    print(x)
for x in sorted(q)[2:6]: # python forgets slicing "[3,4,5]"
 print(x)
print(list(str(max(q))))
for x in q:
    print(list(str(sorted(q))))
    print(list(str(min(q))))


dic={"japan":["hiroshima",[1,3,{"china":["beijing",["korea",[23,46,12,{"usa":["texas",{"france":"paris"}]}]]]}]]}
print(dic["japan"][1][2]["china"][1][1][3]['usa'])
print(dic["japan"][1][2]["china"][1][0])
print(dic["japan"][1][2]["china"][1][1][3]["usa"][1])
print(dic["japan"][1][2]["china"][1][1][3]["usa"][1]["france"].upper())




r=(1,3,2,4,3,5,4,6,3478,89,675,56,45,33) #for loop in "tuple"
for x in r:
    print(sorted(r))
for x in r:
    print(sorted(set(r)))

for x in r:
       print(str(set(r)))


op=65|76
print(op)
print(90^56)

u="uganda"
print(not("u"in "uganda"))
print("u"!="uganda")

t=[1,2,3,4,5,6,7,8,9,10]
print(t[0:5])
print(t[-2:])
print(t[4::])
print(t[::-2])
print(t[:-2])
print(t[2:])
print(t[1:11:2])
print(list(str(t[0:3])))



q=[90,784,5,23,77,78,45,2828]
for x in q:
    print(q)
for letters in q:
    print(sorted(q))



a="united states of america"
for x in a:
    print(a)
for china in a:
    print(china)
for cuba in a:
    print("paris".upper())

e={"sports":"cricket","esports":"pubg","star":"virat kohli","player":"shroud","count":4} # for loop in "dictionary
for x in e:
    print(e)
for dhoni in e.keys():
    print(dhoni.upper())
for modi in e.values():
    print(modi)
for shah in e.items():
    print(shah)
for key,value in e.items():
    print(value)


# t=(90,89,77,5,6,34,23) # for loop in "tuple"
# print(type(t))
# for  in t:
#     print(a)
#     print(b)


ty=[(89,45),(34,22),(199,885),(67,45)]

for item in ty:
    print(item)
for (a,b) in ty:
    print(a**0.5)
for a,b in ty:
    print(a)



a={"contry":"china",'india':"delhi","pakistan":"karachi","usa":"texas"}
for key,value, in a.items():
    print(key)
for items in a.items():
    print(items)

numbers = [1, 2, 3]
for x in numbers:
  print(x**x)

# numbers1 = (1, 2, 3, 4, 5) #  advance for loop in tuple
# numbers2 = []
# for x in numbers1:
#   numbers2.append(x)
#   print(numbers2)





r=[90,34,23,12,5,6,45] # for loop in list
for x in r:
    print(sorted(r))
    for items in r:
        print(r)
    for y in r:
        print("player"[2].upper())
    for y in r:
        print(len(r)+3)
s="optimistic player" # counting character
for letters in s:
    print(letters.upper())
    for x in s:
        print(len(s)*2)
    for items_name in s:
        print(s)
        count=0
for character in s:
    print(f"{count}:{character.upper()}")
    count+=1


r="republic of gamers"
count=0
for character in r:
    print(f"{count}:{character}")
    count+=1




k=[2,3,5,7,4,8,90,34,56,77] # for loop use for find even and odd number.
for x in k:
    if (x%2==0):
     print(f"{x} odd.")
    else:print(f"{x} even.")




s=({23,45,23,12.89,87,65,90,9,34,12})
s.add(100)
print(s)
for x in s:
    print(sorted(s)[0:4])
s.add("animal")
s.add("ranbir")
s.add("singh")
for c in s:
    print(s)


u=int(input("value: "))
if u<=50:
    print("D")
elif u<=60:
    print("C")
elif u<=70:
    print("B")
elif u<85:
    print("A")
elif u<100:
    print("excellent".upper())
else:print("nothing")


list_1=[1,4,5,67,89,23] ##########################################   NEW METHOD ZIP METHOD     ##########################################
num_list=["a",'b','c','d','e','f']
for item in zip(list_1,num_list):
    print(item)
print(sorted(list_1))
for t in enumerate(list_1):
    print(t)
for t in enumerate(num_list):
    print(t)
for g in list_1:
    print(g*3)

r="republic of china is not bigger than russia."
for t in r.split():
    if len(t)%2==0:
        print(t)
for y in r.split():
    if y[0]=="r":
        print(y)
for w in enumerate(r):
    print(w)

e=[1,2,3,4,5,6,7,8,9,10]
s=["pratham","om","parth","mann","vishal","rushit","rudra",["shaurya"]]
for y in zip(e,s):
    print(y)
for i in e,s:
    print(i)
for w in enumerate(e):
    print(w*2)
for q in reversed(s[0].upper()):
    print(q*5)

n="narendra modi" ###############################################    FOR LOOP IN APPEND        #########################
m=[]
for word in n:
    m.append(word)
    print(m)
h="hello"
d=[]
for t in h:
    d.append(t)
    print(d)

c=[china for china in "narendra modi"]
print(c)


f=[(12,24),(23,56),(56,78),(89,90)] ###
for a,b in f:
    print(a)
print(set(f))
print(type(f))


q=(12,24),(34,44),(45,46),(78,90)
for a in q:
    if a==(34,44):
        continue
    print(a)
for y in q:
    if y==(45,46):
        break
    print(y[0])



b="buisness"
f=[]
for letter in b:
    f.append(letter)
    print(f)


# name="pratham"
# def name_of_function(name):
#  print(f"hello +name")











# def g(country="india"):
#     print("i am resident of "+country)
#
# g("usa")
# g("sweden")
# g("canada")
# g("japan")
# g("australia")

# def phones(iphone):
#     for t in iphone:
#         print(t)
# samsung=["iphone1","iphone2","iphone3","iphone4"]
# phones(samsung)
#
# def alpha(numbers):
#     for h in numbers:
#         print(h)
# words=[1,9,4,2,4,5,7,8]
# alpha(sorted(words))
#
# def g(alphabets):
#     for f in alphabets:
#         print(f)
# r=["a","b","c","d","e","f","g"]
# g(r)





# def t(fruits):
#     for u in fruits:
#         print(u)
#     fruits=["tomatoes","potato","onion","lady finger"]
# t(fruit)












u=[0,1,2,34,352,21]
g=[0,1,2,9,8,4]
for n in u:
    for t in g:
        print(t,end=" ")
    print()









# t=["id","name","age","born_year","height",'weight']
# d=[2309786,"pratham",23,2002,"180_cm","78kg"]
# for a in zip((t,d)):
#     print(a)
# s=dict(t,d)


# def d(n):
#     return 4%n
# print(d(40))
# print(d(36))
# print(d(16))
# print(d(20))
# print(d(12))


# def r (x):
#     return 5*x
# print(r(3))
# print(r(4))
# print(r(5))


# n=str(input("word: "))
# if n=="new york":
#     print("N")
# elif n=="uganda":
#     print("U")
# elif n=="paris":
#     print("P")
# elif n=="china":
#     print("C")
# elif n=="india":
#     print("I")
# else:print("no option")
#
#
#
# num=int(input("value:"))
# if num<=90:
#     print(num ,"less than 90")
# elif num<=200:
#     print(num,"less than 200")
# elif num<=500:
#     print(num,"less than 500")
# elif num>=600:
#     print(num,"more than 600")
# elif num>=800:
#      print(num,"more than 800")
# else:print("no")
#
#
# t=(1,2),(3,4),(5,6),(6,7)
# for a,b in t:
#     print(a)
#     print(t)


# y=[2,4,6,8,10]
# for x in y:
#     print(x**3) # 2x2x2, 4x4x4
# for x in y :
#     print(x**x) # (x**x) 4x4x4x4, 6x6x6x6x6x6


# r=[12,24,33,56,43,45,12,35,89,35]
# print(set(r))
# print(list(tuple(r)))














# g=[(12,24),(23,56),(12,89),(90,67)] # tuple
# for letters in g:
#     print(letters)
# for (a,b)in g:
#     print(a)
#     print(b)



# q=[23,4,56,4,5,2,4,5,3,24,236,3,4,235] # how to convert list into pair["TUPLE"].
# print(q)




# w=[2,4,6,7,15]
# k=1
# for num in w:
#     g=k+num
# print(g)




# for num in w:
#     print(w)
# for than_you in w:
#     print(than_you)










# nu=[23,89,78,89]
# list_sum=5
# for num in nu:
#     list_sum=list_sum+num
#     print(list_sum)
#
#
# v=[2,4,6,15,10]
# lis=8
# for num in v:
#     list=lis+num
# print(list)









# dic={"apple":40,"mango":500,"watermelon":50,"pineapple":100,"litchi":200}
# print(dic)
# if "cherry"in dic:
#     print("yes")
# elif 500 in dic:
#
#     print("yes")
# elif "green apple"in dic:
#     print("access")
# elif "pineapple"in dic:
#     print("valid".upper())
# else:
#     print("nothing")





# a=str(input("fruit: "))
# if a=='pineapple':
#     print("sour")
# elif a=="mango":
#     print("sweet")
# elif a=="apple":
#     print("normal taste")
# elif a=="cherry":
#     print("normal")
# else:
#     print("nothing")















# s=({2,3,5,2,3,5,2,5,3,5,2,3,3,5,2,6,8,7,8,7,6,7,6,8})
# print(type(s))
# print(set(s))
# print(s.discard(2))
# print(s.remove(3))
# print(s.add(10))
# print(s.update())
# print(s)







