import matplotlib.pyplot as plt
import numpy as np

dtheta = [0,10,20,30,40,50,60,70,80,90]
R =[0.4,0.5,0.6,0.68,0.8,0.9,1,1.15,1.25]

cos_2_theta = [np.cos(i*np.pi/180)**2 for i in dtheta ]
i = [(k/(10**3))/(100*10**3) for k in u]


plt.title("i en fonction de cos^(theta)")

plt.plot(cos_2_theta,i, 'r+')
plt.xlabel("cos")
plt.ylabel("i")
uy = 10**(-8)
plt.errorbar(cos_2_theta, i, xerr = 0, yerr = np.sqrt(3)*uy, fmt = 'o')
plt.grid()




model = np.polyfit(cos_2_theta, i, 1)
#print(model)

ymodel = model[0]*(np.array(cos_2_theta)) + model[1]
plt.plot(cos_2_theta, ymodel, 'b:')
plt.show()