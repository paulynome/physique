#truc vraiment bizarre

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd
 
#Valeurs initiales
P=np.array([-4,-3,-2,-1,2,3,4])
angles=np.array([-12.62,-9.433,-6.267,-3.15,6.367,9.500,12.70])
angles=angles*(np.pi/180)
 
#incertitude de l'angle en rad
uangle=(1/120)*np.pi/180
onde=546*10**(-6)
N=1000
 
#Méthode de Monte Carlo pour un couple donné
def MC(angle,p):
   anglemc = angle +uangle*rd.uniform(-1,1,N)
   sin=np.sin(anglemc)
   n=sin/(p*onde)
   return n
 
n_indi=[0]*len(angles)
 
#Liste des moyennes des 1000 valeurs de n donné par la méthode de
#Monte Carlo pour chaqur couple
for i in range(len(n_indi)):
   n_indi[i]=np.average(MC(angles[i],P[i]))
 
#Affichage de l'histogramme
plt.hist([MC(angles[i],P[i]) for i in range(len(P))],200,stacked=True)
plt.title("Histogramme du nombre de trait par mm")
plt.xlabel("Nombre de traits/mm")
plt.ylabel("Nombre de valeurs")
plt.show()
 
#Affichage de la moyenne des moyennes et de l'écart-type des moyennes
print(np.average(n_indi))
print(np.std(n_indi))
