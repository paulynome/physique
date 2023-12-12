import numpy as np
import scipy.optimize as sc

# Conditions initiales :
g = 9.8 # en m/s²
m = 1.0 # en kg
v0 = 10 # en m/s
alpha_degre = 50 # en °
lam = 0.20 # en kg/s
tau = m/lam # en s⁻¹

alpha = np.radians(alpha_degre) # en radiant

def dicho(f, a, b, eps) :
	if f(a)*f(b) > 0:
		return None
	while abs(b-a) > eps :
		c = (a+b) /2
		if f(a) * f(c) > 0:
			a = c
		else:
			b = c
	return a,b

def z(t) :
	return (-g*m*t)/lam + (m/lam) * (v0 * np.sin(alpha) + (m*g)/lam) * (1 - np.exp(-t/tau))

def x(t) :
	return ((v0*m)/lam) * np.cos(alpha) * (1 - np.exp(-t/tau))

res = dicho(z,0.5,20,0.01)
moy = round(((res[0] + res[1]) / 2), 3)

print("Date t à laquelle z(t) = 0 : ", moy , " s")
print("Portée x : ", round(x(moy),3), " m")

# Avec bisect
res = sc.bisect(z, 0.5, 20)
print("Date t à laquelle z(t) = 0 : ", round(res,3) , " s")
print("Portée x : ", round(x(res),3), " m")