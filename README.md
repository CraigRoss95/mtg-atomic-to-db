## MTG Atomic JSON to DB

Please provide the latest atomic database file (AtomicCards.jsom) to the root directory of this repo

The file in question can be found here:
https://mtgjson.com/downloads/all-files/#atomiccards


- [X] Speed up loop by creating one list object (rather than make a series for every card and mash them together) 
- [X] Create "working" branch
- [X] Move var_types to JSON (and then get them from that file)
- [X] Use json library to read in AtomicCards.json
- [ ] Fixed DTypes (needed for SQL) 
- [ ] File not found error message
- [ ] Failed on CARDNAME error message
- [ ] CMD Options
- [ ] JSON export option
- [ ] SQL export option
- [ ] VENV?
- [ ] Documentation
- [ ] "Package" for consumption
