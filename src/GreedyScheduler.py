from Utility import *
from Client import *

class Greedy(object):

    def __init__(self): 
        w = 1      
    def schedule(self, cur_time, jobs):
        
        if len(jobs) == 0:
            return 0.0
        score = 0.0
             
        best_job = max(filter(lambda x: x.getUtility(cur_time), jobs)) 
        score += best_job.getServed(cur_time)
        print "Time:", cur_time, "serve job:", best_job.getCid(), "receiving utility:", score
        return score        
