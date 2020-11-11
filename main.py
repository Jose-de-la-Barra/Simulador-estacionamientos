import numpy.random as ran
from event import Event
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


def estacionar(estacionamientos):
  for i in range(len(estacionamientos)):
    if estacionamientos[i] < 1:
      estacionamientos[i] = 1
      return i
  return -1

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)


#time_between_arrives = 30
#tiempo_estacionado = 200
total_events = 1000

avg_queu = []
rhos = []

t_para_estacionar = 0.5
tiempo_espera = 7

for i in range(30, 330, 30):
  
  time_between_arrives = 30
  tiempo_estacionado = i
  aux_fig = plt.figure(figsize=(10, 8))
  aux_ax = aux_fig.add_subplot(111)


# Initialize
  clock = 0
  Event.init_events(time_between_arrives, tiempo_estacionado, t_para_estacionar)


  # report variables
  autos_totales = []
  autos = []
  time = [clock]
  numero_estacionamiento = []
  estacionados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  tipo_evento = []


  for i in range(total_events):
    current_event = Event.get_next_event()
    clock = current_event.time

    #########
    if current_event.type == Event.ARRIVE:
      num_est = estacionar(estacionados)
      Event.new_arrive(clock, num_est)


      if num_est==-1:
        if Event.f() < tiempo_espera:
          Event.estacionarse(num_est, Event.f()+0.000000000001)

        else:
          Event.new_depart(clock + tiempo_espera, -1)
      else:
        estacionados[num_est] += 1
        Event.new_depart(clock + tiempo_estacionado, -1)


      
  #    Event.new_depart(clock, current_event.num)
  #    if total > 10:
  #      if tiempo_espera <
  #        Event.estacionarse(num_est, t_para_estacionar)
    #########

    # Cuando llega y no hay comenzamos a contar
    # estacionarse
    elif current_event.type == Event.PARK:
      num_est = current_event.num
      estacionados[num_est] += 1
      Event.new_depart(clock + tiempo_estacionado, -1)




    elif current_event.type == Event.DEPART:
      num_est = current_event.num
      estacionados[num_est] -= 1
    clock = round(clock, 1)

    time.append(clock)
    est = estacionados[current_event.num]
    numero_estacionamiento.append(current_event.num)
    autos.append(est)
    tipo_evento.append(current_event.type)
    total = sum(estacionados)  # estacionados[0] + estacionados[1] + estacionados[2] + estacionados[3] + estacionados[4] + estacionados[5] + estacionados[6] + estacionados[7] + estacionados[8] + estacionados[9]
    autos_totales.append(total)
    print(estacionados)

  # report
  report = open("report"+str(tiempo_estacionado/time_between_arrives)+".csv", "w")
  report.write("Tiempo|Numero Est.|Cola por estacionamiento|Tipo de evento|Autos en sistema\n")
  for time, num, auto, type, total in zip(time, numero_estacionamiento, autos, tipo_evento, autos_totales):
    if type == 1:
      tipo = "Llegada"
    elif type == 0:
      tipo = "Salida"

    report.write(str(time)+","+str(num)+","+str(auto)+","+str(tipo)+","+str(total)+"\n")
  report.close()

  avg_queu.append(sum(autos_totales)/len(autos_totales))
  rhos.append(tiempo_estacionado/time_between_arrives)
  aux_ax.plot(autos_totales)
  aux_fig.savefig('graph'+str(rhos[-1])+'.png')

ax.plot(rhos,avg_queu)
plt.xlabel("Carga de tráfico")
fig.savefig('graph.png')
