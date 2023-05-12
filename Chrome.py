import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pandas import DataFrame

path = r"/Drivers/chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(service=Service(path), options=chrome_options)
arr = {}

for i in range(101100,0):
    try:
        driver.get("https://www.vignan.ac.in/vsatresult/results.asp?hallticket={}".format(i))
        name = driver.find_element(by=By.XPATH, value="/html/body/center/div/table/tbody/tr/td/table/tbody/tr[2]/td[3]")
        maths = driver.find_element(by=By.XPATH,
                                    value="/html/body/center/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]")
        physics = driver.find_element(by=By.XPATH,
                                      value="/html/body/center/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]")
        chemistry = driver.find_element(by=By.XPATH,
                                        value="/html/body/center/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]")
        english = driver.find_element(by=By.XPATH,
                                      value="/html/body/center/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[4]")
        total = driver.find_element(by=By.XPATH,
                                    value="/html/body/center/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[5]")
        arr[i] = [name.text, maths.text, physics.text, chemistry.text, english.text, total.text]
    except Exception as e:
        print("Error", e)

driver.quit()
df = DataFrame(arr)
df = df.transpose()
df.to_csv("vignan.csv")
print(df)
