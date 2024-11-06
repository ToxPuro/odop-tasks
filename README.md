odop tasks to run:  

reduce.py  
to run reduce.py  
    module load cray-hdf5
    python(3) reduce.py
upload.py  
to run upload.py do the following:  
        module load python-data/(LUMI)cray-python  
        (LUMI) module use /appl/local/csc/modulefiles  
        module load allas    
        allas-conf and choose project_2000403  Magneto-helioseismology in conjunction with dynamo simulations (international use)   
        python(3) upload.py   

SKETCH FOR NEW ODOP TASKS:  
pip install f90nml  

import pencil as pc  

cd $WORKDIR  
mkdir task && cd task && download tarball from allas  
untar tarball && download slices from allas  
slices = pc.read.slices.py()  
pc.visu.rvid_box.plot_box(slices)  

