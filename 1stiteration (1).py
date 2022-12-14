# -*- coding: utf-8 -*-
"""1stIteration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1urSUmGaEaSpigC5ixVm794emDrBE0-cj
"""

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
import pickle
import numpy as np
import os

from google.colab import files
uploaded = files.upload()

"""Preproccessing::"""

file = open("www-gutenberg-org-files-1342-1342-0-txt.txt", "r", encoding = "utf8")


line = []
for i in file:
    line.append(i)


txtData = ""
for i in line:
  txtData = ' '. join(line) 

txtData = txtData.replace('\n', '').replace('\r', '').replace('\ufeff', '').replace('“','').replace('”','')  #new line, carriage return, unicode character --> replace by space

 
txtData = txtData.split()
txtData = ' '.join(txtData)
print(txtData[:300])

print(len(txtData))

"""Tokenizer:"""

token = Tokenizer(oov_token='<OOV>')
token.fit_on_texts([txtData])

# saving the tokenizer for predict function
pickle.dump(token, open('token.pkl', 'wb'))

seq_data = token.texts_to_sequences([txtData])[0]
print(seq_data[:30])
print(len(seq_data))

vocabSize =  len(token.word_index) + 1
print(vocabSize)

"""Creates sequence of 3 words and predicted word """

seq = []
for i in range(3, len(seq_data)): 
  wrd = seq_data[i-3 : i + 1]
  seq.append(wrd)

print("sequence length: " , len(seq))
seq = np.array(seq)
print(seq[:15])

"""Data represents the first 3 letters that the alg will be reading 
:  Predict represents predicted word
"""

data = []
predict = []

for i in seq:
    data.append(i[0:3])
    predict.append(i[3])
    
data = np.array(data)
predict = np.array(predict)

print(data)
print("/n")
print(predict)

