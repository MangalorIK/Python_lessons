import requests
from ehp import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


##################### requests ########################
# открыли страницу кланов игры
doc = requests.get("https://vsmuta.com/info/clans").text

# достали названия кланов
html = Html()
for name in html.feed(doc).find('tr', ('class', 'tr-clan')):
    arr = [a.strip() for a in name.text().split('\n')]
    print(f"{arr[1]}) клана: {arr[2]}, количество бойцов: {arr[3]}")

##################### pandas #########################
df = pd.read_excel("File.xlsx")

fig, ax1 = plt.subplots(figsize=(15, 8), layout='constrained')
test_names = df['Персонаж']
exp = df['Опыт']

rects = ax1.barh(test_names, exp, align='center', height=0.5)
plt.show()