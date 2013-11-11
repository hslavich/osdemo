import threading, time

class Clock(threading.Thread):
    def __init__(self, timer):
        super(Clock, self).__init__()
        self.timer = timer
        self.name = "Clock"
        self.start()

    def run(self):
        while True:
            time.sleep(1)
            self.timer.tick()
