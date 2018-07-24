import numpy as np
import matplotlib.pyplot as plt
import math 



T=5 #milisegundos, tiempo de un slot, duración de un paquete
Tdisputa=50 #milisegundos, tiempo de proceso completo
m=Tdisputa/T #cantidad de slots


def distP(l,x): #distribucion exponencial
	#l lambda
	#x tiempo
	return (1-math.exp(-l*x))

def penvio(i,l): #probabilidad de envio en slot i
	#numero de slot en el que se quiere calcular la probabilidad de envio
	#l lambda
	return distP(l,(i+1)*T)-distP(l,i*T)

def pexito(n,i,l):#probabilidad de tener un envio exitoso en slot i con n nodos disputando
	#n nodos restantes por enviar paquetes
	#i-esimo slot
	#l lambda
	return n*penvio(i,l)*(1-penvio(i,l))**(n-1)

def nodosRestantes(n,i,l): #nodos restantes por enviar paquetes en el i-esimo slot
	return n-distP(l,i*T)*n

def pexitoProceso(m,n,l):
	#m slots
	#n nodos
	#l lambda
	prod=1	
	for i in range(int(m)): 
		#nr=nodosRestantes(n,i,l)
		prod=prod*(1-pexito(n,i,l))	#productoria de la probabilidad de falla
	return 1-prod



nodos=np.linspace(10,600,600-10+1)
L=1./Tdisputa
lamb=[L/0.1,L/0.12,L/0.19]
resultados=np.empty((len(lamb),len(nodos)))
for l in range(len(lamb)):
	for n in range(len(nodos)):
		resultados[l,n]=pexitoProceso(m,nodos[n],lamb[l])
	plt.plot(nodos, resultados[l,:],label="mediaexp="+str(1/(lamb[l]*Tdisputa)))

plt.title("Probability of Success, disputeTime="+str(Tdisputa))
plt.xlabel("Number of nodes")
plt.ylabel("Probability of Success")
plt.legend(loc='upper rigth')
plt.show()
