__author__ = 'Cristian Steib'
import pilasengine
import escenas

class EscenaDeAyuda(pilasengine.escenas.Escena):
    imag_1='./imag/ayuda/ayuda.jpg'
    imag_2='./imag/ayuda/ayuda2.jpg'


    def iniciar(self):
        self.ls=lista
        self.ayuda1 = self.pilas.actores.Actor(imagen=self.imag_1, x=0, y=0)
        self.ayuda1.transparencia=0
        self.ayuda1.escala=1.75
        self.ayuda2 = self.pilas.actores.Actor(imagen=self.imag_2, x=0, y=0)
        self.ayuda2.transparencia=100
        self.ayuda2.escala=1.75
        self.pos=1 # en que imagen esta posicionada

        self.pulsa_tecla.conectar(self.event2)
        self.pulsa_tecla_escape.conectar(self.__escape)

    def __escape(self,evento):
        self.pilas.recuperar_escena()


    def event2 (self,evento):
        valor=evento['codigo']
        if valor ==2:
            if self.pos==1:

                self.pos=2
                self.down_fadingayuda1()
                self.up_fadingayuda2()
        if valor ==1:
            if self.pos ==2:
                self.pos=1
                self.down_fadingayuda2()
                self.up_fadingayuda1()

    def up_fadingayuda1(self):
        self.ayuda1.transparencia=[0],1

    def up_fadingayuda2(self):
        self.ayuda2.transparencia=[0],1

    def down_fadingayuda1(self):
        self.ayuda1.transparencia=[100],1

    def down_fadingayuda2(self):
        self.ayuda2.transparencia=[100],1


iniciar=EscenaDeAyuda

