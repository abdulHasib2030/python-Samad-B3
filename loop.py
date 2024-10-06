# i = 1
# while i <= 5:
#   res=int(input("Enter your obtained result:"))
#   if res >= 80:
#     print("A+")
#   else:
#     print("No A+")
#   i += 1


# num = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(num, 'x', i, '=', num*i )
#     i = i + 1

# n = int(input("Enter a number: "))
# for i in range(1,101,2):
#     print(n, 'x', i, '=', n*i)

# for i in range(20, 23):
#     print("Roll: ", i)
#     for j in range(3):
#         if j == 0:
#             num = int(input("Enter Bangla Result: "))
#             if num >= 80:
#                 print("A+ Bangla")
#             else:
#                 print("No A+ Bangla")
#         elif j == 1:
#             num = int(input("Enter English Result: "))
#             if num >= 80:
#                 print("A+ English")
#             else:
#                 print("No A+ English")
#         else:
#             num = int(input("Enter Math Result: "))
#             if num >= 80:
#                 print("A+ Math")
#             else:
#                 print("No A+ Math")

# for i in range(10):
#     print(i)
#     if i == 5:
#         break

# for i in range(10):
#     if i > 5:
#         continue
#     print(i)

### Question no - 1
# for i in range(1,101):
#     print(i, end=",")

### Question no - 2
# for i in range(2, 101, 2):
#     print(i,end="," )

### Question no - 3
# sum = 0
# for i in range(1, 101):
#     sum = sum + i 
# print(sum) 

### Question no - 4
for i in range(1, 101):
    if i == 1:
        continue
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        print(i, end=",")


