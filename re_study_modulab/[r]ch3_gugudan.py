#3주차 문제1번 구구단프로그램
print("#구구단프로그램")
def gugudan(number):

    n = [1,2,3,4,5,6,7,8,9]
    print(number, "단")
    for i in n:
        if i%2 == 1 and i*number <= 50:
            print(number,"X", i, "=",i * number)

number = int(input("몇 단? : "))
gugudan(number)