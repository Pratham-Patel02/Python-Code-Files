artists = ["starboy", "selena", "dj snake", "marshmello"]
album = ["weekend", "wolves", "encore", "alone"]
co = 0
for i in zip(artists[0], album[0], artists[1], album[1]):
    print(f"{co}:{i}".upper())
    co += 1
print()

for u, d in enumerate(zip(artists[-2], artists[-1], album[-2], album[-1])):
    print(f"{d}:{u}")
    # print(list(u+d))
# for u,d,s in enumerate(zip(artists[-2],artists[-1])):
#     print(u+d+s)
# print(f"{d}:{u}")

for k, m in zip(artists[-2], artists[-1].upper().split()):
    print(k, m)

art = ["weekend", "wolves", "blin", "wings"]
bum = ["baby", "kale", "riddim", "drivers"]
cop = 0
for ikea in zip(art[0], bum[2], art[1], bum[-1]):
    print(f"{cop}:{ikea}".upper())
    cop += 1

op=["om","pratham","donald trump","king charles","kim jong","rishi sunak"]
for condition in op[2]:
    print(condition.title())

a=90
if a<100:
    print("yes")
else:print("no")



r={"hole":"snakes","battery":"lithium","bull":"bear","class":"room","red":"label"}
for k,v in r.items():
    print(k,v)


for n in list(range(0,51)):
    if (n%3==0):
        print(n)

for f in range(0,10):
    if (f%2==0):
        print(f,"is a even")


i=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for w in i[2:21:3]:
#     print(w)
for e in i[3:21:2]:
    print(e)
for q in i[3:21:2]:
    print(q*2)


a=[1,2,3,4,5,6,7,8,9,10] # TABLE OF MULTIPLICATION
for item in a:
    print("2*",item,'=',2*item)
for x in a:
    print("3*",x,"=",3*x)

d=[1,2,3,4,5,6,7,8,8,9,10]
for c in reversed(d):
    print(c)

a="ASUS TUF" # give every number with every alphabet.
count=0
for character in a:
    print(f"{character}:{count}")
    count+=1

c="china"  # single character of string in for loop.
for t in reversed(c):
    print(t*5)
i="india"
for y in i:
    print(y.upper()*5)

numbers = [1, 2, 3] ############################################# 2*2=4,3*3*3=27 #######################################
for x in numbers:
    print(x ** x)


p=[(12,23),(45,89),(90,78),(56,78)] # multiplication in tuple using for loop
for a,b in p:
    print(a,b)
for item in p:
    print(item)
for x in p:
    print(p)
for c in p:
    print("2*",c,"=",2*c)


g=[1,3,[4,5]]
f=[6,7,{"pratham",89}]
for item in g:
    print(item)
for x in f:
    print(f)
print(type(f[2]))

f=[10,20,30,40,50]
a=[100,200,300,400,500]
for m,n in zip(f,a):
    print(m,"+",n,"=",m+n)

for r,t in zip(f,a):
    print(r,"*",t,"=",r*t)




k="keyboard"
for x in reversed(k):
    print(x.upper()*3)
for a in k:
    print("hell'no".upper())
for t in k:
    print(t.upper())


for u in range(0,11):
    if (u%2==0):
        print(u,"is a even")
for a in range(0,51):
    if(a%3==0):
        print(a," divide by 3")

st = 'Print every word in this sentence that has an even number of letters' # in result i get every word in sentence in string in odd and even form.
for word in st.split():
    if len(word)%2 == 0:
        print(word)

a="united states of america"
for q in a.split():
    if len(q)%2==0:
        print(q)

h="hi my name is pratham,i am tall boy in my family"
for w in h.split():
    if len(w)%2==0:
        print(w)

r="russia is better than america"
for e in r.split():
    if len(e)%2==0:
        print(e)
count=0
for character in r:
    print(f"{character.upper()}:{count}")
    count+=1

m="mike and marcus are shooting a movie of bad boy five"
for t in m.split():
    if len(t)%2==0:
        print(t)
for word in m.split():
    if len(word)%2==0:
        print(word)

u="america dropped the atom bomb on japan in world war 2 "
for word in u.split():
    if len(word)%2==0:
        print(word.upper())

c="call of duty modern warfare"
for word in c.split():
    if len(word)%2==0:
        print(word)
o="call of duty world at war and cold war"
for r in o.split():
    if len(r)%3==0:
        print(r)
for q in o.split():
    if len(q)%5==0:
        print(q.upper())


n="india"
count=0
for character in n:
    print(f"{character.upper()}:{count}")
    count+=1
for y in n:
    print(y.upper()*4)

m="mark zucerburg is a ceo of facebook."
for k in m.split():
    if len(k)%3==0:
        print(k)
w="will smith and chris rock"
for x in w:
    print(w)
for t in w:
    print(t.upper())
for x in w.split():
    print(x)
for u in w.split():
    if len(u)%5==0:
        print(u.upper())
count=0
for i in w:
    print(f"{i}:{w}")
    count+=1
count=0
for character in w:
    print(f"{character}:{count}")
    count+=1

s="united states of america"
for t in reversed(s):
    print(t.title())
for i in s:
    print(i,end=" ")
print("joe biden")
for x in s[5:15]:
    print(x)
for y in s:
    print(y.upper()*5)
for c in s.split():
    if len(c)%5==0:
          print(c)
for c in s.split():
    if len(c)%6==0:
        print(c)



st = 'Print only the words that start with s in this sentence' ################################################
for word in st.split():
    if word[0] == 's':
        print(word)

m="mike and marcus are still shooting in bad boys five"
for word in m.split():
    if word[0]=="b":
        print(word)

r="ramayan"
for t in r:
    if len(t)%2==0:
        print(t)
for a in r:
    print(a*2)
for x in r:
    print(r)
for t in r:
    print("raavan"[0:3].upper()*2)
count=0
for character in r:
    print(f"{character}:{count}")
    count+=1


d="danny"
print(f"{d}sell the alcohol bottles.")

d="{1} and {0} are friend.".format("joe","barack")
print(d)
#
e="esports world cup"
count=0
for character in e:
    print(f"{count}:{character.upper()}")
    count+=1

r=["republic of gamers"]
count=0
for character in r[0]:
    print(f"{count}:{character.upper()}")
    count+=1

for character in r[0]:
    print(f"{character}:{count}")
    count+=1

s="soviet union"
count=0
for character in s:
    print(f"{count}:{character}")
    count+=1

x=90
print(x-(x+90))
print(x<(x-4))


y=[1,3,5,7,9,11,13,15,17,19]
for num in y:
    print(num*num)
for v in y:
    print("3*",v,"=",3*v)
    print(3*v)
for loop in reversed(y):
    print(loop)
o=[1,3,5,7,9]
for loop in o:
    print("3*",loop,"=",3*loop)
for i in o:
    print(o)
for u in o:
    print(u)

# f=[1,2,3,45,67,8,89,99,9,8,765,43,22,[34,5678,7,6,543,2,[345,67,[8,[6,543,2],3,45],67,654],32,3,456,7,89,7,65,4,3,45,6]]
# print(f[13][6][2][1][1])

t="there is a forest and in forest there are so many animals such elephant, porcupine, snake, lion, tiger, etc."
for r in t.split():
    if len(r)%2==0:
        print(r)
for w in t.split():
    if len(w)%5==0:
        print(w.upper())
for y in t.split():
    if y[0]=="e":
        print(y)
for i in t.split():
    if i[0]=="i":
        print(i.upper())
for d in t.split():
    if d[0]=="l":
        print(d.title())

a="andanman and nicobar"
count=0
for character in a:
    print(f"{character}:{count}")
    count+=1
for w in a:
    print(f"{w}:{a}")
for q in a.split():
    if len(q)%7==0:
        print(q)
for o in a.split():
    if o[0]=="a":
        print(o)


v="valorant is better than counter strike"
for letter in v.split():
    if len(letter)%6==0:
        print(letter)
for loop in v.split():
    if loop[0]=="s":
        print("counter",loop,"global offensive")





list=["zero","one","two","three","four"] #######        FOR LOOP USING LISTS BY THE HELP OF ENUMERATE     ################
for i,loop in enumerate(list):
    print(i,loop)

t=[(12,24),(23,45),(78,56),(78,90)]
for l,lop in enumerate(t):
    print(l,lop)
for a,b in t:
    print(b)
for y in t:
    if y==(23,45):
        continue
    print(y)
for num in t:
    if num==(23,45):
        break
    print(num)

e="elephant"
for loop in e:
    if loop=="h":
        continue
    print(loop)
for h,hop in enumerate(e):
    print(h,hop)
for r in reversed(e):
    print(r)

q=[2,3,4,5,7,8,5,65,6,8,1,90,89]
for loop in q:
    print("2*",loop,"=",2*loop)

print(sorted(set(q)))
for t in q:
    if t==4:
        break
    print(t)
for y in q:
    if y==5:
        continue
    print(y)
# for v,loop in enumerate(q):
#     print(v,loop)



n="nelson mandela"
for loop in n.split():
    if len(loop)%2==0:
        print(loop)
for i in n.split():
    if i[0]=="m":
        print(i)
count=0
for character in n:
    print(f"{character}:{count}")
    count+=1
for t,y in enumerate(n):
    print(t,y.upper())
for u in reversed(n):
    print(u.upper())
for t in n:
    print(t*3)
for q in n:
    print(q,"south africa"[0:4].upper()*3)
for t in n:
    print(n)

u=[1,35,7,9,11,13] ###################################################################################################
for g,t in enumerate(u):
    print(g,t)
for f in sorted(u):
    print("2*",f,"=",2*f)
for j in u:
    print(j**j)
for r in u:
    print(r*2)
for num in u:
    print(f"{num}:{count}")
for t in u:
    print(t +20)
print(t+20)
for g in u:
    print("2+",g,"=",2+g)
for i in u:
    print(i,"-","2","=",i-2)
for t in u:
    print(t,"/","2","=",t/2)
for g in u:
    print(g**0.5)
for w in u:
    if 7>9 in u:
        print("true".upper())
    else:print(w,'false'.upper())
print(id(136**0.5))



y={"om":45,
   "pratham":90,
   "rushit":23,
   "parth":24,}
for k,v in y.items():
    print(k)
    print(v)
    print(k,v)

k=[2,3,4,5,6,7,8,9,10]
for t in k:
    print("2*",t,"=",2*t)
for r in k:
    print(r,"/2","=",r/2)
for d in k:
    print(d,"%2","=",d%2)

r="republic of china"
for loop in r.split():
    if len(loop)%2==0:
        print(loop)
for t in r.split():
    if t[0]=="c":
        print(t)
for u,i in enumerate(r):
    print(u,i)
for t in r[-2:]:
    print(t.upper())

print(r[-3:])
print(r[3:])
print(r[::3])
print(r[::-1])
print(r[::-2])


l=["pratham","om,","parth"]
for n in l:
    print("what are you doing???",n)

i="india is reaching three trillon dollar economy in upcoming few years."
for l in i.split():
    if l[0]=="t":
        print(l)
for t in i.split():
    if len(t)%2==0:
        print(t.upper())
for y in i.split():
    if len(y)%3==0:
        print(y,"<---- length of the word.")


# n=["pratham","om","parth","rushit","mann"]
# a=[20,34,56,22,12]
#
# for t in n:
#     for r in a:
#         print(f"{t}:{r}"


# s="siddharath"
# for pratham in s: ################################      problem ########################################################
#     print(f"{pratham}  are best friends")


r=["average","count","max","min","dcount","percentage"]
print(sorted(r))
for t,loop in enumerate(r):
    print(t,loop)
count=0

for t in reversed(r):
    print(t)


e=[2,4,6,8,10,9,45,333,434,34]
for t in reversed(e):
    print(t)


d={"dict":"telephone","china":"alibaba","india":"jio","adani":["cement","airports"]}
for b in d.values():
    print(b)
for k,v in d.items():
    print(f"{k}:{v}")



q=[(12,34),(56,78),(87,90)]
for a,b in q:
    print(a,b)
for r,z in enumerate(q):
    print(r,z)
count=0
for num in q:
    print(f"{num}:{count}")
    count+=1

w=[2,4,6,8,10,12,14,16,18,20]
for loop in w:
    print("2*",loop,"=",2*loop)
for u in w:
    print(u**u)
for q in w:
         print(q+2)
for e,i in enumerate(w):
    print(e,i,)


n="new zealand."
for t in n.split():
    if len(t)%2==0:
        print(t)
for a in n.split():
    if a[0]=="n":
        print(a.upper())
for m,e in enumerate(n):
    print(m,e.upper())

t=[(12,23),(34,560),(25,89),(89,90)]
for a,b in t:
    print(a)
    print(b)
print(a,b)
for f,r in enumerate(t):
    print(f,r)
for g in t:
    if g==(34,560):
        break
    print(g)
for f in t:
    if f==(25,89):
     continue
    print(f)


s={2,4,6,8,10,12,14,16,18,20}
for g in s:
  if g==6:
      continue
  print(g)
for t in s:
    if t==10:
        break
    print(t)
for g in s:
    if g==8:
        continue
    print(g)
print(type(s))

index=0
for word in "abcde":
    print("AT index {} the word is {}".format(index,word))
    index+=1


t=[12,3,4,5,678,78,3672]
print(sorted(t))
r=["abc","def","ghi","ijk","jkf","dc","mi"]
for te in zip(t,r):
    print(te)

w=[90,89,67,45,2789,783434890]
print(sorted(w))
a=[]
for t in w:
    a.append(t)
    print(a)


p="%s president of the usa"
print(p%("joe biden"))

print("elephant","is","the","huge","animal","in","the","forest.",sep="/^/^/^/")
print("mukesh {} is the {} person in india".format("amabani","richest"))
print("adani built his new aiprot in",end=" ")
print("navi mumbai.")

t=[(90,45),(33,45),(78,566),(23,455)]
for a,b in t:
    print(a)
    print(b)
    print("\n")

q=[(23,24),(45,78),(12,34),(56,78)] ############### how to find even number and odd number in for loop at one time  #####################################
for a,b in q:
    print(a,b,sep=":")

for r in range(3,30):
    if r%2==0:
        print(r,"even")


s={"keyboard":45,
   "mouse":89,
   "wire":230,
   "monitor":27}
for a,b in s.items():
    print(a)
    print(b)
print("\n")


if x>y:
    x = 2
    y = 4













