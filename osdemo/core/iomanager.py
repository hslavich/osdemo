from osdemo.core.ioresource import IOResource
from Queue import Queue

class IOManager(object):

    def __init__(self, kernel):
        super(IOManager, self).__init__()
        self.kernel = kernel
        self.resources = []
        self.waiting = Queue()
        self._init_resources()

    def _init_resources(self):
        self.resources.append(IOResource("IORES1", self))
        self.resources.append(IOResource("IORES2", self))
        self.resources.append(IOResource("IORES3", self))

    def finish_io(self, resource, pcb):
        resource.free()
        self.kernel.irq("READY", pcb)

    def add_process(self, process):
        self.waiting.put(process)
