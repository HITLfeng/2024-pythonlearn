def wrapper2(fn):
    def inner():
        log()
        fn()
    return inner
@wrapper2
def add():
    # 记录日志的代码
    pass
def delete():
    # 记录日志的代码
    pass
def update():
    # 记录日志的代码
    pass
def search():
    # 记录日志的代码
    pass

def log():
    print("this is a log")



# fadd = wrapper(add)
# fadd()

# 语法糖
add()


def wrapper(fn):
    def inner(username, password):
        """ 在执行fn之前 """
        log()
        fn(username, password)
        """ 在执行fn之后 """

    return inner


@wrapper
def play_game(username, password):
    print(username, password)


play_game("jolin", "dsb")