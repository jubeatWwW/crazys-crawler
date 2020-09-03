from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .driver import get_driver

def get_proxy_cz():
    driver = get_driver()
    proxies = []
    try:
        for page in range(1, 6):
            driver.get('http://free-proxy.cz/en/proxylist/country/all/https/ping/all/%s' % page)
            rows = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#proxy_list tbody tr'))
            )
            for row in rows:
                cols = row.find_elements_by_tag_name('td')
                if len(cols) < 2:
                    continue
                host = cols[0].text
                port = cols[1].text
                if host in proxies:
                    continue
                proxies.append('%s:%s' % (host, port))
    finally:
        driver.quit()
        return proxies

if __name__ == "__main__":
    print(get_proxy_cz())
