import numpy as np
import matplotlib.pyplot as plt
import math 

#plt.rc('xtick', labelsize=20) 
#plt.rc('ytick', labelsize=20) 
plt.rcParams.update({'font.size': 16})


T=5.4 #milisegundos, tiempo de un slot, duración de un paquete
Tdisputa=50 #milisegundos, tiempo de proceso completo
m=round(Tdisputa/T) #cantidad de slots


def distP(l,x): #distribucion exponencial# l=0 dist uniforme
	#l lambda
	#x tiempo
	if (l==0):
		return x*1./Tdisputa
	else:
		return (1-math.exp(-l*x))

def penvio(i,l): #probabilidad de envio en slot i
	#numero de slot en el que se quiere calcular la probabilidad de envio
	#l lambda
	if (i==m-1):
		return 1-distP(l,i*T)
	else:	
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



nodos=[50,100,200,400,800]
L=1./Tdisputa
#lamb=np.linspace(0.08,1,100)
media=np.linspace(0.08,1,100)
lamb=L/media
resultados=np.empty((len(media),len(nodos)))
for n in range(len(nodos)):
	for l in range(len(media)):
		resultados[l,n]=pexitoProceso(m,nodos[n],L/media[l])
	plt.plot(media, resultados[:,n],label="Exp. dist. ("+str(nodos[n])+' nodes)')
plt.plot(media,pexitoProceso(m,50,0)*np.ones((len(lamb))),label='Uniform dist. (50 nodes)')	
plt.title("Probability of Success, DisputeTime="+str(Tdisputa)+' ms')
plt.xlabel("Media of Exponential distribution")
plt.ylabel("Probability of Success")
plt.xlim(min(media),max(media))
plt.ylim(0,1)
plt.legend(loc='upper rigth')
plt.show()
