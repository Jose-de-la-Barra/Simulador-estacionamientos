import numpy.random as ran
import time as tm

class Event:
 ARRIVE = 1
 DEPART = 0
 PARK = 2
 events = []
 TIME_BETWEEN_ARRIVES = 0
 TIME_SERVING = 0
 TIME_PARKING = 0

 def __init__(self,time,type,num):
   self.time = time
   self.type = type
   self.num = num

 @property
 def time(self):
   return self.__time

 @time.setter
 def time(self,new_time):
   self.__time = new_time

 @property
 def type(self):
   return self.__type

 @type.setter
 def type(self, new_type):
   self.__type = new_type

 def init_events(time_between_arrives, tiempo_estacionado, time_parking):
   Event.events = []
   Event.events.append(Event(ran.exponential(time_between_arrives), Event.ARRIVE, 1))
   Event.TIME_BETWEEN_ARRIVES = time_between_arrives
   Event.TIME_SERVING = tiempo_estacionado
   Event.TIME_PARKING = time_parking

 def new_arrive(time, num_est):
   Event.events.append(Event(time + ran.exponential(Event.TIME_BETWEEN_ARRIVES),Event.ARRIVE, num_est))
   Event.events.sort(key=lambda tup: tup.time)

 def new_depart(time,num_est):
   Event.events.append(Event(time + ran.exponential(Event.TIME_SERVING),  Event.DEPART, num_est))
   Event.events.sort(key=lambda tup: tup.time)

 def estacionarse(time, num_est, tiempo_estacionar):
     Event.events.append(Event(tiempo_estacionar, Event.PARK, num_est))
     Event.events.sort(key=lambda tup: tup.time)


 def get_next_event():
   return Event.events.pop(0)
