# read = open('mbox-short.txt')
# count = 0
# for word in read:
#     count = count + 1
# print('line count:', count)
#
# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line:
#         continue
#     print(line)

# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     quit()
#
# count = 0
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

#
# fh = open('mbox-short.txt')
#
# for lx in fh:
#     nlx = lx.rstrip()
#     if nlx.startswith('Received'):
#         print(nlx.upper())

#단어를 찾고, 단어 개수 세는 프로그램
def count_word(news,b):
    count = 0
    for text in news:
        #문장 테스트용
        # print(text)
        if b in text:
            print(b)
            count = count + 1
    return count

#글자 입력 및 파일을 열기
b = input("찾고 싶은 글자를 적으세요 : ")
news = open('overwatch.txt', 'rt', encoding='UTF-8')

print(count_word(news, b))

# #변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록 해줍니다. ??
# add_news = open('overwatch.txt', 'a', encoding='UTF-8')
# add_news.write(b)
# add_news.close()

