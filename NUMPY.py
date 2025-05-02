
import numpy as np

x=np.array([1,2,3])
print(x)
print()
c=np.array((1,2,3))
print(c*c)
print(type(c))
print(

)
p=np.array([10,20,30])
print("dimensions=",p.ndim)
print(

)
# c=np.array([10,20,30],[1,2,3])
# print("dimension=",c.ndim)
v=np.array([[1,2,3],[4,5,6]])
print("dimensions=",v.ndim)
print(

)
s=np.zeros([2,4])
print(s)
print(type(s))
print(

)
o=np.ones([3,2])
print(o)
print(

)
j=np.array([10,20,30])
print(j.dtype)
a=np.array(["sam","tom","plane"])
print(a.dtype)
f=np.array(["china","brazil","russia","india"])
print(f.dtype)
print(

)
x=np.array(["america","cuba","canada","mexico","panama"],dtype="S3")
print(x)
print(x.dtype)
print(

)
z=np.array(["10","20","30","50"])
print(z)
print(z.dtype)

z1=z.astype("i")
print(z1)
print(z1.dtype)

l=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("dimensions=",l.ndim)
k=np.array([[1,2,3],[4,5,6],[10,20,30]])
print(k.ndim)
# b=np.array([[1,2,3]])
j=np.array([[-3,-2,-1],[0,1,2],[3,4,5]])
print(j)
print("dimensions=",j.ndim)
cx=np.array([[[0.5,0.4,0.3],[0.2,0.1,0],[1,2,3]]])
print(cx**2)
print("dimensions=",cx.ndim)
print()
z=np.array([[[0,2,4],[4,6,8],[1,3,5],[7,9,1.1]]])
print(z*z)
print("dimensions=",z.ndim)
print()
s=np.array([[[[0.10,0.9,0.8],[0.7,0.6,0.5],[0.4,0.3,0.2]]]])
print("dimensions=",s.ndim)
print()
# c=np.array([[1,2,3],[2,4,5],[3,4,6]]) #### err
# print(c[1]**2) ### o
# print(c.dtype) ### r
f=np.array([["array","versus","lists"]])
print(f.dtype)
o=np.array([[90,12,3],["strings","data","type"]])
print(o[0],o[0].dtype)
s=np.array([1,2,3])
d=np.array([4,5,6])
print(s/d)
p=np.array(range(5))
print(p,d.dtype)
print(
)
v=np.array([-3,-2,-1],ndmin=5)
print(v)
print(v.ndim)
print()
f=np.array([[10,20,90,]])
print(f.ndim)
print(

)
j=np.array([0.14,-9.214,-.94])
print(j.dtype)
print(

)
x=np.array([[9+2j,2.12,"kg"]])
print(x.dtype)
print()
o=np.arange(2,8)
print(o)
b=np.arange(8,2)
print(b)
c=np.eye(3)
print(c)
print()
# lines_space=np.linspace(1,15,num=2) #### ERR
# print(lines_space) #### OR
li=np.linspace(1,15,num=5)
print(li)
k=np.linspace(0,10,num=5)
print(k)
print(

)
k=np.arange(2,8)
print(k)
print(

)
x=np.linspace(5,10,num=8)
print(x,x.dtype)
print()
c=np.random.rand(5)
print(c,print())
s=np.array([[[{"a":"apple","quantity":[1,2,3],"banana":[10,20,30]}]]])
print(s)
o=np.array([[[1,2,3],[2,4,5],[3,5,6]]])
print(o)
q=np.array([{"c":"china","b":"byd","j":"japan","t":"toyota"}])
print(q,q.dtype)
print(q.ndim)
print()
# x=np.array([[{"a":"apple"},[{"k":"kilogram"},{"g":"grammer"}]]])
# print(x)
i=np.array([[[0.3,0.2,0.1],[-3,-2,-1],[3,2,1]]])
print(i)
print(i.ndim)
print(i.dtype)

o=np.linspace(1,5,num=4)
print(o,o.dtype,o.ndim)
print(

)
byd=np.random.rand(2,5)
print(byd,byd.ndim)
print(

)
k=np.random.randn(5)
print(k)
print()
c=np.random.randn(3)
print(c)
print(

)
cx=np.random.ranf(4)
print(cx[0],cx.dtype)
# a=np.random.randf(2,5)
# print(a[3],a.dtype)

e=np.array([1,2,3,4,5])
c=np.array([10,20,30,40,50])
j=e**c/5
print(j)
print(

)
h=np.array([1.23,89.44,8.34,13.1,7.45,8.42])
w=np.array([5.90,8.14,7.424,78.13,7.13,2.13])
fat=w/h**2
print(fat)
print()
k=np.array([1.32,"is",True])
print(k,k.dtype)
print()
t=[1,2,3]
g=np.array([10,20,30])
e=t+g
print(e,e.dtype)
print(type(e))
j=np.array([[1,9,88,842]])
print(j,j.dtype)
print(type(j))
print(

)

#####    "2/2/2025"     #############
# "B.....M.....I"
w=np.array([0.1,0.42,4.925,9.42,8.131])
h=np.array([9.23,9.84,9.14,14,11])
f=w**h/2
print(f)
print(f>=2)
print(f[f>5])
print(

)
ch=np.array([1,2,3,4,5])
cor=np.array([100,90,80,70,60])
res=ch**cor/2
print(res)
print(res>3)
print(res[res>3])
print(

)
w=np.array([1.994,9.45,8.42,9.23])
# print(np.shape(5))
f=w.shape
print(f)
print(

)
r=np.array([[1,3,5,7],[2,4,6,8]])
print(r)
f=r.shape
print(f)
print(

)
# f=np.array([["1.9","9.13","8.14","8.24"],["65.9","9.3","87.1","15.2"]]) ###
# print(f,f.dtype="<U32")
# print(f,f.dtype)
# d=np.array([[["1.9","9.13","8.14","8.24"],["65.9","9.3","87.1","15.2"]]],dtype="<U32")
# print(d)

f=np.array([["13.9","91.13","82.14","81.24"],["61.9","49.3","7.1","15.2"]])
print(f[0])
print(f[0][2])
print(f[0,3])
print(f[:,0:2])
print(

)
print(f[1,0:2])
print(

)
s=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(s)
# g=np.array(input("g: "))
# print(g)
# e=np.array([[[10,3983,9840,32],[10,9.24,2525,85],[9.3,902,9.144]]])
# print(e)
print()
w=np.array([[[1,2,3],[9,33,1],[1,9,341]]])
print(w.ndim)
print(

)
# s=np.array([[[1,2,3],[9,34,11],[100,3,2,4]]])
# print(s)
d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(d[d>2])
print(

)
ios=np.array([[90,3,42],[98,42,13],[977,42,14]])
print(ios)
print(list(map(lambda f:f%2==0,ios)))
# print(tuple(filter(lambda r:r%2==0,ios)))
print(

)
o=np.array([[[12,89,42],[23,89,53],[87,42,9845]]])
# print(f>=2)
# print(f[f>5])
print(o>=50)
print(o[o>=50])
print(

)
r=np.array([[[1,2,3,5],[40,3,2,12],[78,44,23,32]]])
print(r)
# print(r>40 and r<30)
print(r<25)
print(r[r<25])
# print(r)
print(

)
rog=np.array([[89.42,3.43,13.1],[9.3,2,9.31],[12.3,2,3.14]])
asus=np.array([[1.2,488,2.41],[9.3,5,4.31],[90.342,2.21,1]])
d=rog+asus//rog
print(d)
# print(d>0.5)
print(d>10)
print(d[d>10])
print(

)
# a=np.array([[[90,3,4,1],[1,4,52,2],[9,4,3,1]]])
# print(tuple(filter(lambda i:i%2==0,a)))
# y=np.array([[[1,9,4,2],[9,7,33,1],[1,9,38,83]]])
# print(list(sorted(y,key=lambda g:g)))
# o=sorted(y,key=lambda tom:tom)
# print(o[0][0][0][0])

# w=np.array([[1,8,4,2],[9,3,2,2],[9,3,5,7]])
# e=sorted(w,key=lambda lol:lol)
# print(e)

#####   "3/2/2025"  #####
r=np.array([[1,2,3],[2,3,4],[4,2,1]])
print(r,r.ndim)
print(r.shape)
print(

)
f=np.array([[[0.1,0.2,0.3,0.4],[1.1,1.2,1.3,1.4],[-1,-2,-3,-4]]])
print(f)
print(f.ndim)
print(f.shape)
print(

)
# x=np.array(["america","cuba","canada","mexico","panama"],dtype="S3")
o=np.array(["usa","china","russia","london"],dtype="S2")
print(o)
print(

)
# z3=z.astype("i")
# print(z3)
# h=h.astype("a")
# print(h)
# s=s.astype("o")
# print(s)
q=np.array([[1,2,3],[2,3,4],[4,5,6]])
print(q.shape)
u=np.array([[1,2,3],[2,3,4]])
print(u.shape)
l=np.array([[[10,20,30],[100,200,300],[1000,2000,3000]]])
print(l)
print(l,l.ndim)
print()
i=np.array([[1,2,3],[-1,-2,-3],[10,20,30]])
print(i)
print(i)
print(

)
d=np.array([["1","2","3"]])
q=d.astype("float")
print(q)
print(q.dtype)
print(

)
a=np.array([1,2,3,4,5,6])
print(a.reshape(3,2))
i=np.array([[[0.1,0.2,0.3,0.4],[1.1,1.2,1.3,1.4],[10,20,30,40]]])
print(i)
print(i.reshape(6,2))
print(i,i.ndim)
print(i.reshape(4,3))
print(

)
e=np.array([[1,2],[3,4]])
print(e.reshape(4,1))
print(

)
r=np.array([[[1,2,3],[0.9,8.5,9.2]]])
print(r.reshape(6,1))
print(r.size)
print(

)
w=np.array([[10,20,30,40,50]])
print(w.reshape(-1,1))
print(

)
d=np.array([[[1,2,3,4],[5,6,7,8]]])
print(d.reshape(4,2))
h=np.array([[[[]]]])
print(

)
u=np.array([[[1,2,3],[0.1,0.2,0.3],[90,190,984]]])
print(sum(u)/len(u))
print(u.dtype)
print(

)
o=np.random.randn(1,2)
print(o/len(o))
print(

)
######################################       NP.MEAN       ###################
w=np.array([[-10,-9,-8],[-5.1,-5.2,-5.1],[3,2,1]])
e=np.mean(w[:,0])
print(e)
print()
f=np.array([[1,3,5],[2,4,6],[7,9,11]])
p=np.mean(f[:,2])
print(p)
print()
#################################        NP.MEDIAN           ##############
e=np.array([[-3,6,-1,],[0,9,8],[7,6,5]])
r=np.median(e[:,2])
print(r)
y=np.array([[0.1,0.2,0.3],[1.1,1.2,1.3],[11,22,33]])
w=np.sort(y)
print(w)
print(

)
r=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(r.shape)
print(r.reshape(3,5))
print()
#####   d=np.empty((2,2,2))
# ####  print(d)
# ####  print(d.dtype,type(d))

# import random as rd
# y={1,2,3,4,5}
# g={10,20,30,4,1,5,6}
# c=y|g
# x=y.union(g)
# print(c)
# print(x)
# print(rd.shuffle(x))
# print(rd.choice(x))

####  "4/2/25"  ####
u=np.linspace(0.1,0.3)
print(u)
print()
#####   "CONVERT DATA TYPE INTO ANOTHER DATA TYPE" ####
d=np.array([[1,2,3],[3,2,1]])
print(d.dtype)
dd=np.array([[1,2,3],[3,2,1]],dtype=np.int8)
print(dd)
print(dd.dtype)
print(
)
e=np.array([1,2,3,4,5,6])
print(e.reshape(2,3),e.dtype)
r=np.float32(e)
print(r.dtype)
print(
)
r=np.array([[-1,-2,-3],[-5,-4,-3]])
u=r.astype(float)
print(r.dtype)
print(u.dtype)
print(
)
qe=np.array([1,2,3,4,5,6])
s=qe.reshape(3,2)
print(qe,qe.ndim)
print(s,s.ndim)
print(
)
f=np.array([[-10,-8,-6],[-3,-2,-1]])
print(f.reshape(-1,1))
print(f.reshape(1,-1))
print(f.reshape(-3,1))
print(f.reshape(1,-3))
print(
)
o=np.array([[2,4,6],[3,6,9]])
print(o[0]+o[1])
print(*o)
print(o[0,:2]*o[1,:2])
print(
)

# ar=np.array([[[9,94],[1,39],[9,86]]])
# print(ar.shape(1,3,2))

e=np.array([[1,2],
            [4,0],
            [3,1]])
print(e.reshape(1,-1))
print(e.ndim)
print(e,e.dtype)

hf=np.array([[109,98,42],
            [97,984,4],
            [2,32,1]])
a=np.mean(hf[:,1])
print(a,a.dtype)
print()

print(" INDEXING AND SLICING  in 1-d and 2-d ARRAY")
print()
g=np.array([[1,3,5],
            [2,4,6],
            [7,8,9]])
print(g[0:2,0])
print()
fd=np.array([[1,3,5,7,9],
              [-1,-2,-3,-0.2,1],
              [-10,-9,-8,-6,4]])
print(fd[0:2,1])
print(fd[0:2,2])
print(fd[0:2,3])
print(fd[0:2,4])
# print(fd[0:3,1:3])
print(fd[-1,0])
print(fd[-2,0])
print(fd[-3,0])
print(fd.reshape(5,3))
print()

#### 5/5/25 #####

l=np.array([[-0.1,-0.2,-0.3,-0.4,-0.5],
             [0,1,2,3,4],
             [10,20,30,40,50],
            [100,200,300,400,500],
            [4,5,6,7,8],
            [70,80,90,100,101],
            [2.1,2.2,2.3,2.4,2.5]])
print(l,l.ndim)
print(l,l.ndim)
print(l.shape)
print(l[1:3,2])
print(l[-1:,1])
print(l[0:4,3])
print(l[0:,4])
print(l[-2,:3]) ######  NEW METHOD  #####
print(l[-2,:4])
print(l[-6:,0])
print(l[-7:,2])
print(l[-7:-3,4])
# print(l[-2:,3])
# f=[1,2,3,4,5,6,7,8,9,10]
# print(f[-1:-6])
print()
p=np.array([[[1,2,3,3.3,4.4],
             [4,5,6,7,8]],

             [[7,8,9,100,110],
              [10,11,12,13,14]]])
print(p,p.ndim)
print(p[1,0,0:2])
print(p[1,1,1])
print(p[0,0,0:2])
print(p[1,0,0:4])
print(p[0,1,0:3])
print(bin(int((p[0,1,1]))))
print(complex(p[1,0,2]))
print()

t=np.array([[[0.01,0.02,0.03,0.04,0.05],
             [0.1,0.2,0.3,0.4,0.5],
             [-0,-1,-2,-3,-4]],

             [[1,2,3,4,5],
             [1.1,2.2,3.3,4.4,5.5],
             [100,200,300,400,500]]])
print(type(t),t.ndim)
print(t[0,2,0:4])
print(t[1,1,-4:])
print(t[0,1,3],t[0,2,3])
print(t[0,0,2]and[0,1,2])
print(t[0,2,3]+[0,1,-2]) ####  NEW METHOD + ####
print(t[0,0,2],[1,2,2])
print(t[0,0,2]+[1,2,2])
print(t[1,1,2])
print()

s=np.array([[[[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,11,12],
              [13,14,15],
              [16,17,18],
               [100,200,300],
                [400,500,600],
                [700,800,900]]]])
print(s,s.ndim)
print()
sr=np.array([[[[1,2,3],
              [4,5,6],
              [7,8,9]],

              [[10,11,12],
              [13,14,15],
              [16,17,18]],

               [[100,200,300],
                [400,500,600],
                [700,800,900]]]])
print(sr[0,0])
print(sr[0,0,2,1])
print(sr[0,1,1,1])
print(sr[0,2,0,1])
# print(sr[0,0,0,0],[0,1,0,0],[0,2,0,0])
print(sr[0,0,0,0],sr[0,1,0,0],sr[0,2,0,0])
print(sr[0,0,0,2],sr[0,1,0,2],sr[0,2,0,2])
print(sr[0,0,0,0],sr[0,1,0,2],sr[0,2,0,2])
print(sr[0,0,0,0],sr[0,0,1,1],sr[0,0,2,1],sr[0,1,0,1],sr
      [0,1,1,2],sr[0,1,2,2],sr[0,2,0,2],sr[0,2,1,2],sr[0,2,2,1])
print()
### 6/2/25 ###
z=np.array([[[[100,200,300,2,3],
              [1,2,3,4,5],
              [110,120,130,140,150]],

              [[10,20,30,40,50],
             [60,70,80,90,100],
             [100,102,104,106,108]],

            [[1000,2000,3000,4000,5000],
             [10,30,50,70,90],
             [0,20,40,60,80]],

             [[0.1,0.2,0.3,0.4,0.5,],
             [1.1,1.2,1.3,1.4,1.5],
             [2,4,6,8,10]]]],dtype="U")
print(z.shape,z.ndim)
print(z[0,0,0,0])
print(z[0,1,1,2])
print(z.dtype)
print(z)
print(z[0,2,0,1])
print(z[0,1,1:3,2])
print(z[0,3,0:3,1])
print(z[0,0,2,2])
print(z[0,1,2,3]+z[0,3,0,2])
print(z[0,1,1,2]>z[0,2,0,1])
# print(z.reshape(1,60))
# print(z.reshape(4,15))
print(z.reshape(2,30))
# print(z.reshape(5,12))
# print(r.reshape(2,30))
print()

###   "7/2/25"  ###
 ### 2-D SHAPE shaping and indexing
r=np.array([[1,2,3,4,5],
             [6,7,8,9,10],
             [11,12,13,14,15],
             [16,17,18,19,20],

             [0.1,0.2,0.3,0.4,0.5],
              [1.1,1.2,1.3,1.4,1.5],
              [2.1,2.2,2.3,2.4,2.5],
              [3.1,3.2,3.3,3.4,3.5],

              [1,3,5,7,9],
               [11,13,15,17,19],
               [2,4,6,8,10],
               [12,14,16,18,20]])
print(r,r.ndim,r.shape)
print(r[0])
print(r[0:4,1])
print(r[0:3,3])
print(r[4,1])
print(r[5:10,3])
print(r[-7:-1,0])
print(r[-13:-4,4])
print(r.ndim)
print(
)
# g=np.array([[1,2,3],
#              [4,5,6],
#              [10,11,12],
#              [13,14,15],
#              [16,17,18]],
#
#              [[100,200,300],
#             [400,500,600],
#             [700,800,900],
#             [1000,2000,3000],
#             [10,30,50]]],
#
#             [[1,3,5],
#             [2,4,6],
#             [8,9,10],
#             [12,14,16],
#             [20,22,24]])
# print(g[0,0,2,0])


#### 3-D SHAPE shaping and indexing ####
g=np.array([[[1,2,3],
             [4,5,6],
             [10,11,12],
             [13,14,15],
             [16,17,18]],

            [[100,200,300],
            [400,500,600],
            [700,800,900],
            [1000,2000,3000],
            [10,30,50]],

            [[1,3,5],
            [2,4,6],
            [8,9,10],
            [12,14,16],
            [20,22,24]]])
print(g,g.ndim,)
print(g.shape)
print(g[0,2,1])
print(g[0,0:4,0])
print(g[1,0:3,1])
print(g[1,2,0])
print()
print(g[2,0:3,1])
print(g[-2,-4:-1,1])

# a=np.array([[[10,20,30],
#            [40,50,60],
#            [12,14,16],
#            [11,13,15]],
#
#             [[0,2,4],
#             [6,8,10],
#             [12,124,36],
#             [10,30,21]],
#
#             [[100,200,300],
#             [400,500,600],
#             [700,800,900],
#             [1000,2000,3000]]])
#
# print(a,a.ndim)

####  8/2/25  ####
r=np.array(["1","2","3"])
print(r.astype("complex"))
print()
# z=np.array([1+2j,3+2j,9+8j])
# print(z,z.dtype)
# print(z.astype("float"))
print()
f=np.array([[1,2,3],[10,20,30]])
print(f,f.ndim)
a=f.reshape(1,6)
print(a,a.ndim)
print(f.reshape(3,2))
print(f.reshape(1,-1))
print(f.reshape(-1,1))
print()

p=np.array([[1,2,3,4,5,6]])
# print(p.reshape(2,3),order="F")
d=p.reshape((3,2),order="F")
print(d)
print()
k=p.reshape((2,3),order="F")
print(k)
o=p.reshape(1,2,3)
print(o)
print()

e=np.array([[[0,0.1,0.2,0.3]]])
o=e.reshape((2,2),order="F")
print(o)
print()
j=np.array([[[1,2,3,4,5,6,7,8,9,10]]])
i=j.reshape((2,5),order="F") #### SLEEPING ORDER #####
print(i)
# print(j.reshape(5,2),order="c")
d=j.reshape((5,2),order="C") #####  STANDING ORDER  #####
print(d)
print()
# c=j.reshape((1,10),order="F")
# cj=j.reshape((1,10),order="C")
# print(c)
# print(cj)
# print()
# cs=j.reshape((2,5),order="F")
# cs_1=j.reshape((2,5),order="C")
# print(cs)
# print(cs_1)

"HOW TO get EVEN AND ODD NUMBERS FORM NUMPY ARRAY in SLEEPING & STANDING ORDER."
q=np.array([[[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.10,0.11,0.12]]])
w=q.reshape((2,6),order="F")
e=q.reshape((4,3),order="C")
print(w)
print(e)
print()

g=np.array([[1.0,1.1,1.2,1.3],
            [1.11,1.12,1.13,1.14]])
o=g.reshape((4,2),order="F")
print(o)
print()
# v=np.array([1,3,5,7], ###  1-D ARRAY  ###
#              [2,4,6,8],
#              [9,11,13,15],
#              [17,19,21,23])
# print(v.ndim,v.shape)
# c=v.reshape((2,4))
# print(c)
# ujjain-chitrkot-pragyaraj-
# c=np.array([[1,3,5,7],  ###  2-D ARRAY  ###
#              [2,4,6,8]],
#
#              [[9,11,13,15],
#              [17,19,21,23]])
# print(c.ndim)
# print(cv.ndim)
cv=np.array([[[1,3,5,7],  ###  3-D ARRAY  ###
             [2,4,6,8]],

             [[9,11,13,15],
             [17,19,21,23]]])
print(cv.ndim,cv.shape)
# print(cv.reshape(2,8),order="F")
o=cv.reshape((8,2),order="F")
print(o)
p=cv.reshape((2,8),order="C")
print(p)
print()

s=np.array([[[[100,200,300], ## 9*2 ##
              [400,500,600],
              [700,800,900]],

              [[100,110,120],
              [130,140,150],
              [160,170,180]]]])
print(s.ndim)
# x=s.reshape((3,5),order="F")
# print(x)
v=s.reshape((6,3),order="C")
print(v)
z=s.reshape((2,9),order="F")
print(z)
print()

cub=np.array([[[[0,2,4,6], ## 12*3
                [1,3,5,7],
                [8,10,12,14],

               [9,11,13,15],
               [16,18,20,22],
               [17,19,21,23],

               [24,26,28,30],
              [25,27,29,31],
              [32,34,36,38]]]])
print(cub.ndim)
d=cub.reshape((9,4),order="F")
print(d)
o=cub.reshape((3,6,2),order="C")
print(o)
ne=cub.reshape((3,6,2),order="C")
print(ne)
k=cub.reshape((2,6,3))
print(k)
print()
# s=cub.reshape((1,-2),order="F")
# print(s)
# sc=cub.reshape((1,-2),order="C")
# print(sc)
# scu=cub.reshape((3,-6,2),order="F")
# print(scu)
g=np.array([[[[10,20,30],
              [11,12,13],
              [14,15,16],

             [17,18,19],
             [20,21,22],
            [23,24,25]]]])
print(g.ndim)
print(g.shape)
x=g.reshape((9,2),order="F")
print(x)
k=g.reshape((2,9),order="C")
print(k)
print()
# i=g.reshape((-4,2),order="F")
# print(i,i.ndim,i.shape)
# print()
i=np.array([[1,2,3],
             [1.100,1.200,1.300],
            ["strings","arrays","lists"],

             [1.10,1.12,1.14],
             ["cars","codes","bikes"],
             ["100","200","300"]])
print(i.ndim,i.shape)
c=i.reshape((2,9),order="C")
print(c)
o=i.reshape((6,3),order="F")
print(o)
print()
print(i[0:3,1])
print(i[3:6,1])
print()
k=np.array([[[[1,2,3],
              ["a","b","c"],
              [10,20,30],
              [2,4,6],

              [11,13,15],
              [17,19,21],
              ["e","f","g"],
              [8,10,12],

              [5,10,15],
              [20,25,30],
              ["h","i","j"],
              [14,16,18]]]])
print(k.ndim,k.shape)
print(k[0,0,2])
# print(k[-1,2]) ##### problem #####
# print(k[0])
r=k.reshape((6,2,3),order="F")
print(r)
print()

### 9/2/25 ###


t=np.array([["str","list"],
            ["dict","set"],

            ["one","two"],
            ["bikes","cars"],

            ["stones","bricks"],
            ["shoes","sandals"]])
print(t.ndim,t.shape)
u=t.reshape((4,3),order="F")
print(u)
# k=t.reshape((6,2),order="C")
# print(k)
c=np.array([[["ones"],
             ["twos"],

             ["threes"],
             ["fours"],

             ["fives"],
             ["sixes"]]])
print(c.ndim)
a=c.reshape((2,3),order="F")
print(a)
print()
l=np.array([1,2,3,4,5,6])
i=l.reshape((2,3),order="F")
print(i)
print()
j=l.reshape((2,3),order="C")
print(j)
print()
o=np.array([[[1,3],[2,4],[5,7],[6,8]]])
print(o.shape,o.ndim)
c=o.reshape((2,2,2),order="F")
print(c)
print()
j=o.reshape((2,2,2),order="C")
print(j)
print()

y=np.array([[1.1,1.2],
            [2.1,2.2]])
o=y.reshape(1,4)
print(o)
p=y.reshape(4,1)
print(p)
print(y.size)
# p=y.reshape(y.size,1)
# print(p)
print()
p=np.array([10,30,50,70,90,110])
i=p.reshape(3,2)
print(i)
print(i[2,1])
print()
u=np.array([[1,3,5,7,9],
            [11,13,15,17,19],
            [21,23,25,27,29],
            [31,33,35,37,39],
            [41,43,45,47,49]])
print(u.ndim)
print(u[0:3,2])
print(u[-3:-1,-2])
print(u[-3:,-1])
print(u[0:5,-5])
print(u[3:6,2])
print()
p=np.array([[[2,4,6,8,10],
             [12,14,16,18,20]],

             [[22,24,26,28,30],
              [32,34,36,38,40]],

              [[42,44,46,48,50],
               [0,0.1,0.2,0.3,0.4]]])
print(p.ndim)
print(p[0])
print(p[1])
print([2])
print(p[0,0:2,2])
print(p[1,-2:,0])
print(p[2,-2:,-2])
print()
# k=np.array([[[[1,2,3],
#               [4,5,6],
#               [7,8,9],
#
#               [[10,11,12],
#                [13,14,15],
#                [16,17,18],
#
#                [[1,3,5],
#                [7,9,11],
#                 [13,15,17]]]]]])
# print(k.ndim)
k=np.array([[[[1,2,3],
              [4,5,6],
              [7,8,9]],

              [[10,11,12],
               [13,14,15],
               [16,17,18]],

               [[1,3,5],
               [7,9,11],
                [13,15,17]]]])
print(k.ndim)
print(k[0,0,0:3,0])
# c=k([0,0,0:3,0],order="F")
print(k[0,1,0:3,2])
print(k[0,2,-3:,-1])
print()

####   "BOOLEN MASK INDEXING" ####
ios=np.array([2,4,5,19,924,231])
print(ios%2==0)
# k=list(filter(lambda l:l%2==0,ios))
# print(k)
maask=(ios%2==0)&(ios%4==0)
print(maask)
print()
####   "10/2/25"  ####
g=np.array([[[[1,2,3,4,5],
              [10,90,97,984,4],
              [987,45,97,3,33],
              [9088,32,8,42,2]]]])
print(np.sqrt(g[0]))
# print(np.exp(g))
print(np.sign(g))
print(np.absolute(g))
print(np.max(g))
print(np.min(g))
print()
f=np.array([[[[10,20,30,40],
              [100,200,300,400]],

              [[-1,3,-5,7],
              [-2,4,-6,8]]]])
print(f.ndim)
print(f[0,1])
print(np.sign(f[0,1]))
print(np.sqrt(f[0,0,1]))
# print(np.sqrt(f[0,1,0]))
# print(np.power(f,g))
# print(np.logical_or(g))
l=np.arange(0,10,2.5)
print(l)
print(np.sum(l))
print(np.mean(l))
# print(np.arange(0,10,1.5)
print()
j=np.arange(0,10,0.5)
print(np.mean(j),j.ndim)
# print(np.arange(>=5.1))
b=np.linspace(0,0.5,20)
print(b)
o=np.linspace(0,20,1)
print(o)
c=np.linspace(0,1,20)
print(c)
u=np.linspace(0,1,10)
print(u)
o=np.linspace(0,1,11)
print(o)
l=np.linspace(2,20,10)
print(l)
print(np.median(l))
print(np.mean(l))
# print(np.mode(l))
print(np.linspace(0,2**np.pi,10))
print()
#####    "identity matrix"   ####
y=np.eye(3,3)
print(y)
d=np.eye(4,4)
print(d)
print()
# l=np.eye(-4,-4)
# print(l)
o=np.eye(5,5,dtype=complex)
print(o)
print()
y=np.eye(3,2,dtype="F")
print(y)
print()
# print(np.eye(4,2),dtype=float)
a=np.eye(3,4,dtype=float)
print(a)
print()
o=np.eye(1,3)
print(o)
print()
y=np.eye(3,6,order="F")
print(y)
print()
x=np.array([[1,2,3],[2,4,6],[1,3,5]])
print(x.shape)
print()
n=np.linspace(0,20,2)
print(np.sum(n))
# print(np.mean(n[:,2]))
print(np.mean(n))
print()
j=np.random.randn(10)
print(j)
# o=np.random.random_sample(j)
# print(o)
print()
# i=np.random.randn(5)
# mass=i>5
# print(mass)
# print(o)
l=np.array([99,87,628,64,79,898,87,7])
b=np.array([89,37,53,727,53,85,39,7])
ara=l*b*2
print(ara)
print(ara>10000)
print(ara[ara>10000])
# z=np.unique_counts(ara[ara>10000],bool=True)
# print(z)
print()

x=np.array([[[[1,3,5],
              [7,9,11],
              [13,15,17]]]])
print(np.linspace(x,5))
print()

f=np.array([[[[[1,2,3,4,5],
               [1,3,5,7,9],
               [11,13,15,17,19],
               [21,23,25,27,29],
               [2,4,6,8,10]]]]])
print(f.ndim)
print(f[0,0,0,0:4,1])
ff=np.mean(f[0,0,0,0:5,2])
print(ff)
print()

d=np.array([[[1,2,3],
             [4,5,6]],

             [[1.1,1.3,1.5],
              [2,4,6]],

              [[2.2,2.4,2.6],
            [3.1,3.3,3.5]]])
print(d.ndim)
print(d[0,0:2,1])
x=d.reshape((9,2),order="F")
print(x)
# a=np.reshape(d(3,2,3),order="F")
# print(a)
####### print(d.reshape((2,1,9),order="F"))
# print(d.reshape((1,2,9),order="C"))
print()
c=np.eye(4,2)
print(c)
print()
c=np.array([[[1,3,5,7],
            [0,2,4,6],

            [9,11,13,15],
             [8,10,12,14]]])
print(c.ndim)
print(c[0,0]>5)
print(c[0,0]>5)
print(c[c>5])

###   "11/2/25"   ###

k=np.array([[1,2,3],
          [1,3,5]])
print(k.shape)
print(k.ndim)
print()
# v=np.array([0.1,0.2,0.3,0.4,0.5,0.6],ndim=2)
s=np.array([[[1,3,5],
             [2,4,6]],

             [[7,9,11],
             [8,10,12]],

            [[14,16,18],
             [13,15,17]]])
print(s.ndim)
print(s.shape)
mask=(s[0]%2==0)
print(mask)
mask=(s[1]%4==0)
print(mask)
print()
# k=(s[0]%2==0 and s[2]%5==0)
# print(k)
b=np.array([[32,32,42,321,244,3,5]])
mask=(b%3==0)
# mask=(b%2==0) and (b%5==0)
print(b[mask])
print()
k=np.array([[[-9,-3,-8,-14,-942,252,32]]])
h=(k%2==0)&(k>0)
print(k[h])
print()
i=np.array([14,9,43,232,23])
v=(i%2==0)|(i%5==0)
print(v,i[v])
print()

g=np.array([[10,985,46,2,43,6,22,35,23,34]])
j=np.array([[98,43 ,35,83,97,57,24,13,21,1]])
b=g**j/2
print(b)
print(b>3)
print(b[b>3])
print()
print(b>=3)
print(b[b>=3])
print()

kite=np.array([[[1,2,3],
                [4,5,6],

                [7,8,9],
                [10,11,12],

                [13,14,15],
                [16,17,18]]])

print(kite[0,2])
print(kite.ndim)
print()

kite=np.array([[[1,2,3],
                [4,5,6]],

                [[7,8,9],
                [10,11,12]],

                [[13,14,15],
                [16,17,18]]])
print(kite[1])
print(kite.ndim)
print()

kite=np.array([[[[1,2,3],
                [4,5,6]],

                [[7,8,9],
                [10,11,12]],

                [[13,14,15],
                [16,17,18]]]])
print(kite[0,0])
print(kite.ndim)
print()

cuba=np.array([[[0.100,0.200,0.300],
                [0.1,0.2,0.3],

                [11,12,13],
                [2.1,2.2,2.3],

                [3.1,3.2,3.3],
                [4.1,4.2,4.3]]])
print(cuba.reshape((9,2),order="C"))
print()
print(cuba.reshape((9,2),order="F"))
print()
# print(cuba.reshape((3,3,2),order="C"))
print()
# print(cuba.reshape((3,2,3),order="F"))
i=np.array([[1,2,3,4,5,6,7,8]])
print(i.reshape(2,2,2))
print()
g=np.array([[[100,200,300,400,500],
             [-1000,-800,-600,-400,-200],
             [1,10,11,21,23],
             [10,30,50,70,90]]])
print(g.ndim)
print(g.size)
print(g.reshape(10,1,2))
print()
o=g.reshape((10,2,1),order="F")
print(o)
print()
b=g.reshape((2,5,2))
print(b)
print(b[0,0:5,1])
print()
i=g.reshape(10,2)
print(i)
print()

# k=np.array([[[[1,2,3],
#               [1.1,1.2,1.3],
#
#               [[1,3,5],
#                [2.1,2.2,2.3]],
#
#                [[2,4,6],
#                [3.1,3.2,3.3]],
#
#                [[8,10,12],
#                 [4.1,4.2,4.3]],
#
#                 [[7,9,11],
#                  [5.1,5.2,5.3]]]]])
# print(k.ndim)

k=np.array([[[[1,2,3],
              [1.1,1.2,1.3],

              [1,3,5],
               [2.1,2.2,2.3],

               [2,4,6],
               [3.1,3.2,3.3],

               [8,10,12],
                [4.1,4.2,4.3],

               [7,9,11],
                 [5.1,5.2,5.3]]]])
print(k.ndim)
print(k.size)
o=k.reshape(5,3,2)
print(o)
print(o[0:5,1])
print()
print(o[-5:-2,-3])
print()

klm=np.array([[[100,200],
               [11,12],

               [300,400],
               [13,14],

               [500,600],
               [15,16]]])
print(klm.size)
v=klm.reshape(2,3,2)
print(v)
print(v[0])
print(v[0,0:3,1])
print()
print(v[0,0:3,1]*v[0,0:3,0])
print()
# j=klm.reshape((2,2,3),order="C")
# print(j)
# print(klm.reshape((2,2,3),order="F"))
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(x.size)
print()
o=x.reshape((2,2,3),order="F")
print(o)
l=x.reshape((2,2,3),order="C")
print(l)
print()

# f=np.array([[[0,0.1,0.2,0.3,0.4],
#               [1,3,5,7,9],
#               [11,13,15,17,19],
#               [21,13,14,15,13]],
#
#               [[1,3,5,7,9],
#               [11,13,15,7,19],
#               [21,23,25,27,29],
#               [31,33,35,37,39]],
#
#               [[0,2,4,6,8],
#               [10,12,14,16,18],
#               [20,22,24,26,28],
#               [30,32,34,36,38]]])
# print(f.ndim)
# print(f[0,0],f[0,1],f[0,2],f[0,3])

h=np.array([
    [[1,2,3],
     [4,5,6],
     [7,8,9]]
])

print(h.ndim)
b=np.array([
    [[0.1,0.11,0.111],
     [0.2,0.22,0.222],
     [0.3,0.33,0.333]],

     [[1,2,3],
      [11,22,33],
      [10,20,30]],

      [[100,200,300],
       [100.10,200.20,300.30],
       [1000,2000,3000]]])
print(b[0])
print(b.shape)
print()

b=np.array([[[1,2,3], ####  3-D ARRAY  ####
             [2,3,4]],

             [[10,20,30],
              [100,200,300]],

              [[101,102,103],
               [1.1,1.2,1.3]]])
print(b.ndim)
# print(b[0])
# print(b[0,0])
# print()
ball=np.array([[[[1,2,3], ####  4-D ARRAY  ####
              [4,5,6],

              [7,8,9],
              [10,11,12],

              [13,14,15],
              [16,17,18]]]])
print(ball.ndim)
# print(ball[0])
# print(ball[0,0,0])
print()
bat=np.array([[[[[-3,-2,-1], ####  5-D ARRAY  ####
                 [0,1,2]],

                 [[10,9,8],
                   [7,6,5]],

                   [[4,3,2],
                     [2,1,0]]]]])
print(bat.ndim)
print()
# print(bat[0])
# print(bat[0,0,0])

####   "12/2/25"   ####
f=np.array([[[[[1,2,3,4,5,6],
               [7,8,9,10,11,12],
               [13,14,15,16,17,18]],

               [[0.1,0.2,0.3,0.4,0.5,0.6],
                [1.1,1.2,1.3,1.4,1.5,1.6],
                [2.1,2.2,2.3,2.4,2.5,2.6]],

                [[3.1,3.2,3.3,3.4,3.5,3.6],
                 [4.1,4.2,4.3,4.4,4.5,4.6],
                 [5.1,5.2,5.3,5.4,5.5,5.6]],

                 [[10,20,30,40,50,50],
                  [1,3,5,7,9,11],
                  [0,2,4,6,8,10]]]]])
print(f.ndim)
print(f.shape)
print(f.size)
o=f.reshape(3,3,8)
print(o)
p=f.reshape((9,8),order="C")
print(p)
print()
i=f.reshape(2,6,6)
print(i)
o=f.reshape((6,2,6),order="C")
print(o)
u=f.reshape(3,6,4)
print(u)
j=f.reshape((2,9,4),order="C")
print(j)
k=f.reshape((3,6,4),order="F")
print(k)
# print(f[0,0,0])
# print(f[-1,-1,-4:-2,0])
# print(f[-1,-1,-4:-2,0,1])
print()

e=np.array([[[1,2,3],
             [4,5,6],
             [7,8,9]],

            [[10,11,12],
             [14,15,16],
             [17,18,19]],

            [[10,30,50],
             [70,90,110],
             [1,3,5]],

            [[2,4,6],
             [8,10,12],
             [14,16,18]]])
print(e.ndim)
print(e.size)
print(e.shape)
ele=e.reshape(2,6,3)
print(ele)
u=e.reshape((3,4,3),order="F")
print(u)
r=e.reshape(3,6,2)
print(r)
i=e.reshape(2,9,2)
print(i)
print(i) ####
# print(e[0])
# print(e[-4:-2,0])
# print()
print()

o=np.array([10,30,50,70,90])
print(o[0:2])
print(o[-4:-1])
print()

q=np.array([
    [1,3,5],
    [2,4,6],
    [10,20,30]
])
print(q[2,2])
print(q[0:3,0])
print(q[0,0:2])
print(q[0:2,0:2])
print(q[-3:-1,-3])
print(q[-3:-1,-2])
print()

r=np.array([
    [1.1,1.2,1.3,1.4],
    [2.1,2.2,2.3,2.4],
    [3.1,3.2,3.3,3.4],

    [1,3,5,7],
    [9,11,13,15],
    [2,4,6,8],
    [10,12,14,16]

])
print(r.ndim)
print(r[0:4,0:2])
print(r[-7:,-2])
print(r[-6:-1,-4])
print(r[5:8,3])
print(r[4:7,0:3])
print(r[4:6,-2:])
print(r[-1,-1])
print()

qw=np.array([[1,2,3,4],[10,20,30,40],[90,10,1,13]])
print(q.ndim)

c=np.array([[1,2,3],
            [8,10,12],

           [10,20,30],
            [1,3,5],

            [40,30,21],
           [100,200,300]])
print(c.ndim)
print(c[0])
print(c)

rare=np.array([[[[1,2,3],
                 [1,3,5]],

                 [[10,20,30],
                  [1,11,21]],

                  [[1,3,5],
                   [20,40,60]]]])
print(rare.ndim)
# print(rare[0])
# print(rare[0,1])
# print(rare[0,2])
# print(rare[-1])
# print(rare[-1,-1])
# print(rare[-1,-2:])
# print(rare[-1,-3,-2])
# print(rare[-1,-2])
print(rare[0,1:3,0:2,0:2])
# print(rare[])
print()

res=np.array([[[[[0.1,0.2,0.3],
                  [1.1,1.2,1.3]],

                 [[1,3,5],
                  [2,4,6]],

                  [[10,30,50],
                   [100,300,500]]]]])
print(res.ndim)
# print(res[0,0,0:3])
# print(res[0,0,1:3,0,0:2])
print(res[-1,-1,-3:-1,-2,0:2])

c=np.array([
    [[1,2],
     [3,4]],

    [[5,6],
     [7,8]],

    [[10,20],
    [10,21]],

    [[1,3],
     [2,4]]
])
print(c.ndim)
print(c[0])
print()
ck=np.array([[
    [[1,2],
     [3,4]],

    [[5,6],
     [7,8]],

    [[10,20],
    [10,21]],

    [[1,3],
     [2,4]]
]])
print(ck.ndim)
# print(ck[0])
# print(ck[0,0:3,0,1])
# print(ck[0])
# print(ck[0,0:4,0:2,1])
print(ck[-1,-4:-1,-2:,-1])
print()

print("13/2/25")

d=np.array([[[[10,20,30],
              [1,3,5]],

             [[2,4,6],
              [100,200,300]],

             [[7,9,11],
              [13,15,17]],

             [[8,10,12],
              [14,16,18]],

             [[20,40,60],
              [80,100,120]]]])
print(d.ndim)
# print(d[0,0:3,0:2,0:2])
print(d[-1,-5:-2,-2:,-1])
print(d[-1,-3,-1,-1])
print(d[-1,-3:,-2:,-2:])
print()

t=np.array([[[[[1,2,3],
              [10,20,30]],

              [[100,200,300],
               [500,600,700]],

              [[1,3,5],
               [2,4,6]],

              [[10,30,50],
               [20,40,60]]]]])
print(t.ndim)
print(t[0,0,0:3,0:2,1:3])
print(t[-1,-1,-3:-1,-2:,-2])
print(t[-1,-1,-2:,-2,-2])
print(t[-1,-1,-3,-2,-2]>500)
print(t[t[-1,-1,-3,-2,-2]>500])
print(t[-1,-1,-3,-1,-1]>500)
mask=(t%2==0)
print(mask)
# print(t[t-1,-1,-3,-1>500])
# print(t[-1,-1,-3,-1,-1>500])
print()

# f=np.array([[1,3,5,7,10]])
# print(f[0>0])
# print([f[0>0]])
# print(f[0]>0)
# print(f[f>0])
# print(f[0]>0)
# print(f[f>0])
# print()

emp=np.empty((4,4))
print(emp)
print()

h=np.array([
    [1,2,3],
    [4,5,6],
    [0,10,10]
])
o=np.sum(h)
print(o)
l=np.sum(h,axis=1)
print(l)
p=np.sum(h,axis=0)
print(p)
print()

j=np.array([[[0.1,0.3,0.5],
            [1,3,5],
             [11,13,15],
              [110,130,150]],

            [[0.2,0.4,0.6],
             [2,4,6],
             [20,40,60],
             [200,400,600]],

            [[10,30,50],
             [100,300,500],
             [0.10,0.30,0.50],
             [0.100,0.300,0.500]]])
print(j.ndim)
ps=np.sum(j,axis=0)
print(ps)
psp=np.sum(j,axis=1)
print(psp)
flop=np.sum(j,axis=2)
print(flop)
print()

r=np.array([[[[100,200,300],
              [10,20,30]],

             [[1,2,3],
             [4,5,6]],

             [[0,20,40],
              [10,30,50]]]])
print(r.ndim)
print(r.shape)
# print(np.sum(r,axis=0))
# print(np.sum(r,axis=1))
print(np.sum(r,axis=3))
print()

e=np.array([[[[[1,2,3],
               [4,5,6]],

              [[10,11,12],
               [13,14,15]],

              [[1.0,2.3,2.4],
               [9.4,9.4,22]]]]])
print(e.ndim)
# print(np.sum(e,axis=0))
# print()
# print(np.sum(e,axis=1))
# print()
# print(np.sum(e,axis=2))
# print()
# print(np.sum(e,axis=3))
# print()
# print(np.sum(e,axis=4))
# print()
# print(np.sum(e,axis=5))
print()

f=np.array([[[[[1,2,3],
               [4,5,6]],

              [[10,20,30],
               [100,200,300]],

              [[2,4,6],
               [1,3,5]]]]])
print(f.ndim)
print(f.shape)
print(f.size)
print(np.sum(f,axis=3))
print()
print(np.sum(f,axis=4))
print()
# print(np.sum(f,axis=5))
# print()
# print(np.sum(f,axis=5))
# print()

fk=np.array([[[[[[[1,2,3],
               [4,5,6],
               [7,8,9]],

              [[10,20,30],
               [100,200,300],
               [2,4,6]],

              [[2,4,6],
               [1,3,5],
               [7,9,11]]]]]]])
print(fk.ndim)
o=np.sum(fk,axis=5)
print(o)
op=np.sum(fk,axis=6)
print(op)
# print(np.sum(fk,axis=5))
print()

kp=np.array([[[[[[[[1,2,3],
               [4,5,6],
               [7,8,9]],

              [[10,20,30],
               [100,200,300],
               [2,4,6]],

              [[2,4,6],
               [1,3,5],
               [7,9,11]]]]]]]])
print(kp.ndim)
# print(np.sum(kp,axis=5))
# print()
# print(np.sum(kp,axis=0))
# print(np.sum(kp,axis=1))
# print(np.sum(kp,axis=5))
# print(np.sum(kp,axis=6))
# print(np.sum(kp,axis=7))

kpi=np.array([[[[[[[[1,2],
               [3,4]],

              [[5,6],
               [7,8]],

              [[9,10],
               [11,12]]]]]]]])
print(kpi.ndim)
# print(np.sum(kpi,axis=5))
print(np.sum(kpi,axis=6))
print(np.sum(kpi,axis=5))
print()
print(np.sum(kpi,axis=7))
print()

kpi=np.array([[[[[[[[[1,2,3], ##6
               [3,4,5], ##12
               [6,7,8]],##21

              [[5,6,7],##!8
               [7,8,9], ##24
               [10,11,12]],##33

              [[9,10,11],##30
               [11,12,13],##36
               [14,15,16]]]]]]]]]) ##45
print(kpi.ndim)
print(np.sum(kpi,axis=7))
print()
print(np.sum(kpi,axis=8))
print(kpi[0,0,0,0,0,0,1,0:3,1])
print(kpi[-1,-1,-1,-1,-1,-1,-2,-3:,-1])
print()
g=np.array([[1,2,3,4,5,6,7,8,9,10]])
print(g[0,1::2])
# print(g.reshape(2,1,5),order="F")
# l=g.reshape((2,1,5),order="C")
# print(l)
print(np.linspace(g,3))

print('15/2/25')

# n=np.arange((2,10),order="F")
nk=np.arange((10),dtype="int")
print(nk)
print()

k=np.array([[[1,2,3,4,5],
             [1.1,1.2,2.3,2.4,2.5],
             [10,30,50,70,90]],

            [[1,3,5,7,9],
             [1.3,3.5,5.7,7.9,9.11],
             [100,200,300,400,500]]])
print(k.ndim)
i=np.sum(k,axis=2)
print(i)
# print(k[0,0,])
# o=np.sum(k[0,0,0:3,3],axis=2)
# a=np.sum(k[0,0],axis=1)
# print()
# print(a)
# o=k.reshape(3,2,axis=3)
print()

l=np.array([
    [1,2,3],
    [2,4,6],
    [1,3,5]
])
print(l.shape)

i=np.array([[11,22,33,44,55],
            [50,60,70,80,90],
            [10,30,50,70,90],
            [1,3,5,7,9],
            [2,4,6,8,10]])
print(i.shape)
j=np.sum(i,axis=0)
ju=np.sum(i,axis=1)
print(j)
print(ju)
# v=np.sum(i,axis=2)
# print()

fort=np.array([[[1,2,3,4,5],
                [10,20,30,40,50]],

               [[1,3,5,7,9],
                [1.1,1.2,1.3,9.1,4.1]],

               [[20,40,60,80,100],
                [2,4,6,8,10]],

               [[0.1,0.2,0.3,0.4,0.5],
                [-10,-9,-8,-7,-6]],

               [[50,60,70,80,90],
                [500,600,700,800,900]]])
print(fort.ndim)
print(fort.shape)
o=np.sum(fort[-3],axis=0)
print(o)
print()
# p=np.sum(fort[-3],axis=0 and fort[-2],axis=1)
p=np.sum(fort[-3][-2],axis=0)
print(p)
print()

nite=np.array([[[-5,-4,-3],
                [-2,-1,0],
                [1,3,5],
                [2,4,6]]])
print(nite.shape)
print(nite.size)
print(nite.reshape((6,2),order="C"))
print(nite.reshape((6,2),order="F"))
print(nite.reshape((3,4),order="F"))
print(nite.reshape((4,3),order="C"))
print(nite.ndim)
i=nite.reshape(-1,1)
print(i)
print(i.ndim)
io=nite.reshape(-1)
print(io)
print(io.ndim)
print()

jam=np.array([[[1,2,3,4],
               [2,4,6,8]],

              [[1,3,5,7],
               [3,6,9,12]],

              [[4,8,12,16],
               [5,10,15,20]]])
print(jam.ndim)
print(jam.shape)
print(jam.size)
oo=jam[-2,-2,-3]
print(oo)
o=np.sqrt(jam[-1,-2])
print(o)
# print(oo.sqrt(jam[-2,-2,-3]))
print(np.sqrt(oo))
print(jam[-1,-2]>10)








































































































































