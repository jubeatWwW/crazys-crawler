from proxies import get_proxy_scan, get_ssl_proxies

used_file = open('used.txt', 'a+')
used_file.seek(0, 0)
used = set()

for line in used_file.readlines():
    used.add(line.replace('\n', ''))

def get_proxy_list():
    proxies = []

    proxy_scan_data = filter(lambda x: x.split(':')[0] not in used, get_proxy_scan())
    proxies += proxy_scan_data

    ssl_proxies_data = filter(lambda x: x.split(':')[0] not in used, get_ssl_proxies())
    proxies += ssl_proxies_data

    f = open('proxies.txt', 'w')
    for proxy in proxies:
        f.write(proxy + '\n')

if __name__ == "__main__":
    get_proxy_list()
