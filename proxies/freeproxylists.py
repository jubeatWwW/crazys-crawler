from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# no valid
def get_free_proxy_lists():
    driver = webdriver.Chrome(
        executable_path='/c/WebDrivers/bin/chromedriver.exe',
    )

    driver.get('http://www.freeproxylists.net/zh/?pr=HTTPS')
    proxies = []
    pages = driver.find_elements_by_css_selector('.page a')
    for i in range(pages):
        driver.get('http://www.freeproxylists.net/zh/?pr=HTTPS&page=%d' % i)
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.DataGrid tbody tr'))
        )
        for row in rows:
            if row.get_attribute('class') == 'Caption':
                continue
            cols = row.find_elements_by_tag_name('td')
            if len(cols) < 2:
                continue
            host = cols[0].text
            port = cols[1].text
            proxies.append('%s:%s' % (host, port))
    return proxies

if __name__ == "__main__":
    print(get_free_proxy_lists())
