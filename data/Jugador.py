# -*- encoding: utf-8 -*-
# Robot-Game a game of robot
#
#
#
#
#
#
import data

__author__ = 'cristian'

__doc__ = """
Modulo Jugador:
============

al crear la instancia de jugador , luego hay que asignarle valoreres , con el metodo setJugador
ej:
    instancia=data.Jugador()
    instancia.jugador(nombre)

"""


class Jugador(object):
    def __init__(self):
        # Se crea la instancia que maneja el archivo, es necesario porque
        # si quiero consultar la lista de los jugadores , previamente tengo
        # que crear la instancia de la clase Manager , para levantar el archivo
        self._archivo = data.Manager()

    def setIniciarJugador(self, lista):
        """
        Metodo para crear un nuevo Jugador

        """
        self._nombre_de_jugador = lista
        self._nivel = 0
        self._datos = {}
        self._datos['niveles'] = {}
        self._datos['niveles'][self._nivel] = {None}
        self._datos['niveles'][self._nivel] = {None}


        self.vida_lost           =0
        self.vida_start          =3
        self.puntaje_maximo      =0
        self.puntaje_obtenido    =0
        self.tiempo_inicio       =0
        self.tiempo_fin          =0
        self.tiempo_minimo       =0
        self.movimiento_minimos  =0
        self.movimientos_hechos  =0
        self.cantidad_choques    =0
        self.cantidad_caidas     =0



        self.SaveDatosNivel()

    JugadorNuevo = property(fset=setIniciarJugador)

    def setJugador(self, nombre):
        """
        Se establecen los datos del jugador llamado , como argumento nombre

        """

        self._nombre_de_jugador = nombre
        self._datos = self._archivo.getJugador(nombre)
        self._setIndiceNivel(0)
        self.cant_niveles = self._datos['niveles'].keys()

        for nivel in self.cant_niveles:
            print '---------------Jugador:{1}----------Nivel:{0} ------------------------------------------'.format(nivel , self._nombre_de_jugador)
            print 'Vidas Perdidas       :   ',self._datos['niveles'][nivel]['vidas_lost']
            print 'Vidas Comienzo       :   ',self._datos['niveles'][nivel]['vidas_start']
            print 'Puntaje max          :   ',self._datos['niveles'][nivel]['pto_max']
            print 'Puntaje obtenido     :   ',self._datos['niveles'][nivel]['pto_obtenido']
            print 'tiempo inicio        :   ',self._datos['niveles'][nivel]['tiempo_inicio']
            print 'tiempo fin           :   ',self._datos['niveles'][nivel]['tiempo_fin']
            print 'tiempo minimo        :   ',self._datos['niveles'][nivel]['tiempo_minimo']
            print 'movimentos minimos   :   ',self._datos['niveles'][nivel]['movimientos_minimos']
            print 'movimientos hechos   :   ',self._datos['niveles'][nivel]['movimientos_hechos' ]
            print 'cantidad de choques  :   ',self._datos['niveles'][nivel]['cantidad_choques']
            print 'cantidad de caidas   :   ',self._datos['niveles'][nivel]['cantidad_caidas']
            print '-------------------------------------------------------------------------------------'

    def getJugador(self):
        """
        Solo retorna nombre del jugador actual

        """

        return self._nombre_de_jugador

    nombre = property(getJugador, setJugador)

    def _getListaJugadores(self):
        """
        devuelve una lista
        :return:
        """
        return self._archivo.getJugadores()

    jugadores = property(_getListaJugadores)

    def SaveDatosNivel(self):
        """
        se guardan los datos del nivel en el diccionario de datos

        """

        dato ={'vidas_lost': self._vida_lost,'vidas_start':self._vida_start,'pto_max':self._pto_max,'pto_obtenido':self._pto_obt,'tiempo_fin':self._tiempo_fin,
                'tiempo_inicio':self._tiempo_inicio,'tiempo_minimo':self._tiempo_minimo,'movimientos_minimos':self._movimientos_minimos,'movimientos_hechos':self._movimientos_realizados,
                'cantidad_choques':self._cantidad_choques,'cantidad_caidas':self._cantidad_caidas}
        try:
            self._datos['niveles'][self._nivel] = dato
            print 'datos de nivel guardados'
            print '/////////////////////DATOS DEL NIVEL {}///////////////////////////////////////////'.format(self._nivel)
            print 'Vidas Perdidas       :   ',self._datos['niveles'][self._nivel]['vidas_lost']
            print 'Vidas Comienzo       :   ',self._datos['niveles'][self._nivel]['vidas_start']
            print 'Puntaje max          :   ',self._datos['niveles'][self._nivel]['pto_max']
            print 'Puntaje obtenido     :   ',self._datos['niveles'][self._nivel]['pto_obtenido']
            print 'tiempo inicio        :   ',self._datos['niveles'][self._nivel]['tiempo_inicio']
            print 'tiempo fin           :   ',self._datos['niveles'][self._nivel]['tiempo_fin']
            print 'tiempo minimo        :   ',self._datos['niveles'][self._nivel]['tiempo_minimo']
            print 'movimentos minimos   :   ',self._datos['niveles'][self._nivel]['movimientos_minimos']
            print 'movimientos hechos   :   ',self._datos['niveles'][self._nivel]['movimientos_hechos' ]
            print 'cantidad de choques  :   ',self._datos['niveles'][self._nivel]['cantidad_choques']
            print 'cantidad de caidas   :   ',self._datos['niveles'][self._nivel]['cantidad_caidas']
            print '////////////////////////////////////////////////////////////////////////////////////'





        except(KeyError):
            print 'class Jugador.SaveDatosNivel no se pudo guardar'


    def _getListaniveles(self):
        """
        Retorna una listas con los niveles alcanzados por ese jugador.
        Ej:
        [0,1,2,3] esto quiere decir q hay datos para los niveles ,0,1,2,3


        """
        return self._datos['niveles']

    niveles = property(_getListaniveles)

    def _setIndiceNivel(self, numero_de_nivel):
        """

        SOLO SIRVE PARA CONSULTAR LOS DATOS DE ALGUN JUGADOR EN PARTICULAR ,. EN EL NIVEL
        INDICADO , PRIRO SE INDICA CUAL ES EL NIVEL A CONSULTAR , LUEGO SE CONSULTAN LOS DATOS
        EJ:
            Primero se indica el nivel:

                jugador.niveldatos= 2

            Luego se puede usar :

                diccionario=jugador.niveldatos

            o bien ;

                    x=jugador.vida_lost
                    x=jugador.vida_start
                    x=jugador.puntaje_maximo
                    x=jugador.puntaje_obtenido
                    x=jugador.tiempo_fin
                    x=jugador.tiempo_minimo
                    x=jugador.movimiento_minimos
                    x=jugador.movimientos_hechos
                    x=jugador.cantidad_choques
                    x=jugador.cantidad_caidas

                de esta manera se obtiene individualmente cada dato de ese nivel.






        """
        self._nivel = numero_de_nivel
        print("###########################3")
        print("datos del jugador {}".format(self._datos))
        self._vida_lost=self._datos['niveles'][numero_de_nivel]['vidas_lost']
        self._vida_start=self._datos['niveles'][numero_de_nivel]['vidas_start']
        self._pto_max=self._datos['niveles'][numero_de_nivel]['pto_max']
        self._pto_obt=self._datos['niveles'][numero_de_nivel]['pto_obtenido']
        self._tiempo_inicio=self._datos['niveles'][numero_de_nivel]['tiempo_inicio']
        self._tiempo_fin=self._datos['niveles'][numero_de_nivel]['tiempo_fin']
        self._tiempo_minimo=self._datos['niveles'][numero_de_nivel]['tiempo_minimo']
        self._movimientos_minimos=self._datos['niveles'][numero_de_nivel]['movimientos_minimos']
        self._movimientos_realizados=self._datos['niveles'][numero_de_nivel]['movimientos_hechos']
        self._cantidad_choques=self._datos['niveles'][numero_de_nivel]['cantidad_choques']
        self._cantidad_caidas=self._datos['niveles'][numero_de_nivel]['cantidad_caidas']


    def _getDatosNivel(self):
        """Devuelve datos de el nivel solicitado"""
        try:
            value=self._datos['niveles'][self._nivel]
            return value
        except(KeyError):
            print 'class Jugadores.niveldatos, no hay datos para ese nivel'

    niveldatos = property(_getDatosNivel, _setIndiceNivel,
                          "Requiere haber seteado N° de nivel, y Jugador existente")


    ######################################################################
    #####################  DATOS DEL NIVEL ##########################
    #####################################################################
    def _setVidas_lost(self, dato):
        """cantidad de vidas peridas en ese nivel"""
        self._vida_lost = dato

    def _setVidas_start(self, dato):
        """cantidad de vidas al comienzo del nivel"""
        self._vida_start = dato

    def _setPto_max(self, dato):
        """puntaje maximo que se puede obtener en ese nivel"""
        self._pto_max = dato

    def _setPto_obtenid(self, dato):
        """puntaje obtenido en ese nivel"""
        self._pto_obt = dato
        if self._pto_obt<0:
            self._pto_obt=0

    def _setTiempo_inicio(self, dato):
        """tiemp total usado en ese nive"""
        self._tiempo_inicio = dato

    def _setTiempo_fin(self, dato):
        """tiempo total usado en ese nive"""
        self._tiempo_fin = dato
        #self._tiempo_fin= str (self._tiempo_fin)

    def _setTiempo_minimo(self, dato):
        """este es el menor tiempo en el que se podria realizar la partida en tal nivel"""
        self._tiempo_minimo = dato

    def _setMovimentos_minimos(self, dato):
        """esta es la menor cantidad de movimientos que podria realizar el robor para llegar al obstaculo final """
        self._movimientos_minimos = dato

    def _setMovimientos_hechos(self, dato):
        self._movimientos_realizados = dato

    def _setCantidad_choques(self, dato):
        self._cantidad_choques = dato

    def _setCantidad_caidas(self, dato):
        self._cantidad_caidas = dato

    def _getVidas_lost(self):
        return self._vida_lost

    def _getVidas_start(self):
        return self._vida_start

    def _getPto_max(self):
        return self._pto_max

    def _getPto_obtenid(self):
        return self._pto_obt

    def _getTiempo_inicio(self):
        """tiempo total usado en ese nive"""
        return self._tiempo_inicio

    def _getTiempo_fin(self):
        return self._tiempo_fin

    def _getTiempo_minimo(self):
        return self._tiempo_minimo

    def _getMovimentos_minimos(self):
        return self._movimientos_minimos

    def _getMovimientos_hechos(self):
        return self._movimientos_realizados

    def _getCantidad_choques(self):
        return self._cantidad_choques

    def _getCantidad_caidas(self):
        return self._cantidad_caidas

    vida_lost = property(_getVidas_lost, _setVidas_lost)
    vida_start = property(_getVidas_start,_setVidas_start)
    puntaje_maximo = property(_getPto_max, _setPto_max)
    puntaje_obtenido = property(_getPto_obtenid, _setPto_obtenid)
    tiempo_inicio = property(_getTiempo_inicio, _setTiempo_inicio)
    tiempo_fin = property(_getTiempo_fin, _setTiempo_fin)
    tiempo_minimo = property(_getTiempo_minimo, _setTiempo_minimo)
    movimiento_minimos = property(_getMovimentos_minimos,_setMovimentos_minimos)
    movimientos_hechos = property(_getMovimientos_hechos,_setMovimientos_hechos)
    cantidad_choques = property(_getCantidad_choques,_setCantidad_choques)
    cantidad_caidas = property(_getCantidad_caidas,_setCantidad_caidas)



    ####################################################################################################################
    ################################################################################################################
    ################################################################################################################

    def setNivel(self,lvl):
        self._nivel=lvl


    def getNivel(self):
        # nivel actual del jugador
        return self._nivel

        return

    nivel=property(getNivel,setNivel)

    def getNivelmaximo(self):
        cant_niveles = self._datos['niveles'].keys()
        return len(self.cant_niveles)-1
    nivelmax=property(getNivelmaximo)

    def deletedatos(self):
        self._nivel=0
        self.vida_lost           =0
        self.vida_start          =3
        self.puntaje_maximo      =0
        self.puntaje_obtenido    =0
        self.tiempo_inicio          =0
        self.tiempo_fin          =0
        self.tiempo_minimo       =0
        self.movimiento_minimos  =0
        self.movimientos_hechos  =0
        self.cantidad_choques    =0
        self.cantidad_caidas     =0
        self._datos={'niveles':{}}
        self.SaveDatosNivel()
        self.save()

    def save(self):
        self._archivo.guardar_jugador(self._nombre_de_jugador, self._datos)


iniciar = Jugador
