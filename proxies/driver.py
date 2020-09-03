from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    chrome_options = Options() # 啟動無頭模式
    chrome_options.add_argument('--headless')  #規避google bug
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(
        executable_path='/c/WebDrivers/bin/chromedriver.exe',
        chrome_options=chrome_options,
    )
    
    return driver