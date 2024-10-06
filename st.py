
# st = {1, 2, 3}
# st2 = set()
# print(type(st))
# print(type(st2))

# st = set()
# st.add(10)
# print(st)

# st = {1, 2, 3, 1, 2, "samad"}
# st.add(99)
# st.update({1, 6, 7, 8})
# # st.remove(1)
# st.discard(99)
# st.clear()
# print(st)

a = {1, 2, 3, 4, 5}
b = {1, 5, 7, 8, 9}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
