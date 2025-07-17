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
    
    # TODO use type to specify data type
    parser.add_argument("-sv", "--simple_verify",
                        help= "Verifies the exported file with a line count check", 
                        metavar="simple_verify", 
                        choices={"True","False"})
    parser.add_argument("-o", "--output",
                        help= "Sets the output file type",
                        metavar="output",
                        choices=list(itertools.chain.from_iterable(mode_map.values())))
    parser.add_argument("-ots", "-o2s",  "--obj2str", "--object_to_string",
                        help= "wraps objects into strings with \"\"\"tripple quotes\"\"\" (MySQL does not support objects)",
                        metavar="obj2str",
                        choices={"True","False"})
    args = parser.parse_args()
    
    if not args.output == None:
        for key, values in mode_map.items():
            if args.output in values:
                args.output = key
                break
    #Args to non string format
    args.simple_verify = bool_to_str(str=args.simple_verify, default = True)
    args.obj2str = bool_to_str(str=args.obj2str, default = False)

      

    
    app.run_app(args.output, args.simple_verify, args.obj2str)
    

