from enum import Enum
import os
import logging

import datetime

class Log_Levels(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

class CommonLogger:

    def __init__(self, folder_path,log_file):
                # 分析ファイル格納用のフォルダを作成
        tmp = os.path.join(folder_path,'03_logs')
        if not os.path.exists(tmp):
            os.makedirs(tmp)

        self.log_file = os.path.join(tmp,log_file)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def out_put_Log(self ,message, level=Log_Levels.DEBUG):
        self.logger.log(level.value, message)

# test_logss = CommonLogger
# test_logss.__init__(test_logss, 'test.log')
# test_logss.out_put_Log(test_logss,'test', Log_Levels.CRITICAL)

      