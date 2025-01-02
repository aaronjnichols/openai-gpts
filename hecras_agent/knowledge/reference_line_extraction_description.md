# Using the reference_line_extract Function

To call the reference_line_extract function, follow these steps:

1. Import the necessary modules: Ensure you have imported the pandas library and any other required modules.

2. Prepare the file path: Define the path to the HEC-RAS plan HDF5 file you want to process.

3. Call the function: Use the reference_line_extract function, passing the file path as an argument.

4. Handle the returned data: The function returns a dataframe containing:

- A pandas.DataFrame with time series water surface elevations and discharge results for each reference line.

## Example Usage

'''
import sys
import os
import h5py
import pandas as pd

sys.path.append(r'mnt/data')
from reference_line_extraction import reference_line_extract

file  = os.path.join(r'mnt/data', 'HECRAS_Model.p01.hdf')

df = reference_line_extract(file)

print(df.head())
'''
