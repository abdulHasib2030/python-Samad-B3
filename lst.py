
# lst = [10, 5.6, "samad", True]
# print(lst[1])
# print(lst[-1])
# lst[2] = "Adarsha Samad"
# print(lst)

# lst = [10, 21, 31, 5, 6]
# length = len(lst)
# print(length)
# for i in range(length):
#     print(lst[i])

# for i in lst:
#     print(i)

# lst = [1, 2, 5, 1]
# lst.append(92)
# lst.append("Samad")

# lst.remove(5)
# print(lst)
# print(lst.count(1))
### Question no - 1
# lst = [1, 2, 3, 4, 5]

# for i in range(len(lst)):
#     lst.remove(lst[0])
# print(lst)


### Question no - 2
s = ['tanvir', 'kaosar', 'jakir']
m = [32, 52, 88]
p = []
for i in m:
    if i >= 33:
        p.append("passed")
    else:
        p.append("Fail")
results = []
for i in range(len(m)):
    temp = []
    temp.append(s[i])
    temp.append(m[i])
    temp.append(p[i])
    results.append(temp)
print(results)

