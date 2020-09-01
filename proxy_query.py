from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def query(url='https://localhost:8080', proxy='127.0.0.1:3128'):
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy,
        "proxyType": "MANUAL",
    }

    driver = webdriver.Chrome(
        executable_path='/c/WebDrivers/bin/chromedriver.exe',
    )
    try:
        driver.get(url)
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.ID, 'frt'))
        )
    except:
        driver.quit()
    else:
        driver.quit()
    finally:
        driver.quit()
    