import json

newname = input("Name: ")
newlevel = input("Position: ")
newrecord = {"name":newname, "level":newlevel}

with open("C:/Users/shane/Documents/code/schol/nfcpy shi/records/records.json", "r+") as records:
    data = json.load(records)
    data["records"].append(newrecord)
    records.seek(0)
    json.dump(data, records, indent=4)
    
