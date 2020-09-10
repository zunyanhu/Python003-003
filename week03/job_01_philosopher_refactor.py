#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 16:35
# @Author  : huzunyan
# @File    : job_01_philosopher_refactor
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com
import threading
import time
import random
count = 0
output = []


class DiningPhilosophers(threading.Thread):
    def __init__(self, num, index):
        threading.Thread.__init__(self)
        self.index = index
        self.num = num
        self.left_fork = forks[self.index]
        self.right_fork = forks[(self.index + 1) % forks_num]

    def run(self):
        global count
        while True:
            self.left_fork.pick_left_fork()
            self.right_fork.pick_right_fork()
            self.eat()
            self.left_fork.put_left_fork()
            self.right_fork.put_right_fork()
            self.think()
            if count >= self.num:
                break

    def eat(self):
        global output
        global count
        behavior = [self.index, 0, 3]
        output.append(behavior)
        count += 1

    @staticmethod
    def think():
        time.sleep(random.uniform(0, 1))


class Fork():
    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()

    def pick_left_fork(self):
        self._lock.acquire()
        behavior = [self.index, 1, 1]
        output.append(behavior)

    def pick_right_fork(self):
        self._lock.acquire()
        behavior = [self.index, 2, 1]
        output.append(behavior)

    def put_left_fork(self):
        self._lock.release()
        behavior = [self.index, 1, 2]
        output.append(behavior)

    def put_right_fork(self):
        self._lock.release()
        behavior = [self.index, 2, 2]
        output.append(behavior)


def want_to_eat(num):
    philosopher = 5
    for idx in range(philosopher):
        philosopher = DiningPhilosophers(num, idx)
        philosopher.start()
    philosopher.join()
    print(output)


if __name__ == "__main__":
    forks_num = 5
    forks = [Fork(idx) for idx in range(forks_num)]
    # for idx in range(forks_num):
    #     forks = Fork(idx)
    want_to_eat(10)


# import threading
# import queue
#
#
# class DiningPhilosopher(threading.Thread):
#     '''
#     哲学家类
#     '''
#
#     def __init__(self, index, times):
#         super(DiningPhilosopher, self).__init__()
#         self.index = index  # 哲学家的编号
#         self.times = times  # 哲学家需要进食的次数
#         self.left_fork = forks[self.index]  # 左手的叉子
#         self.right_fork = forks[(self.index + 1) % 5]  # 右手的叉子
#         self.take_food_times = 0  # 哲学家已经吃的次数
#
#     def run(self):
#         while self.take_food_times < self.times:
#             if waiter.service(self):
#                 self.dining()
#                 waiter.clean(self)
#                 self.thinking()
#
#     def dining(self):
#         self.take_food_times += 1
#         print(f"哲学家： {self.index} 开始吃第{self.take_food_times}次面")
#         print(f"哲学家： {self.index} 哲学家吃面登记")
#         q.put([self.index, 0, 3])  # 吃面登记
#         print(f"哲学家： {self.index} 面吃完了")
#
#     def thinking(self):
#         print(f"哲学家： {self.index} 开始思考")
#         print(f"哲学家： {self.index} 思考完了")
#
#
# class Fork():
#     '''
#     叉子类，加锁代表稀缺的资源
#     '''
#
#     def __init__(self, id):
#         self.id = id  # 叉子的编号
#         self._lock = threading.Lock()  # 叉子锁
#
#     def pickup(self):
#         self._lock.acquire()  # 拿起上锁
#
#     def putdown(self):
#         self._lock.release()  # 放下解锁
#
#
# class Waiter:
#     '''
#     侍者类，管理叉子
#     '''
#
#     def __init__(self):
#         self.fork_mark = [False] * 5  # 叉子的使用标志，False未使用，True正在使用
#
#     def service(self, philosopher):
#         if (not self.fork_mark[philosopher.left_fork.id]
#                 and not self.fork_mark[philosopher.right_fork.id]):
#             # 如果左手和右手的叉子都没有使用,由侍者类标记已使用，并对叉子进行上锁
#             self.fork_mark[philosopher.left_fork.id] = True
#             self.fork_mark[philosopher.right_fork.id] = True
#             forks[philosopher.left_fork.id].pickup()
#             q.put([philosopher.index, 1, 1])  # 哲学家拿起左边的叉子记录
#             print(f"哲学家： {philosopher.index} 拿起左边的叉子登记")
#             forks[philosopher.right_fork.id].pickup()
#             q.put([philosopher.index, 2, 1])  # 哲学家拿起右边的叉子记录
#             print(f"哲学家： {philosopher.index} 拿起右边的叉子登记")
#             return True
#         else:
#             # 哲学家的左边或者右边的叉子有另外的哲学家使用，不能吃面
#             return False
#
#     def clean(self, philosopher):
#         # 对哲学家使用的叉子解锁，并标记为可以使用状态。
#         forks[philosopher.left_fork.id].putdown()
#         q.put([philosopher.index, 1, 2])  # 哲学家放下左边的叉子记录
#         print(f"哲学家： {philosopher.index} 放下左边的叉子登记")
#
#         forks[philosopher.right_fork.id].putdown()
#         q.put([philosopher.index, 2, 2])  # 哲学家放下右边的叉子记录
#         print(f"哲学家： {philosopher.index} 放下右边的叉子登记")
#
#         # 标记叉子未使用
#         self.fork_mark[philosopher.left_fork.id] = False
#         self.fork_mark[philosopher.right_fork.id] = False
#
#
# if __name__ == '__main__':
#
#     n = 1  # 每个哲学家需要进餐的次数（n在1和60之间）
#     q = queue.Queue()  # 登记动作队列
#     waiter = Waiter()  # 侍者，管理叉子的使用
#     forks = [Fork(i) for i in range(5)]  # 5个叉子
#     philosophers = [DiningPhilosopher(i, n) for i in range(5)]  # 5个哲学家
#
#     # 启动线程
#     for philosopher in philosophers:
#         philosopher.start()
#
#     # 等待所有线程结束
#     for philosopher in philosophers:
#         philosopher.join()
#
#     # 作业要求的输出格式
#     print(list(q.queue))
