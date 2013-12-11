class FirstFit(object):

    def __init__(self, memory):
        super(FirstFit, self).__init__()
        self.memory = memory

    def get_block(self, size):
        for block in self.memory.blocks:
            if block.size >= size and not block.pcb:
                return block
        raise Exception("No block available")

class BestFit(object):

    def __init__(self, memory):
        super(BestFit, self).__init__()
        self.memory = memory

    def get_block(self, size):
        pass

class WorstFit(object):

    def __init__(self, memory):
        super(WorstFit, self).__init__()
        self.memory = memory

    def get_block(self, size):
        pass
