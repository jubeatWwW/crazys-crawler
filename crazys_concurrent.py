import argparse
import time
import threading
import queue

from proxy_query import query

used_file = open('used.txt', 'a+')
used_file.seek(0, 0)
used = set()
for line in used_file.readlines():
    used.add(line.replace('\n', ''))

class Processing(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.size = queue.qsize()
        self.queue = queue

    def run(self):
        print('Start running %d tasks' % self.size)
        if not self.size:
            return
        while self.queue.qsize() > 0:
            print('%.2f' % (1 - (self.queue.qsize() / self.size)))
            time.sleep(5)
            

class QueryJob(threading.Thread):
    def __init__(self, no, queue, lock):
        threading.Thread.__init__(self)
        self.queue = queue
        self.no = no
        self.lock = lock

    def run(self):
        while self.queue.qsize() > 0:
            proxy = self.queue.get()
            host = proxy.split(':')[0]
            if host in used:
                continue
            self.lock.acquire()
            used_file.write(host + '\n')
            used.add(host)
            self.lock.release()
            query(url='https://www.crazys.cc/forum/forum.php?fromuid=733875', proxy=proxy)

def run_job(num=2):
    lock = threading.Lock()
    threads = []

    p = Processing(queue=proxies)
    p.start()
    for i in range(num):
        threads.append(QueryJob(
            no=i,
            queue=proxies,
            lock=lock,
        ))
        threads[i].start()

    for i in range(num):
        threads[i].join()
    p.join()

    used_file.close()
    open('proxies.txt', 'w').close()
    print('Done all jobs')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--threads',
        help='threads run concurrently',
        type=int,
        default=3,
    )
    args = parser.parse_args()
    f = open('proxies.txt', 'r')
    proxies = queue.Queue()
    for line in f.readlines():
        proxies.put(line.replace('\n', ''))
    f.close()

    run_job(num=args.threads)
