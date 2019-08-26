#!/usr/bin/python
import os
from TI import TI
from defaults import DEFAULT_INDIR

### Use the following for testing
# Note that string must be raw.
string = r"""

"""
tmp1 = TI(text=string)
tmp1.print_output()


### Tidy all files in in directory
scripts = os.listdir(DEFAULT_INDIR)
for file in scripts:
    tmp = TI(infile = DEFAULT_INDIR + '/' + file)
    tmp.tidy()
    tmp.write_output()

print('TIdying complete!')