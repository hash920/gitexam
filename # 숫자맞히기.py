# 숫자맞히기
import random

answer = random.randint(1, 100)
count = 0

print("숫자 맞히기 게임!")
print("1부터 100 사이의 숫자를 맞혀 보세요.")

while True:
    guess = int(input("숫자 입력: "))
    count += 1

    if guess < answer:
        print("더 큰 숫자입니다!")
    elif guess > answer:
        print("더 작은 숫자입니다!")
    else:
        print(f"정답입니다! 시도 횟수: {count}")
        break
