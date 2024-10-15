#!/usr/bin/env python
# coding: utf-8
import pencil as pc
from pencil.math import natural_sort
from pencil.io import mkdir
import os
from os.path import join
import glob
import numpy as np
import time
import inspect

def main():
    f = pc.read.var()
    file_heavy = False
    for i in range(100):
        if file_heavy and i%10 == 0:
            f = pc.read.var()
        eta = np.random.uniform()
        rho = np.random.uniform()
        uu = f.uu
        aa = f.uu
        uu_xyaver = np.sum(uu,3)
        aa_xyaver = np.sum(aa,3)
        g = eta*uu_xyaver - rho*aa_xyaver
    print("DONE\n");

if __name__ == "__main__":
    main()

