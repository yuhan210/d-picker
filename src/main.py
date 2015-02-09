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
    print "----- Simulation starts ------"
    print "Client number:", client_num
    print "Simulation length:", sim_duration 
    # create a list of clients
    clients = []
    for i in xrange(client_num):
        #client = Client(i, "hinge", 4000, 500, 200)
        client = Client(i, "hinge", 1/4000.0, 500, 200)
        clients += [client]       
    
    # create scheduler
    greedy = Greedy()
    
    # each step, client with pending jobs determines whether to send a job with some nwk delay   
    cur_time = 0.0
    total_score = 0.0
    while ( cur_time < sim_duration ):
        
        # update client info
        timedout_clients = filter(lambda x: x.hasTimedOut(cur_time) , clients)
        for tc in timedout_clients:
            tc.genJob(cur_time)
        arrived_clients = filter(lambda x: x.getJobArrivalTime() <= cur_time, clients)
                
        total_score += greedy.schedule(cur_time, arrived_clients) 
        
        # update what scheduler sees
        cur_time += 1.0

   # simulation is over, get overall utility score
    print "Total score:", total_score
