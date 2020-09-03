#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 15:08
# @Author  : huzunyan
# @File    : job_01
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com
import threading
import time
import random

lock = threading.Lock()


class DiningPhilosophers(threading.Thread):
    def __init__(self, philosopher):
        super(DiningPhilosophers, self).__init__()
        self.lock = threading.Lock()
        self.name = philosopher
        self.output = []

    # philosopher 哲学家的编号。
    # pickLeftFork 和 pickRightFork 表示拿起左边或右边的叉子。
    # eat 表示吃面。
    # putLeftFork 和 putRightFork 表示放下左边或右边的叉子。

    def run(self):
        self.wants_to_eat()

    def wants_to_eat(self):
        behavior_record = []
        self.lock.acquire()
        behavior_record.append(self.name)
        direction_flag = random.randrange(1, 3)
        if direction_flag == 1:
            self.pick_left_fork(behavior_record)
        else:
            self.pick_right_fork(behavior_record)
        behavior_flag = random.randrange(1, 4)
        if behavior_flag == 1:
            pass
        self.eat()
        self.put_left_fork()
        self.put_right_fork()
        self.lock.release()
        time.sleep(random.randrange(1, 5))
        print(behavior_record)

    @staticmethod
    def pick_left_fork(behavior):
        behavior.append('1')

    @staticmethod
    def pick_right_fork(behavior):
        behavior.append('2')

    @staticmethod
    def put_left_fork():
        print()

    @staticmethod
    def put_right_fork():
        pass

    @staticmethod
    def eat():
        print('3')


if __name__ == "__main__":
    for i in range(5):
        t = DiningPhilosophers(i)
        t.start()