
from event import Event

time_between_arrives = 2
time_serving = 1
total_events = 1000

#Initialize
clock = 0
Event.init_events(time_between_arrives,time_serving)
clients_in_queue = 0
cashier_busy = False

#report variables
clients = [clients_in_queue]
time = [clock]
cashier = [cashier_busy]
for i in range(total_events):
    current_event = Event.get_next_event()
    clock = current_event.time
    if current_event.type == Event.ARRIVE:
        Event.new_arrive(clock)
        clients_in_queue += 1
        if cashier_busy == False:
            clients_in_queue -= 1
            cashier_busy = True
            Event.new_depart(clock)
    elif current_event == Event.DEPART:
        if clients_in_queue > 0:
            cashier_busy = True
            clients_in_queue -=1
            Event.new_depart(clock)
        else:
            cashier_busy = False
    time.append(clock)
    clients.append(clients_in_queue)
    cashier.append(cashier_busy)

#report
report = open("report.csv","w")
for time, cas, cli in zip(time,cashier,clients):
    report.write(str(time)+","+str(cas)+","+str(cli)+"\n")
report.close()
