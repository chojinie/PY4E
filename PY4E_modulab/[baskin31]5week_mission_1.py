def bs31():
    print("베스킨라빈스 써리원 게임")
    print("------------------")
    import random
    number = 0
    while True:
        # my turn
        my = input("My turn - 숫자를 입력하세요: ")
        my = my.split()  # 스플릿시켜서각문자끼리분리 #‘1’ㄹ…. #아직까지는 문자열
        if int(my[0]) != number + 1 or len(my) > 3:
            print("숫자를 제대로 입력하세요")
            continue
        # 숫자 2개 입력 후 연속된 숫자가 아닐 경우 제한
        if len(my) == 2:
            if int(my[1]) - int(my[0]) != 1:
                print("연속된 숫자만 입력하세요")
                continue
        # 숫자 3개 입력 후 연속된 숫자가 아닐 경우 제한
        if len(my) == 3:
            if int(my[2]) - int(my[1]) != 1 or int(my[1]) - int(my[0]) != 1:
                print("연속된 숫자만 입력하세요")
                continue

        number = int(my[-1])  # 마지막값을나타내는
        print(f"현재 숫자 : {number}")

        # 31을 넘겼는지 검사
        if number >= 31:
            print("패배")
            break

        # computer 컴터쪽은 잘 이해가 안되는데.. +=1 이 왜나오지?
        computer = []
        computer_turn_num = random.randint(1, 3)
        for i in range(computer_turn_num):
            number += 1
            # 컴퓨터가 31이 넘는 수를 외치면 31로 되돌리기
            if number > 31:
                number = number - 1
                continue
            computer.append(number)
            print(f"컴퓨터 : {computer[-1]}")
        print(f"현재 숫자 : {number}")
        print()
        # 31이 있는지 검사
        if 31 in computer:
            print("승리!")
            break
    print("게임 종료")
