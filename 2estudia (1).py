from event import EVENT

tiempo_entre_llegada = 2
tiempo_estacionado = 1
eventos_totales = 1000

# inicialización
reloj = 0
Event.init_events(tiempo_entre_llegada, tiempo_estacionado)
en_cola = 0
estacionamientos_ocupados = False

# reporte de variables
autos = [en_cola]
tiempo = [reloj]
estacionamiento = [estacionamientos_ocupados]

for i in range(eventos_totales):
    evento_actual = Event.get_next_event()
    reloj = evento_actual.time
    if current_event.type == Event.ARRIVE:
        Event.new_arrive(clock)
        en_cola += 1
        if estacionamientos_ocupados == False:
            en_cola -= 1
            estacionamientos_ocupados = True
            Event.new_depart(tiempo)
    elif current_event == Event.DEPART:
        if en_cola > 0:
            estacionamientos_ocupados = True
            en_cola -= 1
            Event.new_depart(clock)
        else:
            estacionamientos_ocupados = False

    tiempo.append(tiempo)
    autos.append(en_cola)
    estacionamiento.append(estacionamientos_ocupados)

report = open("report.csv", "w")
for time, cas, cli in zip(tiempo, cashier,clients):
    report.write(str(time) + " ," + str(cas) + " ," + str(cli) + "\n")
report.close()
