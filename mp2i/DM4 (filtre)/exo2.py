# Réponse d'un RLC à un échelon de tension
# On importe les bibliothèques.

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# On introduit les conditions initiales

u0 = 0 # tension initiale en V
up0 = 0 # dérivée initiale en V/s
t0 = 0 # temps caractéristique en s
tmax = 1.5*10**(-3) # à adapter
f0 = 5000 # fréquence propre
w0 = 2*np.pi*f0 # pulsation propre en rad/s
Q = 0 # facteur de qualité

E = 5 # tension du générateur

# On définit la fonction f, qui contient le système d'équations différentielles:
def f(s, t):
	[u, up] = s # On crée un tableau avec u et sa dérivée up. s est le couple (u, up).
	return np.array ( [ up , w0**2 * E - (w0*up/Q) - (w0**2 * u) ])

# On fera varier le temps entre t0 et tmax
t =np.linspace ( t0, tmax, 500 ) # On pourra adapter le nombre de points.


for Q in [5, 0.5, 0.2] :
	# On calcule les valeurs de u et up aux dates t
	s = odeint (f, [u0, up0], t)

	# Tracé de la courbe
	plt.plot (t, s[:, 0]) # on ne retient que la première colonne de s pour avoir u


plt.plot (t, 5+t*0, "r:") # Asymptote
plt.xlabel ("Temps t en s")
plt.ylabel ("Tension en Volt")
plt.yticks (range(0,9))
plt.title ("Tension aux bornes de C en fonction du temps")
plt.suptitle ("Réponse d'un RLC à un échelon de tension de 5V")
plt.legend(["Q = 5", "Q = 0,5", "Q = 0,2", "Asymptote y = 5"])
plt.grid (True)
plt.show ()