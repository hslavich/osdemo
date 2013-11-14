import time
from Queue import PriorityQueue

class FCFS(object):

    def __init__(self, scheduler):
        super(FCFS, self).__init__()
        self.scheduler = scheduler

    def choose_next(self):
        try:
            return self.scheduler.processes[0]
        except IndexError:
            return None


class Priority(object):

    def __init__(self, scheduler):
        super(Priority, self).__init__()
        self.scheduler = scheduler

    def choose_next(self):
        ps = self.scheduler.processes
        if ps:
            queue = PriorityQueue()
            for p in ps:
                queue.put((p.priority, time.time(), p))
            return queue.get()[2]
        else:
            return None
