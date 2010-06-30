'''
Created on 2010/6/26

@author: Victor Lin (bornstub@gmail.com)
'''

class Storage(object):
    """A base class for file storage
    
    """
    
    def list(self):
        """List all files' name
        
        @return: an iterator to all files in this storage
        """
        raise NotImplemented
    
    def exists(self, name):
        """Check does a name exists in storage
        
        @return: True if the name of file exists in the storage, otherwise False
        """
        raise NotImplemented
        
    def write(self, name, data):
        """Write chunk of data to storage
        
        @param name: name of file in storage to write
        @param data: data to write
        """
        raise NotImplemented

    def writeFromFile(self, name, file):
        """Write a file to storage
        
        @param name: Name of file to write
        """
        
    def read(self, name):
        """Read content of file
        
        @param name: name of file in storage to read
        @return: A file like object contains the content of file
        """
        raise NotImplemented
    
    def readToFile(self, name, file):
        """Read content of data to a file
        
        @param name: name of file in storage to read
        @param file: file-like object to write content of file to
        """
        raise NotImplemented