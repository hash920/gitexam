# 성적 계산 프로그램

name = input("이름을 입력하세요: ")

kor = int(input("국어 점수: "))
eng = int(input("영어 점수: "))
math = int(input("수학 점수: "))

total = kor + eng + math
average = total / 3

print("\n===== 성적 결과 =====")
print("이름:", name)
print("총점:", total)
print("평균:", round(average, 2))

if average >= 90:
    print("등급: A")
elif average >= 80:
    print("등급: B")
elif average >= 70:
    print("등급: C")
elif average >= 60:
    print("등급: D")
else:
    print("등급: F")