'''
Created on 2010/6/30

@author: Victor-mortal
'''
import tempfile
import subprocess
import logging

import base

log = logging.getLogger(__name__)

class Mysql(base.Target):
    """Mysql target
    
    """
    
    def __init__(self, user, password, database):
        self.user = user
        self.password = password
        self.database = database
        
    def dump(self):
        temp = tempfile.NamedTemporaryFile()
        cmd = 'mysqldump -u %s -p%s %s' % (
            self.user, self.password, self.database) 
        p = subprocess.Popen(cmd, stdout=temp, stderr=subprocess.PIPE, shell=True)
        if p.wait():
            error = p.stderr.read()
            log.error('Failed to execute mysqldump:')
            log.error(error)
            raise base.TargetError, 'Failed to execute mysqldump: %s' % error
        else:
            log.info('mysqldump finished.')
        temp.seek(0)
        return self.database + '.sql', temp
