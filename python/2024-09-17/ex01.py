total = int(input("รับยอดเงินสินค้า : "))

if total >= 15000:
    dis = total * (20/100)
    percent = 20
elif total >= 10000:
    dis = total * (10/100)
    percent = 10
elif total >= 5000:
    dis = total * (5/100)
    percent = 5
elif total >= 3000:
    dis = total * (2/100)
    percent = 2
else :
    dis = 0

pay = total - dis

print ("ราคาสินค้าทั้งหมด : " , total , "บาท")
print ("ได้ส่วนลด : " , percent , "%" , "เป็นเงิน : " , dis , "บาท")
print ("ยอดชำระ :" , pay , "บาท")