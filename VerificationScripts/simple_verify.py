import pandas as pd
import sqlite3

def verify_csv(df, filename):
    imported_df = import_csv(filename)
    count_verification(df,imported_df)
    
def import_csv(filename = "ExportedFiles/exportedMTGJSON.csv"):
    imported_df = pd.read_csv(filename)
    return imported_df



def verify_pkl(df, filename):
    imported_df = import_pkl(filename)
    count_verification(df,imported_df)
    
def import_pkl(filename = "ExportedFiles/exportedMTGJSON.pkl"):
    imported_df = pd.read_pickle(filename)
    return imported_df



def verify_h5(df, filename):
    imported_df = import_h5(filename)
    count_verification(df,imported_df)
    
def import_h5(filename = "ExportedFiles/exportedMTGJSON.h5"):
    imported_df = pd.read_hdf(filename)
    return imported_df



def verify_db (df, filename, table_name = "mtgCardTable"):
    imported_df = import_db(filename, table_name)
    count_verification(df,imported_df)

def import_db(filename, table_name):
    conn = sqlite3.connect(filename)
    imported_df =pd.read_sql_query(f"SELECT * FROM {table_name}",conn)
    return imported_df


def count_verification(df, imported_df):
    lines_off = abs(len(imported_df) - len(df))
    if(lines_off == 0):
        print("Same number of rows, data verified")
    else:
        print (f"Data verification failed, off by {lines_off} lines")
    