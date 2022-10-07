# 조건1 - 숫자는 0 ~ 100까지 숫자를 3개 만듭니다(중복 불가).
# 조건2 - 5회, 10회까지 정답을 못맞추면 최솟값, 최대값에 대한 힌트를 줍니다.
# 조건3 - 정답을 맞추면, 맞춘 정답이 최솟값인지, 중간값인지, 최댓값인지 알려줍니다.

import random

numlist = random.sample(range(0, 100), 3)  # 중복 없이 숫자 세개를 생성


# print(numlist)

# 입력 검증하는 반복문 함수
def guess_numbers_input():
    while True:
        try:
            myguess = int(input("숫자를 예측해보세요 : "))
            if 0 < myguess < 100:
                break
            else:
                print("숫자는 0~100 사이의 숫자입니다")
        except ValueError:
            print("숫자를 입력하세요")
    return myguess


# 숫자 예측 조건문
def guess_number_cond(myguess, guesslist, n, count):
    if myguess in guesslist:  # 이미 입력한 값을 또 입력한 경우
        print(f"{myguess}는 이미 예측에 사용한 숫자입니다.")
    else:
        if myguess not in numlist:  # 나의 입력이 숫자에 포함되지 않으면
            print(f"{myguess}는 없습니다.")
            n = n + 1
        elif myguess in numlist:  # 나의 입력이 숫자에 포함되면
            if myguess == max(numlist):
                print(f"숫자를 맞추셨습니다! {myguess}는 최댓값입니다.")
            elif myguess == min(numlist):
                print(f"숫자를 맞추셨습니다! {myguess}는 최솟값입니다.")
            else:
                print(f"숫자를 맞추셨습니다! {myguess}는 중간값입니다.")
            count = count + 1
            n = n + 1
    return n, count


# 최대값, 최소값의 힌트를 알려주는 조건문 함수
def guess_number_hint(myguess, numlist, guesslist):
    if min(numlist) not in guesslist:  # 최솟값을 맞추지 못한 경우
        if myguess < min(numlist):
            print(f"최소값은 {myguess}보다 큽니다")
        elif myguess > min(numlist):
            print(f"최소값은 {myguess}보다 작습니다")
    elif max(numlist) not in guesslist:  # 최대값을 맞추지 못한 경우
        if myguess > max(numlist):
            print(f"최대값은 {myguess}보다 작습니다")
        elif myguess < max(numlist):
            print(f"최대값은 {myguess}보다 큽니다")


# 숫자를 예측 게임 함수
def guess_numbers():
    count = 0  # 정답 맞춘 횟수 계산
    n = 1  # n차 시도를 나타냄
    guesslist = []  # input으로 입력한 숫자를 저장하는 함수

    while count != 3:  # 정답을 3회 맞추면 종료되는 반복문
        print(f"{n}차 시도")
        myguess = guess_numbers_input()
        if n != 5 and n != 10:
            n, count = guess_number_cond(myguess, guesslist, n, count)
        else:  # 5차 시도 혹은 10차 시도인 경우
            n, count = guess_number_cond(myguess, guesslist, n, count)
            guess_number_hint(myguess, numlist, guesslist)
        guesslist.append(myguess)  # guesslist에 입력한 원소를 추가함

    if count == 3:  # 3회 정답을 맞추면 출력
        print(f"게임 종료\n{n - 1}번 시도만에 예측 성공")


guess_numbers()

# 1차 시도
# 숫자를 예측해보세요 : 39
# 숫자를 맞추셨습니다! 39는 최솟값입니다.
# 2차 시도
# 숫자를 예측해보세요 : 48
# 숫자를 맞추셨습니다! 48는 최댓값입니다.
# 3차 시도
# 숫자를 예측해보세요 : 100
# 숫자를 맞추셨습니다! 100는 최댓값입니다.
# 게임종료
# 3번 시도만에 예측 성공

# ...
# 5차 시도
# 숫자를 예측해보세요 : 9
# 9는 없습니다
# 최솟값은 9보다 작습니다
# 6차 시도
# 숫자를 예측해보세요 : 9
# 이미 예측에 사용한 숫자입니다
# 6차 시도