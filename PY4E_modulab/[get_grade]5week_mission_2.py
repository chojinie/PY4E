# 학생 답
s = ["김갑,3242524215",
     "이을,3242524223",
     "박병,2242554131",
     "최정,4245242315",
     "정무,3242524315"]

# 정답지
a = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]


def grader(s, a):
    astring = "".strip().join(list(map(str, a)))  # 정답지를 연속된 문자열로 바꿈
    slist = [i.strip().split(",") for i in s]  # 학생 답의 원소를 컴마 기준으로 나누어 리스트로 만듦
    gradelist = []

    # slist: [['김갑', '3242524215'],
    #         ['이을', '3242524223'],
    #         ['박병', '2242554131'],
    #         ['최정', '4245242315'],
    #         ['정무', '3242524315']]

    # 각각 학생 별 점수 계산을 위한 반복문
    for student in slist:
        grade = 0  # 점수 변수
        for i in range(len(a)):  # 정답의 개수만큼 반복
            if student[1].strip()[i] == astring[i]:  # student[1][i]: 학생이 작성한 답(혹시 모를 공백 제거)
                grade = grade + 100 / len(a)  # 학생이 작성한 답이 정답과 같을 때마다 10점 추가
        gradelist.extend([[student[0], grade]])  # gradelist에 학생 이름과 점수를 리스트로 추가한다

    print_sorted_grade(gradelist)


# 성적 sorting & 출력함수
# gradelist: [['정무', 90], ['김갑', 80], ['이을', 70], ['박병', 50], ['최정', 40]]
def print_sorted_grade(gradelist):
    gradelist.sort(key=lambda x: (-x[1], x[0]))  # 점수를 역순으로 우선정렬 & 이름순 정렬
    for i, grade in enumerate(gradelist):
        print(f"학생: {grade[0]}    점수: {int(grade[1])}점    {i + 1}등")


grader(s, a)

# 학생: 정무 점수: 90점 1등
# 학생: 김갑 점수: 80점 2등
# 학생: 이을 점수: 70점 3등
# 학생: 박병 점수: 50점 4등
# 학생: 최정 점수: 40점 5등