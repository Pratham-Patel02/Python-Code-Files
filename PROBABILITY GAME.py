import random as rd
y=["H","T","HH","TT","HT","TH"]
print(y)
print(rd.choice(y))
print(

)
e=[(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),
   (2,1),(2,2),(2,3),(2,4),(2,5),(2,6),
   (3,1),(3,2),(3,3),(3,4),(3,5),(3,6),
   (4,1),(4,2),(4,3),(4,4),(4,5),(4,6),
   (5,1),(5,2),(5,3),(5,4),(5,4),(5,6),
   (6,1),(6,2),(6,3),(6,4),(6,5),(6,6)]
print(type(e))
print(rd.choice(e))
print()

mens=[1,2,3,4,5]
womens=[1,2,3,4,5,6]
b=f" in the Event function there are  {rd.choice(mens)} males and  {rd.choice(womens)} females.".title()
print(b)