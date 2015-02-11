from Utility import *
from Client import *

class FIFO(object):

#    def __init__(self):
    def schedule(self, cur_time, jobs):
        if len(jobs) == 0:
            return (0.0, 0)
        score = 0.0
        
        oldest_arrival_time = min(map(lambda x: x.getJobArrivalTime(), jobs))
        oldest_job = [job for job in jobs if job.getJobArrivalTime() == oldest_arrival_time][0]
        (score, sleep_time) = oldest_job.getServed(cur_time)
        
        print "Time:", cur_time, "serve job:", oldest_job.getCid(), "receiving utility:", score, "\n"
        return (score, sleep_time)        
