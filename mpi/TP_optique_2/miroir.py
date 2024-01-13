#On importe les bibliothèques.
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd

f = 33.1 - 20.8
a = 0.5
incertitude = np.sqrt((a/np.sqrt(3))**2 + (0.5/np.sqrt(3))**2)
 
N= 10000
 
# Calcul des N valeurs de c à  partir des valeurs de f et lmd suivant une loi uniforme
 
fMC = (f + incertitude*np.sqrt(3) * rd.uniform(-1, 1, N))
 
moy = np.average(fMC)
it = np.std(fMC)
Zscore = (moy-12.5)/it
 
print("La moyenne est ", round(moy, 2)," cm")
print("L'incertitude type est ", round(it,3)," cm")
print("Zscore", Zscore)
 
# Tracé de l'histogramme
plt.hist(fMC, bins = 100, color ='#f5970a')
plt.title("Histogramme de f (loi uniforme)")
plt.xlabel("f (cm)")
plt.ylabel("")
 
plt.show()
 
 
# Calcul des N valeurs de c à  partir des valeurs de f et lmd suivant une loi normale
fMC = rd.normal(f, incertitude, N)
 
moy = np.average(fMC)
it = np.std(fMC)
print("\nAvec la loi normale : ")
print("La moyenne est ", round(moy, 2), "cm")
print("L'incertitude type est ", round(it,2),"cm")
Zscore = np.abs((moy-12.5)/it)
print("Zscore", Zscore)
 
# Tracé de l'histogramme
plt.hist(fMC, bins = 100, color = '#82074d')
plt.title("Histogramme de f (loi normale)")
plt.xlabel("f (cm)")
plt.ylabel("")
 
plt.show()