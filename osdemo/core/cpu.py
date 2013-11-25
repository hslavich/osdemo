import logging

class CPU(object):

    def __init__(self, kernel):
        super(CPU, self).__init__()
        self.process = None
        self.ci = None
        self.kernel = kernel

    def assign(self, pcb):
        self.process = pcb

    def _execute_process(self):
        pcb = self.process
        self.ci = pcb.current_instruction()
        self._execute_instruction()
        pcb.increment_pc()
        if pcb.is_finished():
            self.free()
            self.kernel.irq("FINISH", pcb)

    def _execute_instruction(self):
        logging.debug("CPU exec PID: %s, INSTR: %s" % (self.process.pid, self.process.pc))

    def free(self):
        self.process = None
        self.ci = None

    def fetch(self):
        if self.process:
            self._execute_process()
