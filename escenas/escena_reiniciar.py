__author__ = 'cristian Steib'
import pilasengine
import data
import escenas


class Reiniciar(pilasengine.escenas.Escena):
    def __init__(self, instancia_jugador):
        pilas.escena.Base.__init__(self)
        self.jugador = instancia_jugador

    def iniciar(self):
        self.fondo = pilas.fondos.Fondo("./imag/Interfaz/fondo.png")
        self.reiniciar = pilas.actores.Actor(imagen='./imag/Interfaz/pregreinicair.png')
        self.si = pilas.actores.Boton(x=-200, y=-50, ruta_normal='./imag/Interfaz/reinsioff.png',
                                      ruta_press='./imag/Interfaz/reinsipress.png')
        self.si.conectar_sobre(self.si.pintar_presionado)
        self.si.conectar_normal(self.si.pintar_normal)
        self.si.conectar_presionado(self.sii)
        self.no = pilas.actores.Boton(x=200, y=-50, ruta_normal='./imag/Interfaz/reinnooff.png',
                                      ruta_press='./imag/Interfaz/reinnopress.png')
        self.no.conectar_sobre(self.no.pintar_presionado)
        self.no.conectar_normal(self.no.pintar_normal)
        self.no.conectar_presionado(self.noo)
        self.pulsa_tecla_escape.conectar(self.atras)

    def atras(self, evento):
        pilas.recuperar_escena()

    def noo(self):
        pilas.recuperar_escena()

    def sii(self):
        self.jugador.nivel = 0
        self.jugador.deletedatos()
        pilas.cambiar_escena(escenas.escena_juego.iniciar(self.jugador, 'newlevel'))


iniciar = Reiniciar
