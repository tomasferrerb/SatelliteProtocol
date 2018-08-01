import matplotlib.pyplot as plt
import numpy as np
import math 
import argparse

plt.rcParams.update({'font.size': 36})

def string2list(s):
	lista=s.split()
	return list(map(float,lista))

def data2matrix(archivo,est,m,n):
	matrix=np.empty((m,n))
	for line in archivo:
		if est in line:
			for i in range(m):
				matrix[i,:]=string2list(archivo[archivo.index(line)+i+1])
	return matrix
			


def graf(name,xname,title):		
	f = open(name, 'r')
	temp = f.readlines()

	#names and axis for plots 
	
	axisXp=temp[1].split()
	axisZp=temp[2].split()
	X=axisXp[0]
	Z=axisZp[0]
	axisX=list(map(float,axisXp[1:]))
	axisZ=list(map(float,axisZp[1:]))
	markers=['-o','-v','-D','-*','-+','--']

	estadisticas=["SuccessCycles%","Analytical"]#Cycles
	
	matrixSuc=data2matrix(temp,estadisticas[0],len(axisZ),len(axisX))
	matrixAna=data2matrix(temp,estadisticas[1],len(axisZ),len(axisX))

	
	plt.plot(axisX,matrixSuc[2,:],'-vr',label='1.media of Exp. Dist.='+str(axisZ[2]))
	plt.plot(axisX,100*matrixAna[2,:],'--r',label='Analytical 1.')
	plt.plot(axisX,matrixSuc[3,:],'-ob',label='2. media of Exp. Dist.='+str(axisZ[3]))
	plt.plot(axisX,100*matrixAna[3,:],'--b',label='Analytical 2.')

	plt.title(title)			
	plt.xlabel(xname)
	plt.ylabel('Probability of Success (%)')
	plt.xlim(min(axisX),max(axisX))
	plt.ylim(0,100)
	plt.legend(loc='upper right')				
	plt.show()




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot results',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--name', type=str,help='name of txt')
    parser.add_argument('--axisX', type=str,help='axis X label')
    parser.add_argument('--title', type=str,help='title')

    args = parser.parse_args()

    try:
        graf(args.name,args.axisX,args.title)
    except KeyboardInterrupt:
        pass
			

