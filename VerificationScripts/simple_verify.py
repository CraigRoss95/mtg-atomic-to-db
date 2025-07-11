import pandas as pd

def verify_csv(df, filename):
    imported_df = import_csv(filename)
    count_verification(df,imported_df)
    
def import_csv(filename = "ExportedFiles/exportedMTGJSON.csv"):
    imported_df = pd.read_csv(filename)
    imported_df = imported_df[1:]
    return imported_df



def verify_pkl(df, filename):
    imported_df = import_pkl(filename)
    count_verification(df,imported_df)
    
def import_pkl(filename = "ExportedFiles/exportedMTGJSON.pkl"):
    imported_df = pd.read_pickle(filename)
    imported_df = imported_df[1:]
    return imported_df



def verify_h5(df, filename):
    imported_df = import_h5(filename)
    count_verification(df,imported_df)
    
def import_h5(filename = "ExportedFiles/exportedMTGJSON.h5"):
    imported_df = pd.read_hdf(filename)
    imported_df = imported_df[1:]
    return imported_df

def verify_sql (df, filename):
    print("TODO implement simpile verifiy script")

def count_verification(df, imported_df):
    lines_off = abs(len(imported_df) == len(df))
    if(lines_off == 0):
        print("Same number of rows, data verified")
    else:
        print (f"Data verification failed, off by {lines_off} lines")
    