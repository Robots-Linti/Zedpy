# -*- coding: utf-8 -*-
__author__ = 'GasparcitoX'
import duinobot
import data
import pilasengine
import threading
import serial


class Mover_Robot:
    '''
    Recibe un diccionario con pares de tuplas los cuales son los movimientos seleccionados por el jugador
    Ej:{0: ('avanzar', 0), 1: ('avanzar', 0), 2: ('avanzar', 0), 3: ('avanzar', 0)}
    '''

    def __init__(self):
        """
        TOMA LOS DATOS DE LA CONFIGURACION PARA ESTABLECER EL PUERTO DE COMUNICACION Y ID DEL ROBOT


        """
        self.b = None
        self.current_board = None

    def mover(self, diccionario):
        try:
            self.config = data.Configuracion()
            # Instanciar un board tarda un tiempo, lo instanciamos solamente
            # si no existe una instancia o si la configuración cambió.
            if self.b is None or self.config.board != self.current_board:
                self.b = duinobot.Board(self.config.board, debug=True)
                self.current_board = self.config.board
        except serial.serialutil.SerialException:
            return False
        else:
            self.r = duinobot.Robot(self.b, self.config.idrobot)
            self.dict = diccionario
            self.ind = 0
            tarea_send = threading.Thread(target=self._send)
            # Los threads daemon son matados automáticamente cuando el
            # programa termina.
            tarea_send.daemon = True
            tarea_send.start()
        return True


    def _send(self):
        if self.ind >= len(self.dict):
            return

        veces = self.dict[self.ind][1]
        if veces == 0:
            veces = 1

        if (self.dict[self.ind][0] == 'avanzar'):
            print ('avanza')
            self.r.forward(self.config.speedrobot, self.config.timerobot * veces)

        if (self.dict[self.ind][0] == 'der'):
            print ('der')
            self.r.turnRight(self.config.speedrobot, self.config.timerobot * veces)

        if (self.dict[self.ind][0] == 'izq'):
            print ('izq')
            self.r.turnLeft(self.config.speedrobot, self.config.timerobot * veces)

        if (self.dict[self.ind][0] == 'retroceder'):
            print ('atras')
            self.r.backward(self.config.speedrobot, self.config.timerobot * veces)

        self.ind=self.ind+1
        tarea_send = threading.Timer(1,self._send )
        tarea_send.start()

