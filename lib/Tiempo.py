__author__ = 'cristian'
import datetime


class Tiempo(object):
    def __init__(self):
        self._start_time = None
        self._end_time = None
        self._pause_time = None
        self._pause = None

    def iniciar_tiempo(self):
        self._start_time = datetime.datetime.now()

    def getiniciar_tiempo(self):
       return self._start_time

    def finalizar_tiempo(self):
        self._end_time = datetime.datetime.now()

    def next_time(self,seconds=0):
        self.inicio_next = datetime.datetime.now()
        self.fin_next=self.inicio_next + datetime.timedelta(seconds=seconds)
        return self.fin_next

    def getInicionext(self):
        return self.inicio_next
        
    def startPause(self):
        self._pause = datetime.datetime.now()
    
    def stopPause(self):
        self._pause_time = datetime.datetime.now() - self._pause

    def actual (self):
        return datetime.datetime.now()

    def _getTiempo_transcurrido(self):
        """
        cacula el tiempo desde que se llamo al metodo iniciar tiempo, hasta que se lo finalizo

        :return: tiempo transcurrido
        """
        if self._start_time <> None:
            if self._end_time <> None:
                try:
					print self._end_time - self._start_time
					print self._end_time - self._start_time - self._pause_time
                except:
					print self._end_time - self._start_time
                t = self._end_time - self._start_time if self._pause_time == None else self._end_time - self._start_time - self._pause_time
                return t
            else:
                print '*Falta invocar a metodo finalizar_tiempo*'
        else:
            print '*Primero invoca al metodo iniciar_tiempo*'

    elapsed = property(_getTiempo_transcurrido)


iniciar = Tiempo
