import pandas as pd
from src.VerificationScripts import simple_verify
filename = "ExportedFiles/exportedMTGJSON.pkl"

def export_to_pkl(df,simple_verify_arg):
    print ("Exporting to .pkl...")
    df.to_pickle(filename)
    print(f"File saved as {filename}")
    
    if (simple_verify_arg):
        print("Verifiying row count")
        simple_verify.verify_pkl(df,filename)
    