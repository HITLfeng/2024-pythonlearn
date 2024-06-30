# 格式化输出
"""
------------ info of Sylar -----------
Name  : Sylar
Age   : 22
job   : Teacher
Hobbie: girl
------------- end -----------------
"""

info = """
------------ info of Sylar -----------
Name  : %s
Age   : %s
job   : %s
Hobbie: %s
------------- end -----------------
""" % ("feng", "26", "wuye", "lin")
print(info)

name = "feng"
print(f"name is {name}")

# in   |    not in

str1 = "abcdefghijklmnop"
str2 = "bce"
if str2 in str1:
    print("yes")
else:
    print("no")


"""
结论: 
1. ascii : 8bit, 主要存放的是英文, 数字,  特殊符号
2. gbk: 16bit, 主要存放中文和亚洲字符. 兼容ascii
3. unicode: 16bit和32bit两个版本. 平时我们用的是16bit这个版本. 全世界所有国家的文字信息. 缺点: 浪费空间(传输和存储)
4. utf-8 : 可变长度unicode, 英文: 8bit, 欧洲文字: 16bit, 中文24bit. 一般数据传输和存储的时候使用.
5. 以上所有编码必须兼容ascii . 

在python程序中, 当我们的程序运行起来之后. 内存中存储的字符串默认使用的是unicode. 目的是unicode定长. 好处理. 但是, 如果涉及到字符串存储和传输, 就必须要进行编码. 编码成utf-8或者gbk进行传递. 原因是unicode实在是太浪费空间了. 

"""

str = "吴"
enstr = str.encode("utf-8")
print(enstr)
print(str.encode("gbk"))

# 字符串常用操作
