import logging
import sys
import matplotlib.pyplot as plt
from Utility import *
from Client import *
from GreedyScheduler import *
from FIFOScheduler import *

## a discrete-time event simulator

def printAllClients(ts, clients):
    print ts
    for client in clients:
        print client.toString(ts) 
    print ""

if __name__ == "__main__":

    if ( len(sys.argv) != 3 ):
        print "Usage:", sys.argv[0], " client_num sim_duration(ms)" 
        exit(-1)
    
    client_num = int(sys.argv[1])
    sim_duration = int(sys.argv[2])
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    print "----- Simulation starts ------"
    print "Client number:", client_num
    print "Simulation length:", sim_duration 
    
    # create a list of clients
    clients = []
    for i in xrange(5):
        #client = Client(i, "hinge", 4000, 500, 200)
        client = Client(i, "0-1", 2000.0, 500, 200) 
        clients += [client]       
    for i in xrange(5, 10):
        client = Client(i, "hinge", 1/2000.0, 500, 200)
        clients += [client]
    # create scheduler
    greedy = Greedy()
    fifo = FIFO()
    # each step, client with pending jobs determines whether to send a job with some nwk delay   
    cur_time = 0.0
    total_score = 0.0
    server_wakeup_time = 0.0
    while ( cur_time < sim_duration ):
        
        # update client info
        timedout_clients = filter(lambda x: x.hasTimedOut(cur_time) , clients)
        if (len(timedout_clients) > 0):
            logger.debug( "Time: %d, Job timed out!", cur_time)
            
        for tc in timedout_clients:
            logger.debug(tc.toString(cur_time) + "\n")
            tc.genJob(cur_time)
        
        arrived_clients = filter(lambda x: x.getJobArrivalTime() <= cur_time, clients)
       

        if (cur_time >= server_wakeup_time):
            if len(arrived_clients) > 0:
                logger.debug("server scehduling:")
            for ac in arrived_clients:
                logger.debug(ac.toString(cur_time))

            score = 0.0        
            #(score, sleep_time) = greedy.schedule(cur_time, arrived_clients) 
            (score, sleep_time) = fifo.schedule(cur_time, arrived_clients) 
            server_wakeup_time = cur_time + sleep_time
            total_score += score

        # update what scheduler sees
        cur_time += 1.0

   # simulation is over, get overall utility score
    print "Total score:", total_score
    for client in clients:
        print client.getServedList()  

