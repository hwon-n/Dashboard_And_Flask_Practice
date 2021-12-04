import pandas as pd
import os

CSV_FILENAME = 'titanic.csv'
CSV_FILEPATH = os.path.join(os.getcwd(), CSV_FILENAME)

# csv 파일 읽어오기
df = pd.read_csv(CSV_FILEPATH)

# 불필요한 컬럼 삭제 후 결측치 처리
del_list = ['PassengerId', 'Survived', 'Ticket', 'Cabin']
df.drop(del_list, axis = 1, inplace = True)
df.dropna(inplace = True)


# 데이터 전처리 위한 함수
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


def firstName(first):
    if 'Mr.' in first:
        first = first.replace('Mr.', '')
    elif 'Mrs.' in first:
        first =  first.replace('Mrs.', '')
    elif 'Miss.' in first:
        first =  first.replace('Miss.', '')
    elif 'Master.' in first:
        first =  first.replace('Master.', '')
    
    if '"' in first:
        first = first.replace('"', '').strip()
    return first


# 데이터 전처리
df.Age = df.Age.apply(age)
df.Fare = df.Fare.apply(fare)


# Name 컬럼을 Last Name과 First Name으로 나누기
df[['Last_Name', 'First_Name']] = df.Name.str.split(',').tolist()
df.First_Name = df.First_Name.apply(firstName)

# Name 컬럼 삭제
df.drop('Name', axis = 1, inplace=True)


# 다시 csv 파일로 만들기 
df.to_csv(CSV_FILEPATH, index = False)
print('finish data processing')