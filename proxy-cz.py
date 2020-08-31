import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
  executable_path='/c/WebDrivers/bin/chromedriver.exe',
)

f = open('proxies.txt', 'a+')
f.seek(0, 0)
proxies = []
for line in f.readlines():
    proxies.append(line.split(':')[0])

try:
    for page in range(1, 150):
        driver.get('http://free-proxy.cz/en/proxylist/main/%s' % page)
        rows = WebDriverWait(driver, 9000).until(
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
            print(host + ' ' + port)
            f.write('%s:%s\n' % (host, port))
        time.sleep(5)
finally:
    f.close()
    driver.quit()
