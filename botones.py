__author__ = 'cristian'
import pilasengine
import lib
import prompt
import Movimientos
import data


class botones:
    def  __init__(self, pilas):
        self.pilas = pilas
        self.config=data.Configuracion()
        #Se crea instancia de movimientos , donde estaran todos los movientos
        #almacenados de la manera de tupla ('moviento',cantidad de veces)
        self.moves=Movimientos.iniciar()
        self.giro=(-1,-1)

        #variable para habilitar o deshabilitar los botones!
        self.estado_botones=False
        #inicializo variables
        self.numb=False
        self.retorn_boton_ant=False
        self.press=0
        #MATRIZ INICIO PARA POSICIONES DE LOS BOTONES NUMERICOS
        self.posiciones=lib.Matriz(3,3)
        y=432
        for filas in range (0,3):
            x=-2000
            for columnas in range(0,3):
                self.posiciones.set_valor(filas,columnas,(x,y))
                x=x+135
            y=y-129


        #MATRIZ INICIO PARA POSICIONES DE CONTROL FLECHAS

        self.posiciones_flechas=lib.Matriz(3,3)
        y=-134
        for filas in range (0,3):
            x=-2000
            for columnas in range(0,3):
                self.posiciones_flechas.set_valor(filas,columnas,(x,y))
                x=x+135
            y=y-129

        self.control_prompt=prompt.ControladorDePrompt()


        self.boton_1=self.pilas.actores.Boton(x=self.posiciones.get_valor(0,0)[0],y=432,ruta_normal='imag/comando/1off.png', ruta_press='imag/comando/1on.png', ruta_over='imag/comando/1i.png')
        self.boton_1.conectar_presionado(self.__set_1)
        self.boton_1.conectar_sobre(self.boton_1.pintar_sobre)
        self.boton_1.conectar_normal(self.boton_1.pintar_normal)
        self.boton_1.aprender(self.pilas.habilidades.Arrastrable)


        self.boton_2=self.pilas.actores.Boton(x=self.posiciones.get_valor(0,1)[0],y=self.posiciones.get_valor(0,1)[1],ruta_normal='imag/comando/2off.png', ruta_press='imag/comando/2on.png', ruta_over='imag/comando/2i.png')
        self.boton_2.conectar_presionado(self.__set_2)
        self.boton_2.conectar_sobre(self.boton_2.pintar_sobre)
        self.boton_2.conectar_normal(self.boton_2.pintar_normal)

        self.boton_3=self.pilas.actores.Boton(x=self.posiciones.get_valor(0,2)[0],y=self.posiciones.get_valor(0,2)[1],ruta_normal='imag/comando/3off.png', ruta_press='imag/comando/3on.png', ruta_over='imag/comando/3i.png')
        self.boton_3.conectar_presionado(self.__set_3)
        self.boton_3.conectar_sobre(self.boton_3.pintar_sobre)
        self.boton_3.conectar_normal(self.boton_3.pintar_normal)

        self.boton_4=self.pilas.actores.Boton(x=self.posiciones.get_valor(1,0)[0],y=self.posiciones.get_valor(1,0)[1],ruta_normal='imag/comando/4off.png', ruta_press='imag/comando/4on.png', ruta_over='imag/comando/4i.png')
        self.boton_4.conectar_presionado(self.__set_4)
        self.boton_4.conectar_sobre(self.boton_4.pintar_sobre)
        self.boton_4.conectar_normal(self.boton_4.pintar_normal)

        self.boton_5=self.pilas.actores.Boton(x=self.posiciones.get_valor(1,1)[0],y=self.posiciones.get_valor(1,1)[1],ruta_normal='imag/comando/5off.png', ruta_press='imag/comando/5on.png', ruta_over='imag/comando/5i.png')
        self.boton_5.conectar_presionado(self.__set_5)
        self.boton_5.conectar_sobre(self.boton_5.pintar_sobre)
        self.boton_5.conectar_normal(self.boton_5.pintar_normal)

        self.boton_6=self.pilas.actores.Boton(x=self.posiciones.get_valor(1,2)[0],y=self.posiciones.get_valor(1,2)[1],ruta_normal='imag/comando/6off.png', ruta_press='imag/comando/6on.png', ruta_over='imag/comando/6i.png')
        self.boton_6.conectar_presionado(self.__set_6)
        self.boton_6.conectar_sobre(self.boton_6.pintar_sobre)
        self.boton_6.conectar_normal(self.boton_6.pintar_normal)

        self.boton_7=self.pilas.actores.Boton(x=self.posiciones.get_valor(2,0)[0], y=self.posiciones.get_valor(2,0)[1],ruta_normal='imag/comando/7off.png', ruta_press='imag/comando/7on.png', ruta_over='imag/comando/7i.png')
        self.boton_7.conectar_presionado(self.__set_7)
        self.boton_7.conectar_sobre(self.boton_7.pintar_sobre)
        self.boton_7.conectar_normal(self.boton_7.pintar_normal)

        self.boton_8=self.pilas.actores.Boton(x=self.posiciones.get_valor(2,1)[0],y=self.posiciones.get_valor(2,1)[1],ruta_normal='imag/comando/8off.png', ruta_press='imag/comando/8on.png', ruta_over='imag/comando/8i.png')
        self.boton_8.conectar_presionado(self.__set_8)
        self.boton_8.conectar_sobre(self.boton_8.pintar_sobre)
        self.boton_8.conectar_normal(self.boton_8.pintar_normal)

        self.boton_9=self.pilas.actores.Boton(x=self.posiciones.get_valor(2,2)[0],y=self.posiciones.get_valor(2,2)[1],ruta_normal='imag/comando/9off.png', ruta_press='imag/comando/9on.png', ruta_over='imag/comando/9i.png')
        self.boton_9.conectar_presionado(self.__set_9)
        self.boton_9.conectar_sobre(self.boton_9.pintar_sobre)
        self.boton_9.conectar_normal(self.boton_9.pintar_normal)


        self.boton_up=self.pilas.actores.Boton(x=self.posiciones_flechas.get_valor(0,1)[0],y=self.posiciones_flechas.get_valor(0,1)[1],ruta_normal='imag/comando/arribaoff.png', ruta_press='imag/comando/arribaon.png', ruta_over='imag/comando/arribai.png')
        self.boton_up.conectar_presionado(self.__up)
        self.boton_up.conectar_sobre(self.boton_up.pintar_sobre)
        self.boton_up.conectar_normal(self.boton_up.pintar_normal)



        self.boton_left=self.pilas.actores.Boton(x=self.posiciones_flechas.get_valor(1,0)[0],y=self.posiciones_flechas.get_valor(1,0)[1],ruta_normal='imag/comando/izquierdaoff.png', ruta_press='imag/comando/izquierdaon.png', ruta_over='imag/comando/izquierdai.png')
        self.boton_left.conectar_presionado(self.__izquierda)
        self.boton_left.conectar_sobre(self.boton_left.pintar_sobre)
        self.boton_left.conectar_normal(self.boton_left.pintar_normal)

        self.boton_right=self.pilas.actores.Boton(x=self.posiciones_flechas.get_valor(1,2)[0],y=self.posiciones_flechas.get_valor(1,2)[1],ruta_normal='imag/comando/derechaoff.png', ruta_press='imag/comando/derechaon.png', ruta_over='imag/comando/derechai.png')
        self.boton_right.conectar_presionado(self.__derecha)
        self.boton_right.conectar_sobre(self.boton_right.pintar_sobre)
        self.boton_right.conectar_normal(self.boton_right.pintar_normal)



        self.boton_down=self.pilas.actores.Boton(x=self.posiciones_flechas.get_valor(2,1)[0],y=self.posiciones_flechas.get_valor(2,1)[1],ruta_normal='imag/comando/abajooff.png', ruta_press='imag/comando/abajoon.png', ruta_over='imag/comando/abajoi.png')
        self.boton_down.conectar_presionado(self.__down)
        self.boton_down.conectar_sobre(self.boton_down.pintar_sobre)
        self.boton_down.conectar_normal(self.boton_down.pintar_normal)

        #self.boton_duinobot=pilas.actores.boton.Boton(x=1152,y=-1085,ruta_normal='imag/comando/Controles/robotnul.png', ruta_press='imag/comando/Controles/roboton.png', ruta_over='imag/comando/Controles/robotover.png')
        #self.boton_duinobot.conectar_presionado(self.__duinobot)
        #self.boton_duinobot.conectar_sobre(self.boton_duinobot.pintar_sobre)
        #self.boton_duinobot.conectar_normal(self.boton_duinobot.pintar_normal)
        #self.boton_duinobot.y= pilas.interpolar(-485,tipo='lineal',demora=4 , duracion=2)




        self.sumador=0


        self.posiciones=lib.Matriz(3,3)
        y=432
        for filas in range (0,3):
            x=-1235

            for columnas in range(0,3):
                self.posiciones.set_valor(filas,columnas,(x,y))
                x=x+135
            y=y-129

        self.posiciones_flechas=lib.Matriz(3,3)
        y=-134
        for filas in range (0,3):
            x=-1235
            for columnas in range(0,3):
                self.posiciones_flechas.set_valor(filas,columnas,(x,y))
                x=x+135
            y=y-129

        if self.config.graficos==True and self.config.lvlup==False:
             ## comienZo de todas las interpolaciones de los botones
            #self.boton_1.x=pilas.interpolar(self.posiciones.get_valor(0,0)[0],tipo='lineal',demora=1 , duracion=2)
            self.pilas.utils.interpolar(self.boton_1,'x',self.posiciones.get_valor(0,0)[0],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_1,'y',self.posiciones.get_valor(0,0)[1],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_2,'x',self.posiciones.get_valor(0,1)[0],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_2,'y',self.posiciones.get_valor(0,1)[1],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_3,'x',self.posiciones.get_valor(0,2)[0],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_3,'y',self.posiciones.get_valor(0,2)[1],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_4,'x',self.posiciones.get_valor(1,0)[0],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_4,'y',self.posiciones.get_valor(1,0)[1],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_5,'x',self.posiciones.get_valor(1,1)[0],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_5,'y',self.posiciones.get_valor(1,1)[1],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_6,'x',self.posiciones.get_valor(1,2)[0],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_6,'y',self.posiciones.get_valor(1,2)[1],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_7,'x',self.posiciones.get_valor(2,0)[0],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_7,'y',self.posiciones.get_valor(2,0)[1],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_8,'x',self.posiciones.get_valor(2,1)[0],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_8,'y',self.posiciones.get_valor(2,1)[1],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_9,'x',self.posiciones.get_valor(2,2)[0],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_9,'y',self.posiciones.get_valor(2,0)[1],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_up,'x',self.posiciones_flechas.get_valor(0,1)[0],tipo='lineal' ,   duracion=2)
            self.pilas.utils.interpolar(self.boton_up,'y',self.posiciones_flechas.get_valor(0,1)[1],tipo='lineal' ,   duracion=2)
            self.pilas.utils.interpolar(self.boton_down,'x',self.posiciones_flechas.get_valor(2,1)[0],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_down,'y',self.posiciones_flechas.get_valor(2,1)[1],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_left,'x',self.posiciones_flechas.get_valor(1,0)[0],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_left,'y',self.posiciones_flechas.get_valor(1,0)[1],tipo='lineal' , duracion=2)
            self.pilas.utils.interpolar(self.boton_right,'x',self.posiciones_flechas.get_valor(1,2)[0],tipo='lineal' ,duracion=2)
            self.pilas.utils.interpolar(self.boton_right,'y',self.posiciones_flechas.get_valor(1,2)[1],tipo='lineal' ,duracion=2)

        else:
            self.boton_1.x=self.posiciones.get_valor(0,0)[0]
            self.boton_1.y=self.posiciones.get_valor(0,0)[1]
            self.boton_2.x=self.posiciones.get_valor(0,1)[0]
            self.boton_2.y=self.posiciones.get_valor(0,1)[1]
            self.boton_3.x=self.posiciones.get_valor(0,2)[0]
            self.boton_3.y=self.posiciones.get_valor(0,2)[1]
            self.boton_4.x=self.posiciones.get_valor(1,0)[0]
            self.boton_4.y=self.posiciones.get_valor(1,0)[1]
            self.boton_5.x=self.posiciones.get_valor(1,1)[0]
            self.boton_5.y=self.posiciones.get_valor(1,1)[1]
            self.boton_6.x=self.posiciones.get_valor(1,2)[0]
            self.boton_6.y=self.posiciones.get_valor(1,2)[1]
            self.boton_7.x=self.posiciones.get_valor(2,0)[0]
            self.boton_7.y=self.posiciones.get_valor(2,0)[1]
            self.boton_8.x=self.posiciones.get_valor(2,1)[0]
            self.boton_8.y=self.posiciones.get_valor(2,1)[1]
            self.boton_9.x=self.posiciones.get_valor(2,2)[0]
            self.boton_9.y=self.posiciones.get_valor(2,0)[1]

            self.boton_up.x=self.posiciones_flechas.get_valor(0,1)[0]
            self.boton_up.y=self.posiciones_flechas.get_valor(0,1)[1]
            self.boton_down.x=self.posiciones_flechas.get_valor(2,1)[0]
            self.boton_down.y=self.posiciones_flechas.get_valor(2,1)[1]
            self.boton_left.x=self.posiciones_flechas.get_valor(1,0)[0]
            self.boton_left.y=self.posiciones_flechas.get_valor(1,0)[1]
            self.boton_right.x=self.posiciones_flechas.get_valor(1,2)[0]
            self.boton_right.y=self.posiciones_flechas.get_valor(1,2)[1]







    def eliminarmovimientoanterior(self):
        self.moves.elimiarmovimientopop()



    def habilitar_botones(self,estado=True):
        self.estado_botones=estado
        self.control_prompt.aparecer_botones()

    def __retroceso(self):
        self.control_prompt.elimino_todo()

    def __up(self):
        if self.estado_botones:
            self.boton_up.pintar_presionado()
            if self.numb==True:
                self.control_prompt.agregar_elemento('avanzar',cantidad=self.press)
                self.numb=False
                self.__espera_a_flecha(0,recupero=True)
            else:
                self.control_prompt.agregar_elemento('avanzar',0)
            self.moves.add_Movimiento(('avanzar',self.press))
            self.press=0   #press se estableze en 0 para que se pueda repetir el numero anterior en la proxima orden

    def __down(self):
        if self.estado_botones:
            self.boton_down.pintar_presionado()
            if self.numb==True:
                self.control_prompt.agregar_elemento('retroceder',cantidad=self.press)
                self.numb=False
                self.__espera_a_flecha(0,recupero=True)
            else:
                self.control_prompt.agregar_elemento('retroceder',0)
            self.moves.add_Movimiento(('retroceder',self.press))
            self.press=-1   #press se estableze en 0 para que se pueda repetir el numero anterior en la proxima orden


    def getGiro(self):
        #esta funcion la uso para obtener el giro realizado , asi muestro en tiempo real el giro producido por el boton
        return self.giro
    def setGiro(self):
        self.giro=(-1,-1)

    def __derecha(self):
        if self.estado_botones:
            self.boton_right.pintar_presionado()
            if self.numb==True:
                self.control_prompt.agregar_elemento('der',cantidad=self.press)
                self.numb=False
                self.giro=(1,self.press)
                self.__espera_a_flecha(0,recupero=True)


            else:
                self.giro=(1,1)
                self.control_prompt.agregar_elemento('der',0)
            self.moves.add_Movimiento(('der',self.press))
            self.press=0   #press se estableze en 0 para que se pueda repetir el numero anterior en la proxima orden

    def __izquierda(self):
        if self.estado_botones:
            self.boton_left.pintar_presionado()
            if self.numb==True:
                self.control_prompt.agregar_elemento('izq',cantidad=self.press)
                self.numb=False
                self.giro=(-1,self.press)
                self.__espera_a_flecha(0,recupero=True)

            else:
                self.giro=(-1,1)
                self.control_prompt.agregar_elemento('izq',0)
            self.moves.add_Movimiento(('izq',self.press))
            self.press=0    #press se estableze en 0 para que se pueda repetir el numero anterior en la proxima orden

    def __elimino_todo(self):
        self.prompt.elimino_todo

    def __espera_a_flecha(self,boton,recupero=False):


        if self.retorn_boton_ant==True and recupero==False:
            self.aux_boton.pintar_normal()
            self.aux_boton.conectar_normal(self.aux_boton.pintar_normal)
            self.aux_boton.conectar_sobre(self.aux_boton.pintar_sobre)
            boton.pintar_presionado()
            boton.conectar_normal(boton.pintar_presionado)
            boton.conectar_sobre(boton.pintar_presionado)
            self.aux_boton=boton
            self.retorn_boton_ant=True
        elif recupero==False:
            boton.pintar_presionado()
            boton.conectar_normal(boton.pintar_presionado)
            boton.conectar_sobre(boton.pintar_presionado)
            self.aux_boton=boton
            self.retorn_boton_ant=True
        if recupero==True:
            self.aux_boton.pintar_normal()
            self.aux_boton.conectar_normal(self.aux_boton.pintar_normal)
            self.aux_boton.conectar_sobre(self.aux_boton.pintar_sobre)
            self.retorn_boton_ant=False

    def __set_1(self):
        if self.estado_botones:
            if self.press==1:
                self.__espera_a_flecha(0,recupero=True)
                self.press=0
                self.numb=False
            else:
                self.__espera_a_flecha(self.boton_1)
                self.press=1
            self.numb=True

    def __set_2(self):
        if self.estado_botones:
            if self.press==2:
                self.__espera_a_flecha(0,recupero=True)
                self.press=0
                self.numb=False
            else:
                self.__espera_a_flecha(self.boton_2)
                self.press=2
            self.numb=True

    def __set_3(self):
        if self.estado_botones:
            if self.press==3:
                 self.__espera_a_flecha(0,recupero=True)
                 self.press=0
                 self.numb=False
            else:
                 self.__espera_a_flecha(self.boton_3)
                 self.press=3
            self.numb=True

    def __set_4(self):
        if self.estado_botones:
            if self.press==4:
                self.__espera_a_flecha(0,recupero=True)
                self.press=0
                self.numb=False
            else:
                self.__espera_a_flecha(self.boton_4)
                self.press=4
                self.numb=True

    def __set_5(self):
        if self.estado_botones:
            if self.press==5:
                 self.__espera_a_flecha(0,recupero=True)
                 self.press=0
                 self.numb=False
            else:
                 self.__espera_a_flecha(self.boton_5)
                 self.press=5
                 self.numb=True

    def __set_6(self):
        if self.estado_botones:
            if self.press==6:
                 self.__espera_a_flecha(0,recupero=True)
                 self.press=0
                 self.numb=False
            else:
                 self.__espera_a_flecha(self.boton_6)
                 self.press=6
                 self.numb=True

    def __set_7(self):
        if self.estado_botones:
            if self.press==7:
                 self.__espera_a_flecha(0,recupero=True)
                 self.press=0
                 self.numb=False
            else:
                 self.__espera_a_flecha(self.boton_7)
                 self.press=7
                 self.numb=True

    def __set_8(self):
        if self.estado_botones:
            if self.press==8:
                 self.__espera_a_flecha(0,recupero=True)
                 self.press=0
                 self.numb=False
            else:
                 self.__espera_a_flecha(self.boton_8)
                 self.press=8
                 self.numb=True

    def __set_9(self):
        if self.estado_botones:

            if self.press==9:
                 self.__espera_a_flecha(0,recupero=True)
                 self.press=0
                 self.numb=False
            else:
                 self.__espera_a_flecha(self.boton_9)
                 self.press=9
                 self.numb=True

    def __del(self):
        pass

    def __duinobot(self):
        pass



    def get_movimientos (self):
        #devuelve el diccionario con los movimientos ej: ('avanzar',3)
        return self.moves.get_Movimientos()

