import matplotlib.pyplot as plt
import numpy as np

D = [0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2]
R =[4*10**(-3), 5*10**(-3), 6*10**(-3), 6.5*10**(-3), 8*10**(-3), 9*10**(-3), 10*10**(-3), 11.5*10**(-3),12.5*10**(-3)]

plt.title("R en fonction de D")

plt.plot(D,R, 'r+')
plt.xlabel("D")
plt.ylabel("R")
ur = 1*10**(-3)
plt.errorbar(D, R, xerr = 0, yerr = ur, fmt = 'o')
plt.grid()
model = np.polyfit(D, R, 1)
#print(model)
ymodel = model[0]*(np.array(D)) + model[1]

b = 650*10**(-9) / model[0]
print("b = ", b)
plt.plot(D, ymodel, 'b:')
plt.show()

#calcul Z score
for i in range (9) : 
    Rreg = model[0] * D[i] 
    zscore = (R[i] - Rreg)/ur
    print("zscore = ", zscore)