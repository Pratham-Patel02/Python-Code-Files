# python reading files (.txt,.json,.csv)
import json

# file="C:/Users/hp/OneDrive/Desktop/input.tt"
#
# with open(file,"r") as file_1:
#     content=file_1.read()
#     print(content)

# file_path="C:/Users/hp/OneDrive/Desktop/input.txt"
# with open(file_path,"r")as file:
#     data=file.read()
# print(data)
#

# fills="C:/Users/hp/OneDrive/Desktop/input.json"
# with open(fills,"r") as file:
#     d=json.load(file)
#     print(d)
#
with open("test.txt","r") as file: ### success ###
    print(file.read())

sen="this file was created by me.\n i changed whole content by ourselves\nwith help of w"
with open("test.txt","w") as file: #### success 2 ###
    file.write(sen)

mole=open(r"C:/Users/hp/OneDrive/Desktop/pratham.txt","r") #### success 3 ####
print(mole.read())
mole=open("C:/Users/hp/OneDrive/Desktop/pratham.txt","w")
print(mole.write("NOW A DAYS GUJARAT IS NEW TOURIST ATTRACTION."))


appendfile=open("C:/Users/hp/OneDrive/Desktop/pratham.txt","a")
appendfile.write("GURUGRAM IS CYBER SECURITY PLACE IN INDIA.")

# pdf=open(r"C:/Users/hp/OneDrive/Desktop/APPLE - Copy.docx","r")
# print(pdf.read())

test=open(r"C:\Users\hp\OneDrive\Desktop/pratham 3.txt","r") ### success 5 ###
print(test.read())
test=open("C:/Users/hp/OneDrive/Desktop/pratham 3.txt","w")
print(test.write("freedom\n      at\n       midnight\n   was released."))

code=open(r"C:\Users\hp\OneDrive\Desktop/PYTHON CODE.txt","r")
print(code.read())

bullet=open(r"C:\Users\hp\OneDrive\Desktop/pratham.hi.txt","r")
print(bullet.read())
gun=open(r"C:\Users\hp\OneDrive\Desktop/pratham.hi.txt","w")
gun.write("i am a python programming language and i am teaching python to pratham.".title())


goli=open(r"C:\Users\hp\OneDrive\Desktop/patel.txt","r")
print(goli.read())
bike=open("C:/Users\hp\OneDrive\Desktop/patel.txt","w")
# bike.read(r"C:\Users\hp\OneDrive\Desktop/pratham.hi.txt","r")
# bike.write("my name is pratham.")
print(bike.write("my name is pratham."))

# d=(r"C:\Users\hp\OneDrive\Desktop/Excel Exercise files","r")
# print(d.read())
print()

# x=open(r"C:\Users\hp\OneDrive\Desktop/TATAMOTORS","r")
# print(x)

# tie=open("C:\Users\hp\OneDrive\Desktop/patel.txt","a")
# tie.read(r"C:\Users\hp\OneDrive\Desktop/pratham.hi.txt","r")
# print(tie.read())

# code=open("C:\Users\hp\OneDrive\Desktop/CODE 2.txt","a") ############      PAUSE APPEND FILE      #############
# print(appendfile)

# code=open("C:/Users/hp/OneDrive/Desktop/PYTHON CODE.txt","w")
# print(code.write("ALSO I LEARN LIST,TUPLE,STRING,DICTIONARY,ETC"))

# with open("C:/Users/hp/OneDrive/Desktop/input.txt") as file:
#     print(file.read())





