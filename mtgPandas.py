import pandas as pd

pd.set_option('display.max_columns', None)

#Verify this
#TODO use this when creating the database columns (softly implemented for createing the dataframe)
# Also TODO, Move this to a JSON file
#
var_types = {
    "asciiName" : "string",
    "attractionLights" : "int[]",
    "colorIdentity" : "string[]",
    "colors" : "string[]",
    "convertedManaCost": "int",
    "defense" : "string",
    "edhrecRank" : "int",
    "edhrecSaltiness": "int",
    "faceConvertedManaCost": "int",
    "faceManaValue": "int",
    "faceName": "string",
    "firstPrinting" : "string",
    "foreignData": "dict",
    "hand" : "string",
    "hasAlternativeDeckLimit" : "bool",
    "identifiers": "dict",
    "isFunny" : "bool",
    "isReserved" : "bool",
    "keywords": "string[]",
    "layout" : "string",
    "leadershipSkills": "dict",
    "legalities" : "dict",
    "life": "string",
    "loyalty": "string",
    "manaCost": "string",
    "manaValue" : "int",
    "name" : "string",
    "power": "string",
    "printings": "string[]",
    "purchaseUrls" : "dict",
    "relatedCards": "dict",
    "rulings": "dict",
    "side": "string",
    "subsets": "string[]",
    "subtypes": "string[]",
    "supertypes": "string[]",
    "text": "string",
    "toughness" : "string",
    "type": "string",
    "types": "string[]"}


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
print(df.dtypes)