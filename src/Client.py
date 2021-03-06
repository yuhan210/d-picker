import math
from Utility import *
from random import *
from scipy.stats import norm

class Client(object):

    # Global variables
    # some of them might need to be modified to be more realistic
    JOB_HARDNESS_MEAN = 300.0
    JOB_HARDNESS_STD = 20.0

    cid = -1
    nwk_delay = -1.0
    utility_fn = None
    utility_fn_name = ""
    utility_para = -1.0
    job_gen_para = -1.0
    job_arrival_time = -1  
    job_start_time = 0
    job_hardness = -1 # time required to process the job
    served_hist = []

    def __init__(self, cid, utility_fn_name, utility_para, job_gen_mean, nwk_delay):
        self.cid = cid
        self.nwk_delay = nwk_delay # should be updated
        self.utility_fn_name = utility_fn_name
        self.utility_para = utility_para
        self.job_gen_para = job_gen_mean
        self.utility_fn = Utility(self.utility_fn_name, self.utility_para)
        self.served_hist = []
        self.genJob(0)

    def getServedList(self):
        return self.served_hist
             
    def getCid(self):
        return self.cid
         
    def hasTimedOut(self, cur_ts):
        if self.utility_fn.has_timedout(cur_ts - self.job_start_time):
            return True
        return False
         
    def genJob(self, cur_ts):
        self.job_start_time = cur_ts + self.exponential(self.job_gen_para)
        self.job_arrival_time = self.job_start_time + self.nwk_delay
        self.job_hardness = self.normal(self.JOB_HARDNESS_MEAN, self.JOB_HARDNESS_STD) # mean, std
    
    def normal(self, mean, std):
        return norm.ppf(random(), loc=mean, scale=std)
     
    def exponential(self, para): # para -> lambda
        return (-1.0)* para * math.log(1 - random()) 
    
    def getJobArrivalTime(self):
        return self.job_arrival_time

    def getUtility(self, cur_ts):
        if self.job_arrival_time > cur_ts:
            print "Warning: job hasn't arrived yet!", cur_ts, ", ", self.job_arrival_time
        
        score = self.utility_fn.get_utility(cur_ts - self.job_start_time)
        return score

    def toString(self, cur_ts):
        return "Client ID:" +  str(self.cid) + ", start time:" + str(self.job_start_time) \
               + ", arrive time:" +  str(self.job_arrival_time) +  ", hardness:" +  str(self.job_hardness) \
               + ", utility:" +  str(self.getUtility(cur_ts))

    def getServed(self, cur_ts):
        #print "Time:", cur_ts, " ",  self.toString(cur_ts)
        score = self.utility_fn.get_utility(cur_ts - self.job_start_time)
        self.served_hist += [(self.cid, cur_ts, score)]
        server_sleep_time = self.job_hardness
        # once get served, reset job creation time, and arrival time
        self.genJob(cur_ts) 
          
        return (score, server_sleep_time)
