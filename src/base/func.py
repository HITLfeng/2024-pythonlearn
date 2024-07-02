
def func():
    return 'hello world', 'hello x9'

ret = func()
print(ret)
print(type(ret))

x, y = func()
print(x)
print(y)
print(type(x))
print(type(y))


def chi(a, b, *food):
    print("我要吃", a, b, food)

chi("大米饭", "小米饭", "馒头", "面条")   # 前两个参数用位置参数来接收, 后面的参数用动态参数接收

def chi(a, b, c='馒头', *food):
    print(a, b, c, food)

chi("香蕉", "菠萝")  # 香蕉 菠萝 馒头 (). 默认值生效
chi("香蕉", "菠萝", "葫芦娃")  # 香蕉 菠萝 葫芦娃 ()    默认值不生效
chi("香蕉", "菠萝", "葫芦娃", "口罩")    # 香蕉 菠萝 葫芦娃 ('口罩',) 默认值不生效

def fun(*args):
    print(args)


lst = [1, 4, 7]
fun(lst[0], lst[1], lst[2])

fun(*lst)   # 可以使用*把一个列表按顺序打散
s = "臣妾做不到"
fun(*s)     # 字符串也可以打散, (可迭代对象)