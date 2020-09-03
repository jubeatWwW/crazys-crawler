from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .driver import get_driver

def get_ssl_proxies():
    driver = get_driver()
    driver.get('https://www.sslproxies.org/')
    proxies = []
    while True:
        next_btn_wrapper = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'proxylisttable_next'))
        )
        next_btn = next_btn_wrapper.find_element_by_tag_name('a')
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#proxylisttable tbody tr'))
        )
        for row in rows:
            cols = row.find_elements_by_tag_name('td')
            host = cols[0].text
            port = cols[1].text
            proxies.append('%s:%s' % (host, port))

        class_name = next_btn_wrapper.get_attribute('class')
        if 'disabled' in class_name:
            break
        next_btn.click()
    driver.quit()
    return proxies

if __name__ == "__main__":
    print(get_ssl_proxies())
