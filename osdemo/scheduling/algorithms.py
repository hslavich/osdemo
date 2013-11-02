class FCFS(object):

    def __init__(self, scheduler):
        super(FCFS, self).__init__()
        self.scheduler = scheduler

    def choose_next(self):
        try:
            return self.scheduler.processes[0]
        except IndexError:
            return None
