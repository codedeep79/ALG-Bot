import json
import glob

# [{"key1": "value1"}] - (in file1)
# [{"key2": "value2"}] - (in file2)
#       [{"key1": "value1"},
#        {"key2": "value2"}]

readFiles = glob.glob("Curated list/*.json")
outputList = []

for f in readFiles:
    with open(f, "r") as file:
        data = json.load(file)
        i = 0
        # Prevent duplicate the JSON Object
        while i < len(data) and data[i] not in outputList:
                outputList.append(data[i])
                i = i + 1

with open("awesome-list.json", "w") as outFile:
    json.dump(outputList, outFile, indent = 4)

