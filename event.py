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
        Event.eventos.append(Event(ran.exponential(tiempo_entre_llegadas), Event.llegada))
        Event.tiempo_entre_llegadas = tiempo_entre_llegadas
        Event.tiempo_estacionado = time_serving

    def new_arrive(time):
        Event.eventos.append(Event(time + ran.exponential(Event.tiempo_entre_llegadas), Event.llegada))
        Event.eventos.sort(key=lambda tup: tup.time)

    def new_depart(time):
        Event.eventos.append(Event(time + ran.exponential(Event.tiempo_estacionado), Event.salida))
        Event.eventos.sort(key=lambda tup: tup.time)

    def get_next_event():
        return Event.eventos.pop(0)
