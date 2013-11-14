import logging
from osdemo.process.program import Program
from osdemo.process.instruction import Instruction

class Commands(object):

    def __init__(self, kernel):
        super(Commands, self).__init__()
        self.kernel = kernel

    def _parse_instructions(self, name):
        f = open("programs/%s" % name, 'r')
        return [l.strip() for l in f.readlines()]

    def _create_program(self, name, instrs):
        program = Program(name)
        for instr in instrs:
            program.instructions.append(Instruction(instr))
        return program

    def _run(self, name, priority):
        try:
            instr = self._parse_instructions(name)
            prog = self._create_program(name, instr)
            self.kernel.load(prog, priority)
        except Exception, e:
            logging.error(e)

    def load(self, args):
        try:
            name = args[0]
            priority = args[1]
        except IndexError:
            priority = None

        self._run(name, priority)

    def scheduler(self, args):
        self.kernel.scheduler.set_algorithm(args[0])
