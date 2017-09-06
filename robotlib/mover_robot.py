__author__ = 'GasparcitoX'
import duinobot
import data
import pilasengine
import threading


class Mover_Robot:
    '''
    Recibe un diccionario con pares de tuplas los cuales son los movimientos seleccionados por el jugador
    Ej:{0: ('avanzar', 0), 1: ('avanzar', 0), 2: ('avanzar', 0), 3: ('avanzar', 0)}
    '''

    def __init__(self):
        """
        TOMA LOS DATOS DE LA CONFIGURACION PARA ESTABLECER EL PUERTO DE COMUNICACION Y ID DEL ROBOT


        """

    def mover(self, diccionario):

        try:
            self.config = data.Configuracion()
            #~ self.b = duinobot.Board(self.config.board)
            self.b = duinobot.Board("/dev/ttyUSB0")
            #~ self.r = duinobot.Robot(self.b, self.config.idrobot)
            self.r = duinobot.Robot(self.b, 3)
            self.keys = diccionario.keys()
            self.dict = diccionario
            self.ln = len(self.keys)
            self.ind = 0
            tarea_send = threading.Timer(1,self._send )
            tarea_send.start()
        except():
            pilas.avisar("Error en la comunicacion")
            print 'Error de comunicacion'

    def _send(self):
        veces = self.dict[self.ind][1]
        if veces == 0:
            veces = 1

        if (self.dict[self.ind][0] == 'avanzar'):
            print ('avanza')
            self.r.forward(self.config.speedrobot, self.config.timerobot * veces)
            #~ self.r.forward(50,1*veces)

        if (self.dict[self.ind][0] == 'der'):
            print ('der')
            self.r.turnRight(self.config.speedrobot, self.config.timerobot * veces)
            #~ self.r.turnRight(50,1*veces)

        if (self.dict[self.ind][0] == 'izq'):
            print ('izq')
            self.r.turnLeft(self.config.speedrobot, self.config.timerobot * veces)
            #~ self.r.turnLeft(50,1*veces)

        if (self.dict[self.ind][0] == 'retroceder'):
            print ('atras')
            self.r.backward(self.config.speedrobot, self.config.timerobot * veces)
            #~ self.r.backward(50,1*veces)

        if self.ind<=self.ln:
            self.ind=self.ind+1
            tarea_send = threading.Timer(1,self._send )
            tarea_send.start()
        if self.ind>self.ln:
            self.ind=0

