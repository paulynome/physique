# Diagramme de Bode d'un passe-bas du premier ordre

# On importe les bibliothèques numpy (pour faire des tableaux de valeurs) et pyplot (pour les graphes).
import numpy as np
import matplotlib.pyplot as plt

# On demande la valeur de H0 et f0:
H0 = 1 
f0 = 5000

# On définit la fonction de transfert passe-bas du premier ordre:
def H(f):
    return H0/(1 + 1j*f/f0)

# Découpage régulier des puissances en base 10 de la pulsation ici de 10^0 à 10^5
puissance_n = np.arange(0,5,0.01)

# Les fréquences f
f = 10**puissance_n

# La phase en degré
phase = np.angle(H(f),'deg')

# Le gain en dB
GdB = 20*np.log10(abs(H(f)))

#Tracer du diagramme de Bode
plt.suptitle("Filtre passe-bas du 1er ordre avec f0 = 5,0 kHz et H0 = 1")
plt.subplot(211) # Permet d’afficher plusieurs graphes (nombre de graphes (2), colonne (1), ligne (1))
plt.semilogx(f,GdB)  # Tracé en semilog deGdB
plt.xlabel("fréquence en échelle log")
plt.ylabel("GdB")
plt.title("Diagramme de Bode du gain pour le passe-bas du 1er ordre ")
plt.grid(True,which="both", linestyle='--')  # Activation de la grille

plt.subplot(212)
plt.semilogx(f,phase)  #Tracé en semilog du module
plt.xlabel("fréquence en échelle log")
plt.ylabel("Phase en degrés")
plt.title("Diagramme de Bode de la phase pour le passe-bas du 1er ordre ")
plt.grid(True,which="both", linestyle='--')   #Activation de la grille

#On montre le graphique
plt.show()