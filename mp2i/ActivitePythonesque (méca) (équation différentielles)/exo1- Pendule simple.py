# Pendule Simple
# On importe les bibliothèques.
 
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
 
# On introduit les conditions initiales
 
g = 9.81 # Intensité de la pesanteur en N/kg
L = 1 # Longueur du fil en mètre
co = [(0,10),(0,30), (0,60), (0,160)] # Couples Angle initial en degré, Vitesse angulaire intiale en degré/s
t0 = 0
tmax = 6


 
# On définit la fonction f, qui contient le système d'équations différentielles:
def f(s, t):
	[theta, vtheta] = s # On crée un tableau avec theta et sa dérivée vtheta. s est le couple (theta, vtheta).
	return np.array ( [ vtheta , -(g/L)*np.sin(theta) ])
 
# On fera varier le temps entre t0 et tmax
t =np.linspace ( t0, tmax, 500 ) # On pourra adapter le nombre de points.
 
def courbe(theta0, vtheta0) :
	# On calcule les valeurs de theta et vtheta aux dates t
	s = odeint (f, [theta0, vtheta0], t)

	# Tracé de la courbe
	plt.plot (t, np.degrees(s[:, 0])) # on ne retient que la première colonne de s pour avoir theta
	plt.plot (t, np.degrees(theta0*np.cos(np.sqrt(g/L)*t)), "r:") # Approximation des petits angles

for (vtheta0, theta0) in co :
	courbe(np.radians(theta0), np.radians(vtheta0))

	plt.xlabel ("Temps t en s")
	plt.ylabel ("Angle theta en ")
	plt.title ("Vitesse angulaire initiale = " + str(vtheta0) + " °/s et angle intial = " + str(theta0) + "°")
	plt.suptitle ("Modélisation du pendule simple")
	plt.legend(["Signal du pendule", "Signal périodique avec les mêmes CO"], loc = 'upper right')
	plt.grid (True)
	plt.show ()


