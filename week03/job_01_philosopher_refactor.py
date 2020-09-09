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
        self.lock = threading.Lock()

    def pick_left_fork(self):
        self.lock.acquire()
        behavior = [self.index, 1, 1]
        output.append(behavior)

    def pick_right_fork(self):
        self.lock.acquire()
        behavior = [self.index, 2, 1]
        output.append(behavior)

    def put_left_fork(self):
        self.lock.release()
        behavior = [self.index, 1, 2]
        output.append(behavior)

    def put_right_fork(self):
        self.lock.release()
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
