s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
v = ["A", "E", "I", "O", "U"]

for i in range(len(s)):
    for j in v:
        if s[i] == j:
            print("ตำแหน่งของ " + j + " อยู่ที่ " + str(i))
            break

# for i in range(len(s)):
#     if s[i] == "A":
#         print("ตำแหน่งของ A อยู่ที่ " + str(i))
#     elif s[i] == "E":
#         print("ตำแหน่งของ E อยู่ที่ " + str(i))
#     elif s[i] == "I":
#         print("ตำแหน่งของ I อยู่ที่ " + str(i))
#     elif s[i] == "O":
#         print("ตำแหน่งของ O อยู่ที่ " + str(i))
#     elif s[i] == "U":
#         print("ตำแหน่งของ U อยู่ที่ " + str(i))
