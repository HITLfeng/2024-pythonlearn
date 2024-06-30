# ftest1 = open("filedire/test1.txt", "r", encoding="utf-8")
# str = ftest1.read()
# print(str)
#
# ftest1.close()

# with open("filedire/test1.txt", "r", encoding="utf-8") as filetest1:
#     for line in filetest1:
#         if line.strip() != "":
#             print(line.strip())

lstHead = []
lstRes = []
ftest1 = open("filedire/test1.txt", "r", encoding="utf-8")
for line in ftest1:
    # 首次读取到第一行
    # 序号 部门 人数 平均年龄 备注
    if line.strip() != "":
        lstHead = line.strip().split();
        break
for line in ftest1:
    if line.strip() == "":
        continue
    dicttmp = {}
    for index in range(len(lstHead)):
        dicttmp[lstHead[index]] = line.strip().split()[index]
    lstRes.append(dicttmp)
ftest1.close()
print(lstRes)
