## MTG Atomic JSON to DB

Please provide the latest atomic database file (AtomicCards.jsom) to the root directory of this repo

The file in question can be found here:
https://mtgjson.com/downloads/all-files/#atomiccards


- [X] Speed up loop by creating one list object (rather than make a series for every card and mash them together) 
- [X] Create "working" branch
- [X] Move var_types to JSON (and then get them from that file)
- [X] Use json library to read in AtomicCards.json
- [X] <del>Fixed DTypes (needed for SQL)</del> Do this when adding to the Database (JSON or DataFrame)
- [X] File not found error message
- [X] Failed on CARDNAME error message
- [X] CMD Options
- [X] .csv export option
    - [X] Fix header thing (is that a problem?)
- [X] Pickel export option
- [X] .h5 export option
- [X] Simple counting verification
- [X] Move .py files to src directory
    - [X] Create shortcut program in root directory (name it attomic-to-db.py or something)
    - [X] rename main.py to app.py
    - [X] create Schema directory
- [ ] find way to pass params into this shortcut script from terminal (start with simple varify toggle)
    - [ ] Make verification optional
- [X] Static datatypes for DataFrame in import_json.py (verify with .h5 file, it is throwing errors now )
- [ ] Comparison verification
- [X] SQL export option (sqlite)
- [ ] PostgreSQL export option
- [X] requirements.txt
- [ ] Documentation
- [ ] "Package" for consumption


## Bugs
- [ ] Fix performace issue with .h5 file export (see console warning on mode 3, happens on export (important))
- [ ] CSV error (see console warning on mode 1, happens on import (for verification))
## Instalation guide
Comming soon...

## Modes
Comming soon...
