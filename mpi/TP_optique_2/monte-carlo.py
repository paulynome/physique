#On importe les bibliothèques.
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd

OA = -22.3
OB = 26.4 #OA'
a = 0.5
incertitude = np.sqrt(2*(a/np.sqrt(3))**2 + (0.5/np.sqrt(3))**2)
 
N= 10000
 
# Calcul des N valeurs de c à  partir des valeurs de f et lmd suivant une loi uniforme
 
OAMC = (OA + incertitude*np.sqrt(3) * rd.uniform(-1, 1, N))
OBMC = (OB + incertitude *np.sqrt(3)* rd.uniform(-1, 1, N))
 
f = (OAMC*OBMC)/(OAMC-OBMC) 
 
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
OAMC = rd.normal(OA, incertitude, N)
OBMC = rd.normal(OB, incertitude, N)
 
f = (OAMC*OBMC)/(OAMC-OBMC)
 
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