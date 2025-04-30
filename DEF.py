####### def function   ######
def gamma(a,b):
    return a[0]==b[0]
print(gamma("apple","ball"))

def cid(acp,daya):
    return acp + daya
print(cid("pratham","patel"))

def r(gt,mt=650):
    return chr(gt+mt)
print(r(20))

def beta(a="alpha",b='apollo'):
    print(f"the {a[0]}:{b[0]}")
beta("apple","grapple")

def vice_city(o="old",t="town"):
    return o[0]==t[0]
print(vice_city("old","monk"))

def op(x):
    return x[0][0]==x[0][0]
print(op(["animal"]))
print(op(["tiger"]))

def red(j):
    print(f"the {j[0]} == {j[0]}")
red("jungle")
red("animal")

def add_function(num1,num2):
    return num1+num2
result= add_function(1,2)
print(result)


def greeting(h):
    print(f"hello {h}")
greeting("jos")


# def greet():
#     return  "hello! world."

def function(x=[]):
    x.append(1)
    return x
print(function())
print(function())


def sum(a,b):
    c=a+b
    print("sum is",c)
sum(23,89)

def greet(name):
    print("hi"+ name + "!")
    greet("pratham")

def add(num1,num2):
    print(num1+num2)

add(20,40)

def greet(name):
    print("hi" + name +  "!")

greet("pratham")

def grt():
    print("hello world")

grt()

print("outside function")

def jkf(name):
    print("hello",name)

jkf("john")

def kgf():
    print("kolar")
    print("gold")
    print("fields")

kgf()

def sen():
    print("donal trump is going to florida.")
    sen()


def ty():
    print("third year ")


ty()


def usa():
    print("united")
    print("states")
    print("america")


usa()


def msd():
    print("mahendra".upper())
    print("singh".upper())
    print("dhoni".upper())


msd()


def add(v1, v2):
    print(sum(v1, v2))


add(30, 60)


def eu():
    print("europian")
    print("union")


eu()


# def return_result(a,b):
#     return a+b
# return_result(10,30)


def my_function():  ##########################################  DEF METHOD 1 ########################################
    print("this is python.".upper())


my_function()


def jk():
    print("jammu".upper())
    print("kashmir".upper())


jk()


def name(n1,
         n2):  ############################################### DEF METHOD 2 #########################################
    print(n1 + " " + n2)


name("numpy", "pandas")


def uk(name1, name2):
    print(name1 + " " + name2)


uk("united", "kingdom")


def p(m, i):
    print(m + i)


p("mission", "impossible")


def crew(t, c):
    print(t + c)


crew("tom", "cruise")


def c(u, c):
    print(u + " " + c)


c("udemy", "courses")


def m(p, m, o):
    print(p + " " + m + " " + o)


m("prime", "minister", "office")


def laptop(asus, tuf):
    print(asus + " " + tuf)


laptop("ASUS", "the ultimate force".upper())


def dt():
    print("donald")
    print("trump")


dt()


def my(name):
    print(name + "patel")


print("pratham")


def name(firstname, lastname):
    print(firstname + " " + lastname)


name("pratham", "patel")


def n(name1, name2):
    print(name1 + " " + name2)


n("virat", "kohli")


def e(e, u):
    print(e + " " + u)


e("europian", "union")


def c(c, t):
    print(c + " " + t)


c("champions", "trophy")


def c(f, c, b):
    print(f + " " + c + " " + b)


c("football", "club", "barcelona")


def a(i, s, r, o):
    print(i + " " + s + " " + r + " " + o)


a("indian", "space", "research", "orient")


def f(l, h, m):
    print(l + " " + h + " " + m)


f("lock", "heed", "martin")


def my_function(
        *kids):  ################################################     DEF METHOD 3 (ARBITARY ARGUMENTS  *args)   #################################
    print("the youngest boy is " + kids[2])


my_function("pratham", "om", "tintin")


def cars(j, g):
    print(j + " " + g)


cars("japan", "germany")


def d(*defence_company):
    print("the defence company in india " + defence_company[1])


d("lockheed martin", "hindustan aeronautics limited", "boeing")


def f(*friends):
    print(friends[1] + " are both brothers.")


f("tinku and minku", "ram and laxman", "suresh and ramesh")


def g(tower):
    print("tower")


g(f)


def pc(*games):
    print(games[4] + " is survival game.")


pc("cod", "csgo", "fornite", "gta5", "pubg pc")


def computer_games():
    print("pubg".upper())
    print("fortnite".upper())
    print("csgo".upper())


computer_games()


def c(*countries):
    print(countries[3] + " is best country.")


c("america", "china", "russia", "india")


def e(ps, p2,
      pc):  ####################################       DEF METHOD 4  (KEYWORD ARGUMENT)  *args  ######################################
    print(pc + " is best for play games.")


e(ps="playstation", p2="playstation2", pc="personal computer")


def g(g, g2, g3):
    print(g2 + " is all rounder game.")


g(g="pub", g2="gta5", g3="fortnite")


def i(child1, child2, child3):
    print("the youngest child is " + child2)


i(child1="om", child2="pratham.", child3="rohan")


def tower(t1, t2, t3, t4):
    print("the last tower in the society is " + t4)


tower(t1="A", t2="B", t3="C", t4="D.")


def cloth(
        **c):  ###################################### DEF METHOD 5 (ARBITARY KEYWORD ARGUMENTS  **kwargs ##############
    print(c["b"] + " is cover the  human body.")


cloth(t="t-shirt", b="boxer", s="socks", c="capri")


def t(**tower):
    print(tower["a"] + " is first tower in the society.".upper())


t(a="atlanta".upper(), b="bulgaria", c="cuba", d="django")


def l(**language):
    print(language["p"] + " is easy language in the programming world.".upper())


l(j="java", c="c++", p="python".upper(), f="flash", r="react.js")


def a(**monuments):
    print(monuments["t"] + " was made  in the love of mumtaz.")


a(e="effile tower", t="taj mahal")


def m(mm, nm):
    print(nm + " is a current prime minister of india.")


m(mm="manmohan singh", nm="narendra modi")


def p(f, c, m):
    print(c + " is the smallest member of family.")


p(f="father", c="child", m="mother")


def o(*u):
    print(u[0] + " is full with the black people.")


o("uganda", "egypt", "kenya")

def r(games="gta5"):
    print("i have been played such games in my childhood such as "+ games)
r("midtown madness")
r("gta vice city")
r("spiderman")
r("counter strike")

def t(pc="monitor"):
    print("computer equipment = "+pc)
t("desktop")
t("graphic card")
t("keyboard")
t("mouse")

def b(businessman="tata"):
    print("businessman = "+ businessman)
b("gautam adani")
b("mukesh ambani")
b("donald trump")
b("robert kiyosaki")
b("elon musk")

def funt(country="sweden"): ##################################  DEF DEFAULT PARAMETER VALUE  ###########################
    print("zlatan is from "+ country)
funt("usa")
funt("france")
funt("portugal")

def age(agge="19"):
    print("i am "+ agge)
age("23")
age("22")
age("21")

def continent(countries="china"):
    print("countries "+ countries)
continent("russia")
continent("china")
continent("india")
continent("pakistan")

def serials(tv="ramayan"):
    print("indian people see "+ tv)
serials("wagle ki duniya")
serials("bigg boss")
serials("anupama")
serials("tmkoc")

def g(x): ########################################            DEF RETURN           #####################################
    return 5*x
print(g(2))
print(g(3))
print(g(4))
print(g(5))

def r(q):
    return 2*q
print(r(2))
print(r(3))
print(r(4))
print(r(5))

def t(a):
    return 3+a
print(t(2))
print(t(3))
print(t(4))
print(t(5))

def e(s):
    return 5-s
print(e(-5))
print(e(-4))
print(e(-3))
print(e(-2))
print(e(-1))

def compare(a):
    return type(a)==type(a)
print(compare([1,2,3,4,5]))
print(compare({2,4,6,8,10}))

def faug(pubg,fort):
    print(f"{type(pubg)} === {type(fort)}")
    return type(pubg) == type(fort)
faug([1,2,3,4],(1,2,3,4))
print(faug([1,2,3,4],(1,2,3,4)))

def dubai(b,c):
    return b,c==b,c
print(dubai(12,21))

a=2*2//2
b=3//2*3
print(a,b)

def g(biscuit):
    return biscuit[0]==biscuit[0]
print(g("citadel"))

def j(a,b):
    return a%2==0 or b%2==0
print(j(2,3))

########################   DEF WITH FOR LOOP  ######################
def y(food): ####################################################   PASSING AS AS LIST  IN ARGUMENT  ###################
    for x in food:
     print(x)
fruits=["apple","banana","pineapple","watermelon"]
y(fruits)

def g(games):
    for u in games:
        print(u)
video=("pc","ps"),("ps2","ps3"),("gta","cod")
g(video)

def b(businessman):
    for w in businessman:
        print(w)
man={"mukesh":"ambani",
     "elon":"musk",
     "mark":"zucerberg",
     "gautam":"adani"}
b(list(str(man.items())))

def c(continents):
    for x in continents:
        print(x)
q=["africa","asia","north america","pacific","east"]
c(q)
s=[q.append("tiger")]
print(q)
w=[q.append("new zealand")]
print(w)

def summit(**leaders):
    return leaders["n"]+" "+leaders["m"]
print(summit(n="narendra",m="modi"))


def bogo(*free):
    print(f"{free[0]} + {free[1]}=={free[0]+free[1]}")
    return free[0]+free[1]
print(bogo(1,2,3,4,5))

def kenya(nairobi,kisi):
    return nairobi+"\n"+kisi
africa=kenya("donald trump","president")
print(africa)

def dmart(a,b,c,d,e):
    c=d+e
    a=b-c
    d=a%c
    return c,a,d
print(dmart(10000,20,10,400,500))

def sqrt(v,p):
    print(v**p)
sqrt(2,5)

def key(*board,c=2):
    return board[0]*board[1]+board[2]**c
print(key(10,2,5))

e=(12,2,9,89,4,32)
def b(*f):
    print(f[0]*f[1])
b(*e)

def company(brand):
    print(brand +" motors")
    print(brand +" ev")
    print(brand +" salt")
    print(brand +" bigbasket")
company("tata".upper())


def tuf():
    t=2
    u=4
    f=6
    print(t*u+f)
tuf()
tuf()
tuf()

def naam(a):
    print("my name is "+a)
    print(f"{a} stands at a mall.")
    # return f"my name is :{naam("pratham")}"
naam("pratham")

def geometric(a,b,c):
    return 0.5*a*b*c
print(geometric(2,4,6))

def detail(name,age,education,job):
    print("my name is "+name)
    print("i am "+str(age)+" years")
    print("i am study "+education)
    print("i will find jobs about "+job)
detail("pratham",23,"python".title(),"data analyst")


"EXERCISE SOLUTIONS of DEF FUNCTIONS "

def two(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else: return max(a,b)
g=two(2,4)
h=two(2,5)
print(g)
print(h)

def v(i,o,p):
    if i%2==0 and o%2==0 and p%2==0:
        return max(i,o,p)
    else: return min(i,o,p)
b=v(1,29,94)
l=v(12,90,4)
print(l)
print(b)

def animals(text): ######################################## EXPLANATION OF THIS SUM ####################################
    word=text.split()
    print(f"word is: {word}")
    print(f"word[0] is:{word[0]}")
    print(f"word[0][0] is :{word[0][0]}")
    print(f"word[1] is :{word[1]}")
    # print(f"word[1][0] is :{word[1][0]}")
    return word[0][0]==[1][0]
d=animals("Levelheaded Llama")
c=animals("Crazy Kangaroo")

def an(sen):
    s=sen.split()
    # print(f"s is: {s}")
    print(f"s[0] is : {s[0]}")
    print(f"s[0][0] is: {s[0][0]}")
    return s[4]==s[4]
a=an("russia is a great country")
z=an("america is a good into recession")
print(a)
print(z)

def two(mesage):
    m=mesage.split()
    return m[0]==m[0]
k=two("japan")
f=two("india")
print(k)
print(f)

h=[[1,2,3],
   [4,4,5],
   [7,8,9]]
for t in h[0]:
    t+=t
    print(t)

