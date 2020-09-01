import urllib.request

def get_proxy_scan():
    with urllib.request.urlopen('https://www.proxyscan.io/download?type=https') as f:
        data = f.readlines()
        proxies = []
        for proxy in data:
            proxies.append(proxy.decode('utf-8').replace('\n', ''))
        return proxies

if __name__ == "__main__":
    get_proxy_scan()