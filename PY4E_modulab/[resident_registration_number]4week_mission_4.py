registration = input("주민등록번호를 입력하세요 : ")

def check_id() :
    try :
        while len(registration) == 14 :
            registration.index[6] == '-'
            if registration.index[7] == 1 or registration.index[7] == 3 :
                sex = '남자'
            if registration.index[7] == 2 or registration.index[7] == 4 :
                sex = '여자'

    except :
        print("잘 못된 번호입니다. 다시 입력해 주세요.")

check_id(registration)