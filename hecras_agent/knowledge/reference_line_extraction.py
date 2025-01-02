import h5py
import pandas as pd

def extract_reference_line_data(hdf_file_path):
    """
    Extract reference line time series data from HEC-RAS HDF file.
    
    Args:
        hdf_file_path (str): Path to the HEC-RAS HDF file
        
    Returns:
        pandas.DataFrame: DataFrame containing time series data for all reference lines,
                         including discharge and water surface elevation
    """
    # Extract data from HDF file
    with h5py.File(hdf_file_path, 'r') as hdf_file:
        # Extract discharge data
        discharge_data = hdf_file["/Results/Unsteady/Output/Output Blocks/DSS Hydrograph Output/Unsteady Time Series/Reference Lines/Flow"][:]
        
        # Extract water surface elevation data
        wse_data = hdf_file["/Results/Unsteady/Output/Output Blocks/DSS Hydrograph Output/Unsteady Time Series/Reference Lines/Water Surface"][:]
        
        # Extract reference line names
        reference_line_names = hdf_file["/Results/Unsteady/Output/Output Blocks/Base Output/Unsteady Time Series/Reference Lines/Name"][:]
        reference_line_names = [name.decode('utf-8') for name in reference_line_names]
        
        # Extract time data
        time_data = hdf_file["/Results/Unsteady/Output/Output Blocks/DSS Hydrograph Output/Unsteady Time Series/Time"][:]
        time_data_hours = time_data * 24  # Convert days to hours

    # Create DataFrames for discharge and water surface elevation
    df_discharge = pd.DataFrame(discharge_data, columns=reference_line_names)
    df_discharge.insert(0, 'Time (hours)', time_data_hours)
    
    df_wse = pd.DataFrame(wse_data, columns=reference_line_names)
    df_wse.insert(0, 'Time (hours)', time_data_hours)
    
    # Merge the DataFrames
    merged_df = pd.merge(df_discharge, df_wse, on="Time (hours)", suffixes=('_Discharge', '_WSE'))
    
    return merged_df
