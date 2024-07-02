lst = ["胡辣汤", "蛋花汤", "疙瘩汤"]
for index, el in enumerate(lst):
    print(str(index) + "==>" + el)


def func():
    print("呵呵")

print(func)

# 结果:
# <function func at 0x1101e4ea0>

def outer():
    a = 10
    def inner():
        print(a)  # 这个就是闭包
    return inner  # 闭包通常都是返回内层函数

func1 = outer()
func1()