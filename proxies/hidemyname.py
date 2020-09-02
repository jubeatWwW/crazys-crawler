from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# no valid
def get_hide_my_name():
    driver = webdriver.Chrome(
        executable_path='/c/WebDrivers/bin/chromedriver.exe',
    )

    proxies = []
    driver.get('https://hidemy.name/en/proxy-list/?type=s#list')
    rows = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.table_block tbody tr'))
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
    return proxies

if __name__ == "__main__":
    print(get_hide_my_name())
