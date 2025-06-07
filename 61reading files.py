# (08:41:33)

# reading files

# Text file reading
file_path = "test.txt"
with open(file_path , "r") as file:
    data = file.read()
    print(data)

# json file reading
import json
file_path="test.json"
with open(file_path , "r") as file:
    data = json.load(file)
    print(data)

# CSV file reading
import csv
with open(file_path , "r") as file:
    data = csv.reader(file)
    for line in data:
        print(line)