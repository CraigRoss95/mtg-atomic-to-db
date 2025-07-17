import src.import_json as import_json
from src import export_json
from argparse import Namespace
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

def run_app(**kwargs):
    kwargs = Namespace(**kwargs)

    #for debugging
    output_type = ""
    if not kwargs.output == None:
        output_type = str(kwargs.output)
        
    if not output_type:
        print (welcome_message)
        possible_options = ["1", "2", "3", "4", "5"]
        output_type = input()
        while output_type not in possible_options:
            print (f"please select valid input, please pick one of the following: \n{possible_options}")
            output_type = input()
        
    match output_type:
        case "1":
            df = import_json.import_json(obj2str= kwargs.obj2str)
            export_json.export_to_csv(df,kwargs.count_verify)
        case "2":
            df = import_json.import_json(obj2str=kwargs.obj2str)
            export_json.export_to_pkl(df,kwargs.count_verify)
        case "3":
            df = import_json.import_json(obj2str=kwargs.obj2str)
            export_json.export_to_hdf(df,kwargs.count_verify)
        case "4":
            if(kwargs.obj2str == False):
                print("Setting arg 'obj2str' to True (needed for MySQL conversion)")
                kwargs.obj2str = True
            df = import_json.import_json(obj2str=kwargs.obj2str)
            export_json.export_to_db(df,kwargs.count_verify)
        case "5":
            df = import_json.import_json(obj2str=kwargs.obj2str)
            export_json.export_to_sql(df,kwargs.count_verify)
    print ("Done!")  