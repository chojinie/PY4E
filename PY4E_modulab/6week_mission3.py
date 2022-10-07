stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]
# 종목과 수익률을 기록할 딕셔너리 생성
profit_dict = dict()


def stock_profit(stocks, sells):
    # stocks 문자열을 ',' 기준을 나누기
    stocks = stocks.split(',')
    for i in range(4):
        # stocks의 i번째 원소를 '/' 기준으로 나누어서 name, amount, moeny 변수에 저장
        name, amount, money = stocks[i].split('/')
        # profit_dict가 key를 name으로 하고 수익률을 value로 하는 딕셔너리로 만들기
        # 수익률 계산 : (수익률 = 손익 / 투자원금 = (현 매매가 - 구매가) / 구매가 * 100)
        profit_dict[name] = float(format((sells[i] - int(money)) / int(money) * 100, '.2f'))
    # 수익률을 기준으로 딕셔너리 정렬하기
    sorted_dict = dict(sorted(profit_dict.items(), key=lambda x: -x[1]))
    # 결과 출력
    for key, item in sorted_dict.items():
        print(f'{key}의 수익률 {item}')


stock_profit(stocks, sells)