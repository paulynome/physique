import matplotlib.pyplot as plt
import numpy as np

V = np.array([-3,2,3])
d = np.array([23.5, -12.5, -17.5])
f2 = (1/4)*10**2

f = -( f2**2 )/d


#[a, b] = np.polyfit(D,f,1)
#print("a = ",a,"b = ",b) #On affiche le résultat de la régression linéaire

plt.title("f' en fonction de V")
plt.xlabel('V (δ)')
plt.ylabel("f' (cm) ")
plt.grid()

plt.plot(V,f,'ro') #on représente les valeurs expérimentales par des ronds rouges
fmoy = np.average(f) #On définie la courbe de tendance
plt.plot([min(V),max(V)], [fmoy,fmoy], 'b:') #on représente le f' moyen
plt.legend(['f\' expérimentaux', "f' moyenne"])
plt.show() #on affiche le graphique


#Stats

fmoy = np.average(f)
un = np.std(f)

print('fmoy =', fmoy,' et un =', un)