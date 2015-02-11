import logging
from Utility import *
from Client import *


class FIFO(object):
    logger = None
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
         
    def schedule(self, cur_time, jobs):
        if len(jobs) == 0:
            return (0.0, 0)
        score = 0.0
        
        oldest_arrival_time = min(map(lambda x: x.getJobArrivalTime(), jobs))
        oldest_job = [job for job in jobs if job.getJobArrivalTime() == oldest_arrival_time][0]
        (score, sleep_time) = oldest_job.getServed(cur_time)
        
        self.logger.debug("Time:" +  str(cur_time) +  ", serve job:" +  str(oldest_job.getCid()) +  ", receiving utility:" +  \
                     str(score))
        return (score, sleep_time)        
