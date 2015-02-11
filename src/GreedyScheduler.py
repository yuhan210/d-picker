import logging
from Utility import *
from Client import *

class Greedy(object):
    logger = None

    def __init__(self): 
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    # return the utility score
    def schedule(self, cur_time, jobs):
        
        if len(jobs) == 0:
            return (0.0, 0)
        score = 0.0
             
        best_utility = max(map(lambda x: x.getUtility(cur_time), jobs)) 
        best_job = [job for job in jobs if job.getUtility(cur_time) == best_utility][0]
        
        (score, sleep_time) = best_job.getServed(cur_time)
        self.logger.debug("Time:" +  str(cur_time) +  ", serve job:" +  str(best_job.getCid()) +  ", receiving utility:" +  \
                     str(score))
        return (score, sleep_time)        
