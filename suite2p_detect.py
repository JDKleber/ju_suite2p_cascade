#Manual Mode
import os, warnings
import sys
import glob
import numpy as np
import scipy.io as sio
import ruamel.yaml as yaml
yaml = yaml.YAML(typ='rt')
#%matplotlib widget # can be commented back in to make plots interactive
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import pickle
## import functions ##
from functions_general import *
from CASCADE_functions import *
from functions_plots import *
from functions_data_transformation import *


## import gui_configurations ##
import gui_configurations
ops_path

## Activate suite2p
import run_suite2p 
from gui_configurations import main_folder
# gui_configurations.data_extension = 'nd2'
run_suite2p.get_all_image_folders_in_path(main_folder)
# gui_configurations.data_extension = 'tif'
run_suite2p.main()
# gui_configurations.data_extension = 'nd2'
# run_suite2p.main()

# run_suite2p.export_image_files_to_suite2p_format(r'D:\users\JC\pipeline\cysteine toxicity\001-DMEM replicates\DMEM replicates\240322 DMEM high pH acute toxicity')