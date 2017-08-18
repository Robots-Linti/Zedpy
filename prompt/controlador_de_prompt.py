__author__ = 'cristian'
import Prompt
import pilasengine
'''
este modulo maneja las imagenes y cursor del Prompt



'''

class ControladorDePrompt:
    def __init__(self, pilas):
        # creo la instancia para cada movimiento q voy a realizar
        # se guarda de la forma de tupla (<instancia_felcha>,<instancia_numero>,int_numero)
        # sin int_numero==0 entonces <instancia_numero>==0, y no voy a tener un actor
        # como para eliminarlo o desplazarlo por el prompt.


        self.imag_avanzar='imag/Prompt/avanzar.png'
        self.imag_retroceder='imag/Prompt/retroceder.png'
        self.imag_derecha='imag/Prompt/derecha.png'
        self.imag_izquierda='imag/Prompt/izquierda.png'
        self.imag_cursor='imag/Prompt/cursor.png'
        self.imag_1='imag/Prompt/1.png'
        self.imag_2='imag/Prompt/2.png'
        self.imag_3='imag/Prompt/3.png'
        self.imag_4='imag/Prompt/4.png'
        self.imag_5='imag/Prompt/5.png'
        self.imag_6='imag/Prompt/6.png'
        self.imag_7='imag/Prompt/7.png'
        self.imag_8='imag/Prompt/8.png'
        self.imag_9='imag/Prompt/9.png'
        self.pilas = pilas
        self.overfl=False




        self.prompt=Prompt.iniciar(3,9)


         #  Completo las posiciones de las  flechas
        x=-765
        y=-530
        for i in range(0,9):
            t=(x,y)
            self.prompt.set_coordenadas(0,i,t)          # en la fila 0 estan las coordenadas de las flechas y los numeros
            x=x+129

        #  Completo las posiciones de los numeros
        x=-720
        y=-500
        for i in range(0,9):
            t=(x,y)
            self.prompt.set_coordenadas(1,i,t)          # en la fila 1 estan las coordenadas de los numeros
            x=x+129

        #  Completo las posiciones del cusor
        x=-762
        y=-530
        for i in range(0,9):
            t=(x,y)
            self.prompt.set_coordenadas(2,i,t)          # en la fila 2 estan las coordenadas del cursor
            x=x+129





    def aparecer_botones(self):
        cursor_grilla=self.pilas.imagenes.cargar_grilla('imag/Prompt/cursorpront.png',17)
        self.cursor = self.pilas.actores.Animacion(cursor_grilla, ciclica=True, velocidad=50)
        self.__mueve_cursor()

        self.boton_cursor_derecha=self.pilas.actores.Boton(x=513,y=-530,ruta_normal='imag/Prompt/derecha_prompt_1.png', ruta_press='imag/Prompt/derecha_prompt_2.png', ruta_over='imag/Prompt/derecha_prompt_2.png')
        self.boton_cursor_derecha.conectar_presionado(self.__cursor_derecha)
        self.boton_cursor_derecha.conectar_sobre(self.boton_cursor_derecha.pintar_presionado)
        self.boton_cursor_derecha.conectar_normal(self.boton_cursor_derecha.pintar_normal)

        self.boton_cursor_izquierda=self.pilas.actores.Boton(x=414,y=-530,ruta_normal='imag/Prompt/izquierda_prompt_1.png', ruta_press='imag/Prompt/izquierda_prompt_2.png', ruta_over='imag/Prompt/izquierda_prompt_2.png')
        self.boton_cursor_izquierda.conectar_presionado(self.__cursor_izquierda)
        self.boton_cursor_izquierda.conectar_sobre(self.boton_cursor_izquierda.pintar_presionado)
        self.boton_cursor_izquierda.conectar_normal(self.boton_cursor_izquierda.pintar_normal)


    def eliminar_todo(self):
        self.pr.elimino_todo()

    def __cursor_derecha(self):  #deplaza cursor sobre el prompt

        control=self.prompt.inc_poscursor()


        if control==False and self.prompt.dim_logica_visible == self.prompt.dim_fisica_visible-1:
            c=self.prompt.desplaza_derecha()
            self.__refresh_screen('derecha')
            self.__mueve_cursor()
            return c
        else:
            self.__mueve_cursor()
            return True


    def __cursor_izquierda(self): #desplaza cursor sobre el prompt
        control=self.prompt.dec_poscursor()

        if control==False and self.prompt.dim_logica_visible == self.prompt.dim_fisica_visible-1:
            self.prompt.desplaza_izquierda()
            self.__refresh_screen('izquierda')
        self.__mueve_cursor()



    def agregar_elemento(self,direccion,cantidad):
        __doc__="al Agregar una direccion y cantidad" \
                "se crea a partir de estos valores una instancia de actor flecha y otra de actor n" \
                "en caso de que la cantidad sea ==0 entonces no se crea la instancia del actor n"


        if cantidad==1:
            self.n=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_1)
            self.n.set_imagen(imagen)




        if cantidad==2:
            self.n=self.pilas.actores.Actor(x=300,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_2)
            self.n.set_imagen(imagen)


        if cantidad==3:
            self.n=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_3)
            self.n.set_imagen(imagen)

        if cantidad==4:
            self.n=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_4)
            self.n.set_imagen(imagen)



        if cantidad==5:
            self.n=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_5)
            self.n.set_imagen(imagen)



        if cantidad==6:
            self.n=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_6)
            self.n.set_imagen(imagen)




        if cantidad==7:
            self.n=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_7)
            self.n.set_imagen(imagen)



        if cantidad==8:
            self.n=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_8)
            self.n.set_imagen(imagen)


        if cantidad==9:
            self.n=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_9)
            self.n.set_imagen(imagen)




        if direccion=='avanzar':
            self.flecha=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_avanzar)
            self.flecha.set_imagen(imagen)



        if direccion=='retroceder':
            self.flecha=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_retroceder)
            self.flecha.set_imagen(imagen)




        if direccion=='der':
            self.flecha=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_derecha)
            self.flecha.set_imagen(imagen)


        if direccion=='izq':
            self.flecha=self.pilas.actores.Actor(x=500,y=-530)
            imagen = self.pilas.imagenes.cargar(self.imag_izquierda)
            self.flecha.set_imagen(imagen)




        # si mi cursor esta posicionado en cualquier lado
        #primero acomodo el cursor , luego muestro en pantalla lo que se agrega
        self.prompt.cursor=self.prompt.get_dim_logica_visible()+1
        self.__mueve_cursor()
        if self.overfl==True:
            c=self.__cursor_derecha()
            self.prompt.cursor=self.prompt.get_dim_logica_visible()
            self.__mueve_cursor()
            while c==True:
                c=self.__cursor_derecha()






        if cantidad==0:
            self.__agrego_al_prompt(self.flecha,0,cantidad)

        elif cantidad>0:
            self.__agrego_al_prompt(self.flecha,self.n,cantidad)



    def __agrego_al_prompt(self,objeto_flecha,objeto_numero,int_numero):
        t=(objeto_flecha,objeto_numero,int_numero)
        r=self.prompt.setElemento(t)
        self.__refresh_screen('agregar',r)


    def __refresh_screen(self,refresh_type,condicion='ok'):
        __doc__="recibe como parametro el tipo de refresh,teniendno en cuenta la condicion q se recibe en lo q se va a" \
                "hacer en la pantalla"

        if refresh_type=='agregar' and condicion=='ok':
            lista=self.prompt.elemVisibles

            i=0
            for elemento in lista:
                #los elementos son tuplas
                #(<flecha>,<numero>,int_cantidad)

                if elemento[2]!=0:
                    n=elemento[1]
                    Coord=self.prompt.get_coordenada(1,i) #en la fila 0 de la matriz tengo las coordenadas de los numeros
                    n.x=Coord[0]
                    n.y=Coord[1]
                    if self.prompt.cursor==i:
                        n.escala=0
                        n.escala=[1],0.1

                flecha=elemento[0]

                Coord=self.prompt.get_coordenada(0,i) #en la fila 1 de la matriz tengo las coordenadas de las flehcas

                flecha.x=Coord[0]
                flecha.y=Coord[1]
                if self.prompt.cursor==i:
                        flecha.escala=0
                        flecha.escala=[1],0.1
                i=i+1

            self.prompt.inc_poscursor()
            self.__mueve_cursor()


        if refresh_type=='agregar' and condicion=='overflow':
            #entonces hay que eliminar el elemento anterior!
            self.overfl=True
            lista=self.prompt.elemVisibles

            obj_anterior=self.prompt.elemAnt
            if obj_anterior[2]!=0:
                    n=obj_anterior[1]
                    n.x=-2000
                    n.y=-2000
            flecha=obj_anterior[0]
            flecha.x=-2000
            flecha.y=-2000

            i=0
            for elemento in lista:
                #los elementos son tuplas
                #(<flecha>,<numero>,int_cantidad)

                if elemento[2]!=0:
                    n=elemento[1]
                    Coord=self.prompt.get_coordenada(1,i) #en la fila 1 de la matriz tengo las coordenadas de los numeros
                    n.x=Coord[0]
                    n.y=Coord[1]
                    if self.prompt.cursor==i:
                        n.escala=0
                        n.escala=[1],0.1

                flecha=elemento[0]
                Coord=self.prompt.get_coordenada(0,i) #en la fila 0 de la matriz tengo las coordenadas de las flehcas
                flecha.x=Coord[0]
                flecha.y=Coord[1]
                if self.prompt.cursor==i:
                        flecha.escala=0
                        flecha.escala=[1],0.1
                i=i+1


        if refresh_type=='izquierda' or refresh_type=='derecha':
            #entonces hay que eliminar el elemento anterior!

            lista=self.prompt.elemVisibles

            obj_anterior=self.prompt.elemAnt
            if obj_anterior[2]!=0:
                n=obj_anterior[1]
                n.x=-2000
                n.y=-2000
            flecha=obj_anterior[0]
            flecha.x=-2000
            flecha.y=-2000

            i=0
            for elemento in lista:
            #los elementos son tuplas
            #(<flecha>,<numero>,int_cantidad)

                if elemento[2]!=0:
                    n=elemento[1]
                    Coord=self.prompt.get_coordenada(1,i) #en la fila 1 de la matriz tengo las coordenadas de los numeros
                    n.x=Coord[0]
                    n.y=Coord[1]

                flecha=elemento[0]
                Coord=self.prompt.get_coordenada(0,i) #en la fila 0 de la matriz tengo las coordenadas de las flehcas
                flecha.x=Coord[0]
                flecha.y=Coord[1]
                i=i+1





    def __mueve_cursor(self):

        pos=self.prompt.getPoscursor()

        coord=self.prompt.get_coordenada(2,pos)

        if coord<>False:
            self.cursor.x=coord[0]
            self.cursor.y=coord[1]











iniciar=ControladorDePrompt
