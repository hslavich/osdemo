import threading

class Memory(object):

    def __init__(self, manager):
        super(Memory, self).__init__()
        self.manager = manager
        self._lock = threading.Lock()

    def load(self, pcb):
        with self._lock:
            self.manager.load(pcb)

    def unload(self, pcb):
        with self._lock:
            self.manager.unload(pcb)

    def readInstruction(self, pcb):
        with self._lock:
            return self.manager.readInstruction(pcb)

    def __str__(self):
        with self._lock:
            return str(self.manager)
