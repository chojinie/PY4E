mpayment = input("monthly_payment: ")
by = int(mpayment) * 12
if by <= 1200:
    z = 1-0.06
elif by <= 4600:
    z = 0.85
elif by <= 8800:
    z = 1-0.24
elif by <= 15000:
    z = 1-0.35
elif by <= 30000:
    z = 1-0.38
elif by <= 50000:
    z = 1-0.4
else:
    z = 1-0.42

ay = by * z
print("세전 연봉 :", by, "만원")
print("세후 연봉 :", ay, "만원")