

# print("%% writefile my file.txt"
#       "one on first"
#       "two second"
#       "three on third")
# print("my file.txt")



list=[1,3,45,3,1,2,45,[67,45,3,4,2,3,7,8,9,923],"pratham","om","patel"]
print(list[8])
# print(list.count(3))


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












