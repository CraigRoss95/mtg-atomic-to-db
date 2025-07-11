import pandas as pd
from src.VerificationScripts import simple_verify
filename = "ExportedFiles/exportedMTGJSON.h5"

def export_to_hdf(df):
    print ("Exporting to .h5...")
    df.to_hdf(filename, key="df")
    print(f"File saved as {filename}")
    
    print("Verifiying row count")
    simple_verify.verify_h5(df,filename)


    