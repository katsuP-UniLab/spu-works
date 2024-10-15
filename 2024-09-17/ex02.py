n1 = int(input("เงินลงทุน : "))

if n1 >= 150000:
    dis = n1 * (10/100)
    percent = 10
elif n1 >= 100000:
    dis = n1 * (7/100)
    percent = 7
elif n1 >= 50000:
    dis = n1 * (5/100)
    percent = 5
elif n1 >= 10000:
    dis = n1 * (4/100)
    percent = 4
else :
    dis = 0
    percent = 0

n2 = dis + n1

print ("เงินลงทุน" , n1 , "บาท")
print ("ได้รับผลตอบแทน : " , percent , "%" , "เป็นเงิน : " , dis , "บาท")
print ("ยอดเงินลงทุนรวมผลตอบแทน : " , n2 , "บาท")