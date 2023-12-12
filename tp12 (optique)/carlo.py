#On importe les bibliothèques.
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd
 
lmd = 8.6*10**(-3)
f = 39.7*10**3
 
plmd = (1*10**(-3)) / 20
pf = 50
 
N= 10000
 
# Calcul des N valeurs de c à  partir des valeurs de f et lmd suivant une loi uniforme
 
lMC = (lmd + plmd * rd.uniform(-1, 1, N))
fMC = (f + pf * rd.uniform(-1, 1, N))
 
c = lMC*fMC
 
moy = np.average(c)
it = np.std(c)
 
print("La moyenne est ", round(moy, 2)," m/s")
print("L'incertitude type est ", round(it,3)," m/s")
 
 
# Tracé de l'histogramme
plt.hist(c, bins = 100, color ='#f5970a')
plt.title("Histogramme de c (loi uniforme)")
plt.xlabel("c (m/s)")
plt.ylabel("")
 
plt.show()
 
 
# Calcul des N valeurs de c à  partir des valeurs de f et lmd suivant une loi normale
lMC = rd.normal(lmd, plmd/ np.sqrt(3), N)
fMC = rd.normal(f, pf/ np.sqrt(3), N)
 
c = lMC*fMC
 
moy = np.average(c)
it = np.std(c)
print("\nAvec la loi normale : ")
print("La moyenne est ", round(moy, 2), " m/s")
print("L'incertitude type est ", round(it,2)," m/s")
 
# Tracé de l'histogramme
plt.hist(c, bins = 100, color = '#82074d')
plt.title("Histogramme de c (loi normale)")
plt.xlabel("c (m/s)")
plt.ylabel("")
 
plt.show()
