# # abc = 'with ha ri bo yup'
# # stuff = abc.split()
# # print(stuff)
# # print(stuff[2])
# #
# # for w in stuff :
# #     print(w)
# #
# #     #split()  공백이면 띄어쓰기를 기준으로 잘림 but, 공백만을 기준으로 할 필요는 없고 콜론 등도 가능
# #
# # line = 'with;ha;ri;bo;yup'
# # thing = line.split(';')
# # print(thing)
# #
# # day = 'From stepen.marqqq@uct.ac.za Sat Jan 509:14:11:11 2022'
# # word = day.split()
# # b = word[1]
# # print(b)
# # c = b.split('@')
# # print(c[1])
#
# han = open('mbox-short.txt')
#
# for line in han:
#     line = line.rstrip()
#     wds = line.split()
#     #Guardian a bit stronger   if wds has only 'from' then it will be continue
#     if len(wds) < 3 or wds[0] != 'From':   #guardian in a compound statement
#         continue
#     print(wds[2])


num1 = [1, 2, 3, 4]
num2 = [6, 7, 8, 9]

num1.append(num2)

print(num1)