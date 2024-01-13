import matplotlib.pyplot as plt
import numpy as np

D = [400,500,600,700,800,900,1000,1100,1200]
R =[4, 5, 6, 6.5, 8, 9, 10, 11.5,12.5]

plt.title("R en fonction de D")

plt.plot(D,R, 'r+')
plt.xlabel("D")
plt.ylabel("R")
uy = 1
plt.errorbar(D, R, xerr = 0, yerr = uy, fmt = 'o')
plt.grid()




model = np.polyfit(D, R, 1)
#print(model)

ymodel = model[0]*(np.array(D)) + model[1]

b = 650*10**(-9) / model[0]
print("b = ", b)
zscore = (60*10**(-6) - b*10**(-2))/ (uy/100)
print("zscore = ", zscore)


plt.plot(D, ymodel, 'b:')
plt.show()