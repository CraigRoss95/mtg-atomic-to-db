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

# print(df_raw.iloc[30089]["data"])

df = pd.DataFrame()
for key, value in var_types.items():
    if value in ["bool", "string", "int"]:
        df[key] = pd.Series(dtype=value)
    else:
        df[key] = pd.Series(dtype="object")

#set to 100 or 1000 for testing, this takes a long time to run
for index in range(len(df_raw)):
    for alternate in df_raw.iloc[index]["data"]:
        df.loc[len(df)] = alternate
# df.loc[len(df)] = {"asciiName":"test"}
    if (index + 1) % 1000 == 0:
        print (f"{index + 1} cards processed")
print (df.head()) 


#TODO Verify each of these steps:
#create blank dataframe with row names (using types dict)
#loop through using "index" in json
    # get set data using df.loc[index] see above
    
#export