import csv
import random
import time

file_dir = '/Users/emiliano/codebase/python/gui_apps/files/'
file_nm = file_dir+'data.csv'
x_val   = 0
total_1 = 1000
total_2 = 1000

field_names = ["x_val","total_1","total_2"]

with open(file_nm,'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file,fieldnames=field_names)
    csv_writer.writeheader()

while True:
    
    with open(file_nm,'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=field_names)

        info = {
            "x_val"   : x_val,
            "total_1" : total_1,
            "total_2" : total_2
        }

        csv_writer.writerow(info)
        print(x_val,total_1,total_2)

        x_val  += 1
        total_1 = total_1 + random.randint(-6,8)
        total_2 = total_2 + random.randint(-6,8)

        time.sleep(2)
