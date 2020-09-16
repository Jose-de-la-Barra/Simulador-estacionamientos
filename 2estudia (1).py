from event import Estacionamiento
import random as ran

tiempo_entre_llegadas = 5
time_serving = 1
total_events = 10


# Initialize
clock = 0
Estacionamiento.init_events(tiempo_entre_llegadas, time_serving)

clients_in_queue = 0
estacionamiento_ocupado = False
##
estacionamiento_ocupado_2 = False
##

# report variables
clients = [clients_in_queue]
time = [clock]
estacionamientos = [estacionamiento_ocupado]

##
estacionamientos_2 = [estacionamiento_ocupado_2]
##

for i in range(total_events):

    current_event = Estacionamiento.get_next_event()
    clock = current_event.time

    ocupado = False
    lista_est = [estacionamiento_ocupado, estacionamiento_ocupado_2]
    actual = ran.choice(lista_est)
    if actual == estacionamiento_ocupado:
        ocupado = estacionamiento_ocupado


    elif actual == estacionamiento_ocupado_2:
        ocupado = estacionamiento_ocupado_2

    if current_event.type == Estacionamiento.llegada:
        Estacionamiento.new_arrive(clock)
        clients_in_queue += 1

        if ocupado == False:
            clients_in_queue -= 1
            ocupado = True
            Estacionamiento.new_depart(clock)

    elif current_event.type == Estacionamiento.salida:
        if clients_in_queue > 0:
            ocupado = True
            clients_in_queue -= 1
            Estacionamiento.new_depart(clock)
        else:
            ocupado = False

    time.append(clock)
    clients.append(clients_in_queue)

    if ocupado == estacionamiento_ocupado:
        estacionamientos.append(ocupado)

    elif ocupado == estacionamiento_ocupado_2:
        estacionamientos_2.append(ocupado)

# report
report = open("report.csv", "w")
for time, cas, cli in zip(time, estacionamientos, clients):
    report.write('Estacionemiento 1: ' + str(time)+","+str(cas)+","+str(cli)+"\n")
report.close()


# report 2
# report = open("report_2.csv", "w")
# for time_2, cas_2, cli_2 in zip(time, estacionamientos_2, clients):
#    report.write('Estacionemiento 2: ' + str(time_2)+","+str(cas_2)+","+str(cli_2)+"\n")
# report.close()
