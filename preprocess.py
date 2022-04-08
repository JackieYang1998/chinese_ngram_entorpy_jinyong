import os


datapath = "./JinYong"
filelist = os.listdir(datapath)

section = []
for filename in filelist:
    filepath = datapath +'/'+ filename
    with open(filepath, "r", encoding="ANSI") as file:
        text = [line.strip("\n").replace("\u3000", "").replace("\t", "") for line in file]
        section += text[2:-2]

import string
from zhon.hanzi import punctuation

punctuation_string = string.punctuation
print("英文标点：", punctuation_string)

punctuation_str = punctuation
print("中文标点：", punctuation_str)


for num in range(len(section)):
    for i in punctuation_string:
        section[num] = section[num].replace(i, "")
    for i in punctuation_str:
        section[num] = section[num].replace(i, "")


with open("preprocess_data.txt", "w", encoding="utf-8") as f:
    for line in section:
        if len(line) > 1:
            print(line, file=f)          


from langconv import *
def Traditional2Simplified(sentence):
  sentence = Converter('zh-hans').convert(sentence)
  return sentence
  
for num in range(len(section)):
        section[num] = Traditional2Simplified(section[num])


with open("preprocess_langconv_data.txt", "w", encoding="utf-8") as f:
    for line in section:
        if len(line) > 1:
            print(line, file=f)          
