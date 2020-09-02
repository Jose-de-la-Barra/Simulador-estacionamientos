import numpy.random as ran


class Evento:
    llegada = 1
    salida = 0
    eventos = []
    tiempo_entre_llegadas = 0
    tiempo_estacionado = 0

    def __init__(self, time, type):
        self.time = time
        self.type = type

    def time(self):
        return self.__time

    def time(self, new_time):
        self.__time = new_time

    def type(self):
        return self.__type

    def type(self, new_type):
        self.__type = new_type

    def init_events(tiempo_entre_llegadas, time_serving):
        Evento.eventos.append(Evento(ran.exponential(tiempo_entre_llegadas), Evento.llegada))
        Evento.tiempo_entre_llegadas = tiempo_entre_llegadas
        Evento.tiempo_estacionado = time_serving

    def new_arrive(time):
        Evento.eventos.append(Evento(time + ran.exponential(Evento.tiempo_entre_llegadas), Evento.llegada))
        Evento.eventos.sort(key=lambda tup: tup.time)

    def new_depart(time):
        Evento.eventos.append(Event(time + ran.exponential(Event.tiempo_estacionado), Evento.salida))
        Evento.eventos.sort(key=lambda tup:tup.time)

    def get_next_event():
        return Evento.eventos.pop(0)

