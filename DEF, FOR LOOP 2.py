# def lu(veg):
#    for h in veg:
#        print(h)
#    fruits=["apple","banana","chiku","pineapple","watermelon"]
#    lu(fruits)

def g(a):
    return 10*a
b=g(10)
print(b)
c=g(20)
d=g(30)
e=g(40)
print(c,d,e)
print(g(50))
print(g(60))
print(g(70))


def n(x,/):
    print(x)
n(2)

def g(o,b):
    print(o,b)
g(10,"/")

def obc(o,b,c):
    print(o,b,c)
obc(10,"*",20)

def alpha(a,b,/,c,d):
    print(a+b+c+d)
alpha(9,1,c=2,d=0)

def multipy(x,y):
    if x*y==20:
        return True
    else: return False
h=multipy(2,10)
i=multipy(2,8)
print(h)
print(i)

def sen(z="zebra"):
    for k in z.split():
         if k[0:4]=="lion":
             return True
         else: return False
k= sen(z="cristiano")
k_k=sen(z="lionel messi")
print(k)
print(k_k)

un=("selena","ronaldo","bradd","elon","mark","tom")
pack=(12.90,45.98,890.22,990.99,00.222,44.5569)
for z in zip(un,pack):
    print(z)
for s,d in zip(un,pack):
    print()
    print(f"{s}-->{d}".upper())

# ### GRADING SYSTEM
# def grading(a):
#     if a>=100:
#         print("a+")
#     elif a<=80:
#         print("b")
#     elif a<=60:
#         print("c")
#     elif a<=40:
#         print("d")
#     elif a<=20:
#         print("fail")
#     else:print("nothing")
# grading(12)


f=[1,2,3,4,5,66,7,23]
g=(2,3,4,59,90,324,12,12)
for n,m in zip(f,g):
    print(n,"*",m,"=",n*m)

def multi(q,w):
    if q*w==24:
        return True
    else: return  False
q=multi(12,2)
qw=multi(2,9)
print(q)
print(qw)

x=41
if x>10:
    print("above, ten")
if x>20:
    print("and also above 20!")
else:print("but not above 20.")

x=["apple","banana"]
if x[1]!="banana":
    print("2")
else:print("no")


r="russia is the biggest country in the world."
for g in r.split():
    if len(g)%2==0:
        print(g)
for u in r.split():
    if u[0]=="i":
        print(u)

def shows(show):
    for k in str(show).split():
        if len(k)%8==0:
            return k
tv=shows("america is the only country to killing genocide in middle east countries")
print(tv)

g=[1,9,23,0,13,4,90,24,12,5,6,89,324]
g.insert(100,9)
print(g)
g.insert(5,200)
print(g)

an="new.zealand/is/a-small-country-in-world"
print(an[:4].capitalize())
for b in an:
    if b[:5].capitalize()==0 and b[7:11].capitalize()==0:
        print(b)

"EXERCISE SOLUTION OF FUNCTION "

def nu(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:return max(a,b)
ber=nu(10,20)
bom=nu(2,10)
print(ber)
print(bom)

def r(aa,bb):
    if aa%2==0 and bb%2==0:
        return min(aa,bb)
    else:return max(aa,bb)
k=r(2,4)
l=r(2,5)
print(k)
print(l)

# def animald(sen):
#     r=sen.split()
#     return r[0]==r[0]
# d=animald("united kingdom is going into recession")
# f=animald("united kingdom is no one in the economy race")
# print(d)
# print(f)

def animals(tex):
    e=tex.split()
    return e[0]==e[0]
s=animals("america is a great")
d=animals("russia is a bad")
print(s)
print(d)


# def r(data):
#         if data%2==0:
#             return d
# f=r("america has a first place in economy race.")
# print(f)

def checkers(values):
    v=values%2==0
    return v
d=checkers(10)
f=checkers(17)
print(f,d)

def g(gold):
    silver=gold.upper()
    return silver[0:4]
qw=g("kalyan")
war=g("tanishq")
print(qw,war)

def right_wrong(t,op):
    if t+op==20:
        return "response"
s=right_wrong(2,4,)
f=right_wrong(15,5)
print(s)
print(f)
#
def jk (mouse,keyboard):
    if mouse+keyboard==50:
        return True
    else:return False
goa=jk(12,8)
gh=jk(12,3)
print(goa)
print(gh)

def g(l):
    if sum(l)==50:
        print("oh yes")
    else: print("ooh no")
g([10,30,5,5])

def h(tree):
    if sum(tree)<=30 or sum(tree)<=40:
        return "pc".upper()
    else: return "nothing"
s=h([10,20,3,40,4,50])
d=h([1,2,3,4,5,6,7])
print(s,d)

def who_is_right(warz):
    print(f"warz[0] == {warz[0]}")
    return warz[1]==warz[1]
mutual=who_is_right("united king & dom")
sip=who_is_right("united states & america")
print(mutual,sip)

def tower(flat):
    print(f"flat.split()=={flat.split()}")
    return flat.split()==flat.split()
fd=tower("shree balaji agora center")
hijack=tower("hero financial corporation")
print(fd,hijack)

# def listing(martin):
#     if martin%2==0:
#         return "value"
#     else:return "noting"
# lin=listing([1,2,34,5,6,7,8,8,9,9,76,54,33,5465])
# print(lin)

def b(gains):
    for c in gains:
        if c%2==0:
            return True
        else:pass
f=b([1,3,5])
fab=b([2,4,5])
print(fab)

def africe(content):
    for r in content:
        if r%3==0:
            break
    return r
agri=africe([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(agri)


def hi(a,b):
    if id(a)==id(b):
        return id(a)==id(b)
    else:hi(a,b)
print(hi(12,12))

def red(blue,purple):
    if id(blue)==id(purple):
        print(id(blue),id(purple))
    else:print("no")
red(12,12)


# def ipo(listed):
#     for k in listed:
#         if k%2==0:
#             break
# zudio=ipo([1,2,3,4,5,6,7,8,9,10,11,1,2,13])
# print(zudio)

# def key(mouse):
#     f=mouse.split()
#     print(f"f[0]=={f[0:3]}")
#     return f[0:3]==f[0:4]
# nop=key("united states of america")
# mop=key("keyboard is joint with mouse")
# print(nop,mop)

# def guns(sent):
#     for s in sent.split():
#       if len(s)%2==0:
#        print(s)
# guns("america is going into recession")

# k=guns("russia is a great country")
# print(k)

# sen="russia is great country"
# for k in sen.split():
#     if len(k)%2==0:
#          print(k)




# def animal_crackers(text):
#     wordlist = text.split()
#     return wordlist[0][0] == wordlist[1][0]
# f=animal_crackers("Levelheaded Llama")
# g=animal_crackers("crazy kangaroo")
# print(f)
# print(g)

# def htower(bones):
#     ftower = str(bones).split()
#     return ftower[0][0]==ftower[0][3]
# r=htower("russia is the biggest country in the world")
# a=htower("america is the biggest country in economy wise.")
# print(h)
# print(a)
#
# def redlight(tintin):
#     mission=tintin.split()
#     return mission[0][1][0]==mission[0][2][0]
# folk=redlight("kill bill")
# golf=redlight("kill,bill,2")
# print(folk)
# print(golf)
#
# def web(google):
#     micro=google.split()
#     return micro[0][1]==micro[0][1]
# ibm=web("google browser is also known as  chrome browser")
# tata=web("google chrome is handle by itself.")
# print(ibm)
# print(tata)
