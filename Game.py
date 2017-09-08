import pilasengine

import escenas

#~ pilas = pilasengine.iniciar(ancho=2751, alto=1306, titulo='Robot', centrado=False, pantalla_completa=False)
pilas = pilasengine.iniciar(ancho=2751, alto=1306, titulo='Robot',  pantalla_completa=True)
#~ pilas = pilasengine.iniciar(ancho=1024, alto=486, titulo='Robot', pantalla_completa=False)


#vinculo
pilas.escenas.vincular(escenas.EscenaDeUsuarios)
pilas.escenas.vincular(escenas.EscenaDeMenu)
#~ pilas.escenas.vincular(escenas.EscenaMenuq) #deprecated
pilas.escenas.vincular(escenas.EscenaDeJuego)
pilas.escenas.vincular(escenas.EscenaDeAyuda)
pilas.escenas.vincular(escenas.Opciones)

pilas.escenas.EscenaDeUsuarios()

pilas.ejecutar()
