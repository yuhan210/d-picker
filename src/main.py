import sys
import matplotlib.pyplot as plt
from Utility import *
from Client import *

## a discrete-time event simulator

if __name__ == "__main__":

    if ( len(sys.argv) != 3 ):
        print "Usage:", sys.argv[0], " client_num sim_duration" 
        exit(-1)

    client_num = int(sys.argv[1])
    sim_duration = int(sys.argv[2])

    # create a list of clients
    clients = []

    xs = []
    for i in xrange(client_num):
        client = Client("0-1", 3000, 500, 500)
        clients += [client]       
        xs +=[client.getStartTime()]        
    
    # each step, client with pending jobs determines whether to send a job with some nwk delay   
    cur_time = 0
    while ( cur_time < sim_duration ):
        # update client info
                
        # update what scheduler sees

        cur_time += 1

   # simulation is over, get overall utility score

