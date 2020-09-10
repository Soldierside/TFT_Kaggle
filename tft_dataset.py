#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:13:23 2020

@author: soldierside
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pickle
import json
import re
from collections import Counter

url='/Users/soldierside/Documents/Projectes de Kaggle/tft-match-data'


os.chdir(url)
os.listdir(url)

############

data_challenger=pd.read_csv('TFT_Master_MatchData.csv')
pd.set_option('display.max_columns', 10)



data_challenger.head(2)

data_challenger.dtypes

data_challenger['combination']


data_challenger.groupby('combination')['gameId'].count()
data_challenger.groupby('Ranked')['gameId'].count().tolist()

#data_challenger.groupby('champion')['gameId'].count() #massa merda per contar

help(Counter)
help(pickle)
help(re)

# =============================================================================
# Exemple Counter, fer-lo servir per conta les classes dins de combination.
#re.findall i la funció que he copiat
# =============================================================================

# Tally occurrences of words in a list
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1


#exemple de la funció findall
xx = "guru99,education is fun"
r1 = re.findall(r"^\w+",xx)
print(r1)


# =============================================================================
# Combinatons
# =============================================================================

composiciones=data_challenger.combination.apply(lambda x:re.findall(r"[a-zA-Z]+[0-9]?_?[a-zA-Z]+",x)).to_frame()#

#re.findall(r"[a-zA-Z]+[0-9]?_?[a-zA-Z]+",x) aquesta formula le trobat per internet, la x es del lambda

resultado=Counter()
for i in composiciones.combination:
    resultado += Counter(i)#si ho fem com L'exemple del counter ens dona el següent error TypeError: unhashable type: 'list'. D'aquesta manera no dona error

classes=pd.DataFrame.from_dict(resultado,orient='index',columns=['Count']).sort_values('Count')

# Find the ten most common words in Hamlet
#words = re.findall(r'\w+', open('hamlet.txt').read().lower())
#Counter(words).most_common(10)

# =============================================================================
# Time
# =============================================================================

data_challenger.dtypes

data_challenger['gameDuration']#esta en segundos, pasarlo a minutos estaria bien

Duracion_minutos=data_challenger['gameDuration'].apply(lambda x: x/60)

Duracion_minutos.describe()





# =============================================================================
#  Champions
# =============================================================================


data_challenger['champion']

champs=data_challenger.champion.apply(lambda x:re.findall(r"[a-zA-Z]+[0-9]?_?[a-zA-Z]+",x)).to_frame()#

r_champs=Counter()
for i in champs.champion:
    r_champs += Counter(i)


r_champs.pop('items')
r_champs.pop('star')

champs_def=pd.DataFrame.from_dict(r_champs,orient='index',columns=['Count']).sort_values('Count')



# =============================================================================
# Ranked
# =============================================================================

data_challenger['Ranked']
#podria probar a fer un top 3 amb les clases i campeons,





