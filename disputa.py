import matplotlib.pyplot as plt
import numpy as np
import math 

bu=0.1 #miliseconds
message=5.4 #miliseconds
m=message/bu
disputetime=50 #miliseconds
time=disputetime/bu
mediaexp=[0.1, 0.12, 0.19]


def createMatrix(nodes,time,mediaexp):
	matrix=np.zeros((nodes,int(time)))   #nodes vs time
	#create matrix of nodes attempting the dispute
	for i in range(nodes): 
		t=0
		t=round(np.random.exponential(mediaexp*time))
		if (t>=time): 
			t=round(time)-2
		j=1
		matrix[i,t]=1.5 #number orthogonal for the sum with 1
		while j<m:
			if ((t+j)<time):
				matrix[i,t+j]=1
			j=j+1
	return matrix


#vector of successfull tries
def successVector(matrix,n1): #returns a vector with the sum of all the elements of each colon
	v=[]
	s=np.ones((n1))
	for i in range(int(time)):
		v.append(matrix[:,i] @ s) #@ point product, sum of the element of the colons of the matrix
	return v


#pattern of a complete message
def createPattern(): 
	pattern=[1.5]
	for i in range(int(m)-1): 
		pattern.append(1)
	return pattern

#find sublist in list 
def isSublist(l,sl): 
	r=len(sl)
	exito=False
	for i in range(len(l)):
		if l[i]==sl[0] and l[i:i+r]==sl:
			 exito=True	
	return exito
	
repeats=3000	
nodes=600
vectorNodes=np.arange(20,nodes,10)
pattern=createPattern()

for med in mediaexp:
	acumulateSuccess=np.empty(len(vectorNodes))
	for n in range(len(vectorNodes)):
		successN=0 
		for r in range(repeats):
			matrix=createMatrix(vectorNodes[n],time, med)
			v=successVector(matrix,vectorNodes[n])
			if isSublist(v,pattern): 
				successN=successN+1
		acumulateSuccess[n]=successN	
	plt.plot(vectorNodes, acumulateSuccess*(1/repeats), label="mediaexp="+str(med))
plt.title("Probability of Success, disputeTime="+str(disputetime))
plt.xlabel("Number of nodes")
plt.ylabel("Probability of Success")
plt.legend(loc='upper rigth')
plt.show()


