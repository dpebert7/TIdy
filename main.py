#!/usr/bin/python
import os
from TI import TI
from defaults import DEFAULT_INDIR

### Use the following for testing
# Note that string must be raw.
string = r"""
### Spacing & Capitalization
cCube='GL';
cubesetlogchanges(cCube, 1) ;
path = '\\main-directory\test.txt';
nResult = 10\nDenominator-
CellGetN('CubeName', 'V1', 'V2', 'V3');

### Indentation
nIdx=10;
While(nIdx>0);
If (cubeExists(cCube)=1);
cubedestroy(cCube);
else;
 CellPutN(10\nNoOfYears, 'Fishpaste', 'Actual', '2019.01')
endif;
nIdx=nIdx-1;
end;
"""

tmp1 = TI(text=string)
tmp1.tidy()
tmp1.print_output()


### Tidy all files in in directory
scripts = os.listdir(DEFAULT_INDIR)
for file in scripts:
    tmp = TI(infile = DEFAULT_INDIR + '/' + file)
    tmp.tidy()
    tmp.write_output()

print('TIdying complete!')