#단어를 찾고, 단어 개수 세는 프로그램
# def count_word(news,b):
#     count = 0
#     for text in news:
#
#         #문장 테스트용
#         # print(text)
#         if b in text:
#             count = count + 1
#         return count
#
# #글자 입력 및 파일을 열기
# b = input("찾고 싶은 글자를 적으세요 : ")
# news = open('overwatch.txt', 'rt', encoding='UTF-8')
#
# print(count_word(news, b))

# #변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록 해줍니다. ??
# add_news = open('overwatch.txt', 'a', encoding='UTF-8')
# add_news.write(b)
# add_news.close()

word = open('overwatch.txt', 'r', encoding='UTF-8')

#글자를 세고 그 값을 반환하는 구간
def count_word(word):

    wordsearch = word.read()
    print(wordsearch)
    # print(word.read()) 이 경우 출력이 안나옴  왜그럴까?
    print(wordsearch.count(a))
    word.close()

#변수에 담긴 글을 함수에 넣어주면 txt파일로 저장되는 구간
    insert = open('overwatch.txt', 'a', encoding='UTF-8')
    insert.write(a)
    insert.close()

a = input("찾고 싶은 글자를 입력하세요: ")

count_word(word)
