import threading, time

class IOResource(threading.Thread):

    def __init__(self, name, iomanager):
        super(IOResource, self).__init__()
        self.name = name
        self.process = None
        self.iomanager = iomanager

    def assign(self, process):
        self.process = process

    def _execute(self):
        time.sleep(2)
        self.process.increment_pc()
        self.iomanager.finish_io()

    def free(self):
        self.process = None

    def run(self):
        while True:
            if self.process:
                self._execute()
            else:
                time.sleep(2)
