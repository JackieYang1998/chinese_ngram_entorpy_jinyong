import jieba

line = "武林至尊宝刀屠龙号令天下莫敢不从倚天不出谁与争锋"

token = jieba.lcut(line)
print(token)

def combine2gram(cutword_list):
    if len(cutword_list) == 1:
        return []
    res = []
    for i in range(len(cutword_list)-1):
        res.append(cutword_list[i] + "_"+ cutword_list[i+1]) 
    return res
def combine3gram(cutword_list):
    if len(cutword_list) <= 2:
        return []
    res = []
    for i in range(len(cutword_list)-2):
        res.append(cutword_list[i] + cutword_list[i+1] + "_" + cutword_list[i+2] ) 
    return res

token2 = combine2gram(token)
print(token2)
token3 = combine3gram(token)
print(token3)