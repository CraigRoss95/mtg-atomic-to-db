import pandas as pd
import json
import sys

pd.set_option('display.max_columns', None)

var_types = ""
def import_json(obj2str = False):
    print ("Loading var_types.json to object...")
    # TODO this is currently unused, use it when setting up col data types
    with open("var_types.json", "r") as file:
        global var_types 
        var_types = json.load(file)

    try:
        with open("AtomicCards.json", "r", encoding="utf8") as file:
            print ("Loading AtomicCards.json to object (this might take a while)...")
            raw_json = json.load(file)
    except:
        print ("ERROR: Could not find file 'AtomicCards.json' make sure it is in the root directory of this repository")
        sys.exit()   
    print ("Converting JSON object to Data Frame readable content...")
    all_cards_list = []
    card_count = 0
    for json_key, json_value in raw_json["data"].items():
        for card in json_value:
            new_card = {}
            try:
                for key, value in var_types.items():
                    if key in card:
                        if (obj2str):
                            new_card[key] = objects_to_strings(card[key], key,value)
                        else:
                            new_card[key] = card[key]
                    else:
                        new_card[key] = None
            except:
                print(f"ERROR: on card '{card["name"]}' continuing with other cards...")
            
            all_cards_list.append(new_card)
            card_count = card_count + 1
        # if card_count % 1000 == 0:
        #     print(card_count)
    print ("Converting to Pandas Data Frame")
    df = pd.DataFrame(all_cards_list)
    
    
    # print(df.head())

    # print(df.dtypes)

    # this should be 32810
    print (f"{len(all_cards_list)} Cards loaded")
    return df

def objects_to_strings(data ,key, value):
    global var_types
    
    if value in {"string[]", "dict"}:
        data = f"\"{data}\""
        
    return data
    #TODO: Put automate this using var_types.json and put it in a function (make that function only happen if quote wrapping is needed (to_sql <---))
    dtype["colorIdentity"] = f"\"{card["colorIdentity"]}\"" #param 4
    
    
