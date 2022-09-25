def rcp(my):
    import random
    computer=random.randint(0,2) #0:바위 / 1:가위 / 2:보
    if computer==0:
        computer="바위"
    elif computer==1:
        computer="가위"
    else:
        computer="보"
    if computer=="바위":
        if my == "가위":
            print("나:", my)
            print("컴퓨터:", computer)
            print("컴퓨터 승리!")
        if my == "바위":
            print("나:", my)
            print("컴퓨터:", computer)
            print("비김!")
        if my == "보":
            print("나:", my)
            print("컴퓨터:", computer)
            print("나 승리!")
    elif computer=="가위":
        if my == "가위":
            print("나:", my)
            print("컴퓨터:", computer)
            print("비김!")
        if my == "바위":
            print("나:", my)
            print("컴퓨터:", computer)
            print("나 승리!")
        if my == "보":
            print("나:", my)
            print("컴퓨터:", computer)
            print("컴퓨터 승리!")
    else:
        if my == "가위":
            print("나:", my)
            print("컴퓨터:", computer)
            print("나 승리!")
        if my == "바위":
            print("나:", my)
            print("컴퓨터:", computer)
            print("컴퓨터 승리!")
        if my == "보":
            print("나:", my)
            print("컴퓨터:", computer)
            print("비김!")

my = input("가위/바위/보 중 입력하세요 : ")
rcp(my)