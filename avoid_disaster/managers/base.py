import os
import logging
import datetime
import types

log = logging.getLogger(__name__)

class BackupManager(object):
    
    def __init__(self):
        self.backups = []
    
    def add(self, name, target, handler, storage, replaceOld=True):
        """Add backup
        
        """
        self.backups.append((name, target, handler, storage, replaceOld))
        
    def _generateFileName(self, name):
        now = datetime.datetime.utcnow()
        common = {
            'weekday': now.strftime("%A"),
            'month_name': now.strftime("%B"),
            'week_number': now.strftime("%U")
        }
        return name % common
        
    def run(self):
        """Back up everything
        
        """
        # TODO: we should catch the exceptions and handle them here
        log.info('Starting backup process ...')
        for name, target, handler, storage, replaceOld in self.backups:
            log.info('Dump target %s', target)
            dumpPath, dumpFile = target.dump()
            
            log.info('Processing with handler %s ...', handler)
            output = handler.process(dumpPath, dumpFile)
            output.seek(0, os.SEEK_SET)
            
            fileName = self._generateFileName(name)
            log.info('Store %s to storage %s ...', fileName, storage)
            
            if not replaceOld:
                if storage.exists(fileName):
                    log.error('%s already exists in storage %s', 
                              fileName, storage)
                    continue
            storage.writeFromFile(fileName, output)
            
