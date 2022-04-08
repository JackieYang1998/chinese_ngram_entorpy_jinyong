import jieba
from collections import Counter
import math

with open("preprocess_langconv_data.txt", "r", encoding="utf-8") as f:
    section = [eve.strip("\n") for eve in f]

# 1-gram
token = []
for line in section:
    word = jieba.cut(line)
    token += word
token_num = len(token)

ct = Counter(token)
vocab1 = ct.most_common()
entropy_1gram = sum([-(eve[1]/token_num)*math.log((eve[1]/token_num),2) for eve in vocab1])
print(token_num,  len(vocab1))
print(vocab1[:10])
print(entropy_1gram)

# 2-gram
def combine2gram(cutword_list):
    if len(cutword_list) == 1:
        return []
    res = []
    for i in range(len(cutword_list)-1):
        res.append(cutword_list[i] + "_"+ cutword_list[i+1]) 
    return res
token_2gram = []
for para in section:
    cutword_list = jieba.lcut(para)
    token_2gram += combine2gram(cutword_list)
token_2gram_num = len(token_2gram)
ct2 = Counter(token_2gram)
vocab2 = ct2.most_common()
same_1st_word = [eve.split("_")[0] for eve in token_2gram]
assert token_2gram_num == len(same_1st_word)
ct_1st = Counter(same_1st_word)
vocab_1st = dict(ct_1st.most_common())
entropy_2gram = 0
for eve in vocab2:
    p_xy = eve[1]/token_2gram_num
    first_word = eve[0].split("_")[0]
    entropy_2gram += -p_xy*math.log(eve[1]/vocab_1st[first_word], 2)
print( token_2gram_num, len(vocab2))
print( vocab2[:10])
print( entropy_2gram)


# 3-gram
def combine3gram(cutword_list):
    if len(cutword_list) <= 2:
        return []
    res = []
    for i in range(len(cutword_list)-2):
        res.append(cutword_list[i] + cutword_list[i+1] + "_" + cutword_list[i+2] ) 
    return res
token_3gram = []
for para in section:
    cutword_list = jieba.lcut(para)
    token_3gram += combine3gram(cutword_list)
token_3gram_num = len(token_3gram)
ct3 = Counter(token_3gram)
vocab3 = ct3.most_common()
same_2st_word = [eve.split("_")[0] for eve in token_3gram]
assert token_3gram_num == len(same_2st_word)
ct_2st = Counter(same_2st_word)
vocab_2st = dict(ct_2st.most_common())
entropy_3gram = 0
for eve in vocab3:
    p_xyz = eve[1]/token_3gram_num
    first_2word = eve[0].split("_")[0]
    entropy_3gram += -p_xyz*math.log(eve[1]/vocab_2st[first_2word], 2)
print(token_3gram_num, len(vocab3))
print(vocab3[:10])
print(entropy_3gram)

