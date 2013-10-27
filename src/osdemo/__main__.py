from core.kernel import Kernel
from process.program import Program
from process.instruction import Instruction

if __name__ == '__main__':
    k = Kernel()

    p = Program("test")
    p.instructions.append(Instruction("CPU"))
    p.instructions.append(Instruction("CPU"))
    p.instructions.append(Instruction("CPU"))
    k.load(p)
