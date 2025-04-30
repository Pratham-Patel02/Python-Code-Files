i={"ears":2,
   "eyes":2,
   "nose":1,
   "legs":1}
i["legs"]=2
print(sorted(i.values()))

pc={"card":"nvidia",
    "screws":[0,1,2,3],
    "cables":[1,2,3],
    "case":{"insert":6}}
print(pc["cables"][2],print(pc["case"]["insert"]))
print(pc["case"]["insert"])
print(pc["screws"][2]*pc["case"]["insert"])
print(sum(pc["cables"]))

cmp={"brand":{
    "r":"rivian",
    "t":"tesla",
    "maggi":[10,20,12],
    "shampoo":[200,100,300],
    "toyota":{"camry":28}
}}

h=[0,24,23,42,{"news":{"c":"cnn",
                       "a":"abc",
                       "h":"hbo_news"}}]
print(h[4]["news"]["a"].upper())
print(str(h[4]["news"].keys()).upper())

v=[0,234,232,(0,22,221,{"cars":{"t":"tesla",
                                 "r":"rivian",
                                 "c":"chevorlet",
                                 }})]
print(v[3][3]["cars"])
# print(str(v)[3])
print(v[3][3]["cars"]["c"])
print(str(v[3][3]["cars"]["c"]))

c=[0.0,0.1,[1,2,{"a":"america",
                 "d":"donald",
                 "c":"canada"},3,4],0.2,0.3]
print(c[2][2].keys())
print(c[2][4])
print(c[4])
we={"america":'a',
    "cuba":"c",
    "d":[0,2,3,4],
    "n":{"a":"antartica"}}
print(we["d"])
print(we["d"][1]+we["d"][3])
print(we["n"])

p={"random":{1:2,
             3:4,
             5:{50:50,30:60}}}
print(p["random"][1])
print(p["random"][5][50],p["random"][5][30])
# print(p[])

r=(90,23,1,[0,13,4],{"c":"cars",
                     "d":"dance",
                     "p":{"a":"angular",
                          "n":"node"}},{"j":"java",
                                        "js":"javascript"},0,24,2)
print(r[4]["p"]["n"])
print(r[5]["js"].upper().partition("v"))
print(r[7])

light={"bulb":{"h":"headlight",
               "c":"china",
               "e":{"ev":{"t":"tesla",
                          "r":"rivian"}}}}
print(light["bulb"]["e"]["ev"]["r"])

g={"pizza_ser":{"to":{"toy":"toyota"},"delivery"
                :{"a":"amazon","r":"rivian"}}}
print(g["pizza_ser"].values())
print(g["pizza_ser"]["delivery"]["a"])
print(f"i want {g["pizza_ser"]["delivery"]['r']:_>15} car for food delivery service.")
print(f"i bought some things from {g['pizza_ser']['delivery']['a']:.^20}")

cafe={"list":{"c":"choco",
              "s":"strawberry",
              "e":"egg"},"menu":{"c":"crossiant",
                                 "s":"sandwhich",
                                 "g":"garlic_bread","numb":{1:3,
                                                            2:4,
                                                            5:7,"val":{1:3,
                                                                       30:40,
                                                                       50:60}}}}

g={"s":"starboy","w":"weekend"}
f={"c":"chainsmokers","e":"ed sheeran"}
j=list(f.items())
j.append(g)
print(j)
print(type(j))
print(g["s"][0:4]+f["c"][-7:])
print(list(str(g["w"][0:3]+f["e"][-3:])))
print(list(str(f["c"][-7:]+g["s"][-3:]).upper()))

i={"p":{"puri":{"b":"bhelpuri",
                "s":"sevpuri",
                "d":"dahipuri"},"burger":{"m":"macdonald",
                                           "k":"king"}}}
o={"types":{"s":"samosa",
            "c":"chinese",
            "p":"paneer"},"bhajiya":{"b":"bataka",
                                     "pan":"paneer",
                                     "pal":"palak"}}
p=list(o.items())
p.append(i.items())
print(str(p).upper())
print(type(p))
x=list(o)
x.extend(i.values())
print(x)
h=list(o)

######### DICT WITH FOR LOOP #######
car=[{"cars":{"t":"tesla","c":"chevorlet"},
       "laptop":{"r":"razer","lg":"logitech"}}]
for u in car[0]["cars"].values():
    print(u.upper().split("E"))
for d in car[0]["laptop"].values():
    print(d.upper()[::-1].split("E"))

s={"a":"apps",
   "b":"bugs",
   "c":"clutch",
   "d":"decoy"}
for i in s.values():
    print(i.upper())
for k in s.values():
    print(k.upper()[::-2])

r={"fruits":{"c":"cherry",
             "d":"donut","bikes":{"b":"bmw",
                                  "t":"triumph",
                                  "leaders":{"b":"biden",
                                             "d":"donald","cakes":{"s":"strawberry",
                                                                   "c":"chocolate","awards":{"film":"filmfare",
                                                                                             "osc":"oscar",
                                                                                             "fash":"fashion",
                                                                                             "sports":{"c":"cricket",
                                                                                                       "r":"rubgy",
                                                                                                       "foot":'football',
                                                                                                       "s":"skating",
                                                                                                       "p":"polo"}}}}}}}
for u in r["fruits"]["bikes"]["leaders"]["cakes"]["awards"]["sports"].values():
    print(str(u).upper().split())
for j in r["fruits"]["bikes"]["leaders"]["cakes"]["awards"]["sports"].values():
    print(str(j).upper()[0:3:2])
r["fruits"]["bikes"]["h"]="harley"
print(str(r).upper())