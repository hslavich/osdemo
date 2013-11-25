import time
from Queue import PriorityQueue

class FCFS(object):

    def __init__(self, scheduler):
        super(FCFS, self).__init__()
        self.scheduler = scheduler

    def choose_next(self):
        try:
            return (self.scheduler.processes[0], None)
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
            return (queue.get()[2], None)
        else:
            return None

class RoundRobin(object):

    def __init__(self, scheduler):
        super(RoundRobin, self).__init__()
        self.scheduler = scheduler
        self.quantum = 2

    def choose_next(self):
        try:
            return (self.scheduler.processes[0], self.quantum)
        except IndexError:
            return None

class RoundRobinPriority(object):

    def __init__(self, scheduler):
        super(RoundRobinPriority, self).__init__()
        self.scheduler = scheduler
        self.quantum = 2

    def choose_next(self):
        (p, _) = Priority(self.scheduler).choose_next()
        if p:
            return (p, self.quantum)
        else:
            return None
