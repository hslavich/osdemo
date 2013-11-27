import threading, time, logging

class IOResource(threading.Thread):

    def __init__(self, name, iomanager):
        super(IOResource, self).__init__()
        self.name = name
        self.process = None
        self.iomanager = iomanager
        self._lock = threading.Condition()
        self.start()

    def assign(self, process):
        with self._lock:
            self.process = process
            self._lock.notify()

    def _execute(self):
        logging.info("IO %s exec PID: %s, INSTR: %s" % (self.name, self.process.pid, self.process.pc))
        time.sleep(3)
        self.process.increment_pc()
        self.iomanager.finish_io(self, self.process)

    def is_available(self):
        return self.process == None

    def free(self):
        with self._lock:
            self.process = None

    def run(self):
        while True:
            with self._lock:
                while not self.process:
                    self._lock.wait()
                self._execute()
