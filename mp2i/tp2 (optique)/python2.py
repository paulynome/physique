import matplotlib.pyplot as plt
import numpy as np
sini=[0,0.1736,0.342,0.5,0.6428,0.766,0.866,0.9397,0.9848]
sinr=[0,0.1045,0.225,0.3256,0.4384,0.515,0.5878,0.6293,0.682]

plt.title("sin(r) en fonction de sin(i)")

plt.plot(sini,sinr, color="red")
plt.xlabel('sin(i)')
plt.ylabel("sin(r)")

plt.grid()


plt.show()



model = np.polyfit(sini, sinr, 1)
print(model)

#sinmodel = model[0]*sini
#plt.plot(sini, sinmodel, 'b:')
#plt.show()


#Stats

n = []
for i in range(1, len(sini)) :
    n.append(sini[i]/sinr[i])
print(n)

nmoy = np.average(n)
un = np.std(n)

print('nmoy =', nmoy,' et un =', un)
