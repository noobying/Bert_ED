import json
from tqdm import tqdm


'''
用于测试在train中出现过的entity是否都在sub中
'''

# with open("../消歧比赛数据集/train.json",'r',encoding='UTF-8') as f:
#     train_json = json.load(f)
#     print(type(train_json))
#
# for item in train_json:
#     for entity in item["lab_result"]:
#         name = entity[""]


'''
用于测试raw中是不是都在sub里面
'''
# count=0
# bar = tqdm(210000)
# with open("../消歧比赛数据集/raw_texts.txt",'r',encoding='UTF-8') as f_raw:
#     for line in f_raw.readlines():
#         name = line.strip().split('\t')[0].strip()
#         flag=0
#         with open("../消歧比赛数据集/company_2_code_sub.txt",'r',encoding='UTF-8') as f_sub:
#             for item in f_sub.readlines():
#                 name2 = item.strip().split('\t')[1].strip()
#                 if name2==name:
#                     flag=1
#
#         if flag==0:
#             count+=1
#         bar.update(1)
#
# print(count)


'''
获取最长的实体名称
'''
l = []
with open("../消歧比赛数据集/company_2_code_full.txt", 'r', encoding='UTF-8') as f_sub:
    for item in f_sub.readlines():
        name = item.strip().split('\t')[0].strip()
        # if  len(name)==10:
        #     print(name)
        if len(name) not in l:
            l.append(len(name))

print(l)


