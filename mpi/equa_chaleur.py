import numpy as np
import matplotlib.pyplot as plt

# ================= 1D ======================
# (marche pas)

N = 500
T0 = 273
T1 = 273

x = np.linspace(0,1,N)
B = np.full((N), False)
T = np.full((N), T0)

B[0] = True
B[N-1] = True
T[0] = 263
T[N-1] = 293

Tau = 1
D = 87**(-6)

for k in range(0, 500):
    old = np.copy(T)
    for i in range(0, N) :
        if not B[i] :
            dT = D * ((old[i+1] + old[i-1] - 2*old[i]) * ((N)**2)) * Tau
            T[i] = old[i] + dT
plt.plot(x, T)
plt.show()


# ======== 2D ==============












x = np.linspace(0,1,N)
y = np.linspace(0,1,N)
X,Y = np.meshgrid(x,y)

B = np.zeros((N,N), bool)
V = np.zeros((N,N))

B[:,0] = True
B[0, :] = True
B[-1, :] = True
B[:, -1] = True

for j in range (N//2-20, N//2+20+1) :
    B[N//2-10, j] = True
    V[N//2-10, j] = -5

    B[N//2+10, j] = True
    V[N//2+10, j] = 5

for i in range(N) :
    for j in range(N) :
        if ((i-N//2)**2 + (j-N//2)**2 <= 100) :
            B[i,j] = True
            V[i,j] = 5

        if ((i-20-N//2)**2 + (j-N//2)**2 <= 100) :
            B[i,j] = True
            V[i,j] = -5



k = 0
erreur = 1
while k<100 and erreur > (10^(-4)) :
    old = np.copy(V)
    erreur = 0

    for i in range(N) :
        for j in range(N) :
            if not B[i,j] :
                V[i,j]=0.25 * (old[i+1,j] + old[i-1,j] + old[i, j+1] + old[i, j-1])
                erreur += (V[i,j] - old[i,j])**2

    erreur = np.sqrt(erreur/N**2)
    k += 1

plt.figure()
graphe = plt.contour(X,Y,V,30)
#plt.clabel(graphe, fontsize = 5)
#plt.pcolormesh(X,Y,V)
#plt.show()



