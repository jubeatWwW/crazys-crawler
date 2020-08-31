import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

f = open('proxies.txt', 'r')
proxies = []
for line in f.readlines():
    proxies.append(line.replace('\n', ''))
f.close()

used_file = open('used.txt', 'a+')
used_file.seek(0, 0)
used = []
for line in used_file.readlines():
    used.append(line.replace('\n', ''))

valid = open('valid.txt', 'a+')

for proxy in proxies:
    host = proxy.split(':')[0]
    used_file.write(host + '\n')
    if host in used:
        continue
    PROXY = proxy
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",
    }

    driver = webdriver.Chrome(
        executable_path='/c/WebDrivers/bin/chromedriver.exe',
    )
    try:
        driver.get('https://www.crazys.cc/forum/forum.php?fromuid=733875')
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, 'frt'))
        )
        valid.write(proxy + '\n')
        WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'fwinmask'))
        )
    except:
        driver.quit()
    else:
        print('host: %s is valid' % host)
        driver.quit()
    finally:
        driver.quit()

used_file.close()
