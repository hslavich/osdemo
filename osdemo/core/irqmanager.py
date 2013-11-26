import threading, logging
from Queue import Queue

class IRQManager(threading.Thread):

    def __init__(self, kernel):
        super(IRQManager, self).__init__()
        self.kernel = kernel
        self._irqs = Queue()
        self.start()

    def add_irq(self, irq):
        self._irqs.put(irq)

    def _process_irqs(self):
        (type, pcb) = self._irqs.get(True)
        logging.debug("IRQ %s PID: %s", type, pcb.pid)
        if type == "IO":
            self.kernel._evt_io(pcb);
        if type == "READY":
            self.kernel._evt_ready(pcb)
        elif type == "TIMEOUT":
            self.kernel._evt_timeout(pcb)
        elif type == "FINISH":
            self.kernel._evt_finish(pcb)
        self.kernel._exec_pcb()

    def run(self):
        while True:
            self._process_irqs()
