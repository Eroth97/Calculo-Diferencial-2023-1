from manim import *
import numpy as np

def cubica(numero):
    if numero < 0:
        numero = abs(numero)
        return (-1)*(numero**(1/3))
    else: 
        return numero**(1/3)
    
eje_X = np.array([-1, -0.8, -0.6, -0.4, -0.2, -0.1, -0.01, -0.00001, -0.000000000001])
funcion = lambda x: ((-1)*(cubica(x)**2))+2
derivada = lambda x: (-2/3)*(cubica(x)**(-1))

eje_Y, pendientes = np.empty([len(eje_X)]), np.empty([len(eje_X)])
for i in range(len(eje_X)):
  eje_Y[i] =  funcion(eje_X[i])
  pendientes[i] = derivada(eje_X[i])


class cuspide(Scene):        
    def construct(self):
        ejes = NumberPlane()

        nondev = ejes.plot_parametric_curve(
                lambda t: np.array([-t**3, -t**2 + 2, 0]),
                t_range = [-4, 4], 
                color = BLUE
        )
        
        puntos = VGroup()
        rectas = VGroup()
        
        for i in range(len(eje_X)):    
            puntos.add(Dot(np.array([eje_X[i], eje_Y[i], 0]), radius=0.04))
            rectas.add(ejes.plot_parametric_curve(
                        lambda t: np.array([t, ((pendientes[i])*(t-eje_X[i]))+eje_Y[i], 0]),
                        t_range = [-2, 2],
                        color = RED
            ))
        
  
        self.play(Create(nondev))
        for i in range(len(eje_X)):
            self.play(Create(puntos[i]))
            self.play(Create(rectas[i]))
            self.wait(2)
            self.play(FadeOut(puntos[i], rectas[i]))