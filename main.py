import os
import CommandBuilder
'''

Build UI

'''
cb = CommandBuilder.CommandBuilder()

'''
Some operations :
all CommandBuilder methods must be invoked in UI
'''

os.system(cb.returnTestCommand())
