from osdemo.core.clock import Clock

class Timer(object):

    def __init__(self, kernel, cpu):
        super(Timer, self).__init__()
        self.cpu = cpu
        self.quantum = None
        self.kernel = kernel
        Clock(self)

    def _decrease_quantum(self):
        if self.quantum != None:
            self.quantum -= 1

    def _return_process(self):
        p = self.cpu.process
        if p:
            self.kernel.irq("TIMEOUT", p)

    def tick(self):
        self.cpu.fetch()
        self._decrease_quantum()
        if self.quantum != None and self.quantum == 0:
            self._return_process()
