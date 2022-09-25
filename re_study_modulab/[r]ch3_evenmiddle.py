print("#짝수 및 중앙값 출력 프로그램")
def find_even_number(n,m):

    #받은 입력 구간 안의 숫자(짝수) 출력
    numbers = [i for i in range(n, m+1)]

    even_numbers = []
    for i in numbers:
        if i%2 ==0:
            even_numbers.append(i)
    for j in even_numbers:
        print(j, "짝수")

while True:
    #2개의 숫자를 입력

    n = int(input("첫번째 수 입력: "))
    m = int(input("두번째 수 입력: "))


    find_even_number(n,m)

#중앙값 구하는 것부터해야함._09/24