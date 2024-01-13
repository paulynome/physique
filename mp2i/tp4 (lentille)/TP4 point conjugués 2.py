import matplotlib.pyplot as plt
import numpy as np

OA = np.array([-35,-30,-20,20,15,16,80,90,100])
OB = np.array([-8,-6.5,-3,48,27,35,-56,-52,-49])

OA1 = 1/OA
OB1 = 1/OB

def OAth(OA): 
    return ((-33*OA)/(OA-33))

x = np.linspace(-40,24)
x2 = np.linspace(50,120)

[a, b] = np.polyfit(OA1,OB1,1)
print("a = ",a,"b = ",b) #On affiche le résultat de la régression linéaire

plt.title("1/OA' en fonction de 1/OA")
plt.xlabel('1/OA (cm-1)')
plt.ylabel("1/OA'(cm-1) ")
plt.grid()

plt.plot(OA1,OB1,'ro') #on représente les valeurs expérimentales par des ronds rouges
ymodel = a * OA1 +b #On définie la courbe de tendance
plt.plot(OA1, ymodel, 'b:') #on représente la courbe de tendance par des pointillés bleus.
plt.legend(['mesures expérimentales', "régression linéaire"])
plt.show() #on affiche le graphique




#Stats

f = []
for i in range(1, len(OA1)) :
    f.append(1/(OB1[i] - OA1[i]))
print(f)

fmoy = np.average(f)
un = np.std(f)

print('fmoy =', fmoy,' et un =', un)