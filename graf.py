from pylab import plot, show, ylim, xlabel
from numpy import linspace, sin,cos, loadtxt
#x=[]
#y=[]
#for i in range(10):
#	y.append(i*i)
#	x.append(2*i)
#plot(x,y)
#show()

a=linspace(0,10,100)
c=cos(a)
b=sin(a)
plot(a,b)
plot(a,b, "go")
ylim(-1.1,1.1)
xlabel("Radianes")
plot(a,c)
show()



#m=open("doc.dat","w")

#for j  in range(len(a)):
#	m.write("%.2f %.2f\n" % (a[j], b[j]))
#m.close()
#s=loadtxt("doc.dat", float)
#plot(s[:,0],s[:,1])
#show()
