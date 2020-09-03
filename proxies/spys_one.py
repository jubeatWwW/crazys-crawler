from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .driver import get_driver

# no valid
def get_spys_one():
    driver = get_driver()
    driver.get('https://spys.one/en/https-ssl-proxy/')
    proxies = []
    odd_rows = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.spy1x'))
    )
    even_rows = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.spy1xx'))
    )
    rows = odd_rows[1:] + even_rows
    for row in rows:
        col = row.find_element_by_css_selector('td font')
        proxies.append(col.text.replace('\n', ''))
    driver.quit()
    return proxies

if __name__ == "__main__":
    print(get_spys_one())
