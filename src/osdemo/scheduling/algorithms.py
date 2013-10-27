class FCFS(object):

    def __init__(self, scheduler):
        super(FCFS, self).__init__()
        self.scheduler = scheduler

    def choose_next(self):
        return self.scheduler.processes[0]
