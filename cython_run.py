import sys
from cython_leb_lash import initdat
from cython_leb_lash import plotdat
from cython_leb_lash import savedat
from cython_leb_lash import one_energy
from cython_leb_lash import all_energy
from cython_leb_lash import get_order
from cython_leb_lash import MC_step
from cython_leb_lash import main

if int(len(sys.argv)) == 5:
        PROGNAME = sys.argv[0]
        ITERATIONS = int(sys.argv[1])
        SIZE = int(sys.argv[2])
        TEMPERATURE = float(sys.argv[3])
        PLOTFLAG = int(sys.argv[4])
        main(PROGNAME, ITERATIONS, SIZE, TEMPERATURE, PLOTFLAG)
else:
    print("Usage: python {} <ITERATIONS> <SIZE> <TEMPERATURE> <PLOTFLAG>".format(sys.argv[0]))