lst = []
for i in range(1, 15):
    lst.append(i)
print(lst)

lst2 = [i for i in range(1, 15)]
print(lst2)

lst3 = [f"python-{i}" for i in range(1, 15)]
print(lst3)

gen = (i for i in range(10))
print(gen)  # <generator object <genexpr> at 0x0000013339F2E680>

for index in gen:
    print(index)

arr = [[1, 2, 3], [3, 4, 5]]
lst5 = [item for arrx in arr for item in arrx if item == 3]
print(lst5)


# [3, 3]

def func():
    print(111)
    yield 222


g = func()  # 生成器g
g1 = (i for i in g)  # 生成器g1. 但是g1的数据来源于g
g2 = (i for i in g1)  # 生成器g2. 来源g1

print(list(g))  # 获取g中的数据. 这时func()才会被执行. 打印111.获取到222. g完毕.
print(list(g1))  # 获取g1中的数据. g1的数据来源是g. 但是g已经取完了. g1 也就没有数据了
print(list(g2))  # 和g1同理

# 把字典中的key和value互换
dic = {'a': 1, 'b': '2'}
new_dic = {dic[key]: key for key in dic}
print(new_dic)  # {1: 'a', '2': 'b'}

# 在以下list中. 从lst1中获取的数据和lst2中相对应的位置的数据组成一个新字典
lst1 = ['jay', 'jj', 'sylar']
lst2 = ['周杰伦', '林俊杰', 'jolin']
dic = {lst1[i]: lst2[i] for i in range(len(lst1))}
print(dic)

lst = [1, -1, 8, -8, 12]
# 绝对值去重
s = {abs(i) for i in lst}
print(s)


def gen():
    lst = ["麻花藤", "胡辣汤", "微星牌饼铛", "Mac牌锅铲"]
    yield from lst


g = gen()
for el in g:
    print(el)

lst = [1, 2, 3, 4, 5, 6, 7]
ll = filter(lambda x: x % 2 == 0, lst)  # 筛选所有的偶数
print(ll) # <filter object at 0x0000016AECEAE860> filter 对象
print(list(ll))

lst = [{"id": 1, "name": 'jolin', "age": 18},
       {"id": 2, "name": 'tony', "age": 16},
       {"id": 3, "name": 'kevin', "age": 17}]

fl = filter(lambda e: e['age'] > 16, lst)  # 筛选年龄大于16的数据
print(list(fl))

# <filter object at 0x00000242B6BB1F00>
# [2, 4, 6]
# [{'id': 1, 'name': 'jolin', 'age': 18}, {'id': 3, 'name': 'kevin', 'age': 17}]