# Synthèse de Fourier d'un signal triangulaire
# On importe les bibliothèques numpy (pour faire des tableaux de valeurs) et pyplot (pour les graphes).
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# On définit le signal d'entrée
f= 100 # Fréquence du signal d'entrée en Hz

def e(t,n) :
	a = 0 # Correspond à la moyenne du signal d'entrée (modifiable)
	for i in range (n) :
		a = a + 8/(pi*(2*i+1))**2 * np.cos(2*pi*(2*i+1)*f*t) # Je rajoute 1 à 1 les n termes.
	return a

# Tracé de e(t)
# Je trace les uns en dessous des autres les graphes obtenus avec un nombre différents d'harmoniques.
tmax = 3/f # J'ai choisi de tracer e(t) sur 3 périodes (modifiable)
t = np.linspace (0, tmax,1000) # J'ai pris n=1000 points (modifiable)


plt.subplot (611) # Il y aura 6 courbes en tout, en 1 colonne
plt.plot (t, e(t, 1), 'r', label=" n = 1") # avec le fondamental uniquement (n = 1)
plt.legend ()
plt.xlabel ("temps en s")
plt.ylabel ("e(t) en V")
plt.grid (True)

plt.subplot (612)
plt.plot (t, e(t, 2), 'r', label=" n = 2") # avec 2 termes, le fondamental et 1 harmonique
plt.legend ()
plt.xlabel ("temps en s")
plt.ylabel ("e(t) en V")
plt.grid (True)

plt.subplot (613)
plt.plot (t, e(t, 3), 'r', label=" n = 3") # avec 3 termes
plt.legend ()
plt.xlabel ("temps en s")
plt.ylabel ("e(t) en V")
plt.grid (True)

plt.subplot (614)
plt.plot (t, e(t, 4), 'r', label=" n = 4") # avec 4 termes
plt.legend ()
plt.xlabel ("temps en s")
plt.ylabel( "e(t) en V")
plt.grid (True)

plt.subplot (615)
plt.plot (t, e(t, 5), 'r', label=" n = 5") # avec 5 termes
plt.legend ()
plt.xlabel ("temps en s")
plt.ylabel ("e(t) en V")
plt.grid (True)

plt.subplot (616)
plt.plot (t, e(t, 10), 'r', label=" n = 10") # avec 10 termes
plt.legend ()
plt.xlabel ("temps en s")
plt.ylabel ("e(t) en V")
plt.grid (True)
plt.show ()