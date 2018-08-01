import matplotlib.pyplot as plt
import numpy as np
import math 
import argparse

plt.rcParams.update({'font.size': 36})

def string2list(s):
	lista=s.split()
	return list(map(float,lista))


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

	estadisticas=["ChannelOccupation","SuccessCycles%","Fairness%","Analytical"]#Cycles
	for est in estadisticas: 
		for line in temp:	
			if est in line: 
				plt.figure()
				for e in range(len(axisZ)):
					if (est=="ChannelOccupation" and e==0):###BORRAR
						plt.plot(axisX,83.3*np.ones((len(axisX))),'--b', label='Offered Load') ###BORRAR	
					plt.plot(axisX,string2list(temp[temp.index(line)+e+1]),markers[e],label=Z+str(axisZ[e]))
					
				plt.title(title)			
				plt.xlabel(xname)
				plt.ylabel(est+' (%)')
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
			

