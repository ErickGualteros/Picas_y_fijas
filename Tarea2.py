from math import fabs, pi#Paquetes
import matplotlib.pyplot as plt
import numpy as np
print("Area y Perimetro de un circulo y un Cuadrado")
y1=float(input('Ingrese el valor de y1: '))
x1=float(input('Ingrese el valor de x1: '))
y2=float(input('Ingrese el valor de y2: '))
x2=float(input('Ingrese el valor de x2: '))
#radio de la circunferencia 
def rad(x1,x2,y1,y2):
  return np.sqrt((x2-x1)**2+(y2-y1)**2)
#Base
def base(x2,x1):
  if x2!=x1:
    return fabs(x1-x2) 
  else:
    x1+=x2
    return fabs(x1-x2) 
#Altura
def altura (y2,y1):
  if y2!=y1:
    return fabs(y1-y2) 
  else:
    y1+=y2
    return fabs(y1-y2) 

x=np.arange(-x1-rad(x1,x2,y1,y2),x1+rad(x1,x2,y1,y2),0.001)
y=np.sqrt(rad(x1,x2,y1,y2)**2-(x-x1)**2)+y1
yy=-np.sqrt(rad(x1,x2,y1,y2)**2-(x-x1)**2)+y1
### tamaño de la grafica
plt.figure(figsize=(7,7))
#dibuar circulo
plt.plot(x,y,color=(24/255,204/255,23/255))
plt.plot(x,yy,color=(24/255,204/255,23/255))
#pintar radio
plt.plot([x1,x2],[y1,y2])
#pintar el cuadrado
plt.plot([x1,x2,x2,x1,x1],[y1,y1,y2,y2,y1])
#pintar el punto
plt.scatter(x1,y1,color=(24/255,204/255,23/255))
plt.scatter(x2,y2,color=(24/255,204/255,23/255))
plt.title('Grafica del circulo y los cuadrados')
#dibujar cuadrado
plt.grid()
plt.savefig("grafica circulo.png",dpi=400)
#calculo de las distancias del circulo:
A=pi*rad(x1,x2,y1,y2)**2 #area
p=2*pi*rad(x1,x2,y1,y2) # perimetro del circulo
print('Radio del circulo= ',rad(x1,x2,y1,y2), '\n Perimetro del circulo= ',p, '\nArea del circulo= ',A) 

#cálculo de las distancias del rectangulo:
Ac=base(x2,x1)*altura (y2,y1)
pc=2*base(x2,x1)+2*altura (y2,y1)
print('El area del cuadrado es= ',Ac,'\n El perimetro del cuadrado es= ',pc)
plt.show()