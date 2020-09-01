import numpy.random as ran


class Event:
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
        Event.eventos.append(Event(ran.exponential(tiempo_entre_llegadas), Event.llegda))
        Event.tiempo_entre_llegadas = tiempo_entre_llegadas
        Event.tiempo_estacionado = time_serving

    def new_arrive (time):
        Event.eventos.append(Event(time + ran.exponential(Event.tiempo_entre_llegadas), Event.llegda))
        Event.eventos.sort(key=lambda tup: tup.time)

    def new_depart(time):
        Event.eventos.append(Event(time + ran.exponential(Event.tiempo_estacionado), Event.salida))
        Event.eventos.sort(key=lambda tup:tup.time)

    # puse self
    def get_next_event(self):
        return Event.eventos.pop(0)

