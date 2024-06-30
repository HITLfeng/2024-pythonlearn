"""
a = 10
b = 3
print(a ** 3)
print(a // 3)

# 字符串操作 * +
msg1 = "hello world"
msg2 = "mabaoguo"

print(msg1)
print(msg1 + msg2)
print(msg1 * 5)

print(type(a))
print(type(msg1))
msg1 = 10
print(type(msg1))

# a = int(input("please input a:"))
# b = int(input("please input b:"))
# print("a + b = " + str(a + b))

condition = True
if condition:
    print("yes")
else:
    print("no")

i = 100
while i > 0:
    print("i = " + str(i))
    i = i - 1
"""

# sum = 0
# i = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)

# i = 0
# while i <= 100:
#     if i % 2 == 1:
#         print(i)
#     i = i + 1

# sum = 0
# i = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum -= i
#     else:
#         sum += i
#     i += 1
# print(sum)

for num in range(10):
    print(num)

for num in range(1, 10, 2):
    print(num)

for num in range(10, 1, -2):  # 反着来, 和切片一样
    print(num)

lst = ["周杰伦", "马虎疼", "疼不疼", "傻不傻"]
for i in range(len(lst)):
    print(i, lst[i])

# 直接这么写是不是更好
lst = ["周杰伦", "马虎疼", "疼不疼", "傻不傻"]
for el in lst:
    print(el)

tu = (1)
print(type(tu))

tu = (1,)
print(type(tu))

dic = {"id": 123, "name": 'sylar', "age": 18}
dic1 = {"id": 456, "name": "麻花藤", "ok": "wtf"}
dic.update(dic1) # 把dic1中的内容更新到dic中. 如果key重名. 则修改替换. 如果不存在key, 则新增.
print(dic)
print(dic1)
