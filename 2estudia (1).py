from event import Event
import random as rd

tiempo_entre_llegadas = 2
time_serving = 1
total_events = 100


#Initialize
clock = 0
Event.init_events(tiempo_entre_llegadas,time_serving)
clients_in_queue = 0
estacionamiento_ocupado_x = False

estacionamiento_ocupado_0 = False
estacionamiento_ocupado_1 = False
estacionamiento_ocupado_2 = False

#report variables
clients = [clients_in_queue]
time = [clock]


estacionamientos = []
for evento in range(total_events):
    estacionamientos.append(rd.randint(0, 2))

for i in estacionamientos:

    if i == 0:
        estacionamiento_ocupado_x = estacionamiento_ocupado_0
    elif i == 1:
        estacionamiento_ocupado_x = estacionamiento_ocupado_1
    elif i == 2:
        estacionamiento_ocupado_x = estacionamiento_ocupado_2

    current_event = Event.get_next_event()
    clock = current_event.time

    if current_event.type == Event.llegada:
        Event.new_arrive(clock)
        clients_in_queue += 1

        if estacionamiento_ocupado == False:
            clients_in_queue -= 1
            estacionamiento_ocupado_x = True
            Event.new_depart(clock)

    elif current_event == Event.salida:
        if clients_in_queue > 0:
            estacionamiento_ocupado_x = True
            clients_in_queue -= 1
            Event.new_depart(clock)
        else:
            estacionamiento_ocupado_x = False

    time.append(clock)
    clients.append(clients_in_queue)
    estacionamiento.append(estacionamiento_ocupado_x)

#report
report = open("report.csv","w")
for time, cas, cli in zip(time,estacionamiento,clients):
    report.write(str(time)+","+str(cas)+","+str(cli)+"\n")
report.close()
