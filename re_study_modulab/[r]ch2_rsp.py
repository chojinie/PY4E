import random

def rsp(my):
    computer = random.randint(0,2)
    if computer == 0 :
        computer = '가위'
    elif computer == 1 :
        computer = "바위"
    elif computer == 2 :
        computer = "보"

    if my == '0' or my == "가위":
        print("나: 가위")
        if computer == '가위':
            print("컴퓨터: 가위")
            print("비겼습니다!")
        elif computer == "바위":
            print("컴퓨터: 바위")
            print("컴퓨터승리!")
        elif computer == "보":
            print("컴퓨터: 보")
            print("사용자승리!")

    elif my == '1' or my == "바위":
        print("나: 바위")
        if computer == '가위':
            print("컴퓨터 : 가위")
            print("사용자승리!")
        elif computer == "바위":
            print("컴퓨터 : 바위")
            print("비겼습니다!")
        elif computer == "보":
            print("컴퓨터 : 보")
            print("컴퓨터승리!")

    elif my == '2' or my == "보":
        print("나: 보")
        if computer == '가위':
            print("컴퓨터 : 가위")
            print("컴퓨터승리!")
        elif computer == "바위":
            print("컴퓨터 : 바위")
            print("사용자승리!")
        elif computer == "보":
            print("컴퓨터 : 보")
            print("비겼습니다!")
    else :
        print("다시 입력하세요.")

my = input("0 = 가위, 1 = 바위, 2 = 보 : ")
rsp(my)

#while쓰면 실행 이후 바로 입력창을 띄울 수 있음.
