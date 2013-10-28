import threading, time, logging

class CPU(threading.Thread):

    def __init__(self, kernel):
        threading.Thread.__init__(self)
        self.name = "CPU"
        self.process = None
        self.kernel = kernel
        self.start()

    def assign(self, pcb):
        self.process = pcb

    def _execute_process(self):
        p = self.process
        ci = p.current_instruction()
        self._execute_instruction(ci)
        p.increment_pc()
        if p.is_finished():
            self._free()
            self.kernel.irq("FINISH", p)

    def _execute_instruction(self, i):
        logging.debug("CPU exec instruction")
        time.sleep(2)

    def _free(self):
        self.process = None

    def run(self):
        while True:
            if self.process:
                self._execute_process()
            else:
                logging.debug("CPU INACTIVA")
                time.sleep(2)
