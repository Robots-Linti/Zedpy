__author__ = 'cristian Steib'

import pilasengine
import data
class datosplayer():
    def __init__(self,instancia_jugador):
        self.jugador=instancia_jugador
        print "En init de datosplayer"
        self.tiempo_total()
        
    def puntajetotal(self): 
        total=0
        x=self.jugador.nivelmax
        for r in range(0,x+1):
            self.jugador.niveldatos=r
            total=total+self.jugador.puntaje_obtenido
        return total

    def tiempo_total(self):

        x=self.jugador.nivelmax
        print "En tiempo total de datosplayer"
        self.jugador.niveldatos=0 #FIXME?
        print "Despues de nivel datos asignado"
        total=(self.jugador.tiempo_fin-self.jugador.tiempo_inicio)
        for r in range(2,x+1):
            self.jugador.niveldatos=r
            total=(self.jugador.tiempo_fin-self.jugador.tiempo_inicio)  #FIX ME
        print "Despues de nivel datos asignado"
        return total

        
iniciar=datosplayer
