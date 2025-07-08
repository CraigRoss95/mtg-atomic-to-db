import pandas as pd
from VerificationScripts import simple_verify
filename = "ExportedFiles/exportedMTGJSON.csv"

def export_to_csv(df):
    print ("Exporting to .csv...")
    df.to_csv(filename)
    print(f"File saved as {filename}")
    
    print("Verifiying row count")
    simple_verify.verify_csv(df,filename)
    