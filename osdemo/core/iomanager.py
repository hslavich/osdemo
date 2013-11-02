from osdemo.core.ioresource import IOResource

class IOManager(object):

    def __init__(self, kernel):
        super(IOManager, self).__init__()
        self.kernel = kernel
        self.resources = []
        self._init_resources()

    def _init_resources(self):
        self.resources.append(IOResource("IORES1"))
        self.resources.append(IOResource("IORES2"))
        self.resources.append(IOResource("IORES3"))

    def finish_io(self, resource):
        pcb = resource.process
        resource.free()
        self.kernel.irq("READY", pcb)
