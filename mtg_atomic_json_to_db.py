from src import app
import itertools

# app.run_app()
mode_map = {
    1 : ["csv",".csv","1"],
    2 : ["pkl",".pkl","2"],
    3 : ["h5",".h5","3"],
    4 : ["db",".db","4"]
}
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description="A scraping tool for MTGJSON.com"
    )
    
    parser.add_argument("-sv", "--simple_verify", 
                        metavar="simple_verify", 
                        choices={"True","False"})
    parser.add_argument("-m", "--mode",
                        metavar="mode",
                        choices=list(itertools.chain.from_iterable(mode_map.values())))
    args = parser.parse_args()
    
    #Args to non string format
    if args.simple_verify in {"True", None}:
        args.simple_verify = True
    else:
        args.simple_verify = False
        
    if not args.mode == None:
        for key, values in mode_map.items():
            if args.mode in values:
                args.mode = key
                break
    
    app.run_app(args.mode, args.simple_verify)
    

