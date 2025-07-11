import pandas as pd
from src.VerificationScripts import simple_verify
filename = "ExportedFiles/exportedMTGJSON.csv"

def export_to_csv(df,simple_verify_arg):
    print ("Exporting to .csv...")
    df.to_csv(filename)
    print(f"File saved as {filename}")
    
    if(simple_verify_arg):
        print("Verifiying row count")
        simple_verify.verify_csv(df,filename)
    