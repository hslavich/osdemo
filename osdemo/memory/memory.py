class Memory(object):

    def __init__(self, manager):
        super(Memory, self).__init__()
        self.manager = manager

    def load(self, pcb):
        self.manager.load(pcb)

    def unload(self, pcb):
        self.manager.unload(pcb)

    def readInstruction(self, pcb):
        return self.manager.readInstruction(pcb)

    def __str__(self):
        return ' '.join(map(str, self.blocks))
