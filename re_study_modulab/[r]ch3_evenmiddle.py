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


    #중앙값 구하는 구간 : 리스트안의 'ELements 개수 divide 2'번째 혹은 그다음 번째의 숫자를 꺼내기 (엘리먼츠개수가 홀수라면 중앙값이 median, 짝수라면 가운데 두 수의 평균)
    if not len(even_numbers)%2 == 0:
        print(even_numbers[int(len(even_numbers)//2)],"중앙값")

    if len(even_numbers)%2 == 0:
        print((even_numbers[int(len(even_numbers)//2) - 1] + even_numbers[int(len(even_numbers)//2)]) * 0.5 , "중앙값")

while True:
    #2개의 숫자를 입력
    n = int(input("첫번째 수 입력: "))
    m = int(input("두번째 수 입력: "))

    find_even_number(n,m)