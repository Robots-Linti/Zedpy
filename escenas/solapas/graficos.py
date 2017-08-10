__author__ = 'cristian Steib'
import pilasengine
import data

class Graficos():
    fuente = './escenas/interfazusuario/AGENCYB.TTF'


    def __init__(self,config):

        self.config=config
        self.x=-480
        self.y=400
        self.graf=pilas.actores.Actor (x=self.x,y=self.y,imagen='./imag/Interfaz/solapas/cuadro.png')
        self.tick=pilas.actores.Actor (x=self.x,y=self.y,imagen='./imag/Interfaz/solapas/tilde.png')
        self.tick.escala=0
        self.txt=pilas.actores.Texto('Animaciones' ,x=self.x+180,y=self.y,magnitud=35,fuente=self.fuente)

        self.graf.cuando_hace_click= self.alternar_seleccion

        if self.config.graficos==True:
            self.tick.escala=1
            self.seleccion=True
        else:
            self.deseleccionar()



    def seleccionar(self):
        self.seleccion=True
        self.tick.escala=[1],0.3

    def deseleccionar(self):
        self.seleccion=False
        self.tick.escala=[0],0.2



    def alternar_seleccion(self,evento):
        if self.seleccion:
            self.deseleccionar()
        else:
            self.seleccionar()



    def save(self):
        self.config.graficos=self.seleccion
        self.config.save_values()
    def delete(self):
        self.save()
        self.graf.eliminar()
        self.txt.eliminar()
        self.tick.eliminar()
