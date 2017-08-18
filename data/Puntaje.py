# -*- encoding: utf-8 -*-
import pilasengine
import data


class Puntaje(object):
    """Representa un contador de Puntaje"""

    def __init__(self, pilas, jugador=None, texto='0', size = 30, x=0, y=0, color=pilasengine.colores.negro):

        self.instancia_jugador=jugador
        self.color = color
        self.valor = int(texto)
        self.texto=texto
        self.pilas = pilas
        #~ self.text=self.pilas.actores.Texto(self.texto,x,y,magnitud=size,fuente='./data/hollowpoint.ttf') 
        self.text=self.pilas.actores.Texto(self.texto,x,y,fuente='./data/hollowpoint.ttf') #FIXME -> magnitud error

    def definir(self, puntaje_variable = '0'):
        self.instancia_jugador.puntaje_obtenido=puntaje_variable
        self.texto = str(self.instancia_jugador.puntaje_obtenido)
        self.text.texto=self.texto

    def setAumentar(self,value):
        _puntos=self.instancia_jugador.puntaje_obtenido
        _puntos=_puntos+value
        self.instancia_jugador.puntaje_obtenido=_puntos
        self.texto = str(self.instancia_jugador.puntaje_obtenido)
        self.text.texto=self.texto


    def setDisminuir(self,value):
        _puntos=self.instancia_jugador.puntaje_obtenido
        _puntos=_puntos-value
        self.instancia_jugador.puntaje_obtenido=_puntos
        self.texto = str(self.instancia_jugador.puntaje_obtenido)
        self.text.texto=self.texto
        self.text.color= self.pilas.colores.rojo
        self.text.escala=[1.8],1.5
        tarea=self.pilas.mundo.agregar_tarea (1.5,self.retornar)

    def puntos (self):
        return int (self.text.texto)

    def retornar(self):
        self.text.color=self.pilas.colores.blanco
        self.text.escala=[1],1


    def _setZ(self,z):
        self.text.z=z

    z= property(fset=_setZ)

    aumentar= property (fset=setAumentar)
    disminuir=property (fset=setDisminuir)
    puntos = property (fget=puntos)

iniciar=Puntaje





