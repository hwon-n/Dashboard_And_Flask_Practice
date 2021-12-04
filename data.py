import pandas as pd
import os

CSV_FILENAME = 'titanic.csv'
CSV_FILEPATH = os.path.join(os.getcwd(), CSV_FILENAME)

df = pd.read_csv(CSV_FILEPATH)

del_list = ['PassengerId', 'Survived', 'Ticket', 'Cabin']
df = df.drop(del_list, axis = 1)
df = df.dropna()

def age(age):
    if age >= 60:
        return 'over 50s'
    elif age >= 50:
        return '50s'
    elif age >= 40:
        return '40s'
    elif age >= 30:
        return '30s'
    elif age >= 20:
        return '20s'
    elif age >= 10:
        return '10s'
    else:
        return 'under 10s'

def fare(fare):
    if fare >= 80:
        return 'more 80'
    elif fare >=60 :
        return 'more 60 and less 80'
    elif fare >= 40:
        return 'more 40 and less 60'
    elif fare >= 20:
        return 'more 20 and less 40'
    elif fare >= 10:
        return 'more 10 and less 20'
    else:
        return 'less 10'

df.Age = df.Age.apply(age)
df.Fare = df.Fare.apply(fare)

df.to_csv(CSV_FILEPATH, index = False)