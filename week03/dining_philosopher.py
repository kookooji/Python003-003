import threading
import time
import queue
# philosopher 哲学家的编号。
# pickLeftFork 和 pickRightFork 表示拿起左边或右边的叉子。
# eat 表示吃面的次数。
# putLeftFork 和 putRightFork 表示放下左边或右边的叉子。

class DiningPhilosopher(threading.Thread):
    def __init__(self, queue, philosopher, eatTime):
        super().__init__()
        self.lock = threading.Lock()
        self.queue = queue
        self.eat = 0
        self.philosopher = philosopher
        self.eatTime = eatTime
    def pickLeftFork(self):
        self.queue.put([self.philosopher, 1, 1])

    def pickRightFork(self):
        self.queue.put([self.philosopher, 2, 1])

    def eating(self):
        time.sleep(1)
        self.queue.put([self.philosopher,0,3])
        self.eat += 1

    def putLeftFork(self):
        self.queue.put([self.philosopher,1,2])

    def putRightFork(self):
        self.queue.put([self.philosopher,2,2])

    #对于每一个动作都上锁，资源不共享，每次只能一个哲学家吃面
    def run(self):
        while self.eat<self.eatTime:
            self.lock.acquire()
            self.pickLeftFork()
            self.pickRightFork()
            self.eating()
            self.putLeftFork()
            self.putRightFork()
            self.lock.release()


if __name__ == '__main__':
    queue = queue.Queue()
    philosophers = {}
    for i in range(5):
        philosophers[i] = DiningPhilosopher(queue,i,3)
    for i in philosophers:
        philosophers[i].start()

    for i in philosophers:
        philosophers[i].join()
    list = []
    while not queue.empty():
        list.append(queue.get())
    print(list)
    print(len(list))