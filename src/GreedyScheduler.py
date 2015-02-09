from Utility import *
from Client import *

class Greedy(object):

    def __init__(self): 
        w = 1      
    def schedule(self, cur_time, jobs):
       
        best_utility = max(filter(lambda x: x.getUtility(cur_time), jobs)) 
        
