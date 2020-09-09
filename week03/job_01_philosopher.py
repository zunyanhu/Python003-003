#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 15:08
# @Author  : huzunyan
# @File    : job_01_philosopher
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com
# import threading
# import time
# import random
# import queue
#
# q = queue.Queue()
#
#
# class DiningPhilosophers(threading.Thread):
#     def __init__(self):
#         super(DiningPhilosophers, self).__init__()
#         self.lock = threading.Lock()
#         self.philosopher = range(0, 5)
#
#     def run(self):
#         data = self.wants_to_eat()
#         q.put(data)
#
#     def wants_to_eat(self):
#         behavior_record = []
#         self.lock.acquire()
#         behavior_record.append(random.choice(self.philosopher))
#         behavior_flag = random.randint(1, 3)
#         if behavior_flag == 1:
#             direction_flag = random.randint(1, 2)
#             if direction_flag == 1:
#                 self.pick_left_fork(behavior_record)
#             else:
#                 self.pick_right_fork(behavior_record)
#             behavior_record.append(1)
#         elif behavior_flag == 2:
#             direction_flag = random.randint(1, 2)
#             if direction_flag == 1:
#                 self.put_left_fork(behavior_record)
#             else:
#                 self.put_right_fork(behavior_record)
#             behavior_record.append(2)
#         else:
#             direction_flag = random.randint(1, 2)
#             if direction_flag == 1:
#                 self.put_left_fork(behavior_record)
#             else:
#                 self.put_right_fork(behavior_record)
#             self.eat(behavior_record)
#         self.lock.release()
#         time.sleep(random.randint(1, 3))
#         return behavior_record
#
#     @staticmethod
#     def pick_left_fork(behavior_record):
#         behavior_record.append(1)
#
#     @staticmethod
#     def pick_right_fork(behavior_record):
#         behavior_record.append(2)
#
#     @staticmethod
#     def put_left_fork(behavior_record):
#         behavior_record.append(1)
#
#     @staticmethod
#     def put_right_fork(behavior_record):
#         behavior_record.append(2)
#
#     @staticmethod
#     def eat(behavior_record):
#         behavior_record.append(3)
#
#
# def main():
#     out_put = []
#     n = 10
#     for _ in range(n):
#         threads = [DiningPhilosophers() for _ in range(5)]
#         for t in threads:
#             t.start()
#             out_put.append(q.get())
#     print(out_put)
#
#
# if __name__ == "__main__":
#     main()


# import threading
# from time import sleep
# import os
# import random
#
# numPhilosophers = numForks = 5
# each_behavior = []
#
#
# class Waiter:
#     def __init__(self):
#         self.forks = [Fork(idx) for idx in range(numForks)]
#         # 最开始餐叉还没有被分配给任何人，所以全部 False
#         self.forks_using = [False] * numForks
#
#     # 如果哲学家的左右餐叉都是空闲状态，就为这位哲学家服务提供餐叉
#     def serve(self, philor):
#         if not self.forks_using[philor.leftFork.index] and not self.forks_using[philor.rightFork.index]:
#             self.forks_using[philor.leftFork.index] = True
#             self.forks_using[philor.rightFork.index] = True
#             self.forks[philor.leftFork.index].pickup()
#             self.forks[philor.rightFork.index].pickup()
#             return True
#         else:
#             return False
#
#             # 哲学家用餐完毕后，清理并回收餐叉
#
#     def clean(self, philor):
#         self.forks[philor.leftFork.index].putdown()
#         self.forks[philor.rightFork.index].putdown()
#         self.forks_using[philor.leftFork.index] = False
#         self.forks_using[philor.rightFork.index] = False
#
#
# class Philosopher(threading.Thread):
#     def __init__(self, index):
#         threading.Thread.__init__(self)
#         self.index = index
#         self.leftFork = forks[self.index]
#         self.rightFork = forks[(self.index + 1) % numForks]
#
#     def run(self):
#         while True:
#             if waiter.serve(self):
#                 self.dining()
#                 waiter.clean(self)
#             self.thinking()
#
#     def dining(self):
#         print("Philosopher", self.index, " starts to eat.")
#         sleep(random.uniform(1, 3) / 1000)
#         print("Philosopher", self.index, " finishes eating and leaves to think.")
#
#     def thinking(self):
#         sleep(random.uniform(1, 3) / 1000)
#
#
# class Fork():
#     def __init__(self, index):
#         self.index = index
#         self._lock = threading.Lock()
#
#     def pickup(self):
#         self._lock.acquire()
#
#     def putdown(self):
#         self._lock.release()
#
#
# if __name__ == '__main__':
#     # 创建服务生与哲学家实例
#     waiter = Waiter()
#     forks = [Fork(idx) for idx in range(numForks)]
#     philosophers = [Philosopher(idx) for idx in range(numPhilosophers)]
#
#     # 开启所有的哲学家线程
#     for philosopher in philosophers:
#         philosopher.start()


import threading
import os, random
from time import sleep

log = []
inter = 0


class DiningPhilosophers(threading.Thread):
    def __init__(self, index, num):
        threading.Thread.__init__(self)
        self.num = num
        self.index = index
        self.leftFork = forks[self.index]  # 分配叉子的序号
        self.rightFork = forks[(self.index + 1) % numForks]  # 右边叉子的序号如下

    def run(self):
        global inter
        # print(self.num)
        print(f'num: {self.num}')
        while True:
            self.leftFork.pickLeftFork()
            self.rightFork.pickRightFork()
            self.eat()
            self.leftFork.putLeftFork()
            self.rightFork.putLeftFork()
            sleep(random.uniform(1, 3) / 1000)
            if (inter > self.num * 5 - 1):
                break

    def eat(self):
        global inter
        global log
        # print("Philosopher", self.index, " starts to eat.")
        inter += 1
        print(f'inter: {inter}')
        log_ok = [self.index, 0, 3]
        # print(log_ok)
        log.append(log_ok)
        sleep(random.uniform(1, 3) / 1000)

        # print("Philosopher", self.index, " finishes eating and leaves to think.")


class Fork():
    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()

    def pickLeftFork(self):
        self._lock.acquire(timeout=5)
        log_ok = [self.index, 1, 1]
        # print(log_ok)
        log.append(log_ok)

    def pickRightFork(self):
        self._lock.acquire(timeout=5)
        log_ok = [self.index, 2, 1]
        # print(log_ok)
        log.append(log_ok)

    def putLeftFork(self):
        self._lock.release()
        log_ok = [self.index, 1, 2]
        # print(log_ok)
        log.append(log_ok)

    def putRightFork(self):
        self._lock.release()
        log_ok = [self.index, 2, 2]
        # print(log_ok)
        log.append(log_ok)


def wantsToEat(num):
    philosopher = 5  # 五个哲学家
    philosophers = [DiningPhilosophers(idx, num) for idx in range(philosopher)]

    # 开启所有的哲学家线程
    for philosopher in philosophers:
        philosopher.start()
    philosopher.join()

    print(log)
    # philosopher.terminate()
    try:  # 异常处理语句，检测try后语句是否正常
        while True:
            sleep(0.1)
    except Exception as e:
        raise e


if __name__ == '__main__':
    numForks = 5  # 五个叉子，相当于有五个锁，能占有对应左右两个就能吃东西
    forks = [Fork(idx) for idx in range(numForks)]
    wantsToEat(2)  # 进行多少次查找
