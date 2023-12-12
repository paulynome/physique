import matplotlib.pyplot as plt
import numpy as np

i=[0,10,20,30,40,50,60,70,80]
i2=[0, -9, -19, -29, -39, - 49, -59, -69, - 78]

plt.title("i' en fonction de i")

plt.plot(i,i2, color="red")
plt.xlabel('i (°)')
plt.ylabel("i (°)'")

plt.grid()


plt.show()

model = np.polyfit(i, i2, 1)
print(model)