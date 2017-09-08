# -*- coding: utf-8 -*-
__author__ = 'cristian'
__doc__ = """
    Este modulo transforma los movimientos enviado de la forma ('movimiento',cantidad)
    a una ubicacion dentro del mapa.
    movimiento= 'avanzar',

    El personaje puede tener 4 posiciones a las que apunta para avanzar o retroceder
    0=Apunta ARRIBA
    1=Apunta DERECHA
    2=Apunta ABAJO
    3=Apunta IZQUIERDA
"""


class Transformador:
    def __init__(self,cant_filas,cant_columnas,posicion_inicial,apunta_actor=0):
         #recibe posicion inicial (fila,columna) que es dentro de mapa
        self.posicion_inicial=posicion_inicial
        self.apunta_actor=apunta_actor
        self.apunta_actor_inicial=apunta_actor
        self.pos_recorrido={}
        self.filas=cant_filas
        self.columnas=cant_columnas

    def set_Movimientos(self,diccionario):
        #recibe el diccionario y lo transforma
        self.apunta_actor=self.apunta_actor_inicial
        self.__convertidor(diccionario)


    def get_Movimientos(self):
        return self.pos_recorrido

    def getApunta_actor(self):
        #devuelve la posicion hacia donde estaba apuntando
        return self.apunta_actor

    def __dentro_del_mapa(self, pos):
        return 0 <= pos[0] < self.filas and 0 <= pos[1] < self.columnas

    def __calcular_deltas(self, movimiento):
        '''
        Calcula coordenadas en base al movimiento y la orientación
        actual.
        Un delta es el valor a sumar para dar un solo paso.
        '''
        if movimiento in ('avanzar', 'retroceder'):
            # Avanzar representaría sumar la tupla
            # (delta_fila, delta_columna, 0) a la posición actual
            delta_apunta = 0
            if self.apunta_actor == 0:
                delta_fila, delta_columna = 1, 0
            elif self.apunta_actor == 1:
                delta_fila, delta_columna = 0, 1
            elif self.apunta_actor == 2:
                delta_fila, delta_columna = -1, 0
            elif self.apunta_actor == 3:
                delta_fila, delta_columna = 0, -1

            # Retroceder es lo contrario de avanzar :P
            if movimiento == 'retroceder':
                delta_fila, delta_columna = -delta_fila, -delta_columna
        else:
            # Si no avanza ni retrocede: gira
            # El robot gira en su lugar, sin moverse
            delta_fila, delta_columna = 0, 0

            if movimiento == 'izq':
                delta_apunta = -1
            else:
                delta_apunta = 1

        return delta_fila, delta_columna, delta_apunta

    def __convertidor(self,diccionario_movimientos):

        lista_claves=diccionario_movimientos.keys()
        i=0
        pos_ant=self.posicion_inicial
        pos_act=self.posicion_inicial
        for clave in lista_claves:
            movimiento=diccionario_movimientos[clave]
            if movimiento[1]==0:
                veces=1
            elif movimiento[1]>0:
                veces=movimiento[1]

            delta_fila, delta_columna, delta_apunta = self.__calcular_deltas(movimiento[0])

            # Cada movimiento con sus repeticiones
            for x in range (0,veces):
                self.apunta_actor = (self.apunta_actor + delta_apunta) % 4
                pos_act=(pos_ant[0] + delta_fila, pos_ant[1] + delta_columna, self.apunta_actor)
                pos_ant=pos_act

                if self.__dentro_del_mapa(pos_act):
                    self.pos_recorrido[i]=pos_act
                    i=i+1
                else:
                    # False marca que ya no hay movimientos
                    self.pos_recorrido[i]=False
                    return

iniciar=Transformador
