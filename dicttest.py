import json

data = {
    "TAR123": {
        "parkeringar": [["11:30", "15:30"]],
        "typ" : "stor"
        }
}

with open('data.txt', 'r') as outfile:  
    d = json.load(outfile)
    for key, value in d.items():
        print(key)
        print(value)
