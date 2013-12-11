import logging, sys
from osdemo.core.kernel import Kernel
from osdemo.shell.commands import Commands

sys.path.append('lib/pyshell')
from pyshell.model.shell import Shell
from pyshell.gui.shellframe import ShellFrame

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s | %(message)s', level=logging.INFO)
    k = Kernel()

    shell = Shell()
    shell.addCommand("load", Commands(k).load)
    shell.addCommand("scheduler", Commands(k).scheduler)
    shell.addCommand("memory", Commands(k).memory)
    ShellFrame(shell).start()

