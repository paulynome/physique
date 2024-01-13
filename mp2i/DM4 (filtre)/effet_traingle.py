# Effet d'un passe-bas du premier ordre sur un signal triangulaire
# On importe les bibliothèques numpy (pour faire des tableaux de valeurs) et pyplot (pour les graphes).
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# On définit le signal d'entrée
def e(t, f):
	a = 0 # Correspond à la moyenne du signal d'entrée (ajustable)
	for i in range (10):
		a = a + 8 / (pi* (2*i+1) )**2 * np.cos ( 2* pi * (2*i+1) * f * t )
	return a # Il y a 10 termes dans la somme, de f à 19f

# On définit la fonction de transfert passe-bas du premier ordre:
H0 = 1 # gain statique, modifiable
f0 = 5000 # fréquence propre du filtre, modifiable

def H(f):
	return H0 / (1 + 1j * f/f0 )

# La phase en radian
def phase (f):
	return np.angle ( H(f) )

# Le gain
def gain(f):
	return np.abs ( H(f) )

# La fonction de sortie
a = 0 # Moyenne de e(t) (modifiable)
def u(t, f):
	b = H0 * a
	for i in range (10):
		b = b + gain( (2*i+1) * f) * 8 / (pi* (2*i+1) )**2 * np.cos (2*pi* (2*i+1) *f *t + phase((2*i+1)*f))
	return b

# Tracés de e(t) et de u(t)

f= f0/100 # Fréquence du signal d'entrée en Hz
tmax = 3/f # J'ai choisi de tracer e(t) et u(t) sur 3 périodes.
t = np.linspace ( 0, tmax, 1000) # J'ai pris n = 1000 points
plt.plot ( t, e(t, f), 'r', label = "e(t) pour f/f0 = 0,01")
plt.plot (t, u(t, f), 'b', label= " u(t)")
plt.xlabel("temps en s")
plt.ylabel("tension en V")
plt.legend ()
plt.title ("Effet d'un passe-bas d'ordre 1 sur un signal triangulaire")
plt.grid()


fig, ax1 = plt.subplots()
fig.suptitle("Effet d'un passe-bas d'ordre 1 sur un signal triangulaire")

f= 100*f0 # Fréquence du signal d'entrée en Hz
tmax = 3/f
t = np.linspace ( 0, tmax, 1000 )

color = 'tab:red'
ax1.plot(t, e(t, f), 'r', label = "e(t) pour f/f0 = 100")
ax1.set_xlabel('temps en s')
ax1.set_ylabel('e(t) en V', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True)

ax2 = ax1.twinx()  # initialise un second axe qui partage le même axe x

color = 'tab:blue'
ax2.plot(t, u(t, f), 'b', label= " u(t)")
ax2.set_ylabel('u(t) en V', color=color)
ax2.tick_params(axis='y', labelcolor=color)


# On affiche une légende
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0)

fig.tight_layout()

# Et pour voir le tout…
plt.show ()