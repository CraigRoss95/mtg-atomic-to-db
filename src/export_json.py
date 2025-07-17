import pandas as pd
from src.VerificationScripts import simple_verify
import sqlite3
import os
from sqlalchemy import create_engine, BIGINT, text, FLOAT

file_path = "ExportedFiles"
file_name = "exportedMTGJSON"
file_extension = ""

def export_to_csv(df,simple_verify_arg):
    file_extension = "csv"
    full_file_dir = f"{file_path}/{file_name}.{file_extension}"
    print ("Exporting to .csv...")
    df.to_csv(full_file_dir)
    print(f"File saved as {full_file_dir}")
    
    if(simple_verify_arg):
        print("Verifiying row count")
        simple_verify.verify_csv(df,full_file_dir)

def export_to_hdf(df,simple_verify_arg):
    file_extension = "h5"
    full_file_dir = f"{file_path}/{file_name}.{file_extension}"
    print ("Exporting to .h5...")
    df.to_hdf(full_file_dir, key="df")
    print(f"File saved as {full_file_dir}")
    if (simple_verify_arg):
        print("Verifiying row count")
        simple_verify.verify_h5(df,full_file_dir)
        
def export_to_pkl(df,simple_verify_arg):
    file_extension = "pkl"
    full_file_dir = f"{file_path}/{file_name}.{file_extension}"
    print ("Exporting to .pkl...")
    df.to_pickle(full_file_dir)
    print(f"File saved as {full_file_dir}")
    
    if (simple_verify_arg):
        print("Verifiying row count")
        simple_verify.verify_pkl(df,full_file_dir)
        




def export_to_sql(df,simple_verify_arg):
    
    file_extension = "db"
    full_file_dir = f"{file_path}/{file_name}.{file_extension}"
    
    table_name = "mtgCardTable"

    db_string = f"sqlite+pysqlite:///{full_file_dir}"
    engine = create_engine(db_string, future=True)
    
    if os.path.exists(full_file_dir):
        print (f"deleting previous .db file at: \"{full_file_dir}\"")
        os.remove(full_file_dir)
    print ("Exporting to .db...")
    
    df.to_sql(table_name, engine)
    '''
    engine.connect() has auto ROLLBACK
    engine.begin() has auto COMMIT
    ''' 
    print(f"File saved as {full_file_dir}")
    
    if (simple_verify_arg):
        print("Verifiying row count")
        simple_verify.verify_db(df=df,filename=full_file_dir,table_name=table_name)
    