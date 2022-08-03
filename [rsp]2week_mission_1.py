import random
computer = random.randint(0,2)

my = input("가위[0], 바위[1], 보[2] 입력해랏!: ")
print("my:", my)
print("computer:", computer)

while int(my) == 0:
    if int(computer) == 0:
        print("비겼습니다!")
    elif int(computer) == 1:
        print("컴퓨터 승리!")
    else:
        print("당신의 승리!")
    break

while int(my) == 1:
    if int(computer) == 0:
        print("당신의 승리!")
    elif int(computer) == 1:
        print("비겼습니다!")
    else:
        print("컴퓨터 승리!")
    break

while int(my) == 2:
    if int(computer) == 0:
        print("컴퓨터 승리!")
    elif int(computer) == 1:
        print("당신의 승리!")
    else:
        print("비겼습니다")
    break