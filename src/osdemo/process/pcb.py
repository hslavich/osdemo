class PCB(object):

    def __init__(self, program):
        self.program = program
        self.pc = 0
        self.priority = 0
        self.total_instructions = len(program.instructions)

    def increment_pc(self):
        self.pc += 1

    def current_instruction(self):
        self.program.instructions[self.pc]

    def is_finished(self):
        return self.pc >= self.total_instructions
