#Partie 3 TP 6
 
#On importe les bibliothèques.
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd
 
def rad(d, m) : #Transforme des degré minute en radian
   return (d + m/60)*np.pi/180
# On entre les valeurs numériques
a1 =  rad(170,00)
a2 =  rad(129,45)
p = 1
n = 600 * (10**-6)
 
sa1 = rad(0,1/2)
sa2 = rad(0,1/2)
 
N= 10000
 
lMC = []
 
# Calcul des N valeurs de lambda à  partir des valeurs de a1 et a2 suivant une loi uniforme
 
A1MC = (a1 + sa1 * rd.uniform(-1, 1, N))
A2MC = (a2 + sa2 * rd.uniform(-1, 1, N))
 
lMC = (2*np.sin((A1MC-A2MC)/4)/(p*n) )
 
lmoy = np.average(lMC)
it = np.std(lMC)
 
print("La moyenne est ", round(lmoy, 1), " nm")
print("L'incertitude type est ", round(it,2)," nm")
 
 
# Tracé de l'histogramme
plt.hist(lMC, bins = 100, color ='#f5970a')
plt.title("Histogramme de λ (loi uniforme)")
plt.xlabel("λ (nm)")
plt.ylabel("")
 
plt.show()
 
 
# Calcul des N valeurs de lambda à  partir des valeurs de a1 et a2 suivant une loi normale
lMC = []
A1MC = rd.normal(a1, sa1/ np.sqrt(3), N)
A2MC = rd.normal(a2, sa2/ np.sqrt(3), N)
lMC = (2*np.sin((A1MC-A2MC)/4)/(p*n) )
 
lmoy = np.average(lMC)
it = np.std(lMC)
print("\nAvec la loi normale : ")
print("La moyenne est ", round(lmoy, 1), " nm")
print("L'incertitude type est ", round(it,2)," cm")
 
# Tracé de l'histogramme
plt.hist(lMC, bins = 100, color = '#82074d')
plt.title("Histogramme de λ (loi normale)")
plt.xlabel("λ (nm)")
plt.ylabel("")
 
plt.show()