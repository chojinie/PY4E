# def rsp_advanced(games):
#     my_point, com_point, draw_point = 0, 0, 0
#     for i in range(games):
#         my_input = input("가위 바위 보 : ") #입력은 0,1,2,가위,바위,보만가능
#         while my_input != "0" and my_input != "1" and my_point != "2" and my_input != "가위" and my_input != "바위" and my_input != "보":
#             print("잘못 입력하셨습니다. 다시 입력해주세요.")
#             print()
#             my_input = input("가위 바위 보: ")
#
#         com_input = random.randint(0, 2)
#         result = rsp_judge(my_input, com_input)
#         rsp_print(i+1, result)
#
#         if result == "컴퓨터":
#             com_point += 1
#         elif result == "나":
#             my_point += 1
#         else result == "무승부":
#             draw_point += 1
#
#     return rsp_result(my_point, com_point, draw_point)
# games = int(input("몇 판을 진행하시겠습니까? : "))
# print()
# rsp_advanced(games)
games = int(input("몇 판을 진행하시겠습니까? : "))
def rsp_advanced(games):
    stage = 1
    user_win = 0
    draw = 0
    computer_win = 0

    while stage <=games:
        print("가위바위보", stage, "번째 판!")

        user = input("나: ")
        if user == '가위':
            num_user = 0
        elif user == '바위':
            num_user = 1
        elif user == '보':
            num_user = 2

        import random
        num_computer = random.randrange(0,3)
        if num_computer == 0:
            computer = "가위"
        elif num_computer == 1:
            computer = "바위"
        elif num_computer == 2:
            computer = "보"
        print("컴퓨터: ", computer)

        if num_user == num_computer:
            print(stage, "번째 판 비겼습니다.")
            draw += 1
        elif num_user - num_computer == 1 or num_user - num_computer == -2:
            print(stage, "번째 판은 나의 승리다 풍악을 울려라 예압베이비!")
            user_win += 1
        else:
            print(stage, "번째 판은 컴퓨터의 승리다 분하지만 다음엔 내가이긴다.")
            computer_win += 1

        stage += 1
    # return user_win, draw, computer_win

rsp_advanced(games)
