# Modélisation - Tir de Projectile
# On importe les bibliothèques.
 
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
 
# On introduit les conditions initiales
 
g = 9.81 # Intensité de la pesanteur en m/s²
v0 = 10 # Vitesse initiale en m/s
alpha = 50 # Angle de tir en °
b = 0.20 # USI
c = 0.1 # USI

t0 = 0
tmax = 6

# Conversion en radians :
alpha = np.radians(alpha)

 
# On définit la fonction f, qui contient le système d'équations différentielles:
def f(s, t, b ,c):
	[x, z ,vx, vz] = s # On crée un tableau avec les données du mouvement
	v = np.sqrt((vx**2)+(vz**2)) #On calcule la vitesse en fonction de ses composantes 
	return np.array ( [ vx , vz, 0 - b*vx - c*v*vx, -g - b*vz - c*v*vz])
 
# On fera varier le temps entre t0 et tmax
t =np.linspace ( t0, tmax, 500 ) # On pourra adapter le nombre de points.
 

''' Cette fonction prend en argrument les coordonées x0 et z0 à l'origine,
les vitesses vx0 et vz0 initiales, le coefficicent de frottement linéaire b,
le coefficient de frottement et le nom de la courbe '''
def courbe(x0, z0, vx0, vz0, b , c, label) :
	# On calcule les valeurs de u et up aux dates t
	s = odeint (f, [x0, z0, vx0, vz0], t, (b, c))

	# On ne représente sur le graphique que les z positifs
	indice=0
	for z in s[:,1] :
	    if z<0:
	        break
	    indice+=1
	# Tracé de la courbe
	plt.plot (s[:,0][:indice+1], s[:,1][:indice+1], label = label) # on ne retient que la première colonne de s pour avoir theta



courbe(0,0, v0*np.cos(alpha), v0*np.sin(alpha), 0, 0, "Sans frottements")
courbe(0,0, v0*np.cos(alpha), v0*np.sin(alpha), b, 0, "Frottements en v")
courbe(0,0, v0*np.cos(alpha), v0*np.sin(alpha), 0, c, "Frottements en v²")

plt.xlabel ("x (en m)")
plt.ylabel ("z (en m)")
plt.suptitle ("Modélisation d'un tir de projectile")
plt.title ("Différentes modélisation de la trajectoire en fonction du type de frottement")
plt.legend(loc = 'upper right')
plt.grid (True)
plt.show ()


