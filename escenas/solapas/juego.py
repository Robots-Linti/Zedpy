__author__ = 'cristianSteib'

import pilasengine
import data


class OpcionJuego():
    fuente = './escenas/interfazusuario/AGENCYB.TTF'

    def __init__(self, config):
        self.config = config
        self._tiempomax()
        self._tiempodescuento()
        self._factorbombas()
        self._maxbomb()
        self._puntosbomb()
        self._puntostiempo()
        self._puntoscolision()

    def _tiempomax(self):
        self.txt_tiempomax = pilas.actores.Texto('Tiempo Maximo(seg) para llegar al final:', x=-250, y=500,
                                                 fuente=self.fuente, magnitud=30)
        self.tiempomax = pilas.interfaz.IngresoDeTexto(str(self.config.tiempomaximo), x=-400, y=440, ancho=100)
        self.tiempomax.escala = 2

    def _tiempodescuento(self):
        self.txt_tiempodescuento = pilas.actores.Texto('Tiempo Descuento (cada X seg se descuenta puntaje):', x=-165,
                                                       y=360, fuente=self.fuente, magnitud=30)
        self.tiempodescuento = pilas.interfaz.IngresoDeTexto(str(self.config.tiempodescuento), x=-400, y=300, ancho=100)
        self.tiempodescuento.escala = 2

    def _factorbombas(self):
        self.txt_factorbombas = pilas.actores.Texto('Factor multiplicador de bombas por nivel (1.4):', x=-200, y=-210,
                                                    fuente=self.fuente, magnitud=30)
        self.factorbombas = pilas.interfaz.IngresoDeTexto(str(self.config.fmb), x=-400, y=-270, ancho=100)
        self.factorbombas.escala = 2

    def _maxbomb(self):
        self.txt_maxbomb = pilas.actores.Texto('Cantidad maxima de bombas (recomendado= 100):', x=-178, y=70,
                                               fuente=self.fuente, magnitud=30)
        self.maxbom = pilas.interfaz.IngresoDeTexto(str(self.config.bombasmax), x=-400, y=10, ancho=100)
        self.maxbom.escala = 2

    def _puntosbomb(self):
        self.txt_puntosbomba = pilas.actores.Texto('Puntaje restado por colision con bomba:', x=-245, y=-70,
                                                   fuente=self.fuente, magnitud=30)
        self.puntosbomba = pilas.interfaz.IngresoDeTexto(str(self.config.disminuirptosbomba), x=-400, y=-130, ancho=100)
        self.puntosbomba.escala = 2

    def _puntostiempo(self):
        self.txt_puntostiempo = pilas.actores.Texto('Puntaje restado cada X tiempo', x=-318, y=210, fuente=self.fuente,
                                                    magnitud=30)
        self.puntostiempo = pilas.interfaz.IngresoDeTexto(str(self.config.disminuirptostiempo), x=-400, y=150,
                                                          ancho=100)
        self.puntostiempo.escala = 2

    def _puntoscolision(self):
        self.txt_factcolision = pilas.actores.Texto('Factor X de vida restada por colision (nivel*X+5)', x=-190, y=-350,
                                                    fuente=self.fuente, magnitud=30)
        self.factcolision = pilas.interfaz.IngresoDeTexto(str(self.config.factcolision), x=-400, y=-410, ancho=100)
        self.factcolision.escala = 2

    def save(self):
        self.config.tiempomaximo = int(self.tiempomax.texto)
        self.config.tiempodescuento = int(self.tiempodescuento.texto)
        self.config.fmb = float(str(self.factorbombas.texto))
        self.config.bombasmax = int(self.maxbom.texto)
        self.config.disminuirptosbomba = int(self.puntosbomba.texto)
        self.config.disminuirptostiempo = int(self.puntostiempo.texto)
        self.config.factcolision = float(str(self.factcolision.texto))
        self.config.save_values()

    def delete(self):
        self.save()
        self.txt_tiempomax.eliminar()
        self.tiempomax.eliminar()
        self.txt_tiempodescuento.eliminar()
        self.tiempodescuento.eliminar()
        self.txt_factorbombas.eliminar()
        self.factorbombas.eliminar()
        self.txt_maxbomb.eliminar()
        self.maxbom.eliminar()
        self.txt_puntosbomba.eliminar()
        self.puntosbomba.eliminar()
        self.txt_puntostiempo.eliminar()
        self.puntostiempo.eliminar()
        self.txt_factcolision.eliminar()
        self.factcolision.eliminar()
