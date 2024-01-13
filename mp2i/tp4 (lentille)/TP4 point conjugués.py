import matplotlib.pyplot as plt
import numpy as np

OA = np.array([-100,-80,-60,-50,-40,-35,-30,-17,-15,-13,-10,-5,15,20,25,30,40,50])
OB = np.array([34,37,44,52,69,93,162,-46,-30,-27,-16,-9,7,10,12,13,16,17])

OA_1 = 1/OA
OB_1 = 1/OB


x = np.array(OA_1)
y = np.array(OB_1)


[a, b] = np.polyfit(x,y,1)
print("a = ",a,"b = ",b) #On affiche le résultat de la régression linéaire

plt.title("1/OA' en fonction de 1/OA")
plt.xlabel('1/OA (cm-1)')
plt.ylabel("1/OA'(cm-1) ")
plt.grid()

plt.plot(x,y,'ro') #on représente les valeurs expérimentales par des ronds rouges
ymodel = a * x +b #On définie la courbe de tendance
plt.plot(x, ymodel, 'b:') #on représente la courbe de tendance par des pointillés bleus.
plt.show() #on affiche le graphique


#Stats

f = []
for i in range(1, len(x)) :
    f.append(1/(y[i] - x[i]))
print(f)

fmoy = np.average(f)
un = np.std(f)

print('fmoy =', fmoy,' et un =', un)