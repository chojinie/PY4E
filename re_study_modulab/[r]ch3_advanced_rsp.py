import random
# 누가 이기는지 출력하는 함수
def rsp(a, b, i, win, draw, lose):
    if (a - b) == -2 or (a - b) == 1:
        print(i+1,"번째 판","YOU WIN!\n")
        win = win + 1
    elif (a - b) == 0:
        print(i+1,"번째 판","DRAW!\n")
        draw = draw + 1
    else:
        print(i+1,"번째 판","COMPUTER WIN!\n")
        lose = lose + 1
    return [win,draw,lose]

round = int(input("몇 판을 진행하시겠습니까? : "))
win = 0
draw = 0
lose = 0

# 매 판마다 가위바위보를 진행할 알고리즘
for i in range(0,round):
    #나
    while True:
        me_str = input("무엇을 내시겠어요?\n(0: 가위 1: 바위 2:보) : ")
        if me_str in ["0","1","2","가위","바위","보"]:
            break
        else:
            print("다시 입력하기")
            continue
    if me_str == "가위" or me_str == "0":
        me_int = 0
        me_str = "가위"
    elif me_str == "바위" or me_str == "1":
         me_int = 1
         me_str = "바위"
    else:
        me_int = 2
        me_str = "보"
    # 컴퓨터
    com_int = random.randint(0, 2)
    if com_int == 0:
        com_str = "가위"
    elif com_int == 1:
        com_str = "바위"
    else:
        com_str = "보"
    # 누가 무엇을 냈는가
    print("나 :", me_str)
    print("컴퓨터 :", com_str)
    # 누가 이겼는지 출력
    array = rsp(me_int, com_int, i, win, draw, lose)

    win = array[0]
    draw = array[1]
    lose = array[2]

print(str(win) + "승", str(draw) + "무", str(lose) + "패")