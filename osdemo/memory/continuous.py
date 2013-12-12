import logging
from osdemo.memory.block import Block
from osdemo.memory import allocation

class ContinuousAssignment(object):

    def __init__(self):
        super(ContinuousAssignment, self).__init__()
        self.size = 50
        self.blocks = [Block(self.size)]
        self.allocation = allocation.FirstFit(self)

    def load(self, pcb):
        block = self._try_get_block(pcb.size)
        self._assign_pcb(pcb, block)
        new_block = block.compact()
        if new_block and new_block.size:
            index = self.blocks.index(block)
            self.blocks.insert(index + 1, new_block)
            self._merge()

    def unload(self, pcb):
        block = pcb.base
        block.pcb = None
        pcb.base = None
        self._merge()

    def readInstruction(self, pcb):
        return pcb.current_instruction()

    def _try_get_block(self, size):
        try:
            return self.allocation.get_block(size)
        except Exception:
            self._compact()
        return self.allocation.get_block(size)


    def _merge(self):
        new_blocks = [self.blocks[0]]
        for i in range(1, len(self.blocks)):
            prev = new_blocks[-1]
            curr = self.blocks[i]
            if not prev.pcb and not curr.pcb:
                prev.expand(curr.size)
            else:
                new_blocks.append(curr)
        self.blocks = new_blocks

    def _assign_pcb(self, pcb, block):
        block.pcb = pcb
        pcb.base = block

    def _compact(self):
        logging.info("MEMORY compacting")
        free_blocks = []
        used_blocks = []
        for block in self.blocks:
            if not block.pcb:
                free_blocks.append(block)
            else:
                used_blocks.append(block)
        used_blocks.extend(free_blocks)
        self.blocks = used_blocks
        self._merge()

    def __str__(self):
        return ' '.join(map(str, self.blocks))
