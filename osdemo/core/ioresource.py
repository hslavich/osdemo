import threading, time, logging

class IOResource(threading.Thread):

    def __init__(self, name, iomanager):
        super(IOResource, self).__init__()
        self.name = name
        self.process = None
        self.iomanager = iomanager
        self.start()

    def _execute(self):
        logging.info("IO %s exec PID: %s, INSTR: %s" % (self.name, self.process.pid, self.process.pc))
        time.sleep(3)
        self.process.increment_pc()
        self.iomanager.finish_io(self, self.process)

    def free(self):
        self.process = None

    def run(self):
        while True:
            self.process = self.iomanager.waiting.get(True)
            self._execute()
