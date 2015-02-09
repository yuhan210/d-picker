import sys
import matplotlib.pyplot as plt
from Utility import *
from Client import *
from GreedyScheduler import *

## a discrete-time event simulator

if __name__ == "__main__":

    if ( len(sys.argv) != 3 ):
        print "Usage:", sys.argv[0], " client_num sim_duration(ms)" 
        exit(-1)

    client_num = int(sys.argv[1])
    sim_duration = int(sys.argv[2])

    # create a list of clients
    clients = []
    for i in xrange(client_num):
        client = Client(i, "0-1", 4000, 500, 200)
        clients += [client]       
    
    # create scheduler
    greedy = Greedy()
    
    # each step, client with pending jobs determines whether to send a job with some nwk delay   
    cur_time = 0.0
    total_score = 0.0
    while ( cur_time < sim_duration ):
        
        # update client info
        arrived_clients = filter(lambda x: x.getJobArrivalTime() <= cur_time, clients)
                
        total_score += greedy.schedule(cur_time, arrived_clients) 
        
        # update what scheduler sees
        cur_time += 1.0

   # simulation is over, get overall utility score
    print total_score
