from flask import Flask, render_template
import os
import csv
import json

CSV_FILENAME = 'titanic.csv'
CSV_FILEPATH = os.path.abspath(os.path.join('../', CSV_FILENAME))

app = Flask(__name__)

app.config['USER_CSV_FILE'] = CSV_FILEPATH

all_list = []
with open(app.config['USER_CSV_FILE'], 'r') as csv_file:
    reader = csv.reader(csv_file)
    for data in reader:
        if 'Pclass' in data:
            pass
        else:
            all_list.append(data)

@app.route('/')
def index():
    return render_template('index.html', list_name='all', passenger_dict = all_list), 200


@app.route('/')
@app.route('/<sex>')
def get_sex(sex):
    
    filter_sex = []
    
    for data in all_list:
        if sex == data[1]:
            filter_sex.append(data)
    
    return render_template('index.html', list_name=sex, passenger_dict = filter_sex), 200

@app.route('/')
@app.route('/<sex>&<embarked>')
def get_sex_embarked(sex, embarked):
    
    filter_sex_embarked = []
    
    for data in all_list:
        if sex == data[1]:
            if embarked == data[6]:
                filter_sex_embarked.append(data)
    
    return render_template('index.html', list_name=(sex, embarked), passenger_dict=filter_sex_embarked), 200