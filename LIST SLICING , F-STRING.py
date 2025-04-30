

u=[0,2,4,6,8,10]
a=[1,3,5,7,9,11]
b=u+a
print(b)
b[0:6]=-5,-3,-2,-1,0
print(b)
print(b[-1::-2])
b[5::]=100,200,400,600,800
print(b)
print(type(b))
print(a>b)
print(b<u)
print(u<b)
print(a==b)
print(a!=u)
a="mango"
print(f"the {a} on the tree".isalnum())
#print(a.isdigit())
print(a.isalnum())

b="ball goes in the way"
print(b.isalnum())

t='table'
print(input(f"{t.capitalize()} on the way."))

w="we {} on the {} of the {}.".format("stand".capitalize(),"ground".title(),"earth".upper())
print(w)
print(len(w))

print('spacex'.upper(),9)
print(len('spacex'))

list=["clothes","toys","games"]
print(list)
del list[1]
print(list)
list[1]="electronics"
print(list)           

w="happening"      
print(f"what the {w} here??? ")

print(90//56+67-20*67)
print('turtle',300)

u=[90,49,873,987]
print(49 in u)


u=[0,1,2,3,[4,5,6,7,89,100]]
print(u[4][5])

a=[100,300,200,400,500]
print(a.pop())
print(len(a))
print(a[1::])

q=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
print(q[2::])
print(q[::2])
print(q[-3::])
print(q[-3::2])
print(q[-8::2])
print(q[2::5])

p="python"
s="snake"
print(p[0:2])
print(s[3:5])
print(p[0:2]+s[3:5])

t="tiger"
d="deer"
print(t[0:2]+d[0:2])


u_list=[2,4,6,8,10]
a_list=[1,3,5,7,9]
print(u_list[0:3]+a_list[0:3])
print(u_list[0:2]+a_list[0:2])
print(u_list[0:1]+a_list[0:1])
print(u_list[2::]+a_list[3::])

abc=[0,2,2,4,4,6,6,8,10,30,20,30,47,10,5467,452,810,2,2,2,2,2,2,2,2,2,2]
print(abc.count(2))
#print(abc.count(2)*abc[2:4])
print(abc.count(6))
#print(abc.count(6)*abc[0:2])
print(max(abc))
print(min(abc))

abc_list=[1,2,3,4,5,2,3,4,5]
#a=abc_list.count(5)
#print(a)
print(abc_list.count(5))
print(max(abc_list))


sd=[3,4,5,6,3,5,3,4,76,45,34,12,90]
print(sd.index(45))

a=[2,40,40,5,10,7,6,4,7,50,210,]
print(a.sort())



s="stringstr"
print(s.find('t',3))







w=[34,6875,843,202,5759,5859,39,2084,10,20,10,40,450,450,550,50,20,60,100]
#e=w.sort()
#print(e)
#print(sorted(w))
#e=w.reverse()
#print(e)

#ac=[1,2,3,4,5,67,8,9,1]
#bc=ac.reverse()
#print(bc)


#print(max(sorted(w)))
#print(min(sorted(w)))



#a=int(input("the value: "))
#b=int(input("The number: "))
#print(a+b)

#c=int(input("num: "))
#d=int(input("num2: "))
#e=c*d
#print("product:",e)

#abc=input("Enter the value: ")
#efd=input("Enter the value: ")
#print(abc+efd)

#pra=int(input("val: ")
#tha=int(input("val1: "))
#print(pra-tha)

#o=float(input("v: "))
#m=float(input("v3: "))
#p=o*m
#print("product:",p)







