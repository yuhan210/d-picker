from Utility import *
from Client import *

class FIFO(object):

#    def __init__(self):
    def schedule(self, cur_time, jobs):
        if len(jobs) == 0:
            return 0.0
        score = 0.0

        oldest_job = min(filter(lambda x: x.getJobArrivalTime(), jobs))
        score += oldest_job.getServed(cur_time)
        
        print "Time:", cur_time, "serve job:", oldest_job.getCid(), "receiving utility:", score
        return score        
