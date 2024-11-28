import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f'Ошибка: {response.status_code}')


url = 'https://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}

response = requests.post(url, data=payload)

print(response.text)

url = 'https://httpbin.org/get'
headers = {'User-Agent': 'MyApp/1.0'}

response = requests.get(url, headers=headers)

print(response.headers)

import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b

print(c)

array = np.array([1, 2, 3, 4, 5])
mean = np.mean(array)
std_dev = np.std(array)

print(f'Среднее значение: {mean:.2f}')
print(f'Стандартное отклонение: {std_dev:.2f}')

import pandas as pd

data = pd.read_csv('example.csv')

data['age'] = data['age'].astype(int)

filtered_data = data.query("age > 30")

grouped_data = filtered_data.groupby('city')['salary'].mean()

merged_data = pd.merge(data, grouped_data, on='city', how='left')

print(merged_data.head())








