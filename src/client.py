from Utility import *

class Client(object):
    nwk_delay = -1
    utility_fn = None

    def __init__(self, utility_fn_name, para, nwk_delay):
        
        self.nwk_delay = nwk_delay
        self.utility_fn = Utility(utility_fn_name, para)


