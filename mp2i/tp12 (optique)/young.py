# Fentes d'Young
import numpy as np
import matplotlib.pyplot as plt

# Valeurs expérimentales

# Distance Ecran / fente = 186 cm

d = [500, 300, 200] # Distance entre les fentes en µm
i = [3/13, 2.7/7, 2.9/5] # Interfrange en cm
lmd = 250 # Longueur d'onde du laser en nm


# Conversion dans les USI
d = np.array(d)*10**(-6)
i = np.array(i)*10**(-2)

# On prend l'inverse de d
d_1 = 1/np.array(d)

plt.plot(d_1, i, 'ro')

[a, b] = np.polyfit(d_1,i,1)
print("i = ",a,"* 1/d + ",b) #On affiche le résultat de la régression linéaire
 
ymodel = a * d_1 + b #On définie la courbe de tendance
plt.plot(d_1, ymodel, 'b:') #on représente la courbe de tendance par des pointillés bleus.
plt.legend(['mesures expérimentales', "régression linéaire"])


plt.title("Interfrange en fonction de 1/d")
plt.xlabel("1/d en m⁻¹")
plt.ylabel("Interfrange en m")
plt.grid()
plt.show()


# Distance d = 300 µm

D = [40,50,60,70,80,90,100,110,120] # Distance D en cm
i = [0.088,0.113,0.144,0.163,0.175,0.206,0.225,0.263,0.281] # Interfrange en cm


plt.plot(D, i, 'ro')

[a, b] = np.polyfit(D,i,1)
print("i = ",a,"* D + ",b) #On affiche le résultat de la régression linéaire
 
ymodel = a * np.array(D) + b #On définie la courbe de tendance
plt.plot(D, ymodel, 'b:') #on représente la courbe de tendance par des pointillés bleus.
plt.legend(['mesures expérimentales', "régression linéaire"])

plt.title("Interfrange en fonction de D")
plt.xlabel("Distance D en cm")
plt.ylabel("Interfrange en cm")
plt.grid()
plt.show()