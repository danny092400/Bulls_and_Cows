import random

game_rule = Element("game_rule")
try_time = Element("trytime")
number_input = Element("number_input")
result = Element("result")

rule_msg = "숫자야구게임!!\n\n"
rule_msg += "[게임방법]\n\
    1. 4자리숫자를 입력(0~9의숫자4개, 중복가능)\n\
    2. 숫자와 위치 모두 맞으면 S(strike), 숫자는 맞지만 위치가 다르면 B(Ball)\n\
    3. 4자리 모두 숫자와 위치가 맞다면 게임종료\n\n"

rand = [0, 0, 0, 0]
num = [0, 0, 0, 0]
trytime = 1
trytime_msg = f"[게임] {trytime}회째 도전"

game_rule.element.innerText = rule_msg
try_time.element.innerText = trytime_msg

for i in range(4): #4자리숫자 생성
    rand[i] = random.randint(0, 9)
# print(rand)

def play_game(*args):
    global trytime
    trytime += 1
    
    answer = int(number_input.value)
    
    S = 0
    B = 0
    k = 0

    for i in range(4): #4자리 숫자를 리스트로 변형
        num[i] = answer // (10 ** i) - (answer // (10 ** (i + 1))) * 10
    num.reverse()
    for i in range(4):
        if rand[i] == num[i]:
            S += 1
    for i in range(10):
        if num.count(i) != 0 and rand.count(i) != 0:
            if num.count(i) <= rand.count(i):
                k += num.count(i)
            else:
                k += rand.count(i)
    B = k-S
    if S == 4:
        text = "correct : {rand[0]}{rand[1]}{rand[2]}{rand[3]}"
    else:
        text = f"{S}S {B}B"

    result.element.innerText = text
    number_input.clear()
    trytime_msg = f"[게임] {trytime}회째 도전"
    try_time.element.innerText = trytime_msg

# turn = turn - 1

# print("\n축하드립니다!! 정답입니다!!\n%d회만에 성공하셨습니다!" %(turn))
# print()
# print("게임이 종료되었습니다.")

# import random

# number_input = Element("number_input")
# result = Element("result")

# def play_game(*args):
#     user_guess = number_input.value
#     machine_guess = random.randint(0000, 9999)
#     if int(user_guess) == machine_guess:
#         result.element.innerText = "you win"
#     else:
#         result.element.innerText = "you lost"
#     number_input.value = ""

