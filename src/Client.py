import math
from Utility import *
from random import *

class Client(object):
    nwk_delay = -1.0
    utility_fn = None
    utility_fn_name = ""
    utility_para = -1.0
    job_gen_para = -1.0
    job_arrival_time = -1  
    job_start_time = 0
    served_hist = []

    def __init__(self, utility_fn_name, utility_para, job_para, nwk_delay):
        
        self.nwk_delay = nwk_delay
        self.utility_fn_name = utility_fn_name
        self.utility_para = utility_para
        self.job_gen_para = job_para
        self.utility_fn = Utility(self.utility_fn_name, self.utility_para)
        self.genJob(0)
             
    def genJob(self, cur_ts):
        self.job_start_time = cur_ts + self.exponential(self.job_gen_para)
        self.job_arrival_time = self.job_start_time + self.nwk_delay
          
    def exponential(self, para): # para -> lambda
        return (-1.0)* para * math.log(1 - random()) 
    
    def getJobArrivalTime(self):
        return self.job_arrival_time

    def getUtility(self, cur_ts):
        if cur_ts > job_arrival_time:
            print "Error: job hasn't arrived yet!"
            exit(-1)
        score = utility_fn.get_utility(cur_ts - self.job_start_time)
        return score

    def getServed(self, cur_ts):
        score = utility_fn.get_utility(cur_ts - self.job_start_time)
        served_hist += (cur_ts, score)
        return score
