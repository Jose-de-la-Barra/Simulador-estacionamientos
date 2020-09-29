import numpy.random as ran
from event import Event

time_between_arrives = 20
tiempo_estacionado = 90
total_events = 30

# Initialize
clock = 0
Event.init_events(time_between_arrives, tiempo_estacionado)


# report variables
autos_totales = []
autos = []
time = [clock]
numero_estacionamiento = []
estacionados = [0, 0, 0]
tipo_evento = []


for i in range(total_events):
  current_event = Event.get_next_event()
  clock = current_event.time

  if current_event.type == Event.ARRIVE:
    num_est = ran.randint(0, 3)
    estacionados[current_event.num] += 1
    Event.new_arrive(clock, num_est)
    Event.new_depart(clock,current_event.num)

  elif current_event.type == Event.DEPART:
    num_est = current_event.num
    estacionados[num_est] -= 1
  clock = round(clock, 1)

#  if (clock < 60):
#    if (clock < 10):
#      clock = (f"0:0{clock}")
#    else:
#      clock = (f"0:{clock}")
#  elif (clock >= 60):
#    minu = (clock % 60)
#    hora = ((clock - minu) / 60)
#    if (minu < 10):
#      clock = (f"{hora}:0{minu}")
#    else:
#      clock = (f"{int(hora)}:{minu}")


  time.append(clock)
  est = estacionados[current_event.num]
  numero_estacionamiento.append(current_event.num)
  autos.append(est)
  tipo_evento.append(current_event.type)
  total = estacionados[0] + estacionados[1] + estacionados[2]
  autos_totales.append(total)

# report
report = open("report.csv", "w")
report.write("Tiempo|Numero Est.|Ocupado|Cantidad Autos|Sin cupo\n")
for time, num, auto, type, total in zip(time, numero_estacionamiento, autos, tipo_evento, autos_totales):
  if type == 1:
    tipo = "Llegada"
  else:
    tipo = "Salida"
  report.write(str(time)+","+str(num)+","+str(auto)+","+str(tipo)+","+str(total)+"\n")
report.close()
