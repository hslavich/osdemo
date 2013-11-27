import logging
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

    def set_algorithm(self, algo):
        try:
            m = __import__("osdemo.scheduling.algorithms")
            m = getattr(m, "scheduling")
            m = getattr(m, "algorithms")
            self.strategy = getattr(m, algo)(self)
        except Exception:
            raise Exception("Can't set algorithm " + algo)
        logging.info("SCHEDULER algorithm set %s" % algo)

