def find_even_number(i,j):
    if(i%2) : i += 1
    numbers=[a for a in range(i,j+1,2)]
    for a in numbers:
        print(a, "짝수")
        if (n+m)/2 == a: print(a,"중앙값")

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n,m)