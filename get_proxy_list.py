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

def get_proxy_list():
    getters = [
        get_proxy_scan,
        get_ssl_proxies,
        get_proxy_cz,
        get_spys_one,
        get_hide_my_name,
    ]
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
    get_proxy_list()
