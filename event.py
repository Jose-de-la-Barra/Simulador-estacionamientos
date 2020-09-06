import numpy.random as ran

ran.seed(17)

class Estacionamiento:
    llegada = 1
    salida = 0
    eventos = []
    tiempo_entre_llegadas = 0
    tiempo_estacionado = 0

    def __init__(self, time, type):
        self.time = time
        self.type = type

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, new_time):
        self.__time = new_time

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type):
        self.__type = new_type

    def init_events(tiempo_entre_llegadas, time_serving):

        Estacionamiento.eventos.append(Estacionamiento(ran.exponential(tiempo_entre_llegadas), Estacionamiento.llegada))
        Estacionamiento.tiempo_entre_llegadas = tiempo_entre_llegadas
        Estacionamiento.tiempo_estacionado = time_serving

    def new_arrive(time):
        Estacionamiento.eventos.append(Estacionamiento(time + ran.exponential(Estacionamiento.tiempo_entre_llegadas), Estacionamiento.llegada))
        Estacionamiento.eventos.sort(key=lambda tup: tup.time)

    def new_depart(time):
        Estacionamiento.eventos.append(Estacionamiento(time + ran.exponential(Estacionamiento.tiempo_estacionado), Estacionamiento.salida))
        Estacionamiento.eventos.sort(key=lambda tup: tup.time)

    def get_next_event():
        return Estacionamiento.eventos.pop(0)
