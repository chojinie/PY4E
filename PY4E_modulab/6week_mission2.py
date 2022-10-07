def sales_management(person, record):
    # 변수 초기화
    rank = dict()
    score = []
    # 올해 실적 평균 내기
    for s in record:
        score.append(round(sum(s) / len(s), 2))
    for i in range(len(score)):
        rank[person[i]] = score[i]

    # 내림차순으로 등수 매기기
    rank = sorted(rank.items(), key=(lambda x: x[1]), reverse=True)
    rank = [i for i in rank]

    # 출력
    # 조건 1 : 평균 실적 1,2등
    for p, s in rank[:2]:
        # 조건3 : 평균실적 5 이하는 제외
        if s > 5:
            print("보너스 대상자: ", p)
    # 조건 2 : 면담 대상자
    for p, s in rank[-2:]:
        # 조건4 : 평균실적 3 초과는 제외
        if s <= 3:
            print("면담 대상자: ", p)


# 주어진 리스트
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4, 5, 3, 5, 6, 5, 3, 4, 1, 3, 4, 5],
                  [2, 3, 4, 3, 1, 2, 0, 3, 2, 5, 7, 2],
                  [1, 3, 0, 3, 3, 4, 5, 6, 7, 2, 2, 1],
                  [3, 2, 9, 2, 3, 5, 6, 6, 4, 6, 9, 9],
                  [8, 7, 7, 5, 6, 7, 5, 8, 8, 6, 10, 9],
                  [7, 8, 4, 9, 5, 10, 3, 3, 2, 2, 1, 3]]

# 영업 관리 프로그램 실행
sales_management(member_names, member_records)