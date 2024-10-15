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
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import cm
from matplotlib import markers
from scipy.ndimage import gaussian_filter as gf
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
from pencil.math.stats import fit_exp, fit_power
import subprocess as sb


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

if __name__ == "__main__":
    main()

