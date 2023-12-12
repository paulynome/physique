# Méthode de Monte-Carlo
#On importe les bibliothèques.
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd
  
# Calcul des N valeurs de k à partir des valeurs de leq, l0 et m pour le ressort nommé nom suivant une loi uniforme et normale
def monte_carlo(leq, l0, m, nom) :
	lMC = (leq + pl * rd.uniform(-1, 1, N))
	mMC = (m + pm * rd.uniform(-1, 1, N))
	
	
	k = (mMC * g) / (lMC - l0)

	k = np.array(k)
	k = k.flatten()

	moy = np.average(k)
	it = np.std(k)
	
	print("\nPour " + nom + " : ")
	print("La moyenne est ", round(moy, 4)," N/m")
	print("L'incertitude type est ", round(it,4),"N/m")
	 
	 
	# Tracé de l'histogramme
	plt.hist(k, bins = 100, color ='#f5970a')
	plt.title("Histogramme de k (loi uniforme) pour " + nom)
	plt.xlabel("k (N/m)")
	plt.ylabel("")
	 
	plt.show()
	 
	# Calcul des N valeurs de k à partir des valeurs de leq, l0 et m suivant une loi normale
	
	lMC = (rd.normal(leq, pl/ np.sqrt(3), N))
	mMC = (rd.normal(m, pm/ np.sqrt(3), N))
	 
	
	k = (mMC * g) / (lMC - l0)
	 
	moy = np.average(k)
	it = np.std(k)
	print("\nAvec la loi normale : ")
	print("La moyenne est ", round(moy, 4), " N/m")
	print("L'incertitude type est ", round(it,4),"N/m")
	print("------------------")
	 
	# Tracé de l'histogramme
	plt.hist(k, bins = 100, color = '#82074d')
	plt.title("Histogramme de k (loi normale) pour " + nom)
	plt.xlabel("k (N/m)")
	plt.ylabel("")
	 
	plt.show()

# On détermine les valeurs

g = 9.81 # intensité pensanteur en m/s²

pl = 1  *10**(-3) # Précision sur les longueurs en m
pm = 25 *10**(-6) # Précision sur les masses en kg

N = 10000 # Nombre de valeurs dans Monte-Carlo

# Ressort 1
leq = 22.1 *10**(-2) # Longueurs à l'équilibre en m
l0 = 1.4 *10**(-3)   # Longueur à vide en m
m = 50  *10**(-3)    # Masse accrochée à l'extrémité du ressort en kg

monte_carlo(leq, l0, m, "Ressort 1")

# Ressort 2
leq = 12.9 *10**(-2) # Longueurs à l'équilibre en m
l0 = 2.3 *10**(-3)   # Longueur à vide en m
m = 150 *10**(-3)    # Masse accrochée à l'extrémité du ressort en kg

monte_carlo(leq, l0, m, "Ressort 2")

# Ressort 3
leq = 9.5 *10**(-2) # Longueurs à l'équilibre en m
l0 = 1.8 *10**(-3)  # Longueur à vide en m
m = 200 *10**(-3)   # Masse accrochée à l'extrémité du ressort en kg
monte_carlo(leq, l0, m, "Ressort 3")
 



