import builtins # * imports the builtins module which contains the print function among other things.

# * The idea of the following is overwriting the built-in print function with a dummy function that does nothing when print is disabled, and restoring the original print function when print is re-enabled. 

class TogglePrint:
    def __init__(self):
        self.originalPrint = builtins.print
        # * saves the original print function from the builtins module in the instance variable orig_print.
        self.enabled = True
        
    def __enter__(self):
        # * defines a method that is called when the instance is used as a context manager with a with statement. If you do not use it in a with block, this is useless.
        self.disable()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # * defines a method that is called when the instance is used as a context manager with an exit out of a with statement. If you do not use it in a with block, this is useless.
        self.enable()

    def enable(self):
        self.enabled = True
        builtins.print = self.originalPrint
        # * restores the original print function from the originalPrint instance variable.

    def disable(self):
        self.enabled = False
        builtins.print = lambda *args, **kwargs: None # * sets the print function to a lambda function that does nothing.


'''
Test

togglePrint = TogglePrint()

togglePrint.disable()

print("Error in TogglePrint class in togglePrinting.py!")

togglePrint.enable()

print("TogglePrint class is working.")

'''

'''
To use in another module:

from togglePrinting import *

printer = TogglePrint()

Then call to enable printing:

printer.enable()

Call to disable printing:

printer.disable()
'''
