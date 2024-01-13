#On importe les bibliothèques.
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd
D = 100
d = 104.8 - 34.5 
a = 0.5
incertitude = np.sqrt(2*(a/np.sqrt(3))**2 + (0.5/np.sqrt(3))**2)
 
N= 10000
 
# Calcul des N valeurs de c à  partir des valeurs de f et lmd suivant une loi uniforme
 
DMC = (D + incertitude*np.sqrt(3) * rd.uniform(-1, 1, N))
dMC = (d + incertitude *np.sqrt(3)* rd.uniform(-1, 1, N))
 
f = (DMC**2-dMC**2)/(4*DMC)
 
moy = np.average(f)
it = np.std(f)
 
print("La moyenne est ", round(moy, 2)," cm")
print("L'incertitude type est ", round(it,3)," cm")
Zscore = np.abs((moy-12.5)/it)
print("Zscore", Zscore)
 
 
# Tracé de l'histogramme
plt.hist(f, bins = 100, color ='#f5970a')
plt.title("Histogramme de f (loi uniforme)")
plt.xlabel("f (cm)")
plt.ylabel("")
 
plt.show()
 
 
# Calcul des N valeurs de c à  partir des valeurs de f et lmd suivant une loi normale
DMC = rd.normal(D, incertitude, N)
dMC = rd.normal(d, incertitude, N)
 
f = (DMC**2-dMC**2)/(4*DMC)
 
moy = np.average(f)
it = np.std(f)
print("\nAvec la loi normale : ")
print("La moyenne est ", round(moy, 2), "cm")
print("L'incertitude type est ", round(it,2),"cm")
Zscore = np.abs((moy-12.5)/it)
print("Zscore", Zscore)

# Tracé de l'histogramme
plt.hist(f, bins = 100, color = '#82074d')
plt.title("Histogramme de f (loi normale)")
plt.xlabel("f (cm)")
plt.ylabel("")
 
plt.show()