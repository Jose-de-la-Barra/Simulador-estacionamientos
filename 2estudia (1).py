from event import Estacionamiento

tiempo_entre_llegadas = 2
time_serving = 1
total_events = 100
ran.seed(10)


#Initialize
clock = 0
Estacionamiento.init_events(tiempo_entre_llegadas, time_serving)
clients_in_queue = 0
estacionamiento_ocupado = False

#report variables
clients = [clients_in_queue]
time = [clock]
estacionamientos = [estacionamiento_ocupado]

for i in range(total_events):

    current_event = Estacionamiento.get_next_event()
    clock = current_event.time

    if current_event.type == Estacionamiento.llegada:
        Estacionamiento.new_arrive(clock)
        clients_in_queue += 1

        if estacionamiento_ocupado == False:
            clients_in_queue -= 1
            estacionamiento_ocupado = True
            Estacionamiento.new_depart(clock)

    elif current_event == Estacionamiento.salida:
        if clients_in_queue > 0:
            estacionamiento_ocupado = True
            clients_in_queue -= 1
            Estacionamiento.new_depart(clock)
        else:
            estacionamiento_ocupado = False

    time.append(clock)
    clients.append(clients_in_queue)
    estacionamientos.append(estacionamiento_ocupado)

#report
report = open("report.csv","w")
for time, cas, cli in zip(time,estacionamientos,clients):
    report.write(str(time)+","+str(cas)+","+str(cli)+"\n")
report.close()
