#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 15:08
# @Author  : huzunyan
# @File    : job_01_philosopher
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com
import threading
import time
import random
import queue

q = queue.Queue()


class DiningPhilosophers(threading.Thread):
    def __init__(self):
        super(DiningPhilosophers, self).__init__()
        self.lock = threading.Lock()
        self.philosopher = range(0, 5)

    def run(self):
        data = self.wants_to_eat()
        q.put(data)

    def wants_to_eat(self):
        behavior_record = []
        self.lock.acquire()
        behavior_record.append(random.choice(self.philosopher))
        behavior_flag = random.randint(1, 3)
        if behavior_flag == 1:
            direction_flag = random.randint(1, 2)
            if direction_flag == 1:
                self.pick_left_fork(behavior_record)
            else:
                self.pick_right_fork(behavior_record)
            behavior_record.append(1)
        elif behavior_flag == 2:
            direction_flag = random.randint(1, 2)
            if direction_flag == 1:
                self.put_left_fork(behavior_record)
            else:
                self.put_right_fork(behavior_record)
            behavior_record.append(2)
        else:
            direction_flag = random.randint(1, 2)
            if direction_flag == 1:
                self.put_left_fork(behavior_record)
            else:
                self.put_right_fork(behavior_record)
            self.eat(behavior_record)
        self.lock.release()
        time.sleep(random.randint(1, 3))
        return behavior_record

    @staticmethod
    def pick_left_fork(behavior_record):
        behavior_record.append(1)

    @staticmethod
    def pick_right_fork(behavior_record):
        behavior_record.append(2)

    @staticmethod
    def put_left_fork(behavior_record):
        behavior_record.append(1)

    @staticmethod
    def put_right_fork(behavior_record):
        behavior_record.append(2)

    @staticmethod
    def eat(behavior_record):
        behavior_record.append(3)


def main():
    out_put = []
    n = 10
    for _ in range(n):
        threads = [DiningPhilosophers() for _ in range(5)]
        for t in threads:
            t.start()
            out_put.append(q.get())
    print(out_put)


if __name__ == "__main__":
    main()
