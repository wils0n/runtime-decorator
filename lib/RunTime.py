# -*- coding: utf-8 *-*

import time


class Time:
    def __init__(self, a):
        self.a = a
        self.__ini = 0.0
        self.__fin = 0.0

    def __call__(self, *args, **kwargs):
        print ".......iniciando el analisis"
        self.__iniciar()
        self.a(*args, **kwargs)
        self.__finalizar()

        print ".......finalizando el analisis"
        print "Su algoritmo tardo: %f segundos" % self.duracion()
        print "Su algoritmo tardo: ", self.duracion()

    def __iniciar(self):
        self.__ini = time.time()

    def __finalizar(self):
        self.__fin = time.time()

    def duracion(self):
        return self.__fin - self.__ini
