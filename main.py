import import_json
welcome_message = """
This is a tool for importing the MTGJSON AtomicCards.json database as a usable file
Please make sure you have the database stored localy on your device in the repository this project is sitting in

Please select from the following options to choose an export method:

1 - Pandas DataFrame Export (pickle/pkl)
2 - SQL server (comming soon)
"""

print (welcome_message)
possible_options = ["1"]
option = input()
while option not in possible_options:
    print (f"please select valid input, please pick one of the following: \n{possible_options}")
    option = input()
    
import_json.import_json()

match option:
    case "1":
        print ("***This is where the picke export process starts***")