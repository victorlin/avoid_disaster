# -*- coding: utf8 -*-
'''
Created on 2010/6/27

@author: Victor Lin (bornstub@gmail.com)
'''
import logging

import boto.s3.connection
from boto import s3

import base

log = logging.getLogger(__name__)

class S3Storage(base.Storage):
    
    def __init__(self, accessKey, secretKey, bucketName):
        """
        
        @param accessKey: access key of Amazon S3
        @param secretKey: secret key of Amazon S3
        @param bucketName: name of bucket
        """
        self.conn = s3.connection.S3Connection(accessKey, secretKey)
        self.bucket = self.conn.create_bucket(bucketName)
        
    def list(self):
        for key in self.bucket.list():
            yield key.name
    
    def exists(self, name):
        return self.bucket.lookup(name) is not None
        
    def write(self, name, data):
        key = s3.key.Key(self.bucket, name)
        key.set_contents_from_string(data)
        log.info('Write data %d bytes to "%s"', len(data), name)

    def writeFromFile(self, name, file):
        key = s3.key.Key(self.bucket, name)
        key.set_contents_from_file(file)
        log.info('Write file %s to "%s"', file, name)
        
    def read(self, name):
        key = s3.key.Key(self.bucket, name)
        data = key.get_contents_as_string()
        log.info('Read %d bytes from "%s"', len(data), name)
        return data
    
    def readToFile(self, name, file):
        key = s3.key.Key(self.bucket, name)
        key.get_contents_to_file(file)
        log.info('Read "%s" to file %s', name, file)
