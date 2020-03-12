from numpy import loadtxt, zeros
from pylab import  plot,show, ylim, xlim, xlabel, ylabel

a=loadtxt("sunspots.txt",float)
#print(a)
plot(a[:,0],a[:,1])
xlabel("MES")
ylabel("Número de Manchas")
xlim(0,1001)
#show()
r=5
y=zeros(1000,float)
for k in range(0,1000):
	for m  in range(r):
		y[k]+=a[k+m,1]
	y[k]/=2*r+1
plot(a[0:1000,0],y, "b")
show()	
