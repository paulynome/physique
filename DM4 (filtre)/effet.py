# Effet d'un passe-bas du premier ordre sur un signal sinusoïdal
# On importe les bibliothèques numpy (pour faire des tableaux de valeurs) et pyplot (pour les graphes).
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# On définit le signal d'entrée, e(t) = 10 * cos( 2 pi f t)
def e(t):
	return 10*np.cos(2*pi*f * t)

# On définit la fonction de transfert passe-bas du premier ordre:
H0 = 1
f0 = 5000

def H(f):
	return H0/(1 + 1j*f/f0)


# La phase du filtre
def phase(f):
	return np.angle (H(f))

# Le gain du filtre
def gain(f):
	return np.abs(H(f))

# On définit la fonction de sortie u(t) :
def u(t, f):
	return gain(f)*10*np.cos(2*pi*f*t+ phase(f))

# Tracés des 3 courbes demandées les unes en dessous des autres
plt.subplot(311) # pour la 1ère courbe (3 graphes en tout, 1 colonne, 1ère ligne)
f = f0
tmax = 3/f # J'ai choisi de tracer e(t) sur 3 périodes.
t = np.linspace(0, tmax,100) # J'ai pris n=100 points
plt.plot (t, u(t,f), 'b', label="u(t)") # u(t) sera en bleu
plt.plot (t, e(t), 'r', label="e(t) avec f = 5 kHz") # la courbe e(t) sera en rouge
plt.legend () # ligne obligatoire quand on écrit label dans l’instruction plot
plt.title ("Effet d'un filtre passe bas du 1er ordre")
plt.xlabel ("temps en s")
plt.ylabel ("e(t) en V")
plt.grid (True)

plt.subplot (312) # pour la 2nde courbe (3 graphes en tout, 1 colonne, 2nde ligne)
f = f0/100
tmax = 3/f
t = np.linspace (0, tmax,100)
plt.plot (t, u(t,f), 'b', label="u(t)")
plt.plot (t, e(t), 'r', label="e(t) avec f = 50 Hz")
plt.legend ()
plt.xlabel ("temps en s")
plt.ylabel("e(t) en V")
plt.grid (True)

plt.subplot (313) # pour la 3ème courbe (3 graphes en tout, 1 colonne, 3ème ligne)
f = 100*f0
tmax = 3/f
t = np.linspace (0, tmax,100)
plt.plot (t, u(t,f), 'b', label="u(t)")
plt.plot (t, e(t), 'r', label="e(t)  pour f = 500 kHz")
plt.legend ()
plt.xlabel ("temps en s")
plt.ylabel ("e(t) en V")
plt.grid (True)


plt.show()