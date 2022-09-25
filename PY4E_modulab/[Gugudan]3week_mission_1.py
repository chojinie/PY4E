#입력
number = int(input("몇 단?: "))
def gugudan(number):
    for i in range(1, 10):
        if i % 2 != 0 and int(number * i) <= 50:
            print(number, "X ", i, "=", number * i)

print(number, "단")
gugudan(number)