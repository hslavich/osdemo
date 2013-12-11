class Block(object):

    def __init__(self, size):
        super(Block, self).__init__()
        self.size = size
        self.pcb = None

    def compact(self):
        if self.pcb:
            free = self.size - self.pcb.size
            self.size = self.pcb.size
            return Block(free)
        return None

    def expand(self, size):
        self.size = self.size + size

    def __str__(self):
        if not self.pcb:
            free = "FREE"
        else:
            free = "'PID %s'" % self.pcb.pid

        return "[%sKB (%s)]" % (self.size, free)
