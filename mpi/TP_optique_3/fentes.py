import matplotlib.pyplot as plt
import numpy as np

D = [40,50,60,70,80,90,100,110,120]
R =[0.4, 0.5, 0.6, 0.65, 0.8, 0.9, 1, 1.15,1.25]

plt.title("R en fonction de D")

plt.plot(D,R, 'r+')
plt.xlabel("D")
plt.ylabel("R")
uy = 0.1
plt.errorbar(D, R, xerr = 0, yerr = uy, fmt = 'o')
plt.grid()




model = np.polyfit(D, R, 1)
#print(model)

ymodel = model[0]*(np.array(D)) + model[1]

b = 650*10**(-7) / model[0]
print("b = ", b)
zscore = (60*10**(-6) - b*10**(-2))/ (uy/100)
print("zscore = ", zscore)


plt.plot(D, ymodel, 'b:')
plt.show()