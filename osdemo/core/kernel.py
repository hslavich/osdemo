from osdemo.process.pcb import PCB
from osdemo.core.cpu import CPU
from osdemo.core.timer import Timer
from osdemo.scheduling.scheduler import Scheduler

class Kernel():

    _pid_count = 1

    def __init__(self):
        self.scheduler = Scheduler()
        self.cpu = CPU(self)
        self.timer = Timer(self, self.cpu)

    def irq(self, type, pcb):
        if type == "TIMEOUT":
            self._evt_timeout(pcb)
        elif type == "FINISH":
            self._evt_finish(pcb)
        elif type == "CPU":
            self.scheduler.add_process(pcb)
        self._exec_pcb()

    def _exec_pcb(self):
        if self.scheduler.processes:
            (next, quantum) = self.scheduler.get_next()
            if self.cpu.process != next:
                self.timer.quantum = quantum
                self.cpu.assign(next)

    def _evt_timeout(self, pcb):
        self.cpu.free()
        self.scheduler.remove_process(pcb)
        self.scheduler.add_process(pcb)

    def _evt_finish(self, pcb):
        self.scheduler.remove_process(pcb)

    def load(self, program, priority = None):
        pid = self.__class__._pid_count = self.__class__._pid_count + 1
        pcb = PCB(program, pid, priority)
        self.irq("CPU", pcb)
