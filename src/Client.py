import math
from Utility import *
from random import *

class Client(object):
    nwk_delay = -1.0
    utility_fn = None
    utility_fn_name = ""
    utility_para = -1.0
    job_gen_para = -1.0
    job_start_time = -1  
    def __init__(self, utility_fn_name, utility_para, job_para,nwk_delay):
        
        self.nwk_delay = nwk_delay
        self.utility_fn_name = utility_fn_name
        self.utility_para = utility_para
        self.job_gen_para = job_para
        self.utility_fn = Utility(self.utility_fn_name, self.utility_para)
        self.job_start_time = self.exponential(self.job_gen_para)
    
    def exponential(self, para): # para -> lambda
        return (-1.0)* para * math.log(1 - random()) 
    
    def getStartTime(self):
        return self.job_start_time
