# # fruit = 'banana'
# # for word in fruit:
# #     print(word)
#
# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
#     print(count)
#
# # print("quantity of 'a' in word is : ", count)
#
# s = 'Monty Python'
# print(s[0:4]) #마지막 -1 번째 까지만 나옴.
#
# print(s[6:7])
#
# print(s[6:20])

# word = 'banana'
# if word == 'banana':
#     print('All right, bannas.')
#
# if word < 'banana':
#     print('Your word,'+ word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word,' + word + ', comes after banana.')
# else:
#     print('All right, bananas.')

# greet = 'Hello Bob'
# zap = greet.lower()
# print(zap)
#
# # print('Hi There'.lower())
#
# fruit = 'banana'
# pos = fruit.find('n')
# print(pos)
#
# aa = fruit.find('z')
# print(aa)   #z가 없으니까 -1을 반환하게 된다.
#
# great = 'Hello Bob'
# nstr = great.replace('Bob', 'Anna')
# print(nstr)
#
# greet = '      Hello bob    '
# greet.strip()
# print(greet.strip())

#
# data = 'From stephen.marquarc@uct.ac.za Sat Jan 5 09:15:16 2022'
# atpos = data.find('@')
# print(atpos)
#
# sppos = data.find(' ',atpos)
# print(sppos)
#
# host = data[atpos+1 : sppos]
# # print(host)
#
# str = 'X-DSPAM-Confidence: 0.8475'
#
# ipos = str.find(':')
# print(ipos)
#
# piece = str[ipos+2:]
# print(piece)
# value = float(piece)
# print(value)

words = 'Connect Foundation'

if 'F' in words:
    words.lower()
    words[7] = '&'
else:
    print(words)
print(words)