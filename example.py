'''
Created on 2010/6/30

@author: Victor-mortal
'''
import logging 

import avoid_disaster
from avoid_disaster.targets import static, mysql
from avoid_disaster.handlers import zip
from avoid_disaster.storages import s3
from avoid_disaster.managers import base

logging.basicConfig(level=logging.INFO)

handler = zip.Zip()
storage = s3.S3Storage('your_access_key', 
                       'your_secret_key', 
                       'bucket_name')

backup = base.BackupManager()

target = static.Static('/path/to/dir_or_file')
backup.add('backup_dir.%(week_number)s.zip', target, handler, storage)

target = mysql.Mysql('user', 'password', 'database')
backup.add('backup_mysql.%(week_number)s.zip', target, handler, storage)

backup.run()