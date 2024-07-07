import os
import time
import threading


def fun(n):
    start = time.time()
    my_thread_name = threading.current_thread().name  # 获取当前线程名称
    print('%s开始运行...' % my_thread_name)
    time.sleep(n)
    my_thread_id = threading.current_thread().ident  # 获取当前线程id
    print('当前线程为：{}，线程id为：{}，所在进程为：{}'.format(my_thread_name, my_thread_id, os.getpid()))
    print('%s线程运行结束，耗时%ds...' % (my_thread_name, time.time() - start))


t1 = time.time()
# 创建3个线程
for i in range(1, 4):
    t = threading.Thread(target=fun, name='线程%s' % i, args=(i,))
    t.start()


main_thread_name = threading.current_thread().name  # 获取当前线程名称
main_thread_id = threading.current_thread().ident  # 获取当前线程id
print('主线程为：{}，线程id为：{}，所在进程为：{}'.format(main_thread_name, main_thread_id, os.getpid()))

print("一共耗时%ds" % (time.time() - t1))

# 线程1开始运行...
# 线程2开始运行...
# 线程3开始运行...
# 主线程为：MainThread，线程id为：8637730304，所在进程为：19493
# 一共耗时0s
# 当前线程为：线程1，线程id为：13005955072，所在进程为：19493
# 线程1线程运行结束，耗时1s...
# 当前线程为：线程2，线程id为：13022744576，所在进程为：19493
# 线程2线程运行结束，耗时2s...
# 当前线程为：线程3，线程id为：13039534080，所在进程为：19493
# 线程3线程运行结束，耗时3s...


