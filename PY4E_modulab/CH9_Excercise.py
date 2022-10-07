# # counts = dict()
# # names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# # # # for name in names :
# # # #     if name not in counts:
# # # #         counts[name] = 1
# # # #     else:
# # # #         counts[name] = counts[name] + 1
# # # # print(counts)
# # #
# # for name in names :
# #     counts[name] = counts.get(name, 0) + 1    # counts 딕셔너리에 name이라는 키가 존재할 경우 name에 대한 값을 불러오고, 그렇지 않을 경우에는 counts 딕셔너리에
# #     #name이라는 키에 0이라는 값을 갖는 데이터를 추가하라는 의미.
# # print(counts)
# # #
# # # ccc = dict()
# # # # print(ccc['csev'])
# # #
# # # 'csev' in ccc
#
# # jjj = { 'chuch' : 1, 'fred' : 42, 'jan': 100 }
# # for aaa, bbb in jjj.items():
# #     print(aaa, bbb)
#
# name = input('Enter file : ')
# handle = open(name)
#
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1
# #히스토그램이 Counts에 들어가있음.
# bigcount = None #초기에 비교값 none
# bigword = None
# for word, count in counts.items(): #최대값을찾는루프
#     if bigcount is None or count > bigcount:
#         bigword = word #가장많이나온단어
#         bigcount = count   # 그 숫자
#
# print(bigword, bigcount)


fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        #if the key is not there the count is zero
        # oldcount = di.get(w,0)
        # print(w,'old',oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount

        #idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1

        # if w in di :
        #     di[w] = di[w] + 1
        # else:
        #     di[w] = 1

#         # print(w, di[w])
# print(di)

#now we want to find the most common word
largest = -1
theword = None
for k,v in di.items() :
    if v > largest :
        largest = v
        theword = k #cature/remember the key that was largest

print(theword,largest)