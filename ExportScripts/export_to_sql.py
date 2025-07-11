import pandas as pd
import sqlite3
import os
from sqlalchemy import create_engine, BIGINT, text, FLOAT

from VerificationScripts import simple_verify


table_name = "mtgCardTable"
filename = "ExportedFiles/exportedMTGJSON.db"
if os.path.exists(filename):
    print (f"deleting previous .db file at: \"{filename}\"")
    os.remove(filename)


db_string = f"sqlite+pysqlite:///{filename}"
engine = create_engine(db_string, echo=True, future=True)

def export_to_sql(df):
    print ("Exporting to .db...")
    
    df.to_sql(table_name, engine)
    '''
    engine.connect() has auto ROLLBACK
    engine.begin() has auto COMMIT
    ''' 
    df.to_csv(db_string)
    print(f"File saved as {db_string}")
    
    print("Verifiying row count")
    simple_verify.verify_sql(df,db_string)
    
    
    with engine.connect() as conn:
        result = conn.execute(text(f"PRAGMA table_info({table_name})"))
    for row in result:
        print(row)
        
    # get a connection / fetch rows // auto ROLLBACK
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM table_name"))
                
    # # get a connection / drop a table // autocommit
    with engine.begin() as conn:
        conn.execute(
            text("DROP TABLE table_name"))
        