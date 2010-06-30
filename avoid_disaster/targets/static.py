'''
Created on 2010/6/30

@author: Victor-mortal
'''
import os

import base

class Static(base.Target):
    """Static file target
    
    """
    
    def __init__(self, path):
        self.path = path
    
    def dump(self):
        file = None
        if not os.path.isdir(self.path):
            file = open(self.path, 'rb')
        return self.path, file