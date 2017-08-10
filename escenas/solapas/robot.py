__author__ = 'cristian Steib' 
import data
import pilasengine
import duinobot


class OpcionRobot():
    fuente = './escenas/interfazusuario/AGENCYB.TTF'
    boton_off =  './imag/Interfaz/actuoff.png'
    boton_on =  './imag/Interfaz/actuon.png'
    boton_press =  './imag/Interfaz/actupress.png'

    def __init__(self, config):
        self.config = config
        self.delet = False
        self.lista_ids = [None]
        ###########################################
        ### +SE GENERAN LOS ELEMENTOS DEL PANEL DE
        ## OPCIONES     ##########################
        ##########################################
        self.txt_id = pilas.actores.Texto('', magnitud=30, x=-500, y=-400, fuente=self.fuente)
        self.txt_conexiones = pilas.actores.Texto('', magnitud=28, x=130, y=150, fuente=self.fuente)
        self.txt_conexiones.color = pilas.colores.amarillo
        self.txt_conexion = pilas.actores.Texto('Sin conexion', magnitud=30, x=360, y=-450, fuente=self.fuente)
        self.txt_conexion.color = pilas.colores.rojo
        self._board()
        self._nombre()
        self._time()
        self._speed()
        self._id()
        self.btn_robot_refresh=pilas.actores.Actor(self.boton_off,x=-424,y=-300)
        self.btn_robot_refresh.escala=0.6
      #  self.btn_robot_refresh.cuando_hace_click=self.robot



        ######## - FIN DE GENERACION DE ELEMENTOS DE
        ########OPCIONES ########################
        ##########################################
        pilas.mundo.agregar_tarea(1, self._conexion)


    def _conexion(self):
        """
        Metodo para saber si hay un xbee conectado

        """
        try:
            ls = duinobot.boards()
            if len(ls)==0:
                self.txt_conexiones.texto='no_Xbee'
                self.btn_robot_refresh.imagen=self.boton_off
                self.btn_robot_refresh.cuando_hace_click= self.nada
            else:
                self.txt_conexiones.texto = str(ls)
                self.btn_robot_refresh.imagen=self.boton_on
                self.btn_robot_refresh.cuando_hace_click= self.conectar

            if self.delet == False:
                return True
            else:
                return False

        except():
            self.txt_conexiones.texto='Problema_en_Duinobot'

    def nada(self):
        pass

    def conectar(self):
        # Conecta al xbee y lista los id disponibles.
        self.btn_robot_refresh.imagen=self.boton_press
        try:
            self.b = duinobot.Board(self.device.texto)
            lista_ids = self.b.report()
            self.presence = True
            self.cadena = 'Robots:'
            print 'Xbee detected'
            self.txt_conexion.texto = 'Conexion_establecida'
            self.txt_conexion.color = pilas.colores.verde
        except:
            self.presence = False
            lista_ids = []
            print 'Xbee not detected'
            self.txt_conexion.texto = 'Sin_conexion'
            self.txt_conexion.color = pilas.colores.rojo
        finally:
            if self.presence == True:
                for id in lista_ids:
                    self.cadena = self.cadena + str(id) + str('-')
                self.txt_id.texto = self.cadena
            else:
                self.txt_id.texto = 'No_se_Han_Encontrado_Robots'
                self.txt_id.color = pilas.colores.rojo
        self.btn_robot_refresh.imagen=self.boton_on

    def _id(self):
        self.txtid = pilas.actores.Texto('Id del Robot a usar:', x=-380, y=500, fuente=self.fuente, magnitud=30)
        self.id = pilas.interfaz.IngresoDeTexto(str(self.config.idrobot), x=-400, y=440, ancho=100)
        self.id.escala = 2
        self.id.solo_numeros()

    def _nombre(self):
        self.txtnombre = pilas.actores.Texto('Nombre del Robot:', x=-380, y=360, fuente=self.fuente, magnitud=30)
        self.nombre = pilas.interfaz.IngresoDeTexto(self.config.namerobot, x=-350, y=300, ancho=150)
        self.nombre.escala = 2

    def _board(self):
        self.txtboard = pilas.actores.Texto('Dispositivo de Comunicacion:', x=-310, y=210, fuente=self.fuente,
                                            magnitud=30)
        self.device = pilas.interfaz.IngresoDeTexto(self.config.board, x=-200, y=140)
        self.device.escala = 2

    def _speed(self):
        self.txtspeed = pilas.actores.Texto('Speed por Default:', x=-380, y=50, fuente=self.fuente, magnitud=30)
        self.speed = pilas.interfaz.IngresoDeTexto(str(self.config.speedrobot), ancho=100, x=-400, y=-20)
        self.speed.escala = 2
        self.speed.solo_numeros()

    def _time(self):
        self.txttime = pilas.actores.Texto('Tiempo por Default:', x=-380, y=-100, fuente=self.fuente, magnitud=30)
        self.time = pilas.interfaz.IngresoDeTexto(str(self.config.timerobot), ancho=100, x=-400, y=-180)
        self.time.escala = 2
        self.time.solo_numeros()

    def _save(self):
        self.config.board = str(self.device.texto)
        self.config.namerobot = str(self.nombre.texto)
        self.config.speedrobot = int(self.speed.texto)
        self.config.timerobot = int(self.time.texto)
        self.config.idrobot = int(self.id.texto)
        self.config.save_values()
        if self.delet == False:
            return True
        else:
            return False

    def delete(self):
        self._save()
        self.txtnombre.eliminar()
        self.txtboard.eliminar()
        self.txtid.eliminar()
        self.txtspeed.eliminar()
        self.txttime.eliminar()
        self.device.eliminar()
        self.nombre.eliminar()
        self.id.eliminar()
        self.device.eliminar()
        self.speed.eliminar()
        self.time.eliminar()
        self.txt_conexion.eliminar()
        self.txt_id.eliminar()
        self.txt_conexiones.eliminar()
        self.btn_robot_refresh.eliminar()
        self.delet = True
