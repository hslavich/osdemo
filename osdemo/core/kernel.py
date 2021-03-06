from osdemo.process.pcb import PCB
from osdemo.core.cpu import CPU
from osdemo.core.timer import Timer
from osdemo.core.iomanager import IOManager
from osdemo.core.irqmanager import IRQManager
from osdemo.scheduling.scheduler import Scheduler
from osdemo.memory.memory import Memory
from osdemo.memory.continuous import ContinuousAssignment
import logging

class Kernel():

    _pid_count = 1

    def __init__(self):
        self.scheduler = Scheduler()
        self.memory = Memory(ContinuousAssignment())
        self.cpu = CPU(self, self.memory)
        self.timer = Timer(self, self.cpu)
        self.io_manager = IOManager(self)
        self.irq_manager = IRQManager(self)

    def irq(self, type, pcb):
        self.irq_manager.add_irq((type, pcb))

    def _exec_pcb(self):
        if self.scheduler.processes:
            (next, quantum) = self.scheduler.get_next()
            if self.cpu.process != next:
                self.timer.quantum = quantum
                self.cpu.assign(next)

    def _evt_timeout(self, pcb):
        self.cpu.free()
        try:
            self.scheduler.remove_process(pcb)
            self.scheduler.add_process(pcb)
        except ValueError:
            pass

    def _evt_io(self, pcb):
        self.cpu.free()
        self.scheduler.remove_process(pcb)
        self.io_manager.add_process(pcb)

    def _evt_ready(self, pcb):
        self.scheduler.add_process(pcb)

    def _evt_finish(self, pcb):
        logging.info("KERNEL finish PID: %s" % pcb.pid)
        self.scheduler.remove_process(pcb)
        self.memory.unload(pcb)

    def load(self, program, priority = None):
        pid = self.__class__._pid_count = self.__class__._pid_count + 1
        pcb = PCB(program, pid, priority)
        try:
            self.memory.load(pcb)
            self.irq("READY", pcb)
        except Exception:
            logging.error("No memory available")
