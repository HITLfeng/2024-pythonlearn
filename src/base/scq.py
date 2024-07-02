def func():
    print("111")
    yield 111
    print("222")
    yield 222
    print("333")
    yield 333


testfunc = func()
print(testfunc)
print(testfunc.__next__())
print(testfunc.__next__())
print(testfunc.__next__())


# print(next(testfunc))
# print(next(testfunc))
# print(next(testfunc))


def eat():
    print("我吃什么啊")
    a = yield "馒头"
    print("a=", a)
    b = yield "大饼"
    print("b=", b)
    c = yield "韭菜盒子"
    print("c=", c)
    yield "GAME OVER"


gen = eat()  # 获取生成器
ret1 = gen.__next__()
print(ret1)
ret2 = gen.send("胡辣汤")
print(ret2)
ret3 = gen.send("狗粮")
print(ret3)
ret4 = gen.send("猫粮")
print(ret4)
