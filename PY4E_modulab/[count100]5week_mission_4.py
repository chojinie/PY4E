def after_100(mon, day, yoil):
    import datetime
    yoils = ["월", "화", "수", "목", "금", "토", "일"]
    start = datetime.datetime(2022,mon,day) # 시작일
    days_100 = datetime.timedelta(days=99)  # 더할 기간
    after = start + days_100                # 100일후 날짜
    af_mon = after.month                    # 100일후 날짜의 월
    af_day = after.day                      # 100일후 날짜의 일
    af_yoil = after.weekday()               # 100일후 날짜의 요일(0~9의 숫자로 반환)

    # yoils[af_yoil] : 요일의 인덱스를 이용해 yoils 리스트의 원소를 참조함
    print(f"{mon}월 {day}일 {yoil}요일부터 100일 뒤는 {af_mon}월 {af_day}일 {yoils[af_yoil]}요일")

after_100(8,17,"수")