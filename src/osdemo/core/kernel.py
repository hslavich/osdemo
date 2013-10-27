from process.pcb import PCB
from core.cpu import CPU
from scheduling.scheduler import Scheduler

class Kernel():

    def __init__(self):
        self.scheduler = Scheduler()
        self.cpu = CPU(self)

    def irq(self, type, pcb):
        if type == "FINISH":
            self._evt_finish(pcb)
        elif type == "CPU":
            self.scheduler.add_process(pcb)
            next = self.scheduler.get_next()
            if self.cpu.process != next:
                self.cpu.assign(next)

    def _evt_finish(self, pcb):
        self.scheduler.remove_process(pcb)

    def load(self, program):
        pcb = PCB(program)
        self.irq("CPU", pcb)
