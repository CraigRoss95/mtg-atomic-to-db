import pandas as pd
import json

pd.set_option('display.max_columns', None)


# TODO this is currently unused, use it when setting up col data types
with open("var_types.json", "r") as file:
    var_types = json.load(file)

#Get Raw Data
df_raw = pd.read_json("AtomicCards.json")
df_raw.drop(["date","version"], inplace=True)

all_cards_list = []
for index in (range(len(df_raw))):
    for alternate in df_raw.iloc[index]["data"]:
        card = alternate
        new_card = {}
        for key, value in var_types.items():
            if key in card:
                new_card[key] = card[key]
            else:
                new_card[key] = None
        all_cards_list.append(new_card)
    
df = pd.DataFrame(all_cards_list)

# print(df.dtypes)