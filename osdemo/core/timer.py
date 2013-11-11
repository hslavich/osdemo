class Timer(object):

    def __init__(self, kernel, cpu):
        super(Timer, self).__init__()
        self.cpu = cpu
        self.quantum = None
        self.kernel = kernel

    def tick(self):
        self.cpu.fetch()
