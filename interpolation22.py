import numpy as np
from scipy.interpolate import splev,splrep,InterpolatedUnivariateSpline,lagrange
import matplotlib.pyplot as pl

x=[0,1,2,3,4,5]
y=[1.0,2.0,1.0,0.5,4.0,8.0]

x_p=np.linspace(0,5,50)

a=InterpolatedUnivariateSpline(x,y)
b=splrep(x,y,k=2)
c=splrep(x,y,k=3)
d=lagrange(x,y)

y1=a(x_p)
y2=splev(x_p,b)
y3=splev(x_p,c)
y4=d(x_p)

print("lagrange polynomial is",d,".")

pl.plot(x,y,"k*",x_p,y1,"c-",x_p,y2,"m--",x_p,y3,"g--",x_p,y4,"b--")
pl.legend(['given data','linear spline','quadratic spline','cubic spline','lagrange interpolation'])
pl.show()
