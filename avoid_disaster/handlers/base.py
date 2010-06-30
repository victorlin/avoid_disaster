'''
Created on 2010/6/30

@author: Victor-mortal
'''

class FileHandler(object):
    """FileHandler for packaging a path of file into a single file, might be
    zip or some compressed file
    
    """
    
    def process(self, path, file):
        """Package target file into a single file
        
        @param path: path of file to process
        @param file: file object to process
        @return: the result file object
        """
        raise NotImplemented