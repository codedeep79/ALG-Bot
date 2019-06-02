
import json
import glob

# [{"key1": "value1"}] - (in file1)
# [{"k[{"key1": "value1"},
#[{"key1": "value1"},
# {"key2": "value2"}]

readFiles = glob.glob("*.json")
outputList = []

for f in readFiles:
    with open(f, "r") as file:
        data = json.load(file)
        i = 0
        while i < len(data):
                outputList.append(data[i])
                i = i + 1

with open("awesome-list.json", "w") as outFile:
    json.dump(outputList, outFile, indent=4)
