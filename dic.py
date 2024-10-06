
# dic = {"name":"Adarsha", 'place':"Lakshmipur"}
# print(type(dic))
# print(dic)
# print(dic["name"]) 
# dic["name"] = "Samad"
# dic2 = {'age':137, "born":1887}
# dic.update(dic2)
# print(dic)

# dic = {"name":"Samad", "age": 137}
# del dic["age"]
# dic['age'] = 137
# print(dic)
# print(dic.get("age", "key is not valid"))
# cpy = dic.copy()
# print(cpy)
# print(cpy["name"])

dic = {'name': 'samad', "age":137}
# for i in dic:
#     print(i, dic[i])
# for key, value in dic.items():
#     print(key, value)
# for key in dic.keys():
#     print(key)
for value in dic.values():
    print(value)