#On importe les bibliothèques.
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd
 
# On entre les valeurs numériques
OA = np.array([-100,-80,-60,-50,-40,-35,-30,-17,-15,-13,-10,20,25,30,40,50])
OB = np.array([34,37,44,52,69,93,162,-46,-30,-27,-16,10,12,13,16,17])#Liste des OA'
 
sOA = 0.5 #Précision sur OA
sOB = 0.5
 
N= 10000
 
fMC = []
 
# Calcul des N valeurs de la distance focale f' à  partir des valeurs de OA et OA' suivant une loi uniforme
for i in range(0, len(OA)) :
   OAMC = (OA[i] + sOA * rd.uniform(-1, 1, N))
   OBMC = (OB[i] + sOB * rd.uniform(-1, 1, N))
   fMC.append(1/((1/OBMC)-(1/OAMC)))
 
fmoy = np.average(fMC)
it = np.std(fMC)
 
print("La moyenne est ", round(fmoy, 2), " cm")
print("L'incertitude type est ", round(it,2)," cm")
 
 
# Tracé de l'histogramme
plt.hist([fMC[i] for i in range(len(fMC))], bins = 20, stacked=True)
plt.title("Histogramme de f' (loi uniforme)")
plt.xlabel("f'(cm)")
plt.ylabel("")
 
plt.show()
 
 
# Calcul des N valeurs de la distance focale f' à  partir des valeurs de OA et OA' suivant une loi normale
fMC = []
for i in range(0, len(OA)) :
   OAMC = rd.normal(OA[i], sOA/ np.sqrt(3), N)
   OBMC = rd.normal(OB[i], sOB/ np.sqrt(3), N)
   fMC.append(1/((1/OBMC)-(1/OAMC)))
 
fmoy = np.average(fMC)
it = np.std(fMC)
 
print("La moyenne est ", round(fmoy, 2), " cm")
print("L'incertitude type est ", round(it,2)," cm")
 
 
# Tracé de l'histogramme
plt.hist([fMC[i] for i in range(len(fMC))], bins = 20, stacked=True)
plt.title("Histogramme de f' (loi normale)")
plt.xlabel("f'(cm)")
plt.ylabel("")
 
plt.show()