# (08:27:47)

# writing files

txt = "I lov Biriyani and chilli chicken"
file_path = "test.txt"

# w for writing 
# x for writing if file doesn't exist
# a for appending
# r for reading

with open(file = file_path , mode =  "w") as file:
    file.write(txt)
    print(f"Done")




import json
employee = {"Name": "vishwas", "age" : 21 , "Job" : "Slave"}
file_path1 = "test.json"

with open(file_path1 , "w")as file:
    json.dump(employee , file , indent=4)
    print("JSON done")


import csv
employees = [
             ["name" , "age" , "job"],
             ["vishwas1" , 21 , "Slave"],
             ["Vishu" , 21 , "Karmika"],
             ["blackey", 21 , "driver"]
             ]
file_path1 = "test.csv"

with open(file_path1 , "w", newline="")as file:
    writer=csv.writer( file )
    for row in employees:
        writer.writerow(row)
    print("CSV done")