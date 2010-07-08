'''
Created on 2010/6/30

@author: Victor-mortal
'''
import tempfile
import subprocess
import logging

import base

log = logging.getLogger(__name__)

class Subversion(base.Target):
    """Subversion repo target
    
    """
    
    def __init__(self, repoPath, fileName='svndump'):
        self.repoPath = repoPath
        self.fileName = fileName
        
    def dump(self):
        temp = tempfile.NamedTemporaryFile()
        cmd = 'svnadmin dump %s' % self.repoPath 
        p = subprocess.Popen(cmd, stdout=temp, stderr=subprocess.PIPE, shell=True)
        if p.wait():
            error = p.stderr.read()
            log.error('Failed to execute svnadmin dump:')
            log.error(error)
            raise base.TargetError, 'Failed to execute svnadmin dump: %s' % error
        else:
            log.info('svnadmin dump finished.')
        temp.seek(0)
        return self.fileName, temp
