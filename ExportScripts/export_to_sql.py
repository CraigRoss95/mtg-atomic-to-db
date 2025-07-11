import pandas as pd
import sqlite3
import os
from sqlalchemy import create_engine, BIGINT, text, FLOAT

from VerificationScripts import simple_verify

table_name = "mtgCardTable"
filename = "ExportedFiles/exportedMTGJSON.db"

db_string = f"sqlite+pysqlite:///{filename}"
engine = create_engine(db_string, future=True)

def export_to_sql(df):
    if os.path.exists(filename):
        print (f"deleting previous .db file at: \"{filename}\"")
        os.remove(filename)
    print ("Exporting to .db...")
    
    df.to_sql(table_name, engine)
    '''
    engine.connect() has auto ROLLBACK
    engine.begin() has auto COMMIT
    ''' 
    print(f"File saved as {filename}")
    
    print("Verifiying row count")
    
    
    simple_verify.verify_db(df=df,filename=filename,table_name=table_name)
    
        
        