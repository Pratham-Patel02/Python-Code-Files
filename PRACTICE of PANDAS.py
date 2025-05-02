import pandas as pd

d={"student":["pratham","rushit","rinku","jeet","manan"],
   "rank":[1,2,3,4,5],
   "marks":[10,90,42,32,12]}
df=pd.DataFrame(d)
# print(df)
print("students record\n\n",df)
print()
print()

da={"Student":["pratham","rushit","rinku","jeet","manan"],
   "Rank":[1,2,3,4,5],
   "Marks":[10,90,42,32,12]}
k=pd.DataFrame(da,index=["RowA","RowB","RowC","RowD","RowE"])
print("Student Records\n\n",k)

print("Access the value in the student column corresponding to the RowA label")
print("\nValue",k.loc["RowA","Student"])
# print("\nValue",k.loc["RowB","Students","Marks"])
print()
l=[1,2,3,4,5]
c=pd.DataFrame(l)
print(c)
print(type(c))
print()
f={"a":[1,2,3,4,5],"b":[0,2,4,6,8],"c":[1,3,5,7,9],"d":[10,30,50,70,90]}
g=pd.DataFrame(f)
print(g)
o=pd.Series(f)
print(o)
print()
x=pd.DataFrame(f,columns=["c"])
print(x)
print()
k={"Founders":["Mark","Elon","Trump","Jeff","Bill"],
   "Companies":["Facebook","Tesla","Towers","Amazon","Microsoft"]}
l=pd.DataFrame(k)
print(l)
print(l["Founders"][2])
print(l["Founders"][0])
print()

f=[["A","B","C","D","E"],[1,2,3,4,5]]
c=pd.DataFrame(f)
print(c)
print(type(c))
o=pd.Series(f)
print(o)
print(type(o))
print()

g=[["APPLE","BANANA","CHIKU","DAMBAR","FRUIT"],[1,2,3,4,5]]
d=pd.DataFrame(g)
print(d)
print()

print(" #### SERIES  ###")
s=["A","B","C","D","E"]
print(pd.Series(s))
p=pd.Series(s)
print(p)
print(type(p))
print()

e=pd.Series([])
print(e)
print()

j=pd.Series([10,20,30,40,50],index=["A","B","C","D","E"])
print(j)
print()
i=pd.Series(["apple","tesla","oracle","microsoft","facebook"],[1,2,3,4,5],name="companies".upper())
print(i)
print()

ss=pd.Series(0.5)
print(ss)
print()
sss=pd.Series(0.5,index=[1,2,3])
print(sss)
print()

pan_dic=pd.Series({"U":-5,"V":-4,"X":-3,"Y":-2,"Z":-1})
print(pan_dic)
print(pan_dic["V"])
print(pan_dic[-3:])
print()

tri=pd.Series({"E":[1,3,5],"O":[0,2,4],"V":[7,9,11],"D":[6,8,10]})
print(tri)
print(tri["E"][1])
print(tri["V"][0:2])
print(tri[-3:])
print()

print("### DATAFRAME ###")
fra=pd.DataFrame()
print(fra)
print()

fral=pd.DataFrame([1,2,3,4,5])
print(fral)
print(type(fral))
print()

d_fra=[[1,2,3,4,5],["ab",'bc','cd','de','ef']]
g=pd.DataFrame(d_fra)
print(g)
print(type(g))
print()

f=pd.DataFrame([{"a":5,"b":4,"c":3,"d":2,"e":1},
                {'a':-5,"b":-4,"c":-3,"d":-2,"e":-1}])
print(f)
print(f["a"])
print()

k={"roll no.":pd.Series([1,2,3,4,5]),
   "Maths":pd.Series([90,25,14,23,13]),
   "science":pd.Series([10,42,31,23,51])}
da_fry=pd.DataFrame(k)
print(da_fry)
print()
# o=pd.read_csv('C:\Users\hp\OneDrive\Desktop.csv')
# print()

e=pd.Series({"even":[1,3,5,7,9,11,13,15,17,19],
             "odd":[0,2,4,6,8,10,12,14,16,18,20]})
print(e)
print()
# c=pd.Series([[10,30,50,70,90],[0,20,40,60,80,100]],index=["A","B",'C',"D","E"])
# print(c)
l=pd.Series([0,2,4,6,8,10],index=["a","b","c","d","e","f"])
print(l)
print()

e={"APPLE":150,
   "TESLA":230,
   "NVIDIA":100,
   "FB":902}
o=pd.Series(e)
print(o)
print()


i={"Student":["pratham","rushit","rinku","jeet","manan"],
   "Rank":[1,2,3,4,5],
   "Marks":[10,90,42,32,12],
   "Role":["manager","leader","recruiter","assisstant","accountant"]}
y=pd.DataFrame(i)
print(y)
print(y.columns)
print()

g={"COM":["oracle","microsoft","facebook","tesla","chase","towers"],
   "FOUNDERS":["Larry","bill","mark","elon","morgan","trump"],
   "SALARY":[29000,10000,25223,23242,12342,3232],
   "LUXURY":["cars","planes","computers","apps","jets","stocks"],
   "ORIGIN":["arizona","new_york","texas","california","las_vegas","seattle"]}
o=pd.DataFrame(g)
print(o)
print(o.columns)
print(o.shape)
print()

l_t={"Student":["pratham","rushit","rinku","jeet","manan","shaurya","yogi","om","vandan","bheem"],
   "Rank":[1,2,3,4,5,6,7,8,9,10],
   "Marks":[10,90,42,32,12,90,42,12,52,85],
     "roll_no":[20,29,24,15,12,48,24,15,26,32]}
w=pd.DataFrame(l_t)
# print(w.head())
# print(w.head(3))
print(w.tail())
# print(w.tail(6)+w.tail(3))
print(w.describe())
# print(w.info())
print()
print("15/2/25")

f=[1,2,3,4,5,6]
u=pd.DataFrame(f)
print(u)
print(type(u))
print()
dic={"Sr.no":[1,2,3,4,5],
     "name":["elon","trump","hegseth","mark","pam"]}
o=pd.DataFrame(dic)
print(o)
print()

e=pd.Series([10,20,30,40,50],[1,2,3,4,5])
print(e)
print()

f={"country":["india","china","russia","brazil","spain"],
   "rank":[1,2,3,4,5],
   "short_form":["IND","CHI","RUS","BRA",'SPA'],
   "leaders":["modi","xi","putin","neymar","ramos"]}
o=pd.DataFrame(f)
print(o)
p=pd.DataFrame(f,columns=["short_form","leaders"])
print(p)
# print(p.info)
print()

print("17/2/25")

f=pd.DataFrame({"songs":pd.Series(["people","animals","faded","on_my_way","taki_taki"]),
                "artists":pd.Series(["martin_garrix","dj_snake","alan_walker","rihanna","kendrick lamar"]),
                "origin":pd.Series(["france","america","england","netherland","belgium"])})
print(f)
# print(f,columns="artists")
print(type(f))
print(f.columns)
print(f.size)
print(f.shape)
print(f.head(3))
print()
print(f.tail(2))
print(f["origin"][2])
print()

g=pd.Series(["name","age","gender","role","salary"],[1,2,3,4,5],name="order")
print(g[3])
print(g[2],g[4])
print()
print(g)
print(type(g))
print()

# h={"networks":["jio","starlink","airtel","vodafone","ATT"],
#    "country":["india","new zealand","america","spain"]}
# a=pd.DataFrame(h)
# print(a)

q={"cars":["BMW","TESLA","RIVIAN","TOYOTA","NISSAN"],
   "origin":["america","germany","canada","japan","south_korea"]}
i=pd.Series(q,name="made".upper())
print(i)
print()
print(i.shape)
print(i.array)
print(i.head(3))
print()

# q=pd.Series(["cars","bikes","planes","games",'gamers',"wires"],[1,2,3,4,5,6],name="things")
# print(q)
# print(type(q))
# print()

j={"names":["meta","apple","micron","nvda","tsla"],
   "prices":[29.10,10.32,100,130.21,60.31],
   "made":["apps","phones","chips","cards","cars"]}
# print(pd.DataFrame(j))
l=pd.DataFrame(j)
print(l)
o=pd.DataFrame(j,columns=["names"])
print(o)
p=pd.DataFrame(j,columns=["names","made"])
print(p)
print()
c=pd.DataFrame(j)
print(c["names"][0:2])
print()
i=pd.DataFrame(j,index=["M","A","M","N","T"])
print(i)
print()
# print(i["names"],["prices"],["made"][-2])
# print(i["made"][3])

r=pd.Series(["A","B","C","D"],[1,2,3,4],name="order")
print(r[1])
# print(r)
print(type(r))
v=pd.DataFrame(r)
print(v["order"][2])
# print(v)
print(type(v))
print()

i={"games":["gta","rainbow six x","battlefield","pubg","fortnite","warzone","forza horizon","road rash","apex legends"],
   "rank":[10,6,4,2,3,1,7,8,5],
   "years":[2000,2016,2008,2018,2019,2021,2020,1996,2017],
   "type":["open_world","multiplayer","survival_action","battleground","small kids","brutal action","car_racing"
           ,"bike_competition","action_robotics"],}
p=pd.DataFrame(i)
print(p,type(p))
# s=pd.Series(i)
# print(s)
print(p.head(3))
print(p.tail(3))
print()
print(p.describe())
# print(p.info)
print(p["type"][5])
print()

c={"com":["micron","tata","mahindra","reliance",
          "infosys","larsen","pi"],
   "rank":[9,4,1,5,8,3,7],
   "make":["chips","motors","finance","petrol","systems",
           "contruction","glass"]}
f=pd.DataFrame(c,columns=["make"])
print(f)
print(f.describe())
k=pd.DataFrame(c)
print(k)
print(k.ndim)
print(k.shape)
print()
print(k.replace("micron","dixon"),k.replace("infosys","tcs"))
print(k.replace("systems","consultant"))
print(k.replace(["reliance","micron","tata"],["REL","MIC","TA"]))
print(k.replace(["micron","tata","mahindra","reliance"],[0.1,0.2,0.3,0.4]))
print(k.replace(["pi","infosys","larsen"],["rank"[0],[1],[3]]))
print()

# i=pd.Series([10,9,8,7,6,5])
# p=pd.Series([-10,-9,-8,-7,-6,-5])
# o=i+p
print()

c={"model":["tigor","hexon","harrier","sierra","sierra","tigor"],
   "brands":["tata","tata","mahindra","citrogen","tata","citrogen"],
   "sr.no".title():[6,3,2,1,4,5]}
p=pd.DataFrame(c)
print(p)
print()
lc=pd.DataFrame(c)
print(lc.replace("tata",10))
print()
xc=pd.DataFrame(c)
print(xc.replace(["sierra","tigor"],21))
print(xc.columns)
print()

print("20/2/25")

o={"leaders":["putin","trump","modi","treadue","macron","mbs",
              "kim jong un","xi ping"],
   "origin":["russia","america","india","canada","france",
             "saudi arabia","north korea","china"],
   "firms":["telegram","meta","jio","cisco","citrogen","aramco",
            "noodles","ali baba"]}
k=pd.DataFrame(o)
print(k)
l=pd.DataFrame(o,columns=["leaders"])
print(l)
print(l.head(2))
print(l.tail(3))
v=pd.DataFrame(o)
print(v)
print(v.columns)
print(v.shape)
print(v.head(3))
print(v.tail(3))
print(v.describe())
print(v.info())
print()
h=pd.DataFrame(o,[10,20,30,40,5,6,7,8])
print(h)
print(h.replace(["america"],["usa"]))
print(h.replace(["meta"],["nvidia"]))
print(h["leaders"])
print()
# print(h["origin"].replace(["usa","china","russia","india"],[1]))
p=pd.DataFrame(o)
print(p["origin"])
print(p.replace(["russia","india","canada","france"],value=1))
print(p["leaders"].replace(["kim jong un","xi ping","treadue"],value=100))
print(p["firms"].replace(["ali baba","noodles","aramco"
                          ,"citrogen"],value=200))
print()

dog={"numbers":[10,90,3,2,5,225,2,31],
     "comp":["meta","tesla","rivian","amazon","walmart"
             ,"costco","home deport","apple"],
     "games":["warzone","fortnite","pubg","apex legends",
              "uno","monopoly","sims","cars"],
     "ranks":[10,9,4,5,2,3,6,7]}
k=pd.DataFrame(dog)
print(k)
# print(k["comp"].replace(["meta","tesla","rivian"
#                          ,"amazon"],value=[100,200,300,400],inplace=True))
# print(df[col].method(value, inplace=True))
# print(k["comp"].replace(to_replace=["meta"
#                                     ,"amazon",
#                                     "tesla","rivian"],
#                         value=["ABC","DEF","GHI","JKL"],inplace=True))

# print(k.replace('[A-Za-z]',0))
# l=pd.DataFrame(dog)
# print(l.replace('[A-za-z]',100))
# print(l.replace('[A-Za-z]',100,regex=500))
print()

# t=pd.read_xml(r"C:\Users\hp\OneDrive\Desktop\Microsoft Excel Comma Separated Values File (.CSV)")
# print(t)

# df=pd.read_csv("people.csv")
# print(df)

# dataframe=pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\List")
# print("our file",dataframe)
# ex=pd.read_excel(r"C:\Users\hp\OneDrive\Desktop\List")
# print(ex)

df=pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\List.csv')
print(df)
print()

DFC=pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\TATAMOTORS.CSV')
print(DFC)
# print(DFC.head(10))
# print(DFC.tail(10))
v=pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\TATAMOTORS.CSV')
print(v.columns)
print(type(v))
print(v["High"].head(5))
print(v.isnull())
print(v.isnull().sum())
print(v.shape)
print()
x=v.dropna()
print(x.shape)
o=v.dropna(axis=1)
print(o)
print()
l=v
print(l["Open"].head(60))
# print(l.isnull().sum())
print(l["Open"].isnull().sum())
print(l["Open"].head(60).dropna(how="any"))
# print(l["High"].head(70).dropna(how="any"))
print(l["High"].head(70).isnull().sum())
print(l["High"].head(60).isnull().sum)
print()

o=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\TATAMOTORS.CSV")
# print(o["High"])
# print(o["High"].head(60))
c=o
# print(c["High"].head(60).isnull().sum())
# print(c["High"].head(60).shape)
# print(c["High","Low"].shape)
# print(c["Low"].isnull().shape)
print(c["High"].head(50).isnull().sum())
print(c["Low"].head(50).isnull().sum())
print(

)
f=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop/TATAMOTORS.CSV")
print(f,type(f),f["High"])
print(f["High"].head(30).isnull,f["High"].head(35).isnull().sum())
asd=f["High"].head(25).isnull().sum()
print(asd)
print()
x=f["High"].head(60).dropna(axis=0)
print(x)
print(

)
print(" #####  TATA MOTORS DATA SET ########")
hi=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop/TATAMOTORS.CSV")
# print(hi.dropna().head(60))
print(hi.head(60))
# print(hi.head(60).dropna().shape)
print(hi.head(60).isnull().sum())
print()
hello=hi
# print(hello.head(60).dropna(axis=0))
print()
print(hello.head(60).dropna(axis=1))
# print(hello.head(30).isnull().sum())
print(hello.head(60).dropna(axis=1).shape)
print()
hell=hi
print(type(hell))
hole=hell.head(30).dropna(inplace=True)
print(hole)
hal=hello.head(30).dropna(inplace=False)
print(hal)
print(

)
print("#####  21/2/25  #####")
tea=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\Tesla.csv")
print(tea)
print(tea.isnull().sum())
print(tea.isnull().sum().sum())
t=tea.dropna()
print(t.shape)
print(t.dropna(axis=0))
k=tea.dropna(axis=1)
print(k)
print()
b=tea.dropna(how="any")
print(b)
bc=tea.dropna(how="all")
print(bc)
j=tea.dropna(inplace=False)
print(j.shape)
z=tea.fillna(".")
print(z)
# print(z.fillna({"Open":".","High":"|","Low":"-"}))
print()
joke=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\Tesla.csv")
print(joke.fillna({"Open":".","High":"|"}))
print()
print(joke)
print(joke.fillna(method="ffill"))
print(joke)
print()
# j=joke
# print(j.fillna(method="ffill",axis=1))
j=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\Tesla.csv")
print(j)
# print(j.fillna(method="ffill",axis=1))
# print(j.fillna("+"))
# print(j.fillna(method="ffill"))
# o=j
# o=j.bfill(inplace=False)
# print(o)
# print(j.head(25).bfill(inplace=False))
print(

)
game=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\GAMES LIST.csv")
print(game)
print(game["last_update"].head(70))
print(game["last_update"].head(70).isnull().sum())
print(game["last_update"].head(70).dropna(inplace=False).isnull().sum())
# print(game["last_update"].head(70).isnull())
# print(game.head(1000).isnull().sum())
# print(game["release_date"].isnull().sum())
# print(game["release_date"].tail(60).isnull().shape)
# print(game["release_date"].tail(60).dropna().shape)
# print()
# print(game["release_date"].tail(40).isnull().sum())il(60).isnull)
# print(game["release_date"].tail(60).

print("8/3/2025")
g={"cars":["tesla","lamborghini","ferrai","bmw","rivian","toyota","nissan","dodge","ford"],
   "country":["america","italy","abu dhabi","germany","america","japan","south korea","canada","united kingdom"],
   "rank":[1,4,8,9,2,3,5,6,7]}
h=pd.DataFrame(g)
print(h)
print()
f=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop/GAMES LIST.csv")
print(f)
# print(type(f))
print(f["title"])
print(f["title"].head(4),f['title'].tail(4))
# print(f["title"].head(10).count("Grand Theft Auto V"))
# print(f["title"].head(10).insert(5,"SIA",f["a"]))
# print(f["title"].insert(1,"python",f["a"]))
print(f.columns)
# print(f["console"])
print(f.shape)
print(f.size)
print(f.describe())
print(f.info())


















