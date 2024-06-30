s1 = "python最牛B"
# print(s1[0])    # 获取第0个
# print(s1[1])
# print(s1[2])
# print(s1[3])
# print(s1[4])
# print(s1[5])
# print(s1[6])
# print(s1[7])
# print(s1[8])
# # print(s1[9])    # 没有9, 越界了. 会报错
# print(s1[-1])   # -1 表示倒数.
# print(s1[-2])   # 倒数第二个

print(s1[2:3])

s1.capitalize()
print(s1)     # 输出发现并没有任何的变化. 因为这里的字符串本身是不会发生改变的. 需要我们重新获取

ret1 = s1.capitalize()
print(ret1)

# 大小写的转换
ret = s1.lower()       # 全部转换成小写
print(ret)

ret = s1.upper()         # 全部转换成大写
print(ret)

# 应用, 校验用户输入的验证码是否合法
# verify_code = "abDe"
# user_verify_code = input("请输入验证码:")
# if verify_code.upper() == user_verify_code.upper():
#        print("验证成功")
# else:
#        print("验证失败")

ret = s1.swapcase()         # 大小写互相转换
print(ret)

# 不常用
ret = s1.casefold()         # 转换成小写, 和lower的区别: lower()对某些字符支持不够好. casefold()对所有字母都有效. 比如东欧的一些字母
print(ret)

s2 = "БBß"   # 俄美德
print(s2)
print(s2.lower())
print(s2.casefold())

# 每个被特殊字符隔开的字母首字母大写
s3 = "sylar chuchu,baoheizi*展昭_麻花藤"
ret = s3.title()             # Sylar chuchu,baoheizi*展昭_麻花藤
print(ret)

# 中文也算是特殊字符
s4 = "sylar最喜欢heihei_bao"         # Sylar最喜欢Heihei_Bao
print(s4.title())

# 居中
s5 = "周杰伦"
ret = s5.center(10, "*")     # 拉长成10, 把原字符串放中间.其余位置补*
print(ret)


# 去空格
s7 = "     heihei bao     haha "
ret = s7.strip()       # 去掉左右两端的空格
print(ret)

ret = s7.lstrip()     # 去掉左边空格
print(ret)

ret = s7.rstrip()     # 去掉右边空格
print(ret)

# 应用, 模拟用户登录. 忽略用户输入的空格
# username = input("请输入用户名:").strip()
# password = input("请输入密码: ").strip()
# if username == 'ren' and password == '123':
#        print("登录成功")
# else:
#        print("登录失败")

s7 = "abcdefgabc"
print(s7.strip("abc"))   # defg 也可以指定去掉的元素,


# 字符串替换
s8 = "bao_heihei_nezha_huhu"
ret = s8.replace('bao', '包')       # 把bao替换成包
print(s8)     # bao_heihei_nezha_huhu 切记, 字符串是不可变对象. 所有操作都是产生新字符串返回
print(ret)   # 包_heihei_nezha_huhu

ret = s8.replace('i', 'SB', 1)         # 把i替换成SB, 替换1个
print(ret)   # bao_heSBhei_nezha_huhu

# 字符串切割
s9 = "bao_heihei_nezha_huhu"
lst = s9.split("_")         # 字符串切割, 根据_进行切割
print(lst)

lst = ['周杰伦', '王力宏', '麻花藤']
s = "_".join(lst)
print(s)  # 周杰伦_王力宏_麻花藤

s10 = """诗人
学者
感叹号
渣渣"""
print(s10.split("\n"))   # 用\n切割

# 坑
s11 = "哈哈包黑黑呵呵包黑黑吼吼包黑黑"
lst = s11.split("银王")     # ['', '哈哈', '呵呵', '吼吼', ''] 如果切割符在左右两端. 那么一定会出现空字符串.深坑请留意
print(lst)