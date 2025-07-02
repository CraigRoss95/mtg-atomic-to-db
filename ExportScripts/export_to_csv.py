import pandas as pd
filename = "ExportedFiles/exportedMTGJSON.csv"

def export_to_csv(df):
    print ("Exporting to CSV...")
    df.to_csv (filename)
    
    print(f"File saved as {filename}")