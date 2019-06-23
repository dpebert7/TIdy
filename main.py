#!/usr/bin/python

import os
from TI import TI
from defaults import DEFAULT_INDIR

scripts = os.listdir(DEFAULT_INDIR)
for file in scripts:
    with open(DEFAULT_INDIR + '/' + file, 'r') as f:
        text_list = f.read().splitlines()

    tmp = TI(text_list)
    tmp.set_outfile(file)
    tmp.tidy()
    tmp.generate_output()

print('TIdying complete!')