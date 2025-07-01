import pandas as pd

#Verify this
# TODO see if these values need to be in quotes bool works instead of "bool"
# Also TODO, Move this to a JSON file
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


pd.set_option('display.max_columns', None)
df_raw = pd.read_json("AtomicCards.json")

df_raw.drop(["date","version"], inplace=True)

print(df_raw.iloc[30089]["data"])

df_test = pd.DataFrame()

df_test["asciiName"] = pd.Series(dtype="string")
df_test.loc[len(df_test)] = {"asciiName":"test"}
print (df_test.head()) 

#TODO Verify each of these steps:
#create blank dataframe with row names (using types dict)
#loop through using "index" in json
    # get set data using df.loc[index] see above
    
#export
