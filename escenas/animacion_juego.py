__author__ = 'cristian'
import botones
import pilasengine
import robotlib
import data


class Animacion(object):
    imagen_actor_robot_1 = 'imag/Interfaz/Actor/robot2.png'
    imagen_actor_robot_2 = 'imag/Interfaz/Actor/robot3.png'
    imag_fuera_de_mapa = 'imag/Interfaz/fueradelmapa.png'

    def __init__(self, pilas):
        self.pilas = pilas
        self.config = data.Configuracion()

        self.robot_animacion = False
        self.robot = robotlib.Mover_Robot()


        # actor que es el led de abajo!
        self.placalcd = self.pilas.actores.Actor(imagen='imag/Interfaz/placalcd.png', x=-100, y=-2000)
        self.placalcd.escala = 1

        # actor que es la imageen de engranajes de la izquierda
        self.imag_engr_izq = self.pilas.actores.Actor(imagen='imag/Interfaz/Engraizq_1.png', x=-1820, y=1)
        self.imag_engr_izq.escala = 1
        self.fin_x_chapa = -1078


        # actor que es la imageen de engranajes de la derecha
        self.imag_engr_der = self.pilas.actores.Actor(imagen='imag/Interfaz/Engrader.png', x=1820, y=1)
        self.imag_engr_der.escala = 1
        self.fin_x_chapa_dercha = 955

        # ENGRANAJE 1 Que SE MUEVE
       
        imag_engranaje = self.pilas.imagenes.cargar('imag/Interfaz/engra1.png')
        #~ self.engranaje_1 = self.pilas.actores.Mono(imagen = imag_engranaje)
        self.engranaje_1 = self.pilas.actores.Actor(imagen = imag_engranaje)
        #~ self.engranaje_1.set_imagen()
        self.engranaje_1.x = 1670
        self.engranaje_1.y = -468
        imag_tele = self.pilas.imagenes.cargar_grilla('imag/Interfaz/tvmenor.png', 2)
        imag_tele.escala = 0.2
        self.tele = self.pilas.actores.Animacion(imag_tele, x=1820, y=180, ciclica=True, velocidad=50)


        # Joystick
        self.joystick = self.pilas.actores.Actor(imagen='imag/comando/Controles/jostick.png', x=949, y=-1085)


        # BOTON RUN
        self.boton_run = self.pilas.actores.Boton(x=820, y=-1085, ruta_normal='imag/comando/Controles/runoff.png',
                                                   ruta_press='imag/comando/Controles/runon.png',
                                                   ruta_over='imag/comando/Controles/runover.png')
        #~ self.boton_run.conectar_presionado(self.__run)
        self.boton_run.conectar_sobre(self.boton_run.pintar_sobre)
        self.boton_run.conectar_normal(self.boton_run.pintar_normal)



        # BOTON ROBOT
        self.boton_robot = self.pilas.actores.Boton(x=1100, y=-1085, ruta_normal='imag/comando/Controles/robotnul.png',
                                                     ruta_press='imag/comando/Controles/roboton.png',
                                                     ruta_over='imag/comando/Controles/robotover.png')
        self.boton_robot.conectar_presionado(self.__run)
        self.boton_robot.conectar_sobre(self.boton_robot.pintar_sobre)
        self.boton_robot.conectar_normal(self.boton_robot.pintar_normal)


        # actor que es la grilla
        self.imag_grilla = self.pilas.actores.Actor(imagen='imag/Interfaz/grilla.png', x=-140, y=1200)


        self.imag_fueradelmapa()  # se crea la imagen con transparencia 100% para que quede por debajo del robot

        


        # TAREA Y VARIABLES QUE SE ENCARGA DE GIRAR EL ENGRANAJE
        self.giro = 0
        self.engranaje_estado = True
        self.factor = 0
        self.velocidad = 1
        self.tarea_engranaje = self.pilas.tareas.agregar(0.01, self.girar_engranaje)
        self.tarea_stop_engranaje = self.pilas.tareas.agregar(1.6, self.stop_engranaje)

        self.botones = botones.Botones(self.pilas)


        if self.config.graficos == True and self.config.lvlup==False:
            self.pilas.utils.interpolar(self.placalcd,'y' ,-390, tipo='lineal', duracion=4)
            self.pilas.utils.interpolar(self.imag_engr_izq,'x',self.fin_x_chapa, tipo='lineal',  duracion=2)
            self.pilas.utils.interpolar(self.imag_engr_der, 'x', self.fin_x_chapa_dercha, tipo='lineal',  duracion=2)
            self.pilas.utils.interpolar(self.engranaje_1,'x',775, tipo='lineal', duracion=2)
            self.pilas.utils.interpolar(self.tele,'x',1100, tipo='lineal',  duracion=2)
            self.pilas.utils.interpolar(self.joystick,'y' ,-485, tipo='lineal',  duracion=2)
            self.pilas.utils.interpolar(self.boton_run,'y' ,-485, tipo='lineal',  duracion=2)
            self.pilas.utils.interpolar(self.boton_robot,'y' ,-485, tipo='lineal',  duracion=2)
            self.pilas.utils.interpolar(self.imag_grilla,'y' ,110, tipo='elastico',  duracion=4)
            # TAREA QUE HABILITA LOS BOTONES DE LOS NUMEROS Y COMANDOS
            #~ self.tarea_habilitar_botones = self.pilas.tareas.agregar_tarea(7, self.habilitar_botones)

            self.pilas.tareas.agregar(7, self.habilitar_botones)



        else:
            self.placalcd.y = -390
            self.imag_engr_izq.x = self.fin_x_chapa
            self.imag_engr_der.x = self.fin_x_chapa_dercha
            self.engranaje_1.x = 775
            self.tele.x = 1100
            self.joystick.y = -485
            self.boton_run.y = -485
            self.boton_robot.y = -485
            self.imag_grilla.y = 110
            self.imag_grilla.y = 110
            # TAREA QUE HABILITA LOS BOTONES DE LOS NUMEROS Y COMANDOS
            self.tarea_habilitar_botones = self.pilas.tareas.agregar(2, self.habilitar_botones)

    def __move_robot(self):
        # ACA ES DONDE SE MANDA LA LISTA CON LOS MOVIMIENTOS
        print ('intentado mover')
        self.robot.mover(self.lista_movimientos)
        print self.lista_movimientos

    def habilitar_boton_robot(self, instancia_botones):
        self.lista_movimientos = instancia_botones.get_movimientos()
        self.boton_robot.conectar_presionado(self.__move_robot)
        self.boton_robot.conectar_sobre(self.boton_robot.pintar_sobre)
        self.boton_robot.conectar_normal(self.boton_robot.pintar_presionado)

    def deshabilitar_boton_robot(self):
        self.boton_robot.conectar_presionado(self.__run)  # no hace nada run tiene un pass
        self.boton_robot.conectar_sobre(self.boton_robot.pintar_normal)
        self.boton_robot.conectar_normal(self.boton_robot.pintar_normal)

    def _fueradelmapatransparencia(self):
        self.trans = self.trans - 1
        self._fuera_del_mapa.transparencia = self.trans
        if self.trans < 0:
            return False
        else:
            return True

    def imag_fueradelmapa(self):
        # primero creo la imagen ., por una cuestion de superposicion de las cosas
        self._fuera_del_mapa = self.pilas.actores.Actor(imagen=self.imag_fuera_de_mapa, x=-140, y=80)
        self._fuera_del_mapa.z = -5
        self.trans = 100
        self._fuera_del_mapa.transparencia = 100

    def fueradelmapa(self):
        tarea_transparencia = self.pilas.tareas.agregar(0.01, self._fueradelmapatransparencia)

    def __run(self):
        #~ pass
        print self.lista_movimientos

    def alternar_animacion_robot(self, r):
        if self.robot_animacion == False:
            #~ r.set_imagen(self.imagen_actor_robot_1)
            r.imagen = self.imagen_actor_robot_1
            self.robot_animacion = True
            return True

        else:
            self.robot_animacion = False
            #~ r.set_imagen(self.imagen_actor_robot_2)
            r.imagen = self.imagen_actor_robot_2
            return True

    def getInstanciaBotones(self):
        return self.botones

    def stop_engranaje(self):
        self.factor = 0.001
        return False

    def girar_engranaje(self):

        if self.velocidad >= 0:
            self.velocidad = self.velocidad - self.factor
            self.giro = self.giro + self.velocidad
            self.engranaje_1.rotacion = self.giro

            if self.giro == 360:
                self.giro = 0
            return True
        else:
            return False

    def habilitar_botones(self):
        self.botones.habilitar_botones(True)
        return False
        
    #~ def connect_movimientos(self, ejuego):
		#~ self.boton_run.conectar_presionado(ejuego.__realizar_movimiento)
