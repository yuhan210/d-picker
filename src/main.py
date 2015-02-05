import sys
from Utility import *

if __name__ == "__main__":

    if (len(sys.argv) != 2):
        print "Usage:", sys.argv[0], " client_num" 
        exit(-1)

    u = Utility("")
    u.get_utility(8)
