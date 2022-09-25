#이름과 점수 입력
Name_info = input("이름 입력 :")
Grade_info = input("점수 입력 :")

a = int(Grade_info)
b = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
def Transcript_Transfer(a, b):
    if a < 60:
        b = b[8]
        print("학점 :", b)
    elif a < 64:
        b = b[7]
        print("학점 :", b)
    elif a < 69:
        b = b[6]
        print("학점 :", b)
    elif a < 74:
        b = b[5]
        print("학점 :", b)
    elif a < 79:
        b = b[4]
        print("학점 :", b)
    elif a < 84:
        b = b[3]
        print("학점 :", b)
    elif a < 89:
        b = b[2]
        print("학점 :", b)
    elif a < 94:
        b = b[1]
        print("학점 :", b)
    else:
        b = b[0]
        print("학점 :", b)

print("학생이름 :", Name_info)
print("점수 :", Grade_info,"점")
Transcript_Transfer(a, b)