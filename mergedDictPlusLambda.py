#Merged Dictionaries and Sorted Dictionaries using lambda

from collections import ChainMap

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = ChainMap(dic1, dic2, dic3)
sorted_dic4 = sorted(dic4.items(), key=lambda x: x[1])
print(dict(sorted_dic4))
