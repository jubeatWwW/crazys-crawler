import argparse
import threading
from proxies import (
    get_proxy_scan,
    get_ssl_proxies,
    get_proxy_cz,
    get_spys_one,
    get_hide_my_name,
)

used_file = open('used.txt', 'a+')
used_file.seek(0, 0)
used = set()

for line in used_file.readlines():
    used.add(line.replace('\n', ''))
used_file.close()

proxies = []

class GetProxy(threading.Thread):
    def __init__(self, query_func, proxies):
        threading.Thread.__init__(self)
        self.query_func = query_func
        self.proxies = proxies

    def run(self):
        data = filter(lambda x: x.split(':')[0] not in used, self.query_func())
        self.proxies += data
        print('get %d proxies' % len(self.proxies))

def get_proxy_list(headless=False):
    getters = [
        get_proxy_scan,
        get_ssl_proxies,
        get_proxy_cz,
        get_spys_one,
    ]
    if not headless:
        getters.append(get_hide_my_name)
    proxies = []
    threads = []
    for getter in getters:
        threads.append(GetProxy(query_func=getter, proxies=proxies))
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    f = open('proxies.txt', 'w')
    for proxy in proxies:
        f.write(proxy + '\n')
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-q',
        '--headless',
    )
    args = parser.parse_args()
    get_proxy_list(bool(args.headless))
