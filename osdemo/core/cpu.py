import threading, time, logging

class CPU(threading.Thread):

    def __init__(self, kernel):
        threading.Thread.__init__(self)
        self._lock = threading.Condition()
        self.name = "CPU"
        self.process = None
        self.ci = None
        self.kernel = kernel
        self.start()

    def assign(self, pcb):
        with self._lock:
            self.process = pcb
            self._lock.notify()

    def _execute_process(self):
        pcb = self.process
        self.ci = pcb.current_instruction()
        self._execute_instruction()
        pcb.increment_pc()
        if pcb.is_finished():
            self._free()
            self.kernel.irq("FINISH", pcb)

    def _execute_instruction(self):
        logging.debug("CPU exec PID: %s, INSTR: %s" % (self.process.pid, self.process.pc))
        time.sleep(2)

    def _free(self):
        self.process = None
        self.ci = None

    def run(self):
        while True:
            with self._lock:
                while not self.process:
                    logging.debug("CPU IDLE")
                    self._lock.wait()
                self._execute_process()
