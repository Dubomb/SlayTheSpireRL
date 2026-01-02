import os
import datetime

class GameDebugger:
    def __init__(self, filename):
        self.filename = filename
        
        script_path = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.join(script_path, f'log/{filename}')

        self.file = open(self.path, 'w')
        self.file.write(f'Script began at {datetime.datetime.now()}\n')
        self.file.write('=========================\n')
        self.file.flush()
    
    def log_message(self, message):
        self.file.write(f'{datetime.datetime.now()} > {message}\n')
        self.file.flush()
        
    def log_warning_message(self, message):
        self.log_message(f'WARNING:\n{message}')

    def log_error_message(self, message):
        self.log_message(f'ERROR:\n{message}')
    
    def close(self):
        if self.file:
            self.file.close()
    
    def __del__(self):
        self.close()
    
    def __enter__(self):
        return self

    def __exit__(self):
        self.close()