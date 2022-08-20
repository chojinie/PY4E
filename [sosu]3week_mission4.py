# #입력값 두 수 사이의 소수가 몇 개인지 출력하는 함수
# def count_prime_number(n, m):
#
#     #소수가 아닌 수의 개수 세기 (나중에 빼서 소수 개수 세기)
#     not_prime = 0
#
#     #입력값 n과 m사이의 수를 하나씩 판별
#     for i in range(n, m):
#
#         #n, m 사이의 수 i가 소수인지 판별하려면 2부터 i까지 중 하나의 수로도 나뉘면 안 됨
#         #나뉠 경우(나머지가 0인 경우) not_prime으로 개수 세기
#         for j in range(2, i):
#             if i % j == 0:
#                 print(i, '는 소수가 아니다') #확인용
#                 not_prime = not_prime + 1
#                 break
#
#     #소수가 아닌 수로 빼서 소수 개수 세기
#     prime = (m - n + 1) - int(not_prime)
#     print(n, '과', m, '사이에 소수는', prime, '개 입니다.')
#
# n = int(input('첫 번째 수 입력 : '))
# m = int(input('두 번째 수 입력 : '))
# count_prime_number(n, m)


#방법2
#함수 정의
def count_prime_number(n, m):
    cnt = 0 #개수 초기화
    is_prime = True #판단하고자 하는 숫자에 대한 참 거짓
    for i in range(n, m+1): #입력 받은 숫자사이의 소수 판단
        for j in range(2, i): # 범위내의 숫자가 소수인지 아닌지 판단
            is_prime = Tue #초기화
            if i % j !=0:
                continue
            else:
                is_prime = False #거짓
                break #이중 For ans 중 안쪽 반복문만 break
        if is_prime:
            cnt += 1 #안쪽 반복문이 끝나면 True 면 카운트
    print("소수개수", cnt)

    count_prime_number(n, m)