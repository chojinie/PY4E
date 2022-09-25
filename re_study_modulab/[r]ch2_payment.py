
def payment():
    y_payment = 12 * m_payment    #y_payment : 세전연봉, m_payment : 월급

    if y_payment <= 1200:
        y_payment = y_payment * (1-0.06)
    elif y_payment <= 4600:
        y_payment = y_payment * (1-0.15)
    elif y_payment <= 8800:
        y_payment = y_payment * (1-0.24)
    elif y_payment <= 15000:
        y_payment = y_payment * (1-0.35)
    elif y_payment <= 30000:
        y_payment = y_payment * (1-0.38)
    elif y_payment <= 50000:
        y_payment = y_payment * (1-0.40)
    else:
        y_payment = y_payment * (1-0.42)
    print("세전 연봉 :", m_payment * 12, "만원")
    print("세후 연봉 :",y_payment, "만원")

m_payment = int(input("월급을 입력하세요.(세전) : "))
payment()



