inputArray = [
    "คะแนนเข้าเรียน(10) : ",
    "คะแนนแบบฝึกหัด(30) : ",
    "คะแนนสอบกลางภาค(20) : ",
    "คะแนนสอบปลายภาค(40) : ",
]

storeInput = []

score = 0

for i in inputArray:
    temp = input(i)
    storeInput.append(float(temp))
    score += float(temp)

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print("-----------------------------")

for i in range(len(inputArray)):
    print(inputArray[i] + str(storeInput[i]))

print("")

print("คะแนนที่ได้ท้ังหมด : ", score)
print("คุณได้เกรด : ", grade)
