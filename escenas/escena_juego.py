# -*- encoding: utf-8 -*-
import sys
import pilasengine
import data
import Generador_movimientos_mapa
import escenas
import lib
import random
try:
	import duinobot
except:
	print "Error al importar el modulo duinobot."


class EscenaDeJuego(pilasengine.escenas.Escena):
    
    def iniciar(self, instancia_jugador, estado):
        self.habilitado = True # boton robot
        self.jugador = instancia_jugador

        # levantamos la configuracion
        self.config = data.Manager_config.Configuracion()
        # se encarga de tomar los horarios y sacar la diferencia
        self.control_tiempo = lib.Tiempo()
        self.en_pausa = False

        self.puntaje_max = 1000 * self.jugador.nivel

        if self.jugador.vida_start <= 0:
            estado = 'withoutlives'

        if estado == 'newlevel' or estado== 'existe':
            '''
            si comienza un nivel nuevo , entonces se esablecen los siguientes datos
            para la clase jugador.
             Hay que tener en cuenta que al avanzar de  nivel hay que almacenar los datos
            del nivel anterior, luego aumentar el nivel ,y volver a inicializar algunos de  los datos que
            estan en las variables.


            '''
            if estado == 'newlevel':
                self.jugador.tiempo_fin = self.control_tiempo.actual()
                self.jugador.SaveDatosNivel()
                self.jugador.save()
            # inicia el nuevo nivel

            self.jugador.nivel = self.jugador.nivel + 1
            '''
            se inicializa las vidas del jugador , de acuerdo al total que halla perdido en el nivel anterior ,y
            ademas se le regala una vida por haber pasado de nivel
            '''
            self.jugador.vida_start = (self.jugador.vida_start - self.jugador.vida_lost) + 1
            if self.jugador.vida_start>10:
                self.jugador.vida_start=10 # limite de vidas
            self.jugador.tiempo_minimo = self.config.tiempomaximo
            self.jugador.cantidad_caidas = 0
            self.jugador.vida_lost = 0
            self.jugador.tiempo_inicio = self.control_tiempo.actual()
            self.jugador.cantidad_choques = 0
            self.jugador.movimientos_hechos = 0
            self.puntaje_max = 1000 * self.jugador.nivel
            self.jugador.puntaje_maximo = self.puntaje_max


        elif estado == 'fallmap':

            self.jugador.cantidad_caidas = self.jugador.cantidad_caidas + 1

            self.jugador.vida_lost = self.jugador.vida_lost + 1

            self.jugador.vida_start = self.jugador.vida_start - 1



            if self.jugador.vida_start <= 0:

                self.puntaje_max = 1000 * self.jugador.nivel
                self.jugador.puntaje_maximo = self.puntaje_max
                self.jugador.deletedatos()
                self.jugador.nivel = 1


        elif estado== 'sinvida':
            self.jugador.vida_lost = self.jugador.vida_lost + 1
            self.jugador.vida_start = self.jugador.vida_start - 1
            if self.jugador.vida_start <= 0:

                self.puntaje_max = 1000 * self.jugador.nivel
                self.jugador.puntaje_maximo = self.puntaje_max
                self.jugador.deletedatos()
                self.jugador.nivel = 1





        elif estado == 'withoutlives':

            self.jugador.deletedatos()
            self.jugador.nivel = 1
            self.puntaje_max = 1000 * self.jugador.nivel
            self.jugador.puntaje_maximo = self.puntaje_max



        self._pto_inicial()  # genera una posicion random en el mapa para el robot
        self._pto_final()  # genera otro punto pero para donde tiene que alcazar el robot
        self.movimientos = Generador_movimientos_mapa.iniciar(12, 15, self.pos_inicio[0])

        self.giro_ant = 0
        self.indi = 0
        self.giro = 0
        self.giro_real = [0, 0]
        self.indice = 0
        self.movtf = {}  # movimientos transformados a ej:{(1,1),(1,2)}
        self.fuera = False  # fuera del mapa?


    # Mueve mi actor a la posicion indicada  por una fila y columna
    
        self.fondo = self.pilas.fondos.Fondo("./imag/Fondo.jpg")
        self.animacion = escenas.Animacion(self.pilas)
        self.botones = self.animacion.getInstanciaBotones()
        self.__genera_matriz_grilla()
        print("+++++pase por matriz grilla++++++++")


        # actor robotaaaa
        try:
			self.b = duinobot.Board("/dev/tty/USB0")
        except:
			self.b = None
			#~ print "Error al conectarse al xBee"
        #~ self.rb = duinobot.Robot(self.b, 1)
        imagen = self.pilas.imagenes.cargar("imag/Interfaz/Actor/robot2.png")
        self.r = self.pilas.actores.Actor()
        self.r.imagen = imagen
        self.r.radio_de_colision = 5
        self.r.escala = 0
        #~ self.r.actor.eliminar_habilidad(self.pilas.habilidades.Arrastrable)
        self.tarea_animacion_robot = self.pilas.tareas.agregar(0.2, self.alternar_animacion_robot)


        if self.config.graficos==True  and self.config.lvlup==False:
            self.tarea_aparecer_todo = self.pilas.tareas.agregar(6, self._mostrar_robot)
        else:
            self.tarea_aparecer_todo = self.pilas.tareas.agregar(1, self._mostrar_robot)

        self.sonido = self.pilas.actores.Sonido()

        self.posicion_jugador = lib.Punto()
        self.posicion_jugador_ant = lib.Punto()
        self.posicion_jugador.punto = self.pos_inicio[0]  # Punto inicial de mi jugador
        self.mover(self.posicion_jugador.punto[0], self.posicion_jugador.punto[1])
        self.__direccionar_robot(0)  # mira para arriba

        self.pulsa_tecla_escape.conectar(self.__escape)
        # self.r.bajalapiz()

        self.config.lvlup=False
        self.config.save_values()
        self.animacion.habilitar_boton_robot(self.botones)

    def show_time(self):
        a = self.tiempo_final - self.control_tiempo.actual()
        if a.seconds == 0:
            self.tiempo.color = self.pilas.colores.rojo
            self.tiempo_final = self.control_tiempo.next_time(self.config.tiempodescuento)
            self.puntaje.disminuir = 100  # cada 15seg se empieza  disminuir el puntaje

        self.jugador.puntaje_obtenido = self.puntaje.puntos

        self.control_tiempo.finalizar_tiempo()
        t = self.control_tiempo.elapsed
        t = str(t)
        self.tiempo.texto = t[2:7]
        return True

    def _mostrar_robot(self):
        self.r.escala = [1], 0.9
        # Dibuja la bandera de fin , osea el objetivo
        self._dibujar_fin()
        self.dibujar_cajas()
        self.detecto_colision()
        self.dibujar_datos()
        self.tiempo.escala = [1], 1.5
        # TAREA QUE MUEVE EL PERSONAJE EN CADA MOMENTO QUE SE PRESIONA UN BOTON
        #~ self.tarea_mover = self.pilas.tareas.siempre(0.01, self.__realizar_movimiento)
        self.animacion.boton_run.conectar_presionado(self.__realizar_movimiento)
        #~ self.botones.connect_movimientos(self)

       #pilas.mundo.agregar_tarea_siempre(2, self._conexiones)
       #pilas.mundo.agregar_tarea_siempre(0.6, self._habilitar_boton_robot)


    def dibujar_datos(self):
        # texto que muestra el tiempo disponible
        self.tiempo = self.pilas.actores.Texto(x=1150, y=-50, magnitud=60, fuente='./data/hollowpoint.ttf')
        self.tiempo.color = self.pilas.colores.verde_transparente
        self.tiempo.escala = 0
        self.control_tiempo.iniciar_tiempo()
        self.tiempo_final = self.control_tiempo.next_time(self.config.tiempomaximo)
        self.tarea_tiempo = self.pilas.tareas.siempre(0.4, self.show_time)

        self.puntaje = data.Puntaje(self.pilas, x=1050, y=290, jugador=self.jugador, size=60)
        self.puntaje.z = -5
        # if self.jugador.nivel == 0:
        self.puntaje.definir(self.puntaje_max)

        self.barra_vida = self.pilas.actores.Energia(x=1130, y=415, progreso=100, ancho=400, alto=60)
        self.barra_vida.z = -6.5
        text = 'Nivel ' + str(self.jugador.nivel)
        self.t = self.pilas.actores.Texto(text, magnitud=70, fuente='./data/hollowpoint.ttf', x=1130, y=130)
        self.t.z = -5

        self.vidas=self.pilas.actores.Texto(x=1100, y=30, magnitud=60, fuente='./data/hollowpoint.ttf')
        self.vidas.texto='Vidas:'+str (self.jugador.vida_start)
        self.vidas.z=-5
        if self.jugador.vida_start == 1:
            self.vidas.color=self.pilas.colores.rojo

    def _dibujar_fin(self):
        coord = self.matrix.get_valor(self.pos_fin[0][0], self.pos_fin[0][1])
        imag_fin = self.pilas.imagenes.cargar_grilla('./imag/Interfaz/Actor/estrella.png', 2)
        self.imag_fin = self.pilas.actores.Animacion(imag_fin, x=coord[0], y=coord[1], ciclica=True, velocidad=10)
        self.imag_fin.escala=2
        self.imag_fin.escala=[1],2

    def __genera_matriz_grilla(self):
        # Matriz que representa la grilla
        # cada fila,columna , tiene su respectiva posicion dentro del mapa

        self.matrix = lib.Matriz(12, 15)

        y = -381.45

        for filas in range(0, 12):
            x = -755
            for columnas in range(0, 15):
                self.matrix.set_valor(filas, columnas, (x, y))
                x = x + 87.82
            y = y + 87.82

    def __obtener_movimientos(self):
        self.movimientos_sn_transformar = self.botones.get_movimientos()
        self.jugador.movimientos_hechos=len(self.movimientos_sn_transformar.keys())

    def __convertir_movimientos(self):
        # llama al modulo que se encarga de transformar los movimientos enviados
        # de la forma de tupla ej : ('avanzar',2) , [0]=sentido [1]=veces que repite el movimiento
        # se le envia la lista con todos esos movimientos [('avanzar',2),....] esa lista contiene
        # los movimientos sin transformarlos a los que realmente se necesitan para mover el actor en el mapa
        # previamente se obtiene la lista de self.movimientos_sin_transformar ,desde la funcion obtener_movimientos()

        self.movimientos.set_Movimientos(self.movimientos_sn_transformar)

    def __tarea_direccionar_robot(self):
        """esta tarea es mas que nadda para que se produzca un delay ,entre que termina el actor de llegar a su posicion
        y luego que gire hacia la orientacion que le corresponde"""
        self.__direccionar_robot(self.giro_ant)
        return False

    def __direccionar_robot(self, value):
        # simplemente recibe un valor , del 1 al 4 ,para que el robot apunte correctamente .
        #    0=Apunta ARRIBA
        #    1=Apunta IZQUIERDA
        #    2=Apunta ABAJO
        #    3=Apunta DERECHA

        if value == 0:
            self.r.rotacion = 180  # 180
        elif value == 1:
            self.r.rotacion = 90  # 90
        elif value == 2:
            self.r.rotacion = 0  # 0
        elif value == 3:
            self.r.rotacion = 270  # 270

        self.giro_ant = value

        # (-1,-1) es la condicion para que no tome datos viejos

    def alternar_animacion_robot(self):
        self.animacion.alternar_animacion_robot(self.r)
        return True

    def _posiciones_aleatorias_cajas(self):
        """
          [(fila,columna),(fila,columna)] * cntidad_obstcls_nivl
            se tiene en cuenta que almenos no tenga un obstaculo por delante o por los costados
            en el comienzo del robot , y tambien con respecto al punto final

        """

        n = 5
        for x in range(0, self.jugador.nivel):
            n = n * self.config.fmb  # fmb  es factor de multiplicacion de bombas  ideal 1.4

        n = int(n)
        if n > 100:
            n = 100
        self.lista_pos_obstaculos = [(random.randrange(0, 12, 1), random.randrange(0, 15, 1)) for x in
                                     range(0, n)]  # TODO: sumar x el n de nivel

        for elem in self.lista_pos_obstaculos:
            self.lista_pos_obstaculos.remove(elem) if self.lista_pos_obstaculos.count(elem) > 1 else None

        for elem in self.lista_pos_obstaculos:
            self.lista_pos_obstaculos.remove(elem) if self.pos_inicio[0][0] == elem[0] and self.pos_inicio[0][1] == \
                                                                                           elem[
                                                                                               1] else None  # QUE NO HAYA OBSTACULO EN EL MISMO LUGAR DONDE NACE EL ROBOT

        for elem in self.lista_pos_obstaculos:
            self.lista_pos_obstaculos.remove(elem) if self.pos_inicio[0][0] == elem[0] and self.pos_inicio[0][1] + 1 == \
                                                                                           elem[
                                                                                               1] else None  # QUE NO HAYA OBSTACULO POR LOS COSTADOS DE LA POS INICIAL

        for elem in self.lista_pos_obstaculos:
            self.lista_pos_obstaculos.remove(elem) if self.pos_inicio[0][0] == elem[0] and self.pos_inicio[0][1] - 1 == \
                                                                                           elem[
                                                                                               1] else None

        for elem in self.lista_pos_obstaculos:
            self.lista_pos_obstaculos.remove(elem) if self.pos_inicio[0][0] + 1 == elem[0] and self.pos_inicio[0][1] == \
                                                                                               elem[
                                                                                                   1] else None  # QUE NO HAYA OBTACULO POR DELANTE DE LA POS INICIAL

        for elem in self.lista_pos_obstaculos:
            self.lista_pos_obstaculos.remove(elem) if self.pos_fin[0][0] == elem[0] and self.pos_fin[0][1] == elem[
                1] else None

        for elem in self.lista_pos_obstaculos:
            self.lista_pos_obstaculos.remove(elem) if self.pos_fin[0][0] == elem[0] and self.pos_fin[0][1] + 1 == elem[
                1] else None

        for elem in self.lista_pos_obstaculos:
            self.lista_pos_obstaculos.remove(elem) if self.pos_fin[0][0] == elem[0] and self.pos_fin[0][1] - 1 == elem[
                1] else None

        for elem in self.lista_pos_obstaculos:
            self.lista_pos_obstaculos.remove(elem) if self.pos_fin[0][0] - 1 == elem[0] and self.pos_fin[0][1] == elem[
                1] else None

        return self.lista_pos_obstaculos

    def dibujar_cajas(self):
        posiciones = self._posiciones_aleatorias_cajas()
        coordenadas = []
        self.lista_cajas = []
        for pos_matriz in posiciones:
            coordenadas.append(self.matrix.get_valor(pos_matriz[0], pos_matriz[1]))
        for coord in coordenadas:
            caja = self.pilas.actores.Bomba()
            caja.escala = [0]
            caja.x = coord[0]
            caja.y = coord[1]
            caja.escala = [1], 1
            self.lista_cajas.append(caja)

    def detecto_colision(self):
       self.pilas.escena_actual().colisiones.agregar(self.r, self.lista_cajas, self.crash)

    def crash(self, robot, caja):
        self.puntaje.disminuir = 250
        self.barra_vida.progreso = self.barra_vida.progreso - 10
        self.jugador.cantidad_choques = self.jugador.cantidad_choques + 1
        caja.eliminar()

    # Mueve mi actor a la posicion indicada  por una fila y columna
    def mover(self, fila, columna):
        # Primero se busca la coordenada correspopndiente dentro de la matriz , para luego posicionar el actor
        # el paramentro de entrada es un Numero de de Fila y otro de columna

        self.coordenada = self.matrix.get_valor(fila, columna)
        self.pilas.utils.interpolar(self.r, 'x', self.coordenada[0], 0.3)
        self.pilas.utils.interpolar(self.r, 'y', self.coordenada[1], 0.3)
        self.posicion_jugador_ant.punto = self.coordenada


        # ESTE METODO , PERTENCE A UNA TAREA QUE SE EJECUTA CICLICAMENTE , SIN FIN , PARA IR HACIENDO LO QUE SE VA INDICANDO

        # EN LOS BOTONES

    def _pto_inicial(self):
        """
        posicion random para el comienzo del jugador
        """
        self.pos_inicio = [(0, random.randrange(0, 15, 1))]
        #####################################################################################
        while self.pos_inicio == [(0, 10)] or self.pos_inicio == [
            (0, 3)]:  ### en 0,3 y 0,10 falla, suponemos que es pilas
            self.pos_inicio = [(0, random.randrange(0, 15, 1))]  ###  parche para solucionarlo
        ######################################################################################
        print 'Posicion Inicial:{}'.format(self.pos_inicio[0])

    def _pto_final(self):
        self.pos_fin = [(11, random.randrange(0, 15, 1))]
        print 'Posicion Final:{}'.format(self.pos_fin[0])

    def _avanzar_nivel(self):
        """
        funcion para avanzar el numero de nivel y de 'escenario'
        guardando todos los datos de ese nivel


        """

    def __realizar_movimiento(self):

        # self.posicion_jugador tiene la instancia de Punto , con la coordenada donde esta ubicado mi actor
        self.__obtener_movimientos()
        self.__convertir_movimientos()
        self.movtf = self.movimientos.get_Movimientos()
        giro = self.botones.getGiro()  # obtengo una tupla (+-1, si es -1 no hay que realizar giro)
        self.giro_real[0] = self.giro_real[0] + giro[0]
        self.giro_real[1] = giro[1]
        
        #~ print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
        #~ print self.movimientos.get_Movimientos()
        #~ print self.indice
        #~ print giro
        #~ print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||"

        #~ while ():
        if self.movtf.has_key(self.indice):
            #~ print "if 1"

            if self.barra_vida.progreso <= 0:
                #~ print "if 2"
                tex = self.pilas.actores.Texto('TE HAS QUEDADO SIN VIDA  :(', magnitud=130, fuente='./data/hollowpoint.ttf')
                tex.color = self.pilas.colores.rojo
                tarea_recomenzar = self.pilas.tareas.agregar(1, self._recomenzarsnvida)

            if self.movtf[self.indice] <> False:
                #~ print "if 3"
                self.__direccionar_robot(self.movtf[self.indice][2])

            if self.movtf[self.indice] <> False:
                #~ print "if 4"
                tupla = (self.movtf[self.indice][0], self.movtf[self.indice][1])
                if self.r.x == self.posicion_jugador_ant.x and self.r.y == self.posicion_jugador_ant.y:  # espero a terminar la interpolacion para avanzar el actor
                    #~ print "if 5"

                    self.posicion_jugador.punto = tupla
                    # self.posicion_jugador_ant.punto = tupla
                    self.mover(self.posicion_jugador.punto[0], self.posicion_jugador.punto[1])
                    self.indice = self.indice + 1
                    #~ self.__realizar_movimiento()

                    if tupla[0] == self.pos_fin[0][0] and tupla[1] == self.pos_fin[0][1]:  # aca llega a la posicion final
                        print 'You Win'
                        self.config.lvlup=True
                        self.config.save_values()
                        tarea_recomenzar = self.pilas.tareas.agregar(0.5, self._recomenzar)
                    else:
                        print "DE NUEVO"
                        #~ self.pilas.tareas.agregar(0.5, self.__realizar_movimiento)
                        self.pilas.tareas.una_vez(0.5, self.__realizar_movimiento)
                #~ else:
                    #~ self.__realizar_movimiento()
                        
            elif self.movtf[self.indice] == False and self.fuera == False:  # SE FUE DEL MAPA
                #~ print "if 7"

                tarea_recomenzar = self.pilas.tareas.agregar(1.5, self._recomenzarfall)  # tareapara volver a arrancar

                self.animacion.fueradelmapa()
                self.__caer_robot_mapa()

                print ('Has caido del mapa')
                self.r.escala = [0], 1
                self.fuera = True
                

        #Esto que sigue sirve? Pareciera siempre valer lo mismo.
        elif giro[1] >= 0:
            #~ print "if 8"
            if giro[0] > 0:  # +1 gira a la derecha
                for i in range(0, giro[1]):
                    self.giro_ant = self.giro_ant + giro[0]
                    self.giro_ant = self.giro_ant % 4
                    self.tarea_aparecer_robot = self.pilas.tareas.agregar(0.15, self.__tarea_direccionar_robot)
                    self.botones.setGiro()
            else:  # -1 gira a la izquierda
                for i in range(0, giro[1]):
                    self.giro_ant = self.giro_ant + giro[0]
                    self.giro_ant = self.giro_ant % 4
                    self.tarea_aparecer_robot = self.pilas.tareas.agregar(0.15, self.__tarea_direccionar_robot)
                    self.botones.setGiro()
        #~ self.__realizar_movimiento()
        
        return True

    def __caer_robot_mapa(self):
        if self.r.x == self.posicion_jugador_ant.x and self.r.y == self.posicion_jugador_ant.y:  # espero a q termine la ultima interpolacion
            if self.r.x > 0 and self.r.y > 0:
                print self.r.x, self.r.y
                self.pilas.utils.interpolar(self.r, 'x', 200, tipo='lineal', duracion=2)
                self.pilas.utils.interpolar(self.r, 'y', 200, tipo='lineal', duracion=2)
            if self.r.x < 0 and self.r.y > 0:
                print self.r.x, self.r.y
                self.pilas.utils.interpolar(self.r, 'x', -200, tipo='lineal', duracion=2)
                self.pilas.utils.interpolar(self.r, 'y', 200, tipo='lineal', duracion=2)

            if self.r.x > 0 and self.r.y < 0:
                print self.r.x, self.r.y
                self.pilas.utils.interpolar(self.r, 'x', 200, tipo='lineal', duracion=2)
                self.pilas.utils.interpolar(self.r, 'y', -200, tipo='lineal', duracion=2)

            if self.r.x < 0 and self.r.y < 0:
                print self.r.x, self.r.y
                self.pilas.utils.interpolar(self.r, 'x', -200, tipo='lineal', duracion=2)
                self.pilas.utils.interpolar(self.r, 'y', 200, tipo='lineal', duracion=2)

    def __escape(self, evento):

        #~ self.pilas.almacenar_escena(escenas.escena_menu_q.iniciar(self.jugador))
        #~ self.pilas.escenas.EscenaMenuq(self.jugador)
        #~ self.pulsa_tecla_escape.deshabilitar()
        if not(self.en_pausa):
			self.control_tiempo.startPause()
			self.en_pausa = True
			self.tarea_tiempo.terminar()
			self.prueba_fea = self.pilas.actores.Actor(imagen="./imag/Interfaz/fondo.png")
			self.boton_reanudar=self.pilas.actores.Boton(x=-740,y=200,ruta_normal='imag/escmenu/reanudar1.png', ruta_press='imag/escmenu/reanudar2.png', ruta_over='imag/escmenu/reanudar2.png')
			self.boton_reanudar.conectar_presionado(self.eliminar_pausa)
			self.boton_reanudar.conectar_sobre(self.boton_reanudar.pintar_presionado)
			self.boton_reanudar.conectar_normal(self.boton_reanudar.pintar_normal)
			self.boton_salir = self.pilas.actores.Boton(x=-740, y=-370, ruta_normal='imag/escmenu/salir1.png',
														 ruta_press='imag/escmenu/salir2.png', ruta_over='imag/escmenu/salir2.png')
			self.boton_salir.conectar_presionado(self.salir)
			self.boton_salir.conectar_sobre(self.boton_salir.pintar_presionado)
			self.boton_salir.conectar_normal(self.boton_salir.pintar_normal)
        else:
			self.eliminar_pausa()
    
    def eliminar_pausa(self, *evnt):
		#~ self.pulsa_tecla_escape.habilitar()
		self.control_tiempo.stopPause()
		self.prueba_fea.eliminar()
		self.boton_reanudar.eliminar()
		self.tarea_tiempo = self.pilas.tareas.siempre(0.4, self.show_time)
		self.en_pausa = False

    def _recomenzar(self):
        #~ self.pilas.cambiar_escena(escenas.escena_juego.iniciar(self.jugador, 'newlevel'))
        self.pilas.escenas.EscenaDeJuego(self.jugador, 'newlevel')
        return False

    def _recomenzarsnvida(self):
        self.pilas.escenas.EscenaDeJuego(self.jugador, 'sinvida')
        return False

    def _recomenzarfall(self):
        self.pilas.escenas.EscenaDeJuego(self.jugador, 'fallmap')
        return False

    def _conexiones(self):
        self.devices=duinobot.boards() # esto cuelga todo en windows
        if len(self.devices)>0:
            self.conexion = True
        else:
            self.conexion = False





    def _habilitar_boton_robot(self):
        if self.conexion == True :
            self.animacion.habilitar_boton_robot(self.botones)
            self.habilitado=True

        elif self.conexion == False:
            self.animacion.deshabilitar_boton_robot()
            self.habilitado = False
            
    def salir(self):
		self.pilas.escenas.EscenaDeMenu('existe',self.jugador.nombre)


iniciar = EscenaDeJuego
