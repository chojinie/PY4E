# #버스 요금 입력
# # 버스 요금 입력
# bus_fare(30, "현금")
#
# # 출력
# 나이: 30세
# 지불유형: 현금
# 버스요금: 1300원
a = int(input("나이를 입력하세요: "))
b = input("지불 유형을 입력하세요: ")

while a < 8:
    if b == "카드":
        print("나이 :", a, "세")
        print("지불유형 :", b)
        print("버스요금 : 무료")
    elif b == "현금":
        print("나이 :", a, "세")
        print("지불유형 :", b)
        print("버스요금 : 무료")
    else:
        print("다시 입력하세요.")
    break
while a < 14:
    if b == "카드":
        print("나이 :", a, "세")
        print("지불유형 :", b)
        print("버스요금 : 450원")
    elif b == "현금":
        print("나이 :", a, "세")
        print("지불유형 :", b)
        print("버스요금 : 450원")
    else:
        print("다시 입력하세요.")
    break
while a < 20:
    if b == "카드":
        print("나이 :", a, "세")
        print("지불유형 :", b)
        print("버스요금 : 720원")
    elif b == "현금":
        print("나이 :", a, "세")
        print("지불유형 :", b)
        print("버스요금 : 1000원")
    else:
        print("다시 입력하세요.")
    break
while a < 75:
    if b == "카드":
        print("나이 :", a, "세")
        print("지불유형 :", b)
        print("버스요금 : 1200원")
    elif b == "현금":
        print("나이 :", a, "세")
        print("지불유형 :", b)
        print("버스요금 : 1300원")
    else:
        print("다시 입력하세요.")
    break
while a >= 75:
    if b == "카드":
        print("나이 :", a, "세")
        print("지불유형 :", b)
        print("버스요금 : 무료")
    elif b == "현금":
        print("나이 :", a, "세")
        print("지불유형 :", b)
        print("버스요금 : 무료")
    else:
        print("다시 입력하세요.")
    break
