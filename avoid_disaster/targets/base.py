'''
Created on 2010/6/30

@author: Victor-mortal
'''

class TargetError(Exception):
    """Error of file target
    
    """

class Target(object):
    """File target for backup
    
    """
    
    def dump(self):
        """Dump files for backup, for example, execute the mysqldump or 
        svnadmin dump to a temporary file
        
        @return: (file path of target, file object)
            if the file is a directory, the file object should be None
        """