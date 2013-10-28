import logging
from core.kernel import Kernel
from process.program import Program
from process.instruction import Instruction

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s | %(message)s', level=logging.DEBUG)
    k = Kernel()

    p = Program("test")
    p.instructions.append(Instruction("CPU"))
    p.instructions.append(Instruction("CPU"))
    p.instructions.append(Instruction("CPU"))
    k.load(p)
