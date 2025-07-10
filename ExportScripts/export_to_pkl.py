import pandas as pd
from VerificationScripts import simple_verify
filename = "ExportedFiles/exportedMTGJSON.pkl"

def export_to_pkl(df):
    print ("Exporting to .pkl...")
    df.to_pickle(filename)
    print(f"File saved as {filename}")
    
    print("Verifiying row count")
    simple_verify.verify_pkl(df,filename)
    
        
