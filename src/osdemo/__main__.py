import logging
from core.kernel import Kernel
from process.program import Program
from process.instruction import Instruction

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
