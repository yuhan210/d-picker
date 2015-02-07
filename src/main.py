import sys
from Utility import *

if __name__ == "__main__":

    if ( len(sys.argv) != 2 ):
        print "Usage:", sys.argv[0], " client_num" 
        exit(-1)

    # create a list of clients
    u = Utility("")
    u.get_utility(8)
    
    sim_duration = 200000
    # each step, client with pending jobs determines whether to send a job with some nwk delay   
    while     
   
    #    
