from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def query(url='https://localhost:8080', proxy='127.0.0.1:3128'):
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy,
        "proxyType": "MANUAL",
    }

    chrome_options = Options()
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(
        executable_path='/c/WebDrivers/bin/chromedriver.exe',
        chrome_options=chrome_options,
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
    