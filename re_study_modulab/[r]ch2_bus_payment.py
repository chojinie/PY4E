# 4번 문제
# 버스 요금 계산기

print('#버스 요금 계산기')
def bus_fare(age, pay):
    try:
        if int(age) >= 8 and int(age) < 14:
            if pay == "카드" or pay == "card":
                fare = 450
            elif pay == "현금" or pay == "cash":
                fare = 450
        elif int(age) >= 14 and int(age) < 20:
            if pay == "카드" or pay == "card":
                fare = 720
            elif pay == "현금" or pay == "cash":
                fare = 1000
        elif int(age) > 20 and int(age) < 75:
            if pay == "카드" or pay == "card":
                fare = 1200
            elif pay == "현금" or pay == "cash":
                fare = 1300

        print("나이: ",age,"세","\n지불유형: ",pay, "\n버스요금: ",fare,"원")

    except:
        print("나이: ", age, "세")
        print("버스요금: ", "무료")

age, pay = input("나이와 지불 방법을 입력하세요 : ").split(",")
bus_fare(age, pay)