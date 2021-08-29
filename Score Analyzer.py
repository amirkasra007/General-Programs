import numpy as np
import matplotlib.pyplot as plt
from statistics import mode

a = []
num = []
n=0

x =(input("enter your numbers"))
while(x != 'end'):
    n=n+1
    a.append(float(x))
    num.append(n)
    x =(input("enter your numbers"))

    if (x =='end') :
        break

print("your data is",a)

Mean=np.mean(a)
Median=np.median(a)
varians=np.var(a)

print("your data average is",Mean)
print("your data Median is",Median)
print("your data varians is",varians)

c=[]
d=[]
e=[]
f=[]

try:
    mod=mode(a)
    print("your data mod is",mod)
except:
    mod=0
    print("there is no mod")

for i in a:
    if(mod!=0):
        c.append(Mean)
        d.append(Median)
        e.append(mod)
        f.append(varians)
    elif(mod==0):
        c.append(Mean)
        d.append(Median)
        e.append(0)
        f.append(varians)

plt.title("Mean to data")
plt.plot(a,c,'g',label='Mean')
plt.grid()
plt.legend(loc='best')
plt.xlabel("data")
plt.ylabel("Mean")
plt.show()


plt.title("Median to data")
plt.plot(a,d,'r',label='Median')
plt.grid()
plt.legend(loc = 'best')
plt.xlabel("data")
plt.ylabel("Median")
plt.show()


plt.title("Varians of data")
plt.plot(a,f,'b',label = 'Varians')
plt.grid()
plt.legend(loc = 'best')
plt.xlabel("data")
plt.ylabel("Varians")
plt.show()


plt.plot(a,e,'y',label = 'mod')
plt.grid()
plt.title("mod of data")
plt.legend(loc = 'best')
plt.xlabel("data")
plt.ylabel("mod")
plt.show()

plt.title("data parameters")
plt.plot(a,c,'g',label='Mean')
plt.plot(a,e,'y',label = 'mod')
plt.plot(a,f,'b',label = 'Varians')
plt.plot(a,d,'r',label='Median')
plt.grid()
plt.legend(loc='best')
plt.xlabel("data")
plt.ylabel("parameters")
plt.show()
