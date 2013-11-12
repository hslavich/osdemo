import logging, sys
from osdemo.core.kernel import Kernel
from osdemo.process.program import Program
from osdemo.process.instruction import Instruction
from osdemo.shell.commands import Commands

sys.path.append('lib/pyshell')
from pyshell.model.shell import Shell
from pyshell.gui.shellframe import ShellFrame

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s | %(message)s', level=logging.DEBUG)
    k = Kernel()

    p = Program("test")
    p.instructions = [Instruction("CPU"), Instruction("CPU"), Instruction("CPU")]
    p2 = Program("test2")
    p2.instructions = [Instruction("CPU"), Instruction("CPU"), Instruction("CPU")]
    p3 = Program("test3")
    p3.instructions = [Instruction("CPU"), Instruction("CPU"), Instruction("CPU")]
    k.load(p)
    k.load(p2)
    k.load(p3)

    shell = Shell()
    shell.addCommand("load", Commands(k).load)
    ShellFrame(shell).start()

