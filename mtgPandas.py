import pandas as pd
import json

pd.set_option('display.max_columns', None)

print ("Loading var_types.json to object...")
# TODO this is currently unused, use it when setting up col data types
with open("var_types.json", "r") as file:
    var_types = json.load(file)

print ("Loading AtomicCards.json to object (this might take a while)...")
with open("AtomicCards.json", "r", encoding="utf8") as file:
    raw_json = json.load(file)
    
print ("converting JSON object to Data Frame readable content...")
all_cards_list = []
card_count = 0
for json_key, json_value in raw_json["data"].items():
    for alternate in json_value:
        card = alternate
        new_card = {}
        for key, value in var_types.items():
            if key in card:
                new_card[key] = card[key]
            else:
                new_card[key] = None
        
        all_cards_list.append(new_card)
        card_count = card_count + 1
    # if card_count % 1000 == 0:
    #     print(card_count)
print ("Converting to Pandas Data Frame")
df = pd.DataFrame(all_cards_list)

# print(df.dtypes)

# this should be 32810
print (f"{len(all_cards_list)} Cards loaded")