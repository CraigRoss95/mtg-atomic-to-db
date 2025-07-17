from src import app
import itertools
import argparse

def bool_to_str(str, default = True):
    
    if str == "True":
        return True
    elif str == "False":
        return False
    else:
        return default

mode_map = {
    1 : ["csv",".csv","1"],
    2 : ["pkl",".pkl","2"],
    3 : ["h5",".h5","3"],
    4 : ["db",".db","4"],
    5 : ["sql",".sql","5"]
}
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A scraping tool for MTGJSON.com"
    )
    parser.add_argument("-c", "--count_verify", "--cv",
                        help= "Verifies line count by importing exported file and comparing it to the original Frame", 
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-o", "--output", "--out",
                        help= "Sets the output file type",
                        metavar="output",
                        choices=list(itertools.chain.from_iterable(mode_map.values())))
    parser.add_argument("-s","--obj2str", "--o2s", "--object_to_string",
                        help= "wraps objects into strings with \"\"\"tripple quotes\"\"\" (MySQL does not support objects)",
                        action="store_true",
                        default=False
                        )
    args = parser.parse_args()
    
    if not args.output == None:
        for key, values in mode_map.items():
            if args.output in values:
                args.output = key
                break
    print(args)
    #TODO run command if present (Ex: only run object2str if the command is present in the kwargs)
    app.run_app(**vars(args))
    

