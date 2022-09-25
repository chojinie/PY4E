# function안에 int를 일일히 쓰는 방법이 아니라 입력으로 들어가는 Point자체를 int 클래스로 인식해서 함수를 좀더 간소화할 수 있는방안???

def grader(name, point):


    if point < 60:
        grade = 'F'
    elif point < 65:
        grade = 'D'
    elif point < 70:
        grade = 'D+'
    elif point < 75:
        grade = 'C'
    elif point < 80:
        grade = 'C+'
    elif point < 85:
        grade = 'B'
    elif point < 90:
        grade = 'B+'
    elif point < 95:
        grade = 'A'
    else:
        grade = 'A+'
    print("학생이름 :",name, "\n점수 :",point, "\n학점 :",grade)


name = input('이름을 입력하세요: ')
point = int(input('점수를 입력하세요: '))
grader(name, point)