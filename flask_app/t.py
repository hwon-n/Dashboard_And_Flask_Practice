import os
import csv


CSV_FILENAME = 'titanic.csv'


all_list = []
with open(os.path.abspath(os.path.join('../', CSV_FILENAME)), 'r') as csv_file:
    reader = csv.reader(csv_file)
    for data in reader:
        if 'Pclass' in data:
            pass
        else:
            all_list.append(data)
                
dict = {'passenger': all_list}

print(dict['passenger'][1][1])