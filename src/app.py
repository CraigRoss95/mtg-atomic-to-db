import src.import_json as import_json
from src import export_json

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

# TODO use kwargs/ args***
def run_app(mode = None, simple_verify_arg=True, obj2str=False ):
    
    #for debugging
    option = ""
    if not mode == None:
        option = str(mode)
        
    if not option:
        print (welcome_message)
        possible_options = ["1", "2", "3", "4", "5"]
        option = input()
        while option not in possible_options:
            print (f"please select valid input, please pick one of the following: \n{possible_options}")
            option = input()
        
    match option:
        case "1":
            df = import_json.import_json(obj2str=obj2str)
            export_json.export_to_csv(df,simple_verify_arg)
        case "2":
            df = import_json.import_json(obj2str=obj2str)
            export_json.export_to_pkl(df,simple_verify_arg)
        case "3":
            df = import_json.import_json(obj2str=obj2str)
            export_json.export_to_hdf(df,simple_verify_arg)
        case "4":
            if(obj2str == False):
                print("Setting arg 'obj2str' to True (needed for MySQL conversion)")
                obj2str = True
            df = import_json.import_json(obj2str=obj2str)
            export_json.export_to_db(df,simple_verify_arg)
        case "5":
            df = import_json.import_json(obj2str=obj2str)
            export_json.export_to_sql(df,simple_verify_arg)
    print ("Done!")  