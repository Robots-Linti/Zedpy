__author__ = 'cristian'

import data
import pilasengine
import solapas

class Opciones(pilasengine.escenas.Escena):
    imag_panel='./imag/Interfaz/panelopciones.png'
    imag_fondo='./imag/Interfaz/fondo.png'
    fuente='./escenas/interfazusuario/AGENCYB.TTF'

    solaparobot1='./imag/Interfaz/solapas/roboton.png'
    solaparobot2='./imag/Interfaz/solapas/robotoff.png'
    solapajuego1='./imag/Interfaz/solapas/juegoon.png'
    solapajuego2='./imag/Interfaz/solapas/juegooff.png'
    solapamodo1='./imag/Interfaz/solapas/modoon.png'
    solapamodo2='./imag/Interfaz/solapas/modooff.png'
    solapasonido1='./imag/Interfaz/solapas/sonidoon.png'
    solapasonido2='./imag/Interfaz/solapas/sonidooff.png'
    solapagrafico1='./imag/Interfaz/solapas/graficoson.png'
    solapagrafico2='./imag/Interfaz/solapas/graficosoff.png'


    def iniciar(self):
        ##########################INTERFAZ GRAFICA############################################

        self.config=data.Manager_config.Configuracion()
        
        self.fondo = pilas.fondos.Fondo(self.imag_fondo)
        self.imagen_consola_usuarios = pilas.actores.Actor(self.imag_panel, x=0, y=50)
        self.btn_robot=pilas.actores.Actor(self.solaparobot1,x=-424,y=600)
        self.btn_robot.cuando_hace_click=self.robot

        self.btn_juego= pilas.actores.Actor (x=-210,y=600,imagen=self.solapajuego2)
        self.btn_juego.cuando_hace_click=self.juego

        self.btn_modo= pilas.actores.Actor (x=2,y=600,imagen=self.solapamodo2)
        self.btn_modo.cuando_hace_click=self.modolibre

        self.btn_sonidos= pilas.actores.Actor (x=213,y=600,imagen=self.solapasonido2)
        self.btn_sonidos.cuando_hace_click=self.sonidos

        self.btn_graficos= pilas.actores.Actor (x=426,y=600,imagen=self.solapagrafico2)
        self.btn_graficos.cuando_hace_click=self.graficos

        #########################FIN INTERFAZ GRAFICA ########################################

        self.opcion=solapas.OpcionRobot(self.config)
        #self.robot()
        self.pulsa_tecla_escape.conectar(self.ir_a_escena_anterior)





    def robot (self):
        self.btn_robot.imagen=self.solaparobot1
        self.btn_juego.imagen=self.solapajuego2
        self.btn_modo.imagen=self.solapamodo2
        self.btn_sonidos.imagen=self.solapasonido2
        self.btn_graficos.imagen=self.solapagrafico2
        self.opcion.delete()
        self.opcion=solapas.OpcionRobot(self.config)


    def juego (self):
        self.btn_robot.imagen=self.solaparobot2
        self.btn_juego.imagen=self.solapajuego1
        self.btn_modo.imagen=self.solapamodo2
        self.btn_sonidos.imagen=self.solapasonido2
        self.btn_graficos.imagen=self.solapagrafico2
        self.opcion.delete()
        self.opcion=solapas.OpcionJuego(self.config)


    def modolibre (self):
        self.btn_robot.imagen=self.solaparobot2
        self.btn_juego.imagen=self.solapajuego2
        self.btn_modo.imagen=self.solapamodo1
        self.btn_sonidos.imagen=self.solapasonido2
        self.btn_graficos.imagen=self.solapagrafico2
        self.opcion.delete()


    def graficos(self):
        self.btn_robot.imagen=self.solaparobot2
        self.btn_juego.imagen=self.solapajuego2
        self.btn_modo.imagen=self.solapamodo2
        self.btn_sonidos.imagen=self.solapasonido2
        self.btn_graficos.imagen=self.solapagrafico1
        self.opcion.delete()
        self.opcion=solapas.Graficos(self.config)


    def sonidos(self):
        self.btn_robot.imagen=self.solaparobot2
        self.btn_juego.imagen=self.solapajuego2
        self.btn_modo.imagen=self.solapamodo2
        self.btn_sonidos.imagen=self.solapasonido1
        self.btn_graficos.imagen=self.solapagrafico2
        self.opcion.delete()


    def ir_a_escena_anterior(self, evento):
        self.opcion.delete()
        pilas.recuperar_escena()

iniciar = Opciones
