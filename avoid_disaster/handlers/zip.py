'''
Created on 2010/6/30

@author: Victor-mortal
'''
import os
import zipfile
import tempfile

import base

class Zip(base.FileHandler):
    
    def __init__(self, compression=zipfile.ZIP_DEFLATED, allowZip64=False):
        self.compression = compression
        self.allowZip64 = allowZip64
    
    def process(self, path, file):
        temp = tempfile.NamedTemporaryFile()
        zip = zipfile.ZipFile(temp, 'w', self.compression, self.allowZip64)
        if not file:
            assert os.path.isdir(path)
            for root, _, files in os.walk(path):
                for file in files:
                    path = os.path.join(root, file)
                    zip.write(path, path)
        else:
            data = file.read()
            zip.writestr(os.path.basename(path), data)
        zip.close()
        return temp
    
if __name__ == '__main__':
    z = Zip()
    print z.process('.')