f = open("filedire/ll.txt", mode="r", encoding="utf-8")
content = f.read()
print(content)
f.close()


f = open("filedire/ll.txt", mode="rb")
content = f.read()
print(content)
f.close()