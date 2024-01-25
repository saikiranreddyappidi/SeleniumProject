from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

path = r"../Drivers/chromedriver.exe"
option = Options()
option.page_load_strategy = 'none'
driver = webdriver.Chrome(service=Service(path), options=option)
driver.get("https://www.google.com")
driver.quit()
