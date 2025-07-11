import import_json
from ExportScripts import export_to_csv, export_to_h5, export_to_pkl, export_to_sql

welcome_message = """
This is a tool for importing the MTGJSON AtomicCards.json database as a usable file
Please make sure you have the database stored localy on your device in the repository this project is sitting in

Please select from the following options to choose an export method:

1 - Comma Seperated Value(.csv)
2 - Pandas Pickle Export (.pkl)
3 - Pandas DataFrame Export (.hdf5)
4 - SQLite (.db file)
5 - PostgreSQL (.sql file(??? Coming soon?))
"""

#for debugging
option = "" #"5"

if not option:
    print (welcome_message)
    possible_options = ["1", "2", "3", "4"]
    option = input()
    while option not in possible_options:
        print (f"please select valid input, please pick one of the following: \n{possible_options}")
        option = input()
    
match option:
    case "1":
        df = import_json.import_json()
        export_to_csv.export_to_csv(df)
    case "2":
        df = import_json.import_json()
        export_to_pkl.export_to_pkl(df)
    case "3":
        df = import_json.import_json()
        export_to_h5.export_to_hdf(df)
    case "4":
        df = import_json.import_json(obj2str=True)
        export_to_sql.export_to_sql(df)
print ("Done!")  