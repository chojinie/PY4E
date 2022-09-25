info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
info_dict = dict()
label = ['아이디', '나이', '전화번호', '성별', '지역', '구매횟수']
# 전화번호가 잘못되어서 쿠폰을 받을 수 없는 사람의 인덱스를 저장하는 리스트
exclude = []

# 각 회원정보 레이블에 대해서 딕셔너리 초기화
for i in label:
    info_dict[i] = list()


def good_customer(info):
    # info 문자열을 ','를 기준으로 나누기
    info = info.split(',')
    for i in range(6):
        # get_info에 info에서 추출한 특정 사람의 회원정보 저장
        get_info = info[0 + 6 * i:6 + 6 * i]
        # 회원의 전화번호가 없다면:
        if get_info[2] == 'x':
            # 010-0000-0000으로 전화번호 대체
            get_info[2] = '010-0000-0000'
            # 쿠폰을 주지 말아야 될 회원으로 추가
            exclude.append(i)
        # 회원정보 출력하기
        for j in range(6):
            info_dict[label[j]].append(get_info[j])
    idx = 0
    for i in info_dict['구매횟수']:
        # 8회 이상 구매한 VIP 대상이면서 exclude 리스트에 인덱스가 포함되어 있지 않다면:
        if int(i) >= 8 and idx not in exclude:
            # 할인 쿠폰을 받을 회원정보 출력
            print('할인 쿠폰을 받을 회원정보 아이디 : ' + info_dict['아이디'][idx] + ', 나이 : ' + info_dict['나이'][idx] + ', 전화번호 : ' + info_dict['전화번호'][idx] + ', 성별 : ' + info_dict['성별'][idx] + ', 지역 : ' + info_dict['지역'][idx] + ', 구매횟수 : ' + info_dict['구매횟수'][idx])
        idx += 1


good_customer(info) 