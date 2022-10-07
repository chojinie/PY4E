name = str(input("이름을 입력하세요 : "))
number = input("전화번호를 입력하세요. 000-0000-000형식: ")

file = open('test_text.txt', 'a', encoding='UTF-8')

if number.startswith('010'):
    if number[3] == '-' and number[8] == '-':
        if len(number) == 13:
            file.write(f'{name},{number}\n')
            # file.write(',')
            # file.write(number)
            # file.write('\n')
        else:
            print("전체 13자리입니다")
            print("잘못 쓴 사람: ", name, "\n잘못 쓴 번호: ", number)
    else:
        print("가운데 하이푼 입력해주세요")
        print("잘못 쓴 사람: ", name, "\n잘못 쓴 번호: ", number)
else:
    print("010으로 시작하세요")
    print("잘못 쓴 사람: ", name, "\n잘못 쓴 번호: ", number)

file.close()

