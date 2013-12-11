import logging, threading

class CPU(object):

    def __init__(self, kernel, memory):
        super(CPU, self).__init__()
        self.process = None
        self.ci = None
        self.kernel = kernel
        self.memory = memory
        self._lock = threading.Condition()

    def assign(self, pcb):
        with self._lock:
            self.process = pcb
            self._lock.notify()

    def _execute_process(self):
        pcb = self.process
        self.ci = self.memory.readInstruction(pcb)
        self._execute_instruction()
        pcb.increment_pc()
        if pcb.is_finished():
            self.free()
            self.kernel.irq("FINISH", pcb)

    def _execute_instruction(self):
        logging.info("CPU exec PID: %s, INSTR: %s" % (self.process.pid, self.process.pc))

    def free(self):
        with self._lock:
            self.process = None
            self.ci = None

    def fetch(self):
        with self._lock:
            while not self.process:
                self._lock.wait()
            if self.process.current_instruction().type == "IO":
                self.kernel.irq("IO", self.process)
            else:
                self._execute_process()

