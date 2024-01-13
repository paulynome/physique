import matplotlib.pyplot as plt
import numpy as np

D = np.array([80,90,100,110,120,130])
d = np.array([14,33,47,60.5,71.5,82.5])

f = (D**2-d**2)/(4*D)


#[a, b] = np.polyfit(D,f,1)
#print("a = ",a,"b = ",b) #On affiche le résultat de la régression linéaire

plt.title("f' en fonction de D")
plt.xlabel('D (cm)')
plt.ylabel("f' (cm) ")
plt.grid()

plt.plot(D,f,'ro') #on représente les valeurs expérimentales par des ronds rouges
fmoy = np.average(f) #On définie la courbe de tendance
plt.plot([min(D),max(D)], [fmoy,fmoy], 'b:') #on représente le f' moyen
plt.legend(['f\' expérimentaux', "f' moyenne"])
plt.show() #on affiche le graphique


#Stats

fmoy = np.average(f)
un = np.std(f)

print('fmoy =', fmoy,' et un =', un)