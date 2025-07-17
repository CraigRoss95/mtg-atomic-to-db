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
                        help= "Verifies the exported file with a line count check", 
                        type=bool,
                        default= True,
                        metavar="count_verify", 
                        choices={True,False})
    parser.add_argument("-o", "--output", "--out",
                        help= "Sets the output file type",
                        metavar="output",
                        choices=list(itertools.chain.from_iterable(mode_map.values())))
    parser.add_argument("-s","--obj2str", "--o2s", "--object_to_string",
                        help= "wraps objects into strings with \"\"\"tripple quotes\"\"\" (MySQL does not support objects)",
                        type=bool,
                        default=False,
                        metavar="obj2str",
                        choices={True,False})
    args = parser.parse_args()
    
    if not args.output == None:
        for key, values in mode_map.items():
            if args.output in values:
                args.output = key
                break
    print(args)
    
    #TODO Have this use args or kwargs
    app.run_app(mode=args.output, simple_verify_arg=args.count_verify, obj2str=args.obj2str)
    

