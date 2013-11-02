from osdemo.scheduling import algorithms

class Scheduler(object):

    def __init__(self):
        self.processes = []
        self.strategy = algorithms.FCFS(self)

    def add_process(self, process):
        self.processes.append(process)

    def remove_process(self, process):
        self.processes.remove(process)

    def get_next(self):
        return self.strategy.choose_next()
