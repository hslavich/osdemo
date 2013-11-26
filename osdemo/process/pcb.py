class PCB(object):

    NEW = 0
    READY = 1
    RUNNING = 2
    WAITING_IO = 3
    IO = 4
    END = 5

    def __init__(self, program, pid, priority = 5):
        self.program = program
        self.pid = pid
        self.pc = 0
        self.priority = priority
        self.state = PCB.NEW
        self.total_instructions = len(program.instructions)

    def increment_pc(self):
        self.pc += 1

    def current_instruction(self):
        return self.program.instructions[self.pc]

    def is_finished(self):
        return self.pc >= self.total_instructions
