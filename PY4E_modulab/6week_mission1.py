# 왕이름
korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

king_dict = dict()
# korea_king 문자열을 ',' 기준으로 나누기
# king_dict을 각 왕 이름을 key로 하고 1을 value로 하는 딕셔너리로 만들기
for i in korea_king.split(','):
    king_dict[i] = 1

# chosun_king 문자열을 ',' 기준으로 나누기
for i in chosun_king.split(','):
    # 만약 조선 왕 이름이 이미 king_dict 안에 있다면
    if i in king_dict:
        # king_dict에서 key가 i인 value 값을 1 증가시키기
        king_dict[i] += 1

cnt = 0
# king_dict의 key와 value에 대해서
for key, item in king_dict.items():
    # value 값이 2라면:
    if item == 2:
        # 결과를 출력하고 고려와 조선에 모두 있었던 왕의 이름 개수를 세는 cnt를 1 증가시키기
        print(f'조선과 고려에 모두 있는 왕 이름 : {key}')
        cnt += 1
# 고려와 조선에 모두 있었던 왕의 이름 개수 출력
print(f'조선과 고려에 모두 있는 왕 이름은 총 {cnt}개 입니다')